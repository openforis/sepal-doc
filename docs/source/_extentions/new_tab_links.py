"""Open links from the remote-access guides in a new browser tab."""

from docutils import nodes


def set_link_targets(app, doctree, docname):
    if docname not in {"developers/vscode", "setup/ssh_keys"}:
        return
    for node in doctree.findall(nodes.reference):
        if node.get("refuri") and not node["refuri"].startswith("#"):
            node["target"] = "_blank"
            node["rel"] = "noopener noreferrer"


def setup(app):
    app.connect("doctree-resolved", set_link_targets)
    return {"parallel_read_safe": True, "parallel_write_safe": True}
