.. _fix_venvs:

Recovering broken Python environments
======================================

On 5 March 2026, SEPAL sandboxes upgraded from Ubuntu Jammy to Ubuntu Noble. As part of this upgrade, the system Python changed from version 3.10 to 3.12. This was a deliberate and necessary change: Python 3.10 reaches end of life in October 2026, meaning it will no longer receive security patches, and an increasing number of libraries are dropping support for it and requiring Python 3.11 or newer. Staying on 3.10 would eventually mean being locked out of updated packages and exposed to unpatched security issues.

If you created Python virtual environments using ``python -m venv`` on SEPAL before this upgrade, those environments are now broken. This page explains why, and how to recover.

.. note::

   This only affects environments created with ``python -m venv``. Environments created with :guilabel:`uv` or :guilabel:`micromamba` are not affected.

See :ref:`env_management` for full guidance on using :guilabel:`uv` and :guilabel:`micromamba` — better alternatives that will not break when SEPAL upgrades Python in the future.

.. note::

   Python 3.10 reaches end of life on 4 October 2026. Rather than putting effort into restoring environments on the old version, consider migrating to Python 3.12 at the same time.

.. _fix_venvs_why:

Why venvs break after a Python upgrade
----------------------------------------

A venv is not a fully self-contained copy of Python. It is a lightweight directory structure that relies on the system Python being present at a specific path. When you run ``python -m venv myenv``, it records the exact path to the Python binary (e.g. ``/usr/bin/python3.10``) and creates symbolic links inside the environment's ``bin/`` directory pointing back to it. Installed packages land in a versioned subdirectory, for example ``lib/python3.10/site-packages/``.

When the system Python changes from 3.10 to 3.12, two things go wrong simultaneously:

- The symlinks inside ``bin/`` now point to a Python binary that no longer exists at the recorded path, so the environment cannot start correctly.
- Any packages with compiled C extensions (numpy, scipy, cryptography, etc.) were built against the Python 3.10 ABI. Python 3.12 has a different ABI, so those compiled ``.so`` files are no longer valid and will crash or fail to load.

The package files themselves — the pure Python code and the package metadata — are still intact on disk. Only the wiring is broken, which is why it is possible to extract a list of what was installed without activating the environment.

.. _fix_venvs_kernels:

Why Jupyter kernels disappear
-------------------------------

When you register a venv as a Jupyter kernel using ``ipykernel``, Jupyter saves a small ``kernel.json`` file under ``~/.local/share/jupyter/kernels/<name>/``. This file contains the absolute path to the Python binary inside the environment.

After the upgrade, Jupyter still finds the ``kernel.json`` file and may still show the kernel in the launcher — but when you try to start it, it attempts to launch the Python binary at the recorded path. Because that binary no longer works, the kernel either fails to start or starts and immediately crashes, which JupyterLab reports as the kernel repeatedly dying.

In some cases the kernel disappears from the launcher entirely. In others it appears but cannot be used. Either way, notebooks that relied on it cannot run.

.. _fix_venvs_symptoms:

Symptoms of a broken environment
----------------------------------

You may see any of the following:

- A Jupyter kernel that was previously available has disappeared from the launcher, or starts and immediately dies
- ``ModuleNotFoundError: No module named 'pip'`` when running pip commands
- Packages that were previously installed fail to import
- Compiled packages (numpy, scipy, etc.) segfault or raise ``ImportError``
- ``python --version`` inside the activated environment shows 3.12 even though it was created with 3.10

All of these have the same root cause: the environment's internal symlinks and compiled extensions were built against Python 3.10 and are no longer valid.

.. _fix_venvs_recovery:

Recovery
---------

.. _fix_venvs_extract:

Extract your requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^

You cannot activate the broken environment, but the package metadata is still readable on disk. SEPAL provides a script that extracts the list of installed packages from a broken environment. Run it from the terminal:

.. code-block:: bash

   ~/shared/scripts/venv_to_requirements.py ~/path/to/broken-venv requirements.txt

