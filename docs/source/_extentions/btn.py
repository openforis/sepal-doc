# -*- coding: utf-8 -*-

from docutils import nodes

def btn_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    """add inline btn

    Returns 2 part tuple containing list of nodes to insert into the
    document and a list of system messages.  Both are allowed to be
    empty.

    :param name: The role name used in the document.
    :param rawtext: The entire markup snippet, with role.
    :param text: The text marked with the role. (it should use the following format: `<fontawesome icon> text`) color is optional
    :param lineno: The line number where rawtext appears in the input.
    :param inliner: The inliner instance that called us.
    :param options: Directive options for customization.
    :param content: The directive content for customization.
    """
    node =nodes.reference()
    
    # get the icon parameters
    if text.find("<") != -1:
        start = text.find("<")
        end = text.find(">")
        icon = text[start+1:end]
        text = text[end+1:]
    else:
        icon = ""
    
    margin = 'mr-1' if text else ''
    html = f'<span class="guilabel"><i class="{icon} {margin}"></i>{text.strip()}</span>'
    
    node = nodes.raw('', html, format='html')
    return [node], []

def setup(app):
    """Install the plugin.

    :param app: Sphinx application context.
    """
    app.add_role('btn', btn_role)
    return