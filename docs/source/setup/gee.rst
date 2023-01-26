Use Google Earth Engine (GEE) with SEPAL
========================================

Sign up for a GEE account and connect with SEPAL
------------------------------------------------

In this article, you can learn how to:

-  Set up your GEE account
-  Connect your GEE account and SEPAL account
-  Upload files to GEE
-  Use GEE assets in SEPAL

GEE and SEPAL
-------------

SEPAL is closely linked to GEE, a Google-powered Earth-observation cloud-computing platform. SEPAL can access data stored in the GEE data catalog, use GEE for processing large datasets, and read and write data to GEE assets. A large part of SEPAL's existing code is based on the JavaScript GEE application programming interface (API).  

All SEPAL recipes are based on GEE and run scripts written by SEPAL team members to enable access to state-of-the-art processing algorithms without having to write code. In the SEPAL **Applications** list, the applications tagged with the Google logo (:icon:`fab fa-google`) are also running with the Python GEE API and don't require you to use big instances to run complex operations. 

SEPAL recipes can be run from the main SEPAL interface using default SEPAL credentials or your personal GEE access credentials; however, to run the SEPAL applications that employ GEE, you will need to link your SEPAL and GEE accounts. SEPAL applications that make use of GEE will not run (i.e. authentication will not work) if your GEE and SEPAL accounts are unlinked.

Set up your GEE account
-----------------------

Sign up
^^^^^^^

A GEE account is required to properly export images and data products as GEE assets or SEPAL applications using GEE from the SEPAL interface. A Google account is required to sign up for GEE.

To sign up for a Google account, go to https://accounts.google.com/servicelogin.

To request a GEE account, go to https://earthengine.google.com/new_signup/.

.. thumbnail:: ../_images/setup/register/gee_landing.png
    :title: Request access to google earth engine.
    :align: center

Once you have a GEE account, go to https://code.earthengine.google.com/ to access the **Earth Engine Code Editor**.

.. thumbnail:: ../_images/setup/register/gee_code.png
    :title: GEE code editor
    :align: center

.. tip::

    When you first connect to the **Earth Engine Code Editor**, it is strongly advised to take the short tour provided in the interface. 

    .. thumbnail:: ../_images/setup/gee/editor_tour.png
        :title: GEE code editor tour
        :align: center
        :width: 40%

.. tip::

    If you experience trouble while linking your Google account to GEE, contact the SEPAL team at SEPAL@fao.org.
    
Initialize the **Home** folder
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To use your GEE account in the SEPAL interface, you need to set up the **Home** folder, where all of your **Assets** (i.e. **Vectors**, **Rasters**, **Collections**, **Mosaics** and **Classifications**) will be exported. Failing to set up this folder will prevent you from successfully executing export requests.

1. To set up the **Home** folder, go to the **Earth Engine Code Editor**.

.. thumbnail:: ../_images/setup/gee/gee_code.png
    :title: GEE code editor
    :align: center

The page is divided into three zones and a map:

**Zone 1**: Provides you with access to your GEE account information, which is divided into three panes:
    
    -   **Assets**: Displays all of the assets in your account.
    -   **Scripts**: Displays all of the scripts available with your account (shared and written).
    -   **Doc**: Displays documentation of the JS GEE API, if you need to code in this editor.

**Zone 2**: Allows advanced users to code their own scripts using the GEE JS API.

**Zone 3**: Displays information about current processes, which is divided into three panes:

    -   **Inspector**: Transforms the arrow of the mouse into a pointer, allowing you to click anywhere on the map to view information about what you are displaying.
    -   **Tasks**: Displays all of the tasks of your account, as well as their statuses (i.e. *running*, *finished* or *failed*). 
    -   **Console**: Displays the console panel of running scripts.

2. Go to **Zone 1** > Select **Assets** > Select **Create home folder**.

.. thumbnail:: ../_images/setup/gee/create_home.png
    :title: gee asset creation
    :align: center
    :width: 60%

