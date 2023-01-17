"""Build the documentation in isolated environment

The nox run are build in isolated environment that will be stored in .nox. to force the venv update, remove the .nox/xxx folder.
"""

import nox

@nox.session(reuse_venv=True)
def docs(session):
    """Build the documentation."""
    session.install("-r", "requirements.txt")
    session.run("sphinx-build", "-b", "html", "docs/source", "docs/build")