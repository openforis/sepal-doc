.. _developers_apps_types:

Docker vs. Jupyter apps
=======================
*The two endpoints you'll choose between, and where each one fits*

Every catalog entry declares an ``endpoint`` that tells SEPAL how to run the
app. For new apps the practical choice is between ``docker`` and ``jupyter``.

.. note::

    ``shiny`` is a legacy endpoint and is no longer recommended for new apps —
    package the same UX as a Jupyter/Voila app instead. ``rstudio`` is
    reserved for the built-in RStudio tool. Both still work, but neither
    should be picked for anything new.

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
      - ``jupyter``
    * - Where it runs
      - Its own container, on its own port, on the shared SEPAL server
      - Inside the user's own SEPAL instance (sandbox), served through Voila
    * - Who pays for compute
      - The shared SEPAL server — all users hit the same instance
      - The user, on the instance size they have selected
    * - Versioning
      - Pinned to a commit SHA (required)
      - Tracks the catalog's ``branch``; no commit pin
    * - Code location
      - Cloned from ``repository`` into the container
      - Cloned from ``repository`` into the shared sandbox at
        ``/home/sepal-user/shared/apps/<app>/``
    * - Isolation
      - Strong — separate container and dependencies
      - Own micromamba kernel built from ``sepal_environment.yml``
        (see :ref:`developers_apps_kernels`)
    * - Update trigger
      - Catalog PR bumps ``commit`` → app-manager redeploys
      - app-manager refreshes the clone to the branch tip and rebuilds the
        kernel if the env file changed

Docker apps
-----------

A docker app lives in its own repository and runs in its own container with a
dedicated ``port`` on the shared SEPAL server. Because it is fully isolated,
the catalog schema requires ``repository``, ``branch``, ``commit``, ``port``
and ``path`` for every ``endpoint: docker`` entry.

When SEPAL launches the app it runs the equivalent of:

.. code-block:: bash

    git fetch origin <branch>
    git checkout --detach <commit>

That is why the pinned ``commit`` must be reachable from ``branch`` (see
:ref:`developers_apps_releases`). The app's dependencies are baked into its
container, so its update cycle is independent of the rest of the platform — it
changes only when you bump its commit in the catalog.

Because the docker app runs on the shared SEPAL server, every user hits the
same instance. That makes docker a good fit for **lightweight, low-compute
apps that act as a single service for many users** — interfaces over a small
API, lookups, light visualizations, dashboards. It is *not* a good fit for
heavy per-user compute: there is only one container backing all users.

Jupyter apps
------------

A jupyter app does not get its own container. Its code is cloned from the
``repository`` into the shared sandbox under
``/home/sepal-user/shared/apps/<app>/``, and its ``ui.ipynb`` notebook is
rendered with `Voila <https://voila.readthedocs.io>`__ (hence catalog paths
such as ``/sandbox/jupyter/voila/render/shared/apps/<app>/ui.ipynb``).
Crucially, it runs **inside each user's own SEPAL instance** — so the compute
budget is whatever the user has provisioned for themselves.

Versioning is by branch, not by commit: the app-manager keeps the cloned
``shared/apps/<app>/`` working tree on the tip of the catalog's ``branch`` and
rebuilds the app's kernel whenever ``sepal_environment.yml`` (or
``requirements.txt``) changes — see :ref:`developers_apps_kernels`. Pushing to
that branch is enough to ship a new version; no catalog PR is required (the
catalog PR is only needed to *list* the app in the first place).

Because compute lives on the user's instance, a jupyter app is the right
choice for **heavy, scalable, per-user workloads**: anything where the user
needs to be able to size their machine to the job — training pipelines, large
geospatial analyses, model inference, parallel processing.

When to use which
-----------------

A simple rule of thumb:

.. list-table::
    :header-rows: 1
    :widths: 24 38 38

    * -
      - Use ``docker``
      - Use ``jupyter``
    * - Compute profile
      - Light; same load no matter who is using it
      - Heavy or variable; each user should be able to scale their own
        instance
    * - Usage pattern
      - Single backend service serving many users
      - Per-user notebook session, isolated per user
    * - Versioning needs
      - You want strict, audited control of *exactly* which commit is live
      - Push-to-branch is a fine release model
    * - Runtime needs
      - Custom system stack, services, ports, or a non-Python runtime
      - Standard SEPAL geospatial / scientific Python stack (extended via
        ``sepal_environment.yml``)

If the answer to most of these points the same way, that's your endpoint. If
the app is genuinely a notebook UI doing heavy compute, jupyter is almost
always the right pick — that is the most common pattern on SEPAL.

.. graphviz::

    digraph endpoints {
        rankdir=LR;
        node [shape=box, fontname="sans-serif"];

        catalog [label="Catalog entry\n(endpoint)"];
        docker  [label="Docker app\nshared SEPAL server\nprivate container + port\npinned commit"];
        jupyter [label="Jupyter app\nuser's own instance\nVoila + kernel\nbranch tip"];

        catalog -> docker  [label="docker"];
        catalog -> jupyter [label="jupyter"];
    }
