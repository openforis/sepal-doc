Python
======

Usage
-----

SEPAL instances run on :code:`focal` ubuntu machines and thus provide a fully functional :code:`Pyhton 3.8` environment. This environment is accecible through Jupyter Notebook, JupyterLab or the terminal:

.. thumbnail:: ../_images/cli/python/jupyter_example.png
    :title: a code run in Jupyterlab
    :group: python_environment
    :width: 32%

.. thumbnail:: ../_images/cli/python/notebook_example.png
    :title: a code run in Jupyter Notebook
    :group: python_environment
    :width: 32%

.. thumbnail:: ../_images/cli/python/terminal_example.png
    :title: a code run in the terminal
    :group: python_environment
    :width: 32%

Description
-----------

The SEPAL python environment is not empty and embed numerous librairies. They are listed here:

.. literalinclude:: ../_data/python_lib.txt
    :language: sh

Run :code:`pip show <name of your lib>` to check if it's already installed.


Customization
-------------

The SEPAL environment can be customized to user needs using any third-party librairies and pip. By default installation will be run in :code:`--user` mode and won't affect other SEPAL users.


.. thumbnail:: ../_images/cli/python/install_sphinx.gif
    :title: a code run in the terminal

.. note::

    If you face compatibility issues when customizing your SEPAL environment, please let us know in the `Github issue tracker <https://github.com/openforis/sepal/issues/new/choose>`__.

Virtual environment
-------------------

.. warning::

    SEPAL does not support conda environments, if you need to install compiled librairies, please the SEPAL team via the  `Github issue tracker <https://github.com/openforis/sepal/issues/new/choose>`__.

SEPAL supports python venv creation. in this section we'll explain how you can create a venv and link it to Jupyter so you can run your processes on the associated kernel.

By design Jupyter is runnnig on the Python Kernel described in the previous section. you can also use the kernel associated to our applications (they start with :code:`venv`). If your work rely on very specific version numbers it might be good to run everything on a dedicated environment.

If not existing, create a directory to host your virtual environments. From the root directory, run the following line:

.. code-block:: bash

    folder_name="my_virtual_env"  # Replace my_virtual_env with the name you want to give to the folder that will hold your virtual environment

And then, copy and paste the following lines in your terminal:

.. code-block:: bash

    mkdir -p "$folder_name" # Create your folder (included partents if are given).
    python3 -m venv "$folder_name" # Create the venv, this line could take some time.
    source "$folder_name/bin/activate" # Activate the virtual enviroment just created.
    pip install ipykernel # Install ipykernel in our venv.
    python -m ipykernel install --user --name="$folder_name" -display-name="(venv) - $folder_name" # Add the new venv kernel to jupyter.
    deactivate # (optional) exit from environment.

Now this venv will be available as a kernel inside your Jupyter workspace. This kernel will be automatically removed if you destroy the venv directory.

Note that If you want to install libs inside this venv you need first to activate it:

.. code-block:: console

    source your_venv_path/bin/activate

