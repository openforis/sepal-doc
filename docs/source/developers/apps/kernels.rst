.. _developers_apps_kernels:

Request a new kernel
====================
*Package an environment once and share it with every SEPAL user as a named Jupyter kernel*

A "kernel" in the SEPAL catalog is really just a special-purpose jupyter app:
the same catalog entry, the same PR flow, the same release lifecycle. The only
difference is *intent* — the deliverable is the environment, not a notebook UI.
If you have read :ref:`developers_apps_catalog`, you already know 90% of how to
ship one.

Why request a kernel
--------------------

Some notebooks need a large or unusual environment: a deep-learning stack, a
pinned GDAL build, a model with awkward native dependencies. Asking every user
— or every training participant — to build that environment by hand is slow,
fragile, and easy to get subtly wrong.

A shared kernel solves that. You package the environment once, in a repository;
SEPAL builds it centrally and exposes it as a named Jupyter kernel that lives
in the shared sandbox. Every user then simply *selects* that kernel for the
relevant notebook — no per-user installation, and everyone runs the same,
reproducible environment.

This is the right approach when:

-   You are preparing a notebook or workflow for a training and want every
    participant on an identical environment.
-   A notebook needs heavy dependencies (GPU/ML, large geospatial stacks) that
    are wasteful to rebuild per user.
-   You want a stable, named environment that several notebooks can share.

It is *not* the right approach for quick, personal experiments. For an
environment only you need, build it yourself with :guilabel:`uv` or
:guilabel:`micromamba` — see :ref:`env_management`.

It's the same flow as a jupyter app
------------------------------------

A kernel-only entry in the catalog is just a jupyter app that:

-   has ``"hidden": true`` (no dashboard tile — see below), and
-   ships a ``sepal_environment.yml`` at the root of its repository.

Everything else — the PR against ``apps.test.json``, the validation and
review-helper workflows, the promotion to ``apps.prod.json`` — works exactly as
described in :ref:`developers_apps_catalog`.

The one extra behaviour, which fires automatically whenever the app-manager
updates a jupyter app, is the kernel build itself: if the cloned repository
contains a ``sepal_environment.yml`` (or a legacy ``requirements.txt``), SEPAL
builds an isolated environment from it and registers it as a named Jupyter
kernel. For a ``sepal_environment.yml`` the build is, in essence:

.. code-block:: bash

    micromamba create -y -p <venv_path> -f sepal_environment.yml
    <venv_path>/bin/pip install ipykernel

The script then writes a ``kernel.json`` so the environment shows up in
JupyterLab as ``(venv) <app label>``, and wires the geospatial environment
variables (``PROJ_LIB``, ``PROJ_DATA``, ``GDAL_DATA``) to the environment's own
data directories. The kernel is rebuilt only when the environment file changes
(the script compares timestamps against an ``.installed`` marker), so unchanged
apps don't pay a rebuild cost on every update.

Hiding the app
--------------

A packaged kernel usually has no dashboard UI of its own — it exists to back
*other* notebooks. Set ``"hidden": true`` on its catalog entry so SEPAL builds
the environment and registers the kernel without showing a tile in the apps
dashboard.

Worked example: ``sepal-sam``
------------------------------

The catalog entry below is a real, hidden kernel app. Its description is simply
*"SAM environment"* — it ships the environment for SAM-based notebooks and
never appears in the dashboard:

.. code-block:: json

    {
      "hidden": true,
      "id": "sepal-sam",
      "label": "Sepal SAM",
      "endpoint": "jupyter",
      "repository": "https://github.com/dfguerrerom/sepal-sam",
      "branch": "main",
      "description": "SAM environment"
    }

Because the ``sepal-sam`` repository contains a ``sepal_environment.yml``,
SEPAL builds its micromamba environment and registers a ``(venv) Sepal SAM``
kernel. Any notebook a user opens can then select that kernel and run against
the SAM stack immediately.

.. _developers_apps_kernels_envfile:

Recommended: ``sepal_environment.yml``
--------------------------------------

Declare your kernel with a ``sepal_environment.yml`` at the root of the app
repository. It is a standard conda/micromamba environment file, and it is the
preferred way to define a SEPAL kernel because micromamba bundles native
libraries (GDAL, GEOS, CUDA, HDF5, …) inside the environment — so it keeps
working when SEPAL upgrades system-level libraries. A plain ``requirements.txt``
is still supported for backward compatibility, but it installs into a
system-Python venv and can break on platform upgrades.

A minimal example:

.. code-block:: yaml

    name: sepal-sam
    channels:
      - conda-forge
    dependencies:
      - python=3.12
      - gdal
      - rasterio
      - pip:
        - segment-geospatial

.. tip::

    You do not need to add ``ipykernel`` yourself — SEPAL installs it into the
    environment when it builds the kernel.

Once the file is in your repository and the app is in the catalog (see
:ref:`developers_apps_catalog`), every release that changes
``sepal_environment.yml`` triggers a rebuild of the shared kernel on the next
update.

.. seealso::

    :ref:`env_management` — managing your *own* environments and kernels
    interactively, when you don't need a shared, centrally built one.
