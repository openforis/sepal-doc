Use Google Earth Engine (GEE) with SEPAL
==================================

GEE and SEPAL
-------------

SEPAL is a free, open-source cloud-computing platform that gives you access to geospatial data resources (either via the GEE data catalogue or user-provided data) and powerful computing resources to process these data to produce useful information.

SEPAL currently "resides" in the Amazon Web Services (AWS) ecosystem and makes use of AWS cloud computers, or instances, that can be used to process data using pre-programmed SEPAL applications or your own code (in R, Python or in the terminal). SEPAL is also closely linked to GEE, a Google-powered Earth-observation cloud-computing platform. SEPAL can access data stored in the GEE data catalog, use GEE for processing large datasets, and read and write data to GEE assets. A large part of SEPAL's existing code is based on the JavaScript GEE Application Programming Interface (API).  

All SEPAL recipes are based on GEE and run scripts written by SEPAL team members to enable access to state-of-the-art processing algorithms without having to write code. In the SEPAL applications list, the applications tagged with the Google logo ("**G**") are also running with the Python GEE API and don't require you to use big instances to run complex operations. 

SEPAL recipes can be run from the main SEPAL interface using default SEPAL credentials or your personal GEE access credentials. However, to run the SEPAL applications that employ GEE, you will need to link your SEPAL and GEE accounts. SEPAL applications that make use of GEE will not run (e.g. authentication will not work) if your GEE and SEPAL accounts are unlinked.

.. tip:

   See linking SEPAL and GEE accounts in the previous section for more information.

To get the best of SEPAL, we highly suggest that all users open their own GEE account and link it to SEPAL. 

In this section of SEPAL documentation, we will guide you through the full process of creating a GEE account and linking it to SEPAL. 

Create a GEE account
--------------------

Sign-up
^^^^^^^

Signing up for GEE is required to properly export images and data products from SEPAL as GEE assets or SEPAL applications using GEE. 

You will need to have a Google account to sign up. If you don't have one already, you can set one up here: https://accounts.google.com/servicelogin. 

To request a GEE account, please visit https://earthengine.google.com/new_signup/.

.. image:: ../_images/setup/register/gee_landing.png
   :alt: Request access to google earth engine.
   :align: center

Once you have a GEE account, you can access the platform here: https://code.earthengine.google.com/.

.. image:: ../_images/setup/register/gee_code.png
   :alt: GEE code editor
   :align: center

.. tip::

    When you first connect to the code editor, it is strongly advised to take the short tour provided in the interface. 

    .. image:: ../_images/setup/gee/editor_tour.png
        :alt: GEE code editor tour
        :align: center

.. tip::

    If you experience trouble while linking your Google account to GEE, we encourage you to contact the SEPAL team for support.
    
Initialize the **Home** folder
^^^^^^^^^^^^^^^^^^^^^^^^^^

To use your GEE account in SEPAL, you need to  set up the **Home** folder, where all your assets (vectors, rasters, collections, mosaics, classifications, etc.) will be exported. Failing to set up this folder will prevent you from successfully executing export requests.

To set up the **Home** folder, go to the GEE Code Editor.

.. image:: ../_images/setup/gee/gee_code.png
   :alt: GEE code editor
   :align: center

The webpage is divided into 3 zones and a map:

1.  **Zone 1**: Provides you with access to your GEE account information, which is divided into three panels:
    
    -   **Assets**: Displays all of the assets in your account. 
    -   **Scripts**: Displays all of the scripts available with your account (shared and written).
    -   **Doc**: Displays documentation of the JS GEE API, if you need to code in this editor.

2.  **Zone 2**: Allows advanced users to code their own scripts using the GEE JS API.

3.  **Zone 3**: Displays information about current processes, which is divided into 3 panels:

    -   **Inspector**: Transforms the arrow of the mouse into a pointer, allowing you to click anywhere on the map to view information about what you are displaying.
    -   **Tasks**: Displays all of the tasks of your account (running, finished or failed). 
    -   **Console**: Displays the console panel of running scripts.

Go to **Zone 1** and select the **Assets** panel. Click on the red :code:`Create home folder` button.

.. image:: ../_images/setup/gee/create_home.png
    :alt: gee asset creation
    :align: center

This opens a pop-up menu to select the name of the folder, which can only be set once and never changed. If you're not satisfied with the suggested name, you can create your own (the only limitation is that you can not use spaces or special characters).

.. image:: ../_images/setup/gee/home_pop_up.png
    :alt: GEE popup for Home creation
    :align: center

When you return to your list of assets (**Zone 1** panel "**Assets**") you should see the name you provided as the first folder at the root of the asset tree. In this example, we used "galatheetest":

.. image:: ../_images/setup/gee/asset_tree.png
    :alt: asset tree

.. note:: 

    Now that you have initialized your GEE account, you can start the connection process between SEPAL and GEE.

Connection between GEE and SEPAL
--------------------------------

SEPAL can work without being connected to your GEE account, but you will miss numerous opportunities to interact with the platform. In this section, the connection procedure between GEE and SEPAL will be presented. 

