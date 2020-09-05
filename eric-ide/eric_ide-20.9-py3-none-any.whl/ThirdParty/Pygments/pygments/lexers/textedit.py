# -*- coding: utf-8 -*-
"""
    pygments.lexers.textedit
    ~~~~~~~~~~~~~~~~~~~~~~~~

    Lexers for languages related to text processing.

    :copyright: Copyright 2006-2019 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

import re
from bisect import bisect

from pygments.lexer import RegexLexer, include, default, bygroups, using, this
from pygments.token import Text, Comment, Operator, Keyword, Name, String, \
    Number, Punctuation

from pygments.lexers.python import PythonLexer

__all__ = ['AwkLexer', 'VimLexer']


class AwkLexer(RegexLexer):
    """
    For Awk scripts.

    .. versionadded:: 1.5
    """

    name = 'Awk'
    aliases = ['awk', 'gawk', 'mawk', 'nawk']
    filenames = ['*.awk']
    mimetypes = ['application/x-awk']

    tokens = {
        'commentsandwhitespace': [
            (r'\s+', Text),
            (r'#.*$', Comment.Single)
        ],
        'slashstartsregex': [
            include('commentsandwhitespace'),
            (r'/(\\.|[^[/\\\n]|\[(\\.|[^\]\\\n])*])+/'
             r'\B', String.Regex, '#pop'),
            (r'(?=/)', Text, ('#pop', 'badregex')),
            default('#pop')
        ],
        'badregex': [
            (r'\n', Text, '#pop')
        ],
        'root': [
            (r'^(?=\s|/)', Text, 'slashstartsregex'),
            include('commentsandwhitespace'),
            (r'\+\+|--|\|\||&&|in\b|\$|!?~|'
             r'(\*\*|[-<>+*%\^/!=|])=?', Operator, 'slashstartsregex'),
            (r'[{(\[;,]', Punctuation, 'slashstartsregex'),
            (r'[})\].]', Punctuation),
            (r'(break|continue|do|while|exit|for|if|else|'
             r'return)\b', Keyword, 'slashstartsregex'),
            (r'function\b', Keyword.Declaration, 'slashstartsregex'),
            (r'(atan2|cos|exp|int|log|rand|sin|sqrt|srand|gensub|gsub|index|'
             r'length|match|split|sprintf|sub|substr|tolower|toupper|close|'
             r'fflush|getline|next|nextfile|print|printf|strftime|systime|'
             r'delete|system)\b', Keyword.Reserved),
            (r'(ARGC|ARGIND|ARGV|BEGIN|CONVFMT|ENVIRON|END|ERRNO|FIELDWIDTHS|'
             r'FILENAME|FNR|FS|IGNORECASE|NF|NR|OFMT|OFS|ORFS|RLENGTH|RS|'
             r'RSTART|RT|SUBSEP)\b', Name.Builtin),
            (r'[$a-zA-Z_]\w*', Name.Other),
            (r'[0-9][0-9]*\.[0-9]+([eE][0-9]+)?[fd]?', Number.Float),
            (r'0x[0-9a-fA-F]+', Number.Hex),
            (r'[0-9]+', Number.Integer),
            (r'"(\\\\|\\"|[^"])*"', String.Double),
            (r"'(\\\\|\\'|[^'])*'", String.Single),
        ]
    }


class VimLexer(RegexLexer):
    """
    Lexer for VimL script files.

    .. versionadded:: 0.8
    """
    name = 'VimL'
    aliases = ['vim']
    filenames = ['*.vim', '.vimrc', '.exrc', '.gvimrc',
                 '_vimrc', '_exrc', '_gvimrc', 'vimrc', 'gvimrc']
    mimetypes = ['text/x-vim']
    flags = re.MULTILINE

    _python = r'py(?:t(?:h(?:o(?:n)?)?)?)?'

    tokens = {
        'root': [
            (r'^([ \t:]*)(' + _python + r')([ \t]*)(<<)([ \t]*)(.*)((?:\n|.)*)(\6)',
             bygroups(using(this), Keyword, Text, Operator, Text, Text,
                      using(PythonLexer), Text)),
            (r'^([ \t:]*)(' + _python + r')([ \t])(.*)',
             bygroups(using(this), Keyword, Text, using(PythonLexer))),

            (r'^\s*".*', Comment),

            (r'[ \t]+', Text),
            # TODO: regexes can have other delims
            (r'/[^/\\\n]*(?:\\[\s\S][^/\\\n]*)*/', String.Regex),
            (r'"[^"\\\n]*(?:\\[\s\S][^"\\\n]*)*"', String.Double),
            (r"'[^\n']*(?:''[^\n']*)*'", String.Single),

            # Who decided that doublequote was a good comment character??
            (r'(?<=\s)"[^\-:.%#=*].*', Comment),
            (r'-?\d+', Number),
            (r'#[0-9a-f]{6}', Number.Hex),
            (r'^:', Punctuation),
            (r'[()<>+=!|,~-]', Punctuation),  # Inexact list.  Looks decent.
            (r'\b(let|if|else|endif|elseif|fun|function|endfunction)\b',
             Keyword),
            (r'\b(NONE|bold|italic|underline|dark|light)\b', Name.Builtin),
            (r'\b\w+\b', Name.Other),  # These are postprocessed below
            (r'.', Text),
        ],
    }

    def __init__(self, **options):
        from pygments.lexers._vim_builtins import command, option, auto
        self._cmd = command
        self._opt = option
        self._aut = auto

        RegexLexer.__init__(self, **options)

    def is_in(self, w, mapping):
        r"""
        It's kind of difficult to decide if something might be a keyword
        in VimL because it allows you to abbreviate them.  In fact,
        'ab[breviate]' is a good example.  :ab, :abbre, or :abbreviate are
        valid ways to call it so rather than making really awful regexps
        like::

            \bab(?:b(?:r(?:e(?:v(?:i(?:a(?:t(?:e)?)?)?)?)?)?)?)?\b

        we match `\b\w+\b` and then call is_in() on those tokens.  See
        `scripts/get_vimkw.py` for how the lists are extracted.
        """
        p = bisect(mapping, (w,))
        if p > 0:
            if mapping[p-1][0] == w[:len(mapping[p-1][0])] and \
               mapping[p-1][1][:len(w)] == w:
                return True
        if p < len(mapping):
            return mapping[p][0] == w[:len(mapping[p][0])] and \
                mapping[p][1][:len(w)] == w
        return False

    def get_tokens_unprocessed(self, text):
        # TODO: builtins are only subsequent tokens on lines
        #       and 'keywords' only happen at the beginning except
        #       for :au ones
        for index, token, value in \
                RegexLexer.get_tokens_unprocessed(self, text):
            if token is Name.Other:
                if self.is_in(value, self._cmd):
                    yield index, Keyword, value
                elif self.is_in(value, self._opt) or \
                        self.is_in(value, self._aut):
                    yield index, Name.Builtin, value
                else:
                    yield index, Text, value
            else:
                yield index, token, value
