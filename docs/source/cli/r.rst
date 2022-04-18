R code
======

Usage
-----

SEPAL instances run on :code:`focal` ubuntu machines and provide a fully functional :code:`R 4.1.2` environment. This environment is accecible Rstudio, Jupyterlab or the terminal: 

.. thumbnail:: ../_images/cli/r/rstudio_example.png
    :title: a code run in Rstudio
    :group: r_environment
    :width: 32%

.. thumbnail:: ../_images/cli/r/jupyter_example.png
    :title: a code run in Jupyterlab
    :group: r_environment
    :width: 32%

.. thumbnail:: ../_images/cli/r/terminal_example.png
    :title: a code run in the terminal
    :group: r_environment
    :width: 32%

Description
-----------

The SEPAL :code:`R` environment is not empty and embed numerous packages:

.. literalinclude:: ../data/r_packages.sh
    :language: sh
    :emphasize-lines: 32-298
    
To check the availability of a specific package: 

-   Open RStudio
-   Navigate to :guilabel:`Help` -> :guilabel:`R Help` (from the menu above)
-   You will see the help panel opened.
-   Then follow, :code:`Reference` --> :code:`Packages`

.. thumbnail:: ../_images/cli/r/package_list.png
    :title: how to display the R packages in **Rstudio**
    :group: r_environment


Customization
-------------

The SEPAL environment can be customized to user needs using any third-party packages and CRAN in **Rstudio**:

.. code-block:: r

        install.packages("vioplot")

.. note:: 

    If you face compatibility issues when customizing your SEPAL environment, please let us know in the `Github issue tracker <https://github.com/openforis/sepal/issues/new/choose>`__.

