Python
======

Usage
-----

SEPAL instances run on :code:`focal` ubuntu machines and thus provide a fully functional :code:`Pyhton 3.8` environment. This environment is accecible though Jupyter Notebook, JupyterLab or the terminal: 

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

.. literalinclude:: ../data/python_lib.txt
    :language: sh

Run :code:`pip freeze | grep <name of your lib>` to check if it's already installed. 


Customization
-------------

The SEPAL environment can be customized to user needs using any third-party librairies and pip. By default installation will be run in :code:`--user` mode and won't affect other SEPAL users. 


.. thumbnail:: ../_images/cli/python/install_sphinx.gif
    :title: a code run in the terminal

.. note:: 

    If you face compatibility issues when customizing your SEPAL environment, please let us know in the `Github issue tracker <https://github.com/openforis/sepal/issues/new/choose>`__.
