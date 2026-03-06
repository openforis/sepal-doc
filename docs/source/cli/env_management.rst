.. _env_management:

Python environment management
==============================

SEPAL provides two tools for managing Python environments: :guilabel:`uv` and :guilabel:`micromamba`. Both are already installed and both are better choices than the built-in :guilabel:`venv` for work on SEPAL.

The core problem with :guilabel:`venv` on a shared platform is that it creates environments tightly coupled to the system Python. When SEPAL upgrades Python — as happened with the Ubuntu Noble upgrade from 3.10 to 3.12 — every venv breaks. The tools described on this page do not have this problem.

.. warning::

   Do not use :guilabel:`venv` for new work on SEPAL. Use :guilabel:`uv` or :guilabel:`micromamba` instead.

.. _env_management_which:

Which tool should I use?
-------------------------

The right choice depends on what your project needs.

.. list-table::
   :header-rows: 1
   :widths: 40 25 35

   * - Your stack includes...
     - Use
     - Why
   * - Web frameworks, APIs, pure Python tools
     - :guilabel:`uv`
     - Fast, lightweight, no overhead
   * - Data science: pandas, scikit-learn, statsmodels
     - :guilabel:`uv`
     - Good PyPI wheel coverage for Python 3.12
   * - Geospatial: GDAL, rasterio, fiona, GEOS
     - :guilabel:`micromamba`
     - Bundles native libraries inside the environment
   * - GPU / ML: CUDA, cuDNN, PyTorch with CUDA
     - :guilabel:`micromamba`
     - Pins CUDA runtime inside the environment
   * - Mixed: some native libraries, some pure Python
     - :guilabel:`micromamba` + pip
     - micromamba for native libraries, pip for the rest

.. note::

   :guilabel:`uv` environments can still break if SEPAL upgrades a system-level native library such as GDAL or CUDA. This is because :guilabel:`uv` installs Python packages from PyPI but cannot bundle the underlying ``.so`` files they depend on. If your project uses geospatial or GPU packages, use :guilabel:`micromamba`.

.. _env_management_uv:

uv
---

:guilabel:`uv` is a fast, modern Python and package manager. It manages its own Python versions independently of the system, so a system Python upgrade will not affect your environments.

Why use uv
~~~~~~~~~~~

- **Survives system Python upgrades.** uv pins the Python version inside the project. If you create an environment with Python 3.12.2, it stays on 3.12.2 regardless of what the system does.
- **Much faster than pip and venv.** Dependency resolution and installation are typically 10–100× faster due to parallel downloads and a compiled resolver.
- **Lockfiles for reproducibility.** ``uv lock`` generates a precise, cross-platform lockfile — more reliable than ``pip freeze`` for sharing environments with colleagues.
- **Drop-in pip compatibility.** ``uv pip install`` works exactly like ``pip install``. Any package on PyPI works with uv. No new formats to learn.
- **Works with standard project files.** Reads ``pyproject.toml`` and ``requirements.txt`` natively.
- **Manages multiple Python versions.** ``uv python install 3.10`` lets you run any Python version without touching the system.
- **Single lightweight binary.** No base environment, no shell hooks, no overhead.

Creating a uv environment
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Create a new environment pinned to Python 3.12
   uv venv --python 3.12 ~/envs/myproject

   # Activate
   source ~/envs/myproject/bin/activate

   # Install packages
   uv pip install numpy pandas matplotlib

   # Or install from a requirements file
   uv pip install -r requirements.txt

Adding a Jupyter kernel
~~~~~~~~~~~~~~~~~~~~~~~~

Register your environment as a named kernel so it appears in JupyterLab:

.. code-block:: bash

   # Activate the environment first
   source ~/envs/myproject/bin/activate

   # Install ipykernel inside the environment
   uv pip install ipykernel

   # Register as a Jupyter kernel
   python -m ipykernel install --user --name myproject --display-name "My Project (3.12)"

   # Verify it appears
   jupyter kernelspec list

To remove a kernel:

.. code-block:: bash

   jupyter kernelspec remove myproject

.. _env_management_micromamba:

micromamba
-----------

:guilabel:`micromamba` works like conda (if you have used conda before, you already know how to use micromamba). Unlike :guilabel:`uv`, it bundles native system libraries — GDAL, CUDA, HDF5, and others — inside the environment itself, completely isolated from the system. This makes it the right choice for geospatial and GPU workloads.

Why use micromamba
~~~~~~~~~~~~~~~~~~~

- **Complete isolation including native libraries.** GDAL, CUDA, HDF5, GEOS, and other system libraries are installed inside the environment. Upgrading system libraries on SEPAL will not break your environment.
- **conda-forge provides excellent binary coverage.** conda-forge provides pre-compiled, compatible builds of complex packages across all platforms — often better than what is available on PyPI.
- **Environment files capture the full stack.** ``environment.yml`` files describe both Python packages and native libraries in one place, making environments fully reproducible by colleagues.
- **Pins native library versions.** You can pin ``cudatoolkit=11.8`` or ``gdal=3.6`` and those exact versions live inside the environment, regardless of what is installed system-wide.
- **Faster than conda.** Written in C++, micromamba solves and installs dependencies significantly faster than the original conda tool.
- **No base environment.** micromamba has no base environment that needs updating — cleaner and lighter on disk.

Creating a micromamba environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Create environment with Python 3.12
   micromamba create -n myproject python=3.12 -c conda-forge

   # Activate
   micromamba activate myproject

   # Install native libraries from conda-forge
   micromamba install -c conda-forge gdal rasterio fiona

   # Install remaining Python packages via pip
   pip install -r requirements.txt

Using an environment.yml file (recommended)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

An ``environment.yml`` file captures the full environment — Python version, native libraries, and Python packages — in one place:

.. code-block:: yaml

   name: myproject
   channels:
     - conda-forge
     - defaults
   dependencies:
     - python=3.12
     - gdal=3.8
     - rasterio
     - fiona
     - pip:
       - pandas
       - scikit-learn

Create or update an environment from the file:

.. code-block:: bash

   # Create from file
   micromamba env create -f environment.yml

   # Update after editing the file
   micromamba env update -f environment.yml

Adding a Jupyter kernel
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Activate the environment
   micromamba activate myproject

   # Install ipykernel
   pip install ipykernel

   # Register as a Jupyter kernel
   python -m ipykernel install --user --name myproject --display-name "My Project (conda)"

   # Verify
   jupyter kernelspec list

To remove a kernel:

.. code-block:: bash

   jupyter kernelspec remove myproject

.. _env_management_broken:

Recovering a broken venv
--------------------------

If you have an existing venv that broke due to the Python upgrade, see :ref:`fix_venvs` for step-by-step recovery instructions, including a script to extract your requirements without activating the broken environment.
