"""
copy the module documentation from the corresponding repositories and link it to the SEPAL documentation
"""
import json
from pathlib import Path
from shutil import copy
from urllib.request import urlretrieve

# dirs
source_dir = Path(__file__).expanduser().parents[1]
module_dir = source_dir / "modules"
module_dir.mkdir(exist_ok=True)
dwn_dir = module_dir / "dwn"
dwn_dir.mkdir(exist_ok=True)
template_dir = source_dir / "_templates"
locale_dir = source_dir / "_locale"

# templates
tag_template = template_dir / "module_tag.rst"
doc_template = template_dir / "no_module.rst"
index_template = template_dir / "index.rst"

# data
module_json = source_dir / "_data" / "modules" / "en.json"
no_module_url = "https://github.com/openforis/sepal-doc/blob/master/docs/source/_templates/no_module.rst"

# destination file shared by the methods
module_index = module_dir / "index.rst"


def get_index():
    """Create an index file for module from the template"""
    [f.unlink() for f in module_dir.glob("*.rst")]
    copy(index_template, module_index)

    return


def get_modules():
    """Get the documentation file for all modules"""
    # flush the modules folder in case something was left by the previous build
    [f.unlink() for f in dwn_dir.glob("*.rst")]

    module_list = json.loads(module_json.read_text())

    for name in module_list:
        dst = dwn_dir / f"{name}.rst"

        file = module_list[name].get("url", no_module_url)
        if file != no_module_url:
            urlretrieve(file, dst)
        else:
            copy(doc_template, dst)

        txt = dst.read_text()

        # update content if the module was not found
        # it's a customization of the template
        if file == no_module_url:
            txt = txt.replace("Module_name", name).replace("=", "=" * len(name))

        if file != no_module_url:
            # add the custom edit directive to the file to ensure the "edit this page"
            # point to the correct file.
            txt += f"\n.. custom-edit:: {file}\n"

        dst.write_text(txt)

        # prompt for the readthedoc build
        print(f"{name} documentation have been copied to the dwn folder")

    return


def get_tags():
    """Create tags table for the modules"""
    module_list = json.loads(module_json.read_text())

    # extract the list of tags
    tags = []
    for module in module_list.values():
        tags += module.get("tag", ["other"])
    tags = list(dict.fromkeys(tags))

    for tag in tags:
        # create a stub file
        tag_file = module_dir / f"{tag}.rst"
        copy(tag_template, tag_file)
        txt = tag_file.read_text()
        txt = txt.replace("module_tag", tag.capitalize()).replace("=", "=" * len(tag))
        tag_file.write_text(txt)

        # add the stub file in the index
        with module_index.open("a") as f:
            f.write(f"\n    {tag}")

        # create the toc with all the primary modules
        primary_modules = [
            m for m, v in module_list.items() if v.get("tag", ["other"])[0] == tag
        ]
        with tag_file.open("a") as f:
            for m in primary_modules:
                f.write(f"\n    dwn/{m}")

        # create a table with the all the included modules (primary and secondary tags)
        secondary_modules = [
            m for m, v in module_list.items() if tag in v.get("tag", ["other"])
        ]
        with tag_file.open("a") as f:
            f.write("\n\n")
            f.write(".. csv-table::\n\n")
            for m in secondary_modules:
                link = f":doc:`dwn/{m}`"
                desc = module_list[m].get("description", "...")
                f.write(f'    {link},"{desc}"\n')
            f.write("\n")

        # prompt for the readthedoc build
        print(f"{tag} stub file have been hydrated")

    return


def get_translation():
    """Get the translation .po files from the repository"""

    module_list = json.loads(module_json.read_text())
    locale_list = [d.stem for d in locale_dir.glob("*/")]

    # loop in the modules
    for name in module_list:
        locale_folder = module_list[name].get("locale")
        doc_url = module_list[name].get("url")

        if locale_folder is None or doc_url is None:
            print(f"{name} module has no translations in any languages")
            continue

        for loc in locale_list:
            filename = Path(doc_url).stem
            src_file = Path(locale_folder) / loc / "LC_MESSAGES" / f"{filename}.po"
            dst_file = (
                locale_dir / loc / "LC_MESSAGES" / "modules" / "dwn" / f"{name}.po"
            )

            try:
                urlretrieve(src_file, dst_file)
            except Exception:
                print(f"{name} module has no translations in {loc}")


if __name__ == "__main__":
    """Copy the modules documentation"""

    get_index()
    get_modules()
    get_translation()
    get_tags()
