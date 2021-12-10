SEPAL modules
=============

.. custom-edit:: https://raw.githubusercontent.com/openforis/sepal-doc/docs/source/data/template/index.rst

Overview
--------

SEPAL applications are tools provided by the SEPAL team from FAO or from other developers. These tools are based on advanced GIS libraries and complement the functionalities of the SEPAL recipes. It provides the end user access to complex workflows without requirering knowledge of digital programming. These applications are served in SEPAL with nice User Interfaces to ensure the best possible user experience. 

They run on various shells from pure HTML to shinny based R apps but also Jupyter powered Python kernels. This flexibility and variety of tools allows developer to bring any workflows and make them available for SEPAL users. Click on any of the module documentation to know more about its usage.




Start applications 
------------------

To start a SEPAL application gor to the dashboard of application by clicking on the wrench icon on the left side of the window ((1) on the following image). This will bring up a list of apps you can run in SEPAL. More information about each app is found by clicking on the “i” on the right hand side. The top 3 app (2) are not real app but code editors: 

-   R Studio: provides access to R environment where you can run processing scripts and upload data to your SEPAL folder
-   Juyter Notebook: an open-source web application that allows you to create and share documents that contain live code, equations, visualizations and narrative text. support Kernels in many different languages including R, Python and NodesJS.
-   JupyterLab: JupyterLab is a web-based interactive development environment for Jupyter notebooks, code, and data.

.. thumbnail:: ../_images/module/index/dashboard.png
    :title: the landing page of the dashboard of application

To find the aplication he's looking for, the user can navigate in the different app pages (3), use the tags (4) or use the search bar (5).

Once the desired application is found simply click on it to start the process. This will as well start the smallest instance to run the SEPAL sandbox (:code:`t1`). Please refer to the next section to start aspecific instance manually.

.. warning:: 

    Applications that includes a "G" in their descriptor require a connection to Google Earth Engine to run, please refer to `Connect GEE and SEPAL <../setup/gee.html#connection-between-gee-and-sepal>`__ for more information.
    
.. warning::

    Application need to set up numerous tools and system, don't rush and be patient it can take up to 5 min to start. If the application doesn't start after 5 min, close the tab and start it again, it's usually a Amazon cloud connection issue. On the other hand if one run in an bug or crash please report this issue in SEPAL or the specific app issue tracker.
    
.. important:: 

    Application are running on the current instance so closing it (by disconecting from SEPAL or stop the instance manually) will end up in killing the application workflow. The already performed work will be available in SEPAL folders but the user will need to restart the process to finish it.
    


Start instance manually
-----------------------

Some applications require more powerful instances than the default :code:`t1`. If the app documentation requires the user to start a specific instance type (e.g. a GPU machine :code:`g4` or :code:`g8`) please follow these steps prior to start the application. 

#.  Go to the SEPAL termninal and wait for the instance selector to start

    .. thumbnail:: ../_images/module/index/terminal.png
       :title: the SEPAL instance selector
        
#.  Type the instance name suggested in the documentation of your app and press :kbd:`Enter`.

#.  Wait for the instance to finish loading

    .. thumbnail:: ../_images/module/index/m4_started.png
        :title: start a m4 instance
        
#.  Go back to the dashboard of application to launch your app. It will be automatically using the instance you opened and won't restart a :code:`t1`.

.. toctree::
    :hidden:
    :maxdepth: 1
