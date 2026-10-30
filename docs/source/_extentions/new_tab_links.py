"""Open external links from the remote-access guides in a new browser tab."""

from urllib.parse import urlparse

from docutils import nodes

DOCNAMES = {"developers/vscode", "setup/ssh_keys", "setup/session_storage"}

# Absolute links to this documentation are internal links, even with a scheme.
INTERNAL_HOSTS = {"docs.sepal.io"}


def is_external(node):
    if node.get("internal"):
        return False
    url = urlparse(node.get("refuri", ""))
    return url.scheme in {"http", "https"} and url.hostname not in INTERNAL_HOSTS


def set_link_targets(app, doctree, docname):
    if docname not in DOCNAMES:
        return
    for node in doctree.findall(nodes.reference):
        if is_external(node):
            node["target"] = "_blank"
            node["rel"] = "noopener noreferrer"


def setup(app):
    app.connect("doctree-resolved", set_link_targets)
    return {"parallel_read_safe": True, "parallel_write_safe": True}
