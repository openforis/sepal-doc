"""Build the documentation in isolated environment

The nox run are build in isolated environment that will be stored in .nox. to force the venv update, remove the .nox/xxx folder.
"""

import nox


@nox.session(reuse_venv=True)
def docs(session):
    """Build the documentation."""
    session.install("-r", "requirements.txt")
    session.run("sphinx-build", "-b", "html", "docs/source", "docs/build/html")


@nox.session(reuse_venv=True)
def i18n(session):
    """Create the translation files"""
    supported_languages = ["en", "fr", "es", "ar", "pt", "zh", "ru", "sv", "it"]
    session.install("-r", "requirements.txt")
    session.install("sphinx", "sphinx-intl")
    session.run("sphinx-build", "-b", "gettext", "docs/source", "docs/build/gettext")
    session.run(
        "sphinx-intl",
        "update",
        "-p",
        "docs/build/gettext",
        "--locale-dir",
        "docs/source/_locale",
        *[f"-l {l}" for l in supported_languages],
    )
