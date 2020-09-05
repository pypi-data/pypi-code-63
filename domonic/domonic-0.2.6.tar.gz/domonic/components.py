import base64
from domonic.html import *

# WARNING. you didn't see this. what is not documented is subject to lots of change!
# use this as example for building own components

class Modal(object):  # TODO - shouldn't this extend dom?

    def __init__(self, reference=None, content=None):
        self.reference = reference
        self.content = content

    def __str__(self):
        return str(
            div(
                div(
                    span("&times;", _class="close", **{"_data-ref": self.reference}),
                    div(self.content),
                    _class="modal-content"
                ), _class="modal", _id=self.reference
            )
        )


class Webpage(object):  # TODO - shouldn't this extend html?

    def __init__(self, content=None):
        self.content = content

    def __str__(self):
        classless_css = link(_rel="stylesheet", _href="https://unpkg.com/marx-css/css/marx.min.css")
        jquery = script(_src="https://code.jquery.com/jquery-3.5.1.min.js")
        code = script('''
            $(document).on( "click", ".close", function() {
                var _id = $(this).data('ref');
                $('#'+_id).css("display","none");
            });
            $(document).on( "click", ".open", function() {
                var _id = $(this).data('ref');
                $('#'+_id).css("display","block");
            });

            // When the user clicks anywhere outside of the modal, close it
            //window.onclick = function(event) {
            //    if (event.target == modal) {
            //        modal.style.display = "none";
            //    }
            //}

            // pass an ElementID and an endpoint to redraw that div with the endpoints response
            window.redraw = function( _id, endpoint ){
                $.get( endpoint, function( data ) {
                window.console.log(data)
                $( "#"+_id ).html( $(data).html() );
                });
            }

        ''')
        styles = style('''
            .domonic-container {
                padding:20px;
            }
            .modal {
                display: none;
                position: fixed;
                z-index: 1;
                left: 0;
                top: 0;
                width: 100%;
                height: 100%;
                overflow: auto;
                background-color: rgb(0,0,0);
                background-color: rgba(0,0,0,0.4);
            }
            .modal-content {
                background-color: #fefefe;
                margin: 15% auto;
                padding: 20px;
                border: 1px solid #888;
                width: 80%;
            }
            .btn-sm {
                font-size:10px;
                padding: 0px;
                padding-left: 2px;
                padding-right: 2px;
            }
            .del {
                background-color:red;
            }
            .go {
                background-color:green;
            }

        ''')
        return str(
            html(
                '<!DOCTYPE HTML>',
                head(classless_css, jquery, code, styles),
                body(div(self.content, _class="domonic-container"))
                )
            )


'''
def create_element(_type, *args, **kwargs):
    # TODO - check if a component exists..
    # TODO - check if a div exists
    # if not create a new tag type < orignal
    new_tag = type(_type, (closed_tag, Element), {'name': _type, '__init__': tag_init})
    return new_tag


el = create_element


def clone_element():
    pass


def is_valid_element():
    pass


def create_ref():
    pass
'''