Connection
^^^^^^^^^^

The first step is to navigate to the SEPAL landing page (`sepal.io <https://sepal.io>`__) and sign in. 

On the following page, click on your **Username** on the lower-right side of the window (in red below) (:code:`prambaud`).

.. image:: ../_images/setup/gee/sepal_landing.png
    :alt: SEPAL landing
    :align: center

By clicking on the username, a **User Details** pop-up will appear, where you can modify your personal information. On the upper-right side of this pop-up, next to the Google logo (**G**), you will see the status of the connection between your SEPAL and GEE accounts (Note: If you have not connected your accounts, it will read "Disconnected").

.. image:: ../_images/setup/gee/user_interface_disconnected.png
    :alt: SEPAL disconnected

Click on :code:`Google account` in the lower section of the pop-up. Another pop-up will then appear (Note: If your GEE account is disconnected, you will see text that reminds you what functionalities are unavailable without a custom GEE account).

.. image:: ../_images/setup/gee/gee_disconnected.png
    :alt: connection pop-up

Click on :code:`Connect your Google account`. In the list provided, select the account associated with GEE: 

.. image:: ../_images/setup/gee/gee_credential.png

.. Note::

    You will see a message requesting your permission to authorize SEPAL's access to your Google Drive, as well as your **Asset** and **Home** folders to export recipes and module results.

After the connection process is complete, you will be redirected to the SEPAL website. If you click on the "User interface" button again, the pop-up window will display "Connected" in green on the upper-right side.

.. image:: ../_images/setup/gee/user_interface_connected.png
    :alt: SEPAL and GEE connected

Disconnection
^^^^^^^^^^^^^

If you want to change accounts or remove the link between your SEPAL and GEE accounts, you can disconnect SEPAL from GEE at any time. 

Return to the user interface and click on :code:`Google account`. You should see the following window: 

.. image:: ../_images/setup/gee/gee_connected.png
    :alt: gee connected 

Simply click on the :code:`Disconnect your Google account` button and your accounts will no longer be linked. 

Upload files to GEE 
-------------------

When you use SEPAL recipes and modules, you'll be asked to use GEE assets to provide rasters or vectors to the core GEE-based algorithm. These assets can be either public assets that someone shared with you or assets that you created yourself and would like to use.

.. tip::

    For vector files, SEPAL provides an interface to upload them from your computer to the platform and eventually to GEE. This process allows you to deal with the full process directly from SEPAL without going to the GEE code interface. See the :doc:`../modules/dwn/vector_manager` module documentation for more details.

Go to **Assets** in the **Zone 1** panel on the Code Editor page:

.. image:: ../_images/setup/gee/gee_asset_list.png
    :alt: GEE asset list

Click on the :code:`New` button. You will have several choices that will be described in the following sections.

Raster
^^^^^^

If you need to upload a raster image use the :code:`Image` button. In the pop-up window that appears, select the file you want to upload from your computer. It can be in any of the following formats: :code:`.tiff`, :code:`.tif`, :code:`.json`, :code:`.tfrecord` or :code:`.tfrecord.gz`. You can then change the name of your asset in the next textfield.

.. tip:: 

    By default the asset will be named after the tif base-name.

.. image:: ../_images/setup/gee/upload_image.png
    :alt: upload image

Shape
^^^^^

If you need to upload a shape as a :code:`ee.FeatureCollection`, click on the :code:`Shape upload` button. In the pop-up window that appears, select the file you want to upload from your computer. It can be any shape file in the following formats: :code:`.shp`, :code:`.zip`, :code:`.dbf`, :code:`.prj`, :code:`.shx`, :code:`.cpg`, :code:`.fix`, :code:`.qix`, :code:`.sbn` or :code:`.shp.xml`. Keep in mind that if you didn't compress the file, a :code:`.shp` alone is not sufficient and must be accompanied with other files describing the shape as in the following example: 

.. image:: ../_images/setup/gee/upload_shape.png
    :alt: upload shp

Table
^^^^^

If you need to upload a table as a :code:`ee.FeatureCollection`, click on the :code:`csv file upload` button. In the pop-up window that appears, select the file you want to upload from your computer. It can be any table in the following formats: :code:`.csv`, :code:`.json`.

.. image:: ../_images/setup/gee/upload_csv.png
    :alt: upload csv

Use my assets
^^^^^^^^^^^^^

Once you've uploaded your assets, you can use them in SEPAL by copying and pasting the name of each anywhere SEPAL asks for an asset name.

To find the asset name, go back to **Assets** in the **Zone 1** panel and click on any asset in the list. The following pop-up window will appear: 

.. image:: ../_images/setup/gee/asset_popup.png
    :alt: asset popup

If you click on the :code:`Copy link` button, the link will be copied to the clipboard and you can paste it into SEPAL. 

If you want to share this asset with other people, you can send them this link (the one you just copied to the clipboard) and authorize them to use it. Alternatively, you can click on the :code:`Share` button in the pop-up and choose between the different sharing options. 

.. spelling:word-list::

    galatheetest
