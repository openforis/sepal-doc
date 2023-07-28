R code
======

Usage
-----

SEPAL instances run on :code:`focal` Ubuntu machines, providing a fully functional :code:`R 4.1.2` environment that is accessible in RStudio, Jupyterlab or the terminal.

.. thumbnail:: ../_images/cli/r/rstudio_example.png
    :title: A code run in RStudio
    :group: r_environment
    :width: 32%

.. thumbnail:: ../_images/cli/r/jupyter_example.png
    :title: A code run in Jupyterlab
    :group: r_environment
    :width: 32%

.. thumbnail:: ../_images/cli/r/terminal_example.png
    :title: A code run in the terminal
    :group: r_environment
    :width: 32%

Description
-----------

The SEPAL :code:`R` environment is not empty; there are numerous embedded packages.

.. literalinclude:: ../_data/r_packages.sh
    :language: sh
    :emphasize-lines: 32-298

To check the availability of a specific package:

-   Open RStudio.
-   Go to :guilabel:`Help` > :guilabel:`R Help` (from the menu above).
-   You will see the **Help** panel opened.
-   Select :code:`Reference` > :code:`Packages`

.. thumbnail:: ../_images/cli/r/package_list.png
    :title: How to display R packages in **RStudio**
    :group: r_environment

Customization
-------------

The SEPAL environment can be customized to user needs by utilizing third-party packages and CRAN in **RStudio**.

.. code-block:: r

        install.packages("vioplot")

.. note::

    If you face compatibility issues when customizing your SEPAL environment, contact the SEPAL team in the `Github issue tracker <https://github.com/openforis/sepal/issues/new/choose>`__.
