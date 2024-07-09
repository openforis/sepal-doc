Python
======

Usage
-----

SEPAL instances run on :code:`focal` Ubuntu machines and thus provide a fully functional :code:`Python 3.10.12` environment, which is accessible through Jupyter Notebook, JupyterLab or the terminal:

.. thumbnail:: ../_images/cli/python/jupyter_example.png
    :title: A code run in JupyterLab
    :group: python_environment
    :width: 32%

.. thumbnail:: ../_images/cli/python/notebook_example.png
    :title: A code run in Jupyter Notebook
    :group: python_environment
    :width: 32%

.. thumbnail:: ../_images/cli/python/terminal_example.png
    :title: A code run in the SEPAL terminal
    :group: python_environment
    :width: 32%

Description
-----------

The SEPAL Python environment is not empty; there are numerous embedded libraries (see figure below).

.. literalinclude:: ../_data/python_lib.txt
    :language: sh

To check if it's already installed, run :code:`pip show <name of your lib>`.

Customization
-------------

The SEPAL environment can be customized to user needs using any third-party libraries and pip. By default, installation will be run in :code:`--user` mode and won't affect other SEPAL users.

.. thumbnail:: ../_images/cli/python/install_sphinx.gif
    :title: A code run in the terminal

.. note::

    If you face compatibility issues when customizing your SEPAL environment, let us know in the `Github issue tracker <https://github.com/openforis/sepal/issues/new/choose>`__.

Virtual environment
-------------------

.. attention::

    SEPAL does not support conda environments. If you need to install compiled libraries, contact the SEPAL team via the  `GitHub issue tracker <https://github.com/openforis/sepal/issues/new/choose>`__.

SEPAL supports Python venv creation. In this section, we'll explain how to create a venv and link it to Jupyter, so you can run your processes on the associated kernel.

By design, Jupyter is running on the Python Kernel described in the previous section. You can also use the kernel associated with our applications (they start with :code:`venv`). If your work relies on very specific version numbers, it might be good to run everything in a dedicated environment.

If not existing, create a directory to host your virtual environments. From the root directory, run the following line:

.. code-block:: bash

    folder_name="my_virtual_env"  # Replace my_virtual_env with the name you want to give to the folder that will hold your virtual environment.

Then, copy and paste the following lines in your terminal:

.. code-block:: bash

    mkdir -p "$folder_name" # Create your folder (include parents, if they are given).
    python3 -m venv "$folder_name" # Create the venv (this line could take some time).
    source "$folder_name/bin/activate" # Activate the virtual environment just created.
    pip install ipykernel # Install ipykernel in our venv.
    python -m ipykernel install --user --name="$folder_name" --display-name="(venv) - $folder_name" # Add the new venv kernel to Jupyter.
    deactivate # Exit from environment (optional).

Now, this venv will be available as a kernel inside your Jupyter workspace. It will be automatically removed if you destroy the venv directory.

Note that if you want to install libs inside of this venv, you first need to activate it:

.. code-block:: console

    source your_venv_path/bin/activate
