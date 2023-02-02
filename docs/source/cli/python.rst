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

If not existing, create a directory to host your virtual environments. From the root directory run:

.. code-block:: console

    mkdir venv

in this folder create a virtual environment:

.. code-block:: console

    cd venv
    python3 -m venv <venv_name>

Now create a Jupyter Kernel linked to this venv:

.. code-block:: console

    ./<venv_name>/python3 -m ipykernel install --user --name <venv_name> --display-name <a name to display>

Now this venv will be available as a kernel inside your Jupyter workspace. This kernel will be automatically removed if you destroy the venv directory.

If you want to install libs inside this venv you need first to activate it:

.. code-block:: console

    source ./<venv_name>/bin/activate