This scans the package metadata inside the broken environment and writes a ``requirements.txt`` with pinned versions. Verify the output:

.. code-block:: bash

   cat requirements.txt

.. _fix_venvs_choose:

Recreate the environment with uv
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:guilabel:`uv` is a fast, modern Python package manager already installed on SEPAL. Unlike venv, it manages its own Python versions independently of the system, so future upgrades will not break your environments.

.. tip::

   See :ref:`env_management` for full guidance on :guilabel:`uv` and other environment tools available on SEPAL.

You have two options:

.. _fix_venvs_310:

Option A — Recreate on Python 3.10
""""""""""""""""""""""""""""""""""""

*Fewer compatibility issues — use this if you need to get back up and running quickly and cannot yet deal with package compatibility on 3.12.*

.. code-block:: bash

   uv venv --python 3.10 ~/envs/myproject
   source ~/envs/myproject/bin/activate
   uv pip install -r requirements.txt

.. note::

   The ``requirements.txt`` referenced here is the file you extracted in the previous step.

.. _fix_venvs_312:

Option B — Migrate to Python 3.12
""""""""""""""""""""""""""""""""""""

*Better long-term choice — most pure-Python packages work on 3.12 without any changes.*

.. code-block:: bash

   uv venv --python 3.12 ~/envs/myproject
   source ~/envs/myproject/bin/activate
   uv pip install -r requirements.txt

.. note::

   The ``requirements.txt`` referenced here is the file you extracted in the first step.

.. _fix_venvs_pinning:

Handling package version conflicts (Option B)
"""""""""""""""""""""""""""""""""""""""""""""""

When migrating to Python 3.12, the ``requirements.txt`` from the first step contains fully pinned versions (e.g. ``numpy==1.23.4``). Some of these may not have wheels available for Python 3.12. If installation fails, try removing the version pins:

.. code-block:: bash

   # Strip version pins and let the resolver find compatible versions
   sed 's/==.*//' requirements.txt > requirements_unpinned.txt
   uv pip install -r requirements_unpinned.txt

The following packages are known to cause issues when moving from 3.10 to 3.12:

.. list-table::
   :header-rows: 1
   :widths: 25 40 35

   * - Package
     - Issue
     - Fix
   * - ``numpy < 1.24``
     - No Python 3.12 wheels available
     - Unpin: ``numpy``
   * - ``scipy < 1.11``
     - No Python 3.12 wheels available
     - Unpin: ``scipy``
   * - Packages using ``distutils``
     - ``distutils`` was removed in Python 3.12
     - Upgrade or replace the package
   * - Old Cython extensions
     - ABI mismatch, segfaults at import
     - ``uv pip install --force-reinstall <package>``
   * - ``cryptography`` (old versions)
     - Needs a recent version for the 3.12 ABI
     - Unpin: ``cryptography``

.. _fix_venvs_kernel:

Re-register your Jupyter kernel
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

JupyterLab discovers environments through kernel specifications — small JSON files that point to a specific Python binary. When you recreate an environment, the old kernel specification still points to the broken binary, so JupyterLab cannot find or use the new environment. You need to remove the old specification and register a new one.

First, list existing kernels and remove the broken one:

.. code-block:: bash

   # List all registered kernels
   jupyter kernelspec list

   # Remove the broken kernel
   jupyter kernelspec remove <old-kernel-name>

Then register the new environment as a kernel:

.. code-block:: bash

   source ~/envs/myproject/bin/activate
   uv pip install ipykernel
   python -m ipykernel install --user --name myproject --display-name "My Project"

After restarting JupyterLab, the new kernel will appear in the launcher and notebooks that reference it by name will work again.

.. _fix_venvs_going_forward:

Going forward
--------------

To avoid this problem in the future, stop using venv. :guilabel:`uv` manages Python versions independently of the system and will not break when SEPAL upgrades Python.

See :ref:`env_management` for full guidance on creating and managing environments, including how to add Jupyter kernels.
