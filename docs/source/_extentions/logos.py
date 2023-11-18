"""Logo extension to create a list of logos"""
import json
from pathlib import Path
from typing import Dict, List

from docutils import nodes
from sphinx.application import Sphinx
from sphinx.util import logging
from sphinx.util.docutils import SphinxDirective, SphinxTranslator

logger = logging.getLogger(__name__)

SIZES = {"xs": 6, "sm": 8, "md": 10, "lg": 12, "xl": 15, "xxl": 20}
"Accommodate different logo shapes (width values in rem)"


class logo_node(nodes.General, nodes.Element):
    """Logo Node"""

    pass


class Logos(SphinxDirective):
    """Logo directive to create a grid of logos from a json file

    Example:
        .. logo:: funder
    """

    has_content = True
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {}

    def run(self) -> List[logo_node]:

        # get the env
        self.env

        # get the data
        data_dir = Path(__file__).parents[1] / "_data" / "logo"
        logo_file = data_dir / f"{self.arguments[0]}.json"
        logos = json.loads(logo_file.read_text())

        return [logo_node(logos=logos)]


def visit_logo_node_html(translator: SphinxTranslator, node: logo_node) -> None:
    """Entry point of the html logo node"""

    # Write the html content line by line for readability
    # init the html content
    html = '<div class="container my-4">\n'
    html += '\t<div id="funder-logos" class="d-flex flex-wrap flex-row justify-content-center align-items-center">\n'

    for v in node["logos"].values():

        # get information from the parameters
        size = SIZES[v["size"]]
        link = v["html"]
        light_logo = f"_static/logos/{v['light']}"
        dark_logo = f"_static/logos/{v['dark']}"

        # write the html files
        html += f'\t\t<div class="my-1 mx-2" style="width:{size}rem;">'
        html += f'<a href="{link}">'
        html += f'<img class="card-img only-light" src="{light_logo}">'
        html += f'<img class="card-img only-dark" src="{dark_logo}">'
        html += "</a>"
        html += "</div>\n"

    translator.body.append(html)


def depart_logo_node_html(translator: SphinxTranslator, node: logo_node) -> None:
    """exit from the html node and close the container"""

    translator.body.append("\t</div>\n</div>\n")


def visit_logo_node_unsuported(translator: SphinxTranslator, node: logo_node) -> None:
    """Entry point of the ignored logo node."""
    logger.warning("Logo: unsupported output format (node skipped)")
    raise nodes.SkipNode


def setup(app: Sphinx) -> Dict[str, bool]:
    app.add_node(
        logo_node,
        html=(visit_logo_node_html, depart_logo_node_html),
        epub=(visit_logo_node_unsuported, None),
        latex=(visit_logo_node_unsuported, None),
        man=(visit_logo_node_unsuported, None),
        texinfo=(visit_logo_node_unsuported, None),
        text=(visit_logo_node_unsuported, None),
    )
    app.add_directive("logos", Logos)

    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
