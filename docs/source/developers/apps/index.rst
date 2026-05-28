.. _developers_apps:

Develop apps
============
*Build, release and publish your own apps on the SEPAL platform*

These pages explain how SEPAL decides which app code to run and how that code
reaches the platform — useful when you want to add an app, ship a new version
of an existing one, or package a reusable environment for a notebook or
workflow.

.. note::

    The set of apps SEPAL runs is curated in the
    `dfguerrerom/sepal-apps-catalog <https://github.com/dfguerrerom/sepal-apps-catalog>`__
    repository. Getting an app onto SEPAL — or updating one — means opening a
    pull request there. For docker apps, the catalog also pins the *exact
    commit* SEPAL will run; for jupyter and shiny apps, the catalog records the
    ``branch`` and SEPAL still runs the tip of that branch. The pages below
    walk through both flows.

How an app reaches SEPAL
------------------------

.. graphviz::

    digraph lifecycle {
        rankdir=LR;
        node [shape=box, fontname="sans-serif"];

        repo   [label="App source repo\n(your GitHub)"];
        rel    [label="Release / version", shape=ellipse];
        pr     [label="Catalog PR\n(apps.test.json)"];
        ci     [label="CI review\n(validate + risk flags)"];
        test   [label="test.sepal.io", shape=ellipse];
        prod   [label="sepal.io", shape=ellipse];
        kernel [label="Kernel build\n(sepal_environment.yml)", shape=box, style=dashed];

        repo -> rel -> pr -> ci -> test;
        test -> prod [label="promote PR"];
        repo -> kernel [label="jupyter apps", style=dashed];
        kernel -> test [style=dashed];
    }

Contents
--------

.. toctree::
    :maxdepth: 1

    Docker vs. Jupyter apps<app_types>
    Request a new app<app_catalog>
    Request a new kernel<kernels>
    Create a release<releases>
