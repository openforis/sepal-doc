"""
copy the module documentation from the corresponding repositories and link it to the SEPAL documentation
"""
from pathlib import Path
from urllib.request import urlretrieve
from shutil import copy
import json 

# dirs 
source_dir = Path(__file__).expanduser().parents[1]
module_dir = source_dir/"modules"
dwn_dir = module_dir/"dwn"
template_dir = source_dir/"_templates"

# templates
tag_template = template_dir/"module_tag.rst"
doc_template = template_dir/"no_module.rst"
index_template = template_dir/"index.rst"

# data 
module_json = source_dir/"data"/'modules'/'en.json'
no_module_url = "https://github.com/openforis/sepal-doc/blob/master/docs/source/_templates/no_module.rst"

# destination file shared by the methods
module_index = module_dir/"index.rst"

def get_index():
    
    [f.unlink() for f in module_dir.glob("*.rst")]
    copy(index_template, module_index)
    
    return
    
    
def get_modules():
    
    # flush the modules folder in case something was left by the previous build
    [f.unlink() for f in dwn_dir.glob("*.rst")]

    module_list = json.loads(module_json.read_text())

    for name in module_list:
    
        dst = dwn_dir / f'{name}.rst'
    
        file = module_list[name].pop("url", no_module_url)
        if file != no_module_url: 
            urlretrieve (file, dst)
        else:
            copy(doc_template, dst)
        
        txt = dst.read_text()
        txt = txt.replace("Module_name", name).replace("=", "="*len(name))
        dst.write_text(txt)
        
        # add the custom edit directive to the file to ensure the "edit this page" 
        # point to the correct file
        with dst.open("a") as f: 
            f.writelines(["", f".. custom-edit:: {file}"])
            
        # prompt for the readthedoc build
        print(f"{name} documentation have been copied to the dwn folder")
            
    return

def get_tags():
    
    module_list = json.loads(module_json.read_text())
    
    # extract the list of tags 
    tags = []
    for module in module_list.values():
        tags += module.get("tag", ["other"])
    tags = list(dict.fromkeys(tags))
    
    for tag in tags:
        
        # create a stub file 
        tag_file = module_dir/f"{tag}.rst"
        copy(tag_template, tag_file)
        txt = tag_file.read_text()
        txt = txt.replace("module_tag", tag.capitalize()).replace("=", "="*len(tag))
        tag_file.write_text(txt)
        
        # add the stub file in the index
        with module_index.open("a") as f:
            f.write(f"\n    {tag}")
            
        # create the toc with all the primary modules
        primary_modules = [
            m for m, v in module_list.items()
            if v.get("tag", ["other"])[0] == tag
        ]
        with tag_file.open("a") as f:
            for m in primary_modules:
                f.write(f"\n    dwn/{m}")
                
        # create a table with the all the included modules (primary and secondary tags)
        secondary_modules = [
            m for m, v in module_list.items()
            if tag in v.get("tag", ["other"])
        ]
        with tag_file.open("a") as f:
            f.write("\n\n")
            f.write(".. csv-table::\n\n")
            for m in secondary_modules:
                f.write(f'    :doc:`dwn/{m}`,...\n')
            f.write("\n")
                
        # prompt for the readthedoc build
        print(f"{tag} stub file have been hydrated")
        
    return
        
    