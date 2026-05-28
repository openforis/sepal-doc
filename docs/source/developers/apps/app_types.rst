.. _developers_apps_types:

Docker vs. Jupyter apps
=======================
*Two ways an app runs on SEPAL, with different lifecycles*

Every catalog entry declares an ``endpoint`` that tells SEPAL how to run the
app. The two you will meet most often are ``docker`` and ``jupyter`` (``shiny``
and ``rstudio`` behave like ``jupyter`` for lifecycle purposes). The choice
affects how the app is isolated, how it is versioned, and how it is updated.

At a glance
-----------

.. list-table::
    :header-rows: 1
    :widths: 28 36 36

    * -
      - Docker app
      - Jupyter app
    * - ``endpoint``
      - ``docker``
      - ``jupyter`` (also ``shiny``, ``rstudio``)
    * - Runs in
      - Its own container, on its own port
      - The shared user sandbox, served through Voila
    * - Versioning
      - Pinned to a commit SHA (required)
      - Tracks its branch; no commit pin
    * - Code location
      - Cloned from ``repository``
      - ``shared/apps/<app>/ui.ipynb`` in the sandbox
    * - Isolation
      - Strong — separate container and dependencies
      - Shares the sandbox's Python/system stack (plus an
        optional packaged kernel)
    * - Lifecycle
      - Independent; redeploys on commit change
      - Tied to the sandbox and its app-manager-built kernel

Docker apps
-----------

A docker app lives in its own repository and runs in its own container with a
dedicated ``port``. Because it is fully isolated, the catalog schema requires
``repository``, ``branch``, and ``commit`` for every ``endpoint: docker`` entry.

When SEPAL launches the app it runs the equivalent of:

.. code-block:: bash

    git fetch origin <branch>
    git checkout --detach <commit>

That is why the pinned ``commit`` must be reachable from ``branch`` (see
:ref:`developers_apps_releases`). The app's dependencies are baked into its container, so
its lifecycle is independent of the rest of the platform — it changes only when
you bump its commit in the catalog.

Use a docker app when your tool needs strong isolation, its own service, a
specific port, or a runtime that differs from the SEPAL sandbox.

Jupyter (and shiny, rstudio) apps
---------------------------------

A jupyter app does not get its own container. Its code is checked out into the
shared user sandbox under ``shared/apps/<app>/`` and its ``ui.ipynb`` notebook is
rendered with `Voila <https://voila.readthedocs.io>`__ (hence catalog paths such
as ``/sandbox/jupyter/voila/render/shared/apps/<app>/ui.ipynb``). It runs against
the sandbox's Python and system libraries rather than a private container, so it
does not carry a pinned ``commit`` — its lifecycle follows the sandbox and the
kernel built for it by the app-manager.

That kernel is where a jupyter app declares the environment it needs. Packaging
that environment correctly — so it is built once and reused — is the subject of
:ref:`developers_apps_kernels`.

Use a jupyter app when your tool is a notebook-based UI that fits the SEPAL
sandbox and benefits from being close to the user's files and the shared
geospatial stack.

.. graphviz::

    digraph endpoints {
        rankdir=LR;
        node [shape=box, fontname="sans-serif"];

        catalog [label="Catalog entry\n(endpoint)"];
        docker  [label="Docker app\nprivate container + port\npinned commit"];
        jupyter [label="Jupyter app\nshared sandbox\nVoila + kernel"];

        catalog -> docker  [label="docker"];
        catalog -> jupyter [label="jupyter / shiny / rstudio"];
    }
