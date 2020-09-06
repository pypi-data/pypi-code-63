import os
from functools import wraps
import copy
from skitai import was as the_was

class TemplateEngine:
    templates_dirs = []
    DEFAULT_JINJA2_EXTS = {"jinja2.ext.do", "jinja2.ext.loopcontrols"}

    def __init__ (self):
        self.jinja_env = None
        self.chameleon = None
        self._jinja2_patch_options = (
            "{{", "}}", "{%", "%}", "{#", "#}", "%", '##',
            dict (trim_blocks = True, lstrip_blocks = True, newline_sequence = '\n')
        )
        self._jinja2_filters = {}
        self._jinja2_extensions = self.DEFAULT_JINJA2_EXTS
        self._template_globals = {}
        self._template_homes = []

    def setup_template_engines (self, paths):
        self._template_homes = paths
        try:
            import jinja2
        except ImportError:
            pass
        else:
            from ..patches import jinjapatch
            kargs = self._jinja2_patch_options [-1]
            if 'loader' not in kargs:
                kargs ['loader'] = self.get_template_loader ()
            if 'extensions' not in kargs:
                kargs ['extensions'] = list (self._jinja2_extensions)
            self.jinja_env = jinjapatch.overlay (
                self.app_name,
                *self._jinja2_patch_options [:-1],
                **kargs
            )
        # chameleon -------------------------------------
        template_dir = os.path.join (paths [0], "templates")
        if os.path.isdir (template_dir):
            try:
                from chameleon import PageTemplateLoader
            except ImportError:
                pass
            else:
                self.chameleon = PageTemplateLoader (
                    template_dir,
                    auto_reload = self.use_reloader,
                    restricted_namespace = False
                )

    def add_jinja_ext (self, ext):
        self._jinja2_extensions.add (ext)

    def load_jinja_filters (self):
        if not self._jinja2_filters:
            return
        for k, v in self._jinja2_filters.items ():
            self.jinja_env.filters [k] = v
        self._jinja2_filters = {}

    # decorators --------------------------------------------------
    def template_global (self, name):
        def decorator(f):
            self.save_function_spec (f)
            @wraps(f)
            def wrapper (*args, **kwargs):
                return f (the_was._get (), *args, **kwargs)
            self._template_globals [name] = wrapper
            return wrapper
        return decorator

    def template_filter (self, name):
        def decorator(f):
            self._jinja2_filters [name] = f
            @wraps(f)
            def wrapper (*args, **kwargs):
                return f (*args, **kwargs)
            return wrapper
        return decorator

    # template engine -----------------------------------------------
    def skito_jinja (self, option = 0):
        if option == 0:
            return self.jinja_overlay ("{{", "}}")
        elif option == 1:
            return self.jinja_overlay ("${", "}")
        elif option == 5:
            return self.jinja_overlay ("{:", ":}", "{%", "%}", "<!---", "--->")
        raise ValueError ('Invalid template formatting option')

    def jinja_overlay (
        self,
        variable_start_string = "{{",
        variable_end_string = "}}",
        block_start_string = "{%",
        block_end_string = "%}",
        comment_start_string = "{#",
        comment_end_string = "#}",
        line_statement_prefix = "%",
        line_comment_prefix = "##",
        **karg
    ):
        # delay before app is actual imported
        self._jinja2_patch_options = (
            variable_start_string, variable_end_string, block_start_string, block_end_string,
            comment_start_string, comment_end_string, line_statement_prefix, line_comment_prefix,
            karg
        )

    def render (self, was, template_file, _do_not_use_this_variable_name_ = {}, **karg):
        while template_file and template_file [0] == "/":
            template_file = template_file [1:]

        if _do_not_use_this_variable_name_:
            assert not karg, "Can't Use Dictionary and Keyword Args Both"
            karg = _do_not_use_this_variable_name_

        context = copy.copy (karg)
        karg.update (self._template_globals)
        template = self.get_template (template_file)
        rendered = template.render (
            was = was,
            app = was.app,
            request = was.request,
            response = was.response,
            context = context,
            **karg
        )
        return rendered

    def get_template (self, name):
        if name.endswith ('.pt') or name.endswith (".ptal"):
            if self.chameleon is None:
                raise ImportError ('Chameleon template engine is not installed')
            return self.chameleon [name]
        if self.jinja_env is None:
            raise ImportError ("Jinja2 template engine is not installed")
        return self.jinja_env.get_template (name)

    def get_template_loader (self):
        from jinja2 import FileSystemLoader, ChoiceLoader

        templates = []
        for home in self._template_homes:
            template_dir = os.path.join (home, "templates")
            if os.path.isdir (template_dir):
                templates.append (FileSystemLoader (template_dir))
        for tdir in self.templates_dirs:
            if os.path.isdir (tdir):
                templates.append (FileSystemLoader (tdir))
        templates.append (FileSystemLoader(os.path.join (os.path.dirname (__file__), 'contrib', 'templates')))
        return ChoiceLoader (templates)
