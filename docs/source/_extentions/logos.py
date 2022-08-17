# -*- coding: utf-8 -*-

"""
ReST directive for creating a list of logo.
The directive does note require any argument.
Example::
    .. logos:: funders
"""
from pathlib import Path
import json

from docutils import nodes
from docutils.parsers.rst import Directive
    

class Logos(Directive):
    has_content = True
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {}
    
    def run(self):
        
        # accommodate different logo shapes (width values in rem)
        sizes = {"xs": 6, "sm": 8, "md": 10, "lg": 12, "xl": 15, "xxl": 20}
        
        # get the env 
        env = self.state.document.settings.env
        
        # Write the html content line by line for readability 
        # init the html content 
        html = '<div class="container my-4">\n'
        html += '\t<div id="funder-logos" class="d-flex flex-wrap flex-row justify-content-center align-items-center">\n'
        
        # get the funder list as a dict 
        data_dir = Path(__file__).parents[1]/"data"
        logo_file = data_dir/f"{self.arguments[0]}.json"
        funders = json.loads(logo_file.read_text())
        for k, v in funders.items():
            
            # get informations from the parameters
            size = sizes[v["size"]]
            link = v["html"]
            light_logo = f"_static/logos/{v['light']}"
            dark_logo = f"_static/logos/{v['dark']}"
            
            # write the html files
            html += f'\t\t<div class="my-1 mx-2" style="width:{size}rem;">\n'
            html += f'\t\t\t<a href="{link}">'
            html += f'\t\t\t\t<img class="card-img only-light" src="{light_logo}">'
            html += f'\t\t\t\t<img class="card-img only-dark" src="{dark_logo}">'
            html += '\t\t\t</a>'
            html += '\t\t</div>'
        
        # close the container 
        html += '\t</div>'
        html += '</div>'
        
        return [nodes.raw('', html, format='html')]
    
def setup(builder):
    builder.add_directive("logos", Logos)
        