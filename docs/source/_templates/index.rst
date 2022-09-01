SEPAL modules
=============

.. custom-edit:: https://raw.githubusercontent.com/openforis/sepal-doc/main/docs/source/_templates/index.rst

Overview
--------

SEPAL applications are tools provided by the SEPAL team from FAO or other developers. These tools are based on advanced GIS libraries and complement the functionalities of SEPAL recipes, providing the end user with access to complex workflows without requiring knowledge of digital programming. These applications are served in SEPAL with attractive User Interfaces to ensure the best possible user experience. 

They run on various shells from pure HTML and Shiny-based R apps to Jupyter-powered Python kernels. This flexibility and variety of tools allow developers to integrate workflows and make them available for SEPAL users. Review the module documentation below to learn more about its usage.




Start applications 
------------------

To start a SEPAL application go to the dashboard of the application by clicking on the wrench icon on the left side of the window [(1) on the following image]. This will bring up a list of apps you can run in SEPAL. More information about each app is found by clicking the “i” on the right side. Note: The top three apps (2) are code editors, not apps: 

-   R Studio: Provides access to the R environment where you can run processing scripts and upload data to your SEPAL folder.
-   Jupyter Notebook: An open-source web application that allows you to create and share documents that contain live code, equations, visualizations and narrative text (supports Kernels in many different languages, including R, Python and NodesJS).
-   JupyterLab: JupyterLab is a web-based interactive development environment for Jupyter notebooks, code and data.

.. thumbnail:: ../_images/module/index/dashboard.png
    :title: The landing page of the dashboard of the application.

To find the application you're looking for, you can navigate through the different app pages (3), use tags (4), or utilize the search bar (5).

Once the desired application is found, simply click on it to initiate the process. This will start the smallest instance to run the SEPAL sandbox (:code:`t1`). Please refer to the next section to start a specific instance manually.

.. note:: 

    Applications that include a "G" in their descriptor require a connection to Google Earth Engine (GEE) to run. Please refer to `Connect GEE and SEPAL <../setup/gee.html#connection-between-gee-and-sepal>`__ for more information.
    
.. note::

    An application relies on numerous tools and systems to run. Since it can take up to five minutes to start, stay patient and avoid rushing. If the application doesn't start after five minutes, it could simply be an issue with the Amazon cloud connection. We recommend closing the tab and starting again. If you do experience a major bug or crash, please report the issue in the specific app issue tracker or directly in SEPAL.
    
.. important:: 

    To avoid disturbances in the application workflow, avoid stopping instances manually and disconnecting from SEPAL. While completed work will be available in SEPAL folders, you will need to restart the process in order to finish.


Start instance manually
-----------------------

Some applications require more powerful instances than the default :code:`t1`. If the app documentation requires the user to start a specific instance type (e.g. a GPU machine :code:`g4` or :code:`g8`), follow these steps prior to initiating the application. 

#.  Go to the SEPAL terminal and wait for the instance selector to start.

    .. thumbnail:: ../_images/module/index/terminal.png
       :title: The SEPAL instance selector.
        
#.  Type the instance name suggested in the documentation of your app and press :kbd:`Enter`.

#.  Wait for the instance to finish loading.

    .. thumbnail:: ../_images/module/index/m4_started.png
        :title: Start an m4 instance.
        
#.  Go back to the dashboard of the application to launch your app. It will be automatically using the instance you opened and won't restart a :code:`t1`.

.. toctree::
    :hidden:
    :maxdepth: 1
