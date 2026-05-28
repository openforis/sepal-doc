.. _developers_apps_catalog:

Request a new app
=================
*Add your app to the SEPAL apps catalog so it appears on the platform*

The catalog
-----------

The list of apps SEPAL runs lives in a dedicated repository,
`dfguerrerom/sepal-apps-catalog <https://github.com/dfguerrerom/sepal-apps-catalog>`__.
For docker apps the catalog pins the exact commit SEPAL will run; for jupyter
and shiny apps it records the ``branch`` and SEPAL runs its tip. Either way,
adding or updating an app means opening a pull request against this catalog,
where a maintainer reviews the change before it goes live.

The catalog ships two files:

-   ``apps.test.json`` — apps available on test.sepal.io (the staging
    environment used to validate changes before they reach end users)
-   ``apps.prod.json`` — apps available on sepal.io (the production environment)

New apps always land in ``apps.test.json`` first and are promoted to
``apps.prod.json`` only once they behave correctly on test.sepal.io.

Anatomy of a catalog entry
--------------------------

An app is a JSON object in the ``apps`` array. The schema only enforces ``id``
and ``label`` as universally required, plus a docker-specific block — but the
catalog convention is to **fill every field** so each entry carries a complete
dashboard listing. The only practical exceptions:

-   ``port`` applies only to docker apps (and is required there).
-   For hidden kernel-only apps (see :ref:`developers_apps_kernels`) the
    user-facing presentation fields (``description``, ``tagline``,
    ``logoRef``, ``projectLink``, ``author``, ``tags``) can be omitted, since
    they are never shown.

Identification and routing
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows: 1
    :widths: 22 22 56

    * - Field
      - When
      - Meaning
    * - ``id``
      - always (schema)
      - Unique identifier across the catalog (``[A-Za-z0-9_.-]+``).
    * - ``label``
      - always (schema)
      - Display name shown on the apps dashboard.
    * - ``endpoint``
      - always
      - How SEPAL runs the app: ``jupyter``, ``shiny``, ``rstudio`` or
        ``docker``. See :ref:`developers_apps_types`.
    * - ``repository``
      - always
      - ``https://github.com/<owner>/<repo>`` of the app source. SEPAL clones
        it to run the app.
    * - ``branch``
      - always
      - Branch the app tracks (commonly ``release``).
    * - ``path``
      - always
      - Entry point the app-launcher routes to. For jupyter, the Voila URL of
        the notebook (e.g.
        ``/sandbox/jupyter/voila/render/shared/apps/<app>/ui.ipynb``); for
        shiny, the sandbox path of the Shiny project; for docker, **must
        match** ``/api/app-launcher/<id>`` (schema-enforced).

Docker-only fields
~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows: 1
    :widths: 22 22 56

    * - Field
      - When
      - Meaning
    * - ``commit``
      - docker only (schema)
      - Full 40-character lowercase commit SHA. Required for
        ``endpoint: docker``; not allowed for other endpoints, which track the
        branch tip.
    * - ``port``
      - docker only (schema)
      - Container port the docker app listens on. Integer 1–65535. Must be
        unique across the catalog — see
        `dfguerrerom/sepal-apps-catalog#41 <https://github.com/dfguerrerom/sepal-apps-catalog/issues/41>`__.

Presentation
~~~~~~~~~~~~~

These fields populate the dashboard tile and the app's detail page. Skip them
*only* on hidden kernel-only entries.

.. list-table::
    :header-rows: 1
    :widths: 22 22 56

    * - Field
      - When
      - Meaning
    * - ``author``
      - visible apps
      - Who maintains the app (free-form string).
    * - ``description``
      - visible apps
      - Long-form description shown on the app's detail page.
    * - ``tagline``
      - visible apps
      - One-line summary shown on the dashboard tile.
    * - ``logoRef``
      - visible apps
      - Filename of the logo asset bundled with the catalog (e.g.
        ``my-app.svg``).
    * - ``projectLink``
      - visible apps
      - URL to the project's home page, docs, or upstream repository.
    * - ``tags``
      - visible apps
      - Array of tag values defined in the catalog's top-level ``tags`` block
        (e.g. ``["TOOLS", "TIME_SERIES"]``).

Behaviour flags
~~~~~~~~~~~~~~~~

Optional booleans that alter how the app is listed or launched. Defaults are
all ``false``.

