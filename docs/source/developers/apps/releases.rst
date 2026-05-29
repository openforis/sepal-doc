.. _developers_apps_releases:

Create a release
================
*Ship a new version of an app already in the SEPAL catalog*

Once your app is in the catalog (see :ref:`developers_apps_catalog`), the way
you ship a new version depends on the app's ``endpoint`` (see
:ref:`developers_apps_types`):

-   **Jupyter apps** (and :ref:`kernels <developers_apps_kernels>`, which are
    just hidden jupyter apps) are not pinned to a commit. The app-manager
    checks out the tip of the catalog's ``branch`` (defaulting to ``HEAD``)
    every time the sandbox refreshes the app, so a release is just a push to
    that branch in your source repository — no catalog change is needed.
-   **Docker apps** are pinned in the catalog to an exact commit SHA. SEPAL
    keeps running the old commit until that ``commit`` field is advanced, so a
    release is, in practice, a pull request against the catalog.

The rest of this page describes each flow in turn.

.. _developers_apps_releases_jupyter:

Jupyter and kernel apps
-----------------------

These endpoints don't take a ``commit`` field in the catalog — only
``branch`` (which defaults to ``HEAD``). On every sandbox refresh the
app-manager runs the equivalent of ``git fetch`` + checkout of that branch's
tip, so whatever is at the head of the tracked branch is what users get.

Releasing a new version
~~~~~~~~~~~~~~~~~~~~~~~

Push the change to the branch the catalog tracks for your app. The next time
the user's sandbox refreshes the app, the new tip is picked up automatically.
No catalog PR is required.

.. _developers_apps_releases_branch:

The release branch convention
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Because every push to the tracked branch is effectively a release, most
contributors keep a dedicated ``release`` branch and pin ``"branch":
"release"`` in the catalog rather than ``main``. You develop on ``main`` and
merge into ``release`` only when you intend to publish — that way unreviewed
work on ``main`` doesn't go live the moment it is pushed.

This is a convention, not a requirement. Any branch works; if you pin
``main``, every push to ``main`` is a release.

.. _developers_apps_releases_docker:

Docker apps
-----------

Docker apps carry a required ``commit`` SHA in the catalog. The app-launcher
runs ``git fetch origin <branch>`` followed by
``git checkout --detach <commit>``, so SEPAL only ever runs that exact commit
— regardless of what is at the tip of ``branch``. Shipping a new version
therefore means advancing the ``commit`` field in the catalog.

There are two ways to do that: a manual pull request, or an automated bump
triggered when your source repository publishes a release.

The release branch convention
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Many docker apps pin ``"branch": "release"`` rather than ``main``. Since the
catalog validation requires the pinned ``commit`` to be reachable from
``branch``, keeping a dedicated ``release`` branch lets you continue
developing on ``main`` while controlling exactly which commits are eligible to
be pinned: you merge into ``release`` only when you intend to publish, and
that merge commit is the one you pin.

This is a convention, not a requirement — any branch works as long as the
pinned commit is reachable from it.

Manual release
~~~~~~~~~~~~~~

#.  Push the code you want to ship and note the commit SHA on your release
    branch.
#.  Open a PR against ``apps.test.json`` changing the ``commit`` field of your
    app's entry (and ``branch`` if it moved).
#.  The ``Review helper`` bot posts a compare link showing exactly what changed
    upstream between the old and new commit, with risk flags. A maintainer
    reviews and merges; the change goes live on test.sepal.io.
#.  Promote to sepal.io with a second PR against ``apps.prod.json`` (or the
    ``Promote app to production`` workflow).

.. tip::

    Validation requires the new commit to be an *ancestor of* (or equal to) the
    branch tip — exactly what the app-launcher needs, since it runs
    ``git fetch origin <branch>`` then ``git checkout --detach <commit>``. You
    can spot-check this before opening the PR:

    .. code-block:: bash

        gh api repos/<owner>/<repo>/compare/<branch>...<commit> --jq '.ahead_by'
        # must print 0

Automated release from your source repo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The catalog can bump a docker app automatically when your repository publishes
a GitHub release. The catalog's ``update-from-release.yml`` workflow listens
for a ``repository_dispatch`` event of type ``bump-app``; on receipt it
updates the app's ``commit`` in ``apps.test.json`` and opens a pull request
for a maintainer to review.

To wire this up, add a workflow to your app's repository that sends the
dispatch on release. The snippet below is a starting point — adjust the app
``id`` and the catalog repository to match your setup:

.. code-block:: yaml

    # .github/workflows/notify-sepal-catalog.yml in your app repo
    name: Notify SEPAL catalog
    on:
      release:
        types: [published]

    jobs:
      bump:
        runs-on: ubuntu-latest
        steps:
          - name: Dispatch bump-app to the catalog
            run: |
              gh api repos/dfguerrerom/sepal-apps-catalog/dispatches \
                -f event_type=bump-app \
                -F client_payload[id]="my-app" \
                -F client_payload[commit]="${GITHUB_SHA}"
            env:
              GH_TOKEN: ${{ secrets.SEPAL_CATALOG_DISPATCH_TOKEN }}

The token must have permission to dispatch to the catalog repository. The bump
only updates ``commit`` — never ``branch`` — and still goes through the normal
validation, risk-flag review, and maintainer merge before reaching test.

.. note::

    The exact ``client_payload`` fields the catalog expects may evolve. Confirm
    against the catalog's ``update-from-release.yml`` and ``docs/ci.md`` before
    relying on this in production.

.. seealso::

    The end-to-end lifecycle diagram lives on the section landing page —
    :ref:`developers_apps`.