3. Select the name of the folder (Note: This can only be set once and never changed; if you're not satisfied with the suggested name, you can create your own, as long as there are no spaces or special characters).

.. thumbnail:: ../_images/setup/gee/home_pop_up.png
    :title: GEE popup for Home creation
    :align: center
    :width: 50%

4. When you return to your list of **Assets** (located in the **Zone 1** panel), you should see the name you provided as the first folder at the root of the asset tree. In this example, we used *galatheetest*:

.. thumbnail:: ../_images/setup/gee/asset_tree.png
    :title: asset tree
    :align: center
    :width: 60%

.. note:: 

    Now that you have initialized your GEE account, you can start the connection process between SEPAL and GEE.

Connection between GEE and SEPAL
--------------------------------

SEPAL can work without being connected to your GEE account, but you will miss numerous opportunities to leverage the platform's potential. 

In this section, the connection procedure between GEE and SEPAL will be presented. 

Connection
^^^^^^^^^^

1. Go to `sepal.io <https://sepal.io>`__ and sign in.

2. Select your **Username** in the lower-right side of the window (e.g. (:code:`prambaud`) in red in the image below).

.. thumbnail:: ../_images/setup/gee/sepal_landing.png
    :title: SEPAL landing
    :align: center

3. Next to the Google logo (:icon:`fab fa-google`) on the upper-right side of the **User Details** pop-up window, you will see the status of the connection between your SEPAL and GEE accounts (Note: if you have not connected your accounts, it will read *Disconnected*).

.. thumbnail:: ../_images/setup/gee/user_interface_disconnected.png
    :title: SEPAL disconnected
    :align: center
    :width: 40%

4. Select **Google account** in the lower section of the pop-up window (Note: if your GEE account is disconnected, you will see text that reminds you what functionalities are unavailable without a custom GEE account).

.. thumbnail:: ../_images/setup/gee/gee_disconnected.png
    :title: connection pop-up
    :align: center
    :width: 40%

5. Select **Connect your Google account** in the pop-up window that appears. Choose the account associated with GEE in the list.

.. thumbnail:: ../_images/setup/gee/gee_credential.png

.. Note::

    You will see a message requesting your permission to authorize SEPAL's access to your Google Drive, as well as your **Assets** and **Home** folders to export recipes and module results.

6. After the connection process is complete, you will be redirected to the SEPAL website. If you select **User interface** again, the pop-up window will display *Connected* in green in the upper-right.

.. thumbnail:: ../_images/setup/gee/user_interface_connected.png
    :title: SEPAL and GEE connected
    :align: center
    :width: 50%

Disconnection
^^^^^^^^^^^^^

If you want to change accounts or remove the link between your SEPAL and GEE accounts, you can disconnect SEPAL from GEE at any time. 

1. Return to the user interface and select **Google account**. You should see the following window:

.. thumbnail:: ../_images/setup/gee/gee_connected.png
    :title: gee connected
    :align: center
    :width: 40%

2. Select **Disconnect your Google account**.

Upload files to GEE
-------------------

When you use SEPAL recipes and modules, you'll be asked to use GEE assets to provide rasters (:code:`ee.Image`) or vectors (:code:`ee.FeatureCollection`) to the core GEE-based algorithm. These assets can be either public assets that someone shared with you or assets that you created yourself and would like to use.

.. tip::

    For vector files, SEPAL provides an interface to upload them from your computer to the platform and eventually to GEE. This process allows you to deal with the full process directly from SEPAL without going to the **Earth Engine Code Editor** (see the :doc:`../modules/dwn/vector_manager` module documentation for more details).

1. Go to **Assets** in the **Zone 1** panel on the **Earth Engine Code Editor** page:

.. thumbnail:: ../_images/setup/gee/gee_asset_list.png
    :title: GEE asset list
    :align: center
    :width: 50%

2. Select **New**. You will have several choices, including raster, shape, and table, which will be described in the following sections.

Raster
^^^^^^

If you need to upload a raster image: 

1. Select **Image**. 
2. In the pop-up window that appears, select the file you want to upload from your computer (Note: compatible formats include :code:`.tiff`, :code:`.tif`, :code:`.json`, :code:`.tfrecord` or :code:`.tfrecord.gz`; the name of your asset can be changed in the next text field).

.. tip:: 

    By default, the asset will be named after the base-name.

.. thumbnail:: ../_images/setup/gee/upload_image.png
    :title: upload image
    :align: center
    :width: 50%

Shape
^^^^^

If you need to upload a shape as a :code:`ee.FeatureCollection`: 

1. Select **Shape upload**. 
2. In the pop-up window that appears, select the file you want to upload from your computer (note: compatible formats include :code:`.shp`, :code:`.zip`, :code:`.dbf`, :code:`.prj`, :code:`.shx`, :code:`.cpg`, :code:`.fix`, :code:`.qix`, :code:`.sbn` or :code:`.shp.xml`; if you didn't compress the file, a :code:`.shp` alone is not sufficient and must be accompanied with other files describing the shape as in the example in the image below).

.. thumbnail:: ../_images/setup/gee/upload_shape.png
    :title: upload shp
    :align: center
    :width: 50%

Table
^^^^^

If you need to upload a table as a :code:`ee.FeatureCollection`:

1. Select **csv file upload**. 
2. In the pop-up window that appears, select the file you want to upload from your computer (note: compatible formats include :code:`.csv`, :code:`.json`).

.. thumbnail:: ../_images/setup/gee/upload_csv.png
    :title: upload csv
    :align: center
    :width: 50%

Use your GEE assets in SEPAL
----------------------------

Once you've uploaded your assets, you can use them in SEPAL by copying and pasting the name of each anywhere SEPAL asks for an asset name.

To find the asset name, go back to **Assets** in the **Zone 1** pane and click on any asset in the list. The following pop-up window will appear: 

.. thumbnail:: ../_images/setup/gee/asset_popup.png
    :title: asset popup
    :align: center
    :width: 80%


If you select **Copy link**, the link will be copied to the clipboard and you can paste it into SEPAL or send it to someone for authorized use. Alternatively, you can select **Share** in the pop-up window and choose between the different sharing options.


For support, :doc:`ask the community <>` or contact the SEPAL team at SEPAL@fao.org.
