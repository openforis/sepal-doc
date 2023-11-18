"""Extension to dynamically change the value of the "edit this page btn"""

from typing import Dict, List

from docutils import nodes
from sphinx.application import Sphinx
from sphinx.util import logging
from sphinx.util.docutils import SphinxDirective, SphinxTranslator

logger = logging.getLogger(__name__)


class custom_edit_node(nodes.General, nodes.Element):
    """custom edit node"""

    pass


class CustomEdit(SphinxDirective):
    """Customize edit this page button

    Only compatblie with the current theme. The directive require the complete raw file path (from github).

    Example::
        .. custom-edit:: https://raw.githubusercontent.com/openforis/sepal-doc/custom_edit/README.rst
    """

    has_content = False
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {}

    def run(self) -> List[custom_edit_node]:

        raw_link = self.arguments[0]
        split_url = raw_link.replace("raw.githubusercontent.com", "github.com").split(
            "/"
        )
        split_url.insert(5, "edit")
        link = "/".join(split_url)

        return [custom_edit_node(link=link)]


def visit_custom_edit_node_html(
    translator: SphinxTranslator, node: custom_edit_node
) -> None:
    """Entry point of the html custom edit node"""

    html = """
    <script>
        document.addEventListener('DOMContentLoaded', function() {{
            var div = document.getElementsByClassName("tocsection editthispage")[0];
            var link = div.getElementsByTagName("a")[0];
            link.href = "{}";
        }});
    """

    translator.body.append(html.format(node["link"]))


def depart_custom_edit_node_html(
    translator: SphinxTranslator, node: custom_edit_node
) -> None:
    """exit point of the html custom edit node"""

    translator.body.append("</script>")


def visit_custom_edit_node_unsuported(
    translator: SphinxTranslator, node: custom_edit_node
) -> None:
    """Entry point of the ignored custom edit node."""
    logger.warning("CustomEdit: unsupported output format (node skipped)")
    raise nodes.SkipNode


def setup(app: Sphinx) -> Dict[str, bool]:
    app.add_node(
        custom_edit_node,
        html=(visit_custom_edit_node_html, depart_custom_edit_node_html),
        epub=(visit_custom_edit_node_unsuported, None),
        latex=(visit_custom_edit_node_unsuported, None),
        man=(visit_custom_edit_node_unsuported, None),
        texinfo=(visit_custom_edit_node_unsuported, None),
        text=(visit_custom_edit_node_unsuported, None),
    )
    app.add_directive("custom-edit", CustomEdit)

    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