.. list-table::
    :header-rows: 1
    :widths: 22 22 56

    * - Field
      - When
      - Meaning
    * - ``hidden``
      - optional
      - If ``true``, the app builds but does not show a dashboard tile. Used
        for packaged kernels — see :ref:`developers_apps_kernels`.
    * - ``pinned``
      - optional
      - Pin the app to the top of the dashboard.
    * - ``googleAccountRequired``
      - optional
      - The app needs a connected Google account (e.g. for GEE).
    * - ``single``
      - optional
      - Only one instance of this app can run at a time per user (used by the
        built-in ``jupyter-notebook``, ``jupyter-lab`` and ``rstudio`` tools).
    * - ``skip``
      - optional
      - Temporarily skip building/serving this app without removing the entry.

A typical jupyter entry — every field a user sees on the dashboard is filled
in:

.. code-block:: json

    {
      "id": "my-app",
      "label": "My App",
      "endpoint": "jupyter",
      "repository": "https://github.com/me/my-sepal-app",
      "branch": "release",
      "path": "/sandbox/jupyter/voila/render/shared/apps/my-app/ui.ipynb",
      "author": "Me and contributors",
      "tagline": "Short one-line summary shown on the dashboard tile.",
      "description": "Longer description shown on the app's detail page.",
      "logoRef": "my-app.svg",
      "projectLink": "https://github.com/me/my-sepal-app",
      "tags": [
        "TIME_SERIES"
      ]
    }

A docker entry adds the docker-only ``commit``, ``port`` and the
schema-enforced ``/api/app-launcher/<id>`` path; the presentation fields are
the same:

.. code-block:: json

    {
      "id": "my-docker-app",
      "label": "My Docker App",
      "endpoint": "docker",
      "repository": "https://github.com/me/my-sepal-docker-app",
      "branch": "main",
      "commit": "0123456789abcdef0123456789abcdef01234567",
      "port": 8767,
      "path": "/api/app-launcher/my-docker-app",
      "author": "Me and contributors",
      "tagline": "Short one-line summary shown on the dashboard tile.",
      "description": "Longer description shown on the app's detail page.",
      "logoRef": "my-docker-app.svg",
      "projectLink": "https://github.com/me/my-sepal-docker-app",
      "tags": [
        "TOOLS"
      ]
    }

Adding the app
--------------

#.  Open a pull request adding your entry to ``apps.test.json``. The fastest
    way is to edit the file directly on GitHub:
    `edit apps.test.json <https://github.com/dfguerrerom/sepal-apps-catalog/edit/main/apps.test.json>`__.
    For a docker app, ``commit`` must be a full 40-character SHA that exists
    on the declared ``branch``.
#.  The ``Validate catalog`` and ``Review helper`` workflows run automatically.
    Validation is a blocking gate (schema, canonical formatting, and — for
    docker apps — a check that the commit is reachable from its branch). The
    review helper posts a single PR comment with a per-app diff and *risk
    flags* (new dependencies, network calls, shell-outs) to help maintainers
    review safely.
#.  A SEPAL maintainer reviews and merges. Once merged, the app appears on
    test.sepal.io within minutes.
#.  When you are happy with its behaviour on test.sepal.io, promote it to
    production — see `Promoting to production`_.

Promoting to production
-----------------------

Promotion copies the *exact same pinned reference* (commit for docker, branch
for the others) from ``apps.test.json`` into ``apps.prod.json``. There are two
mechanical ways to do it:

-   Open a follow-up PR copying the entry into ``apps.prod.json``, or
-   Trigger the ``Promote app to production`` workflow
    (``workflow_dispatch``, pick an app), which opens that PR for you.

Either way the same validation and review checks run, a maintainer merges, and
the app goes live on sepal.io.

.. note::

    **Promotion is currently restricted to the catalog owner.** The
    ``workflow_dispatch`` trigger and the merge step both require write access
    to the catalog repository, so contributors cannot promote their own apps
    today — they have to ask the catalog owner to do it. Tracked in
    `dfguerrerom/sepal-apps-catalog#40 <https://github.com/dfguerrerom/sepal-apps-catalog/issues/40>`__.

Working on the catalog locally
------------------------------

The catalog files use canonical ``JSON.stringify(parsed, null, 2)`` formatting
(2-space indent, one-element arrays expanded, trailing newline). A
``.prettierignore`` keeps editor formatters off them, and CI rejects PRs that
don't match. Install the pre-commit hooks once so problems are caught before
they fail CI:

.. code-block:: bash

    pip install pre-commit              # or: pipx install pre-commit
    pre-commit install
    npm install --prefix .github/workflows/scripts

To re-canonicalize a file before pushing:

.. code-block:: bash

    node -e 'const fs=require("fs"); for (const f of ["apps.test.json","apps.prod.json"]) fs.writeFileSync(f, JSON.stringify(JSON.parse(fs.readFileSync(f,"utf8")),null,2)+"\n")'

.. seealso::

    The catalog's own ``docs/contributing.md`` and ``docs/ci.md`` document
    every workflow, check, and script in detail.
