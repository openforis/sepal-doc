Use GEE with SEPAL
==================
*Sign up for a GEE account and connect with SEPAL*

In this article, learn how to:

-  set up your GEE account
-  connect your GEE account and SEPAL account
-  upload files to GEE
-  use GEE assets in SEPAL

GEE and SEPAL
-------------

SEPAL is closely linked to Google Earth Engine (GEE), a Google-powered Earth-observation cloud-computing platform. 

SEPAL can: 

-   access data stored in the GEE data catalog; 
-   use GEE for processing large datasets; and 
-   read and write data to GEE assets. 

A large part of SEPAL's existing code is based on the JavaScript GEE application programming interface (API).

All SEPAL recipes are based on GEE and run scripts written by SEPAL team members to enable access to state-of-the-art processing algorithms without having to write code. 

In the SEPAL **Apps** list, the applications tagged with the Google logo (:icon:`fa-brands fa-google`) are also running with the Python GEE API and don't require you to use big instances to run complex operations.

SEPAL recipes can be run from the main SEPAL interface using default SEPAL credentials or your personal GEE access credentials; however, to run the SEPAL applications that employ GEE, you will need to link your SEPAL and GEE accounts. SEPAL applications that make use of GEE will not run (i.e. authentication will not work) if your GEE and SEPAL accounts are unlinked.

Set up your GEE account
-----------------------

Sign up
^^^^^^^

A GEE account is required to properly export images and data products as GEE assets or SEPAL applications using GEE from the SEPAL interface. A Google account is required to sign up for GEE.

To sign up for a Google account, go to https://accounts.google.com/servicelogin.

To request a GEE account, go to https://earthengine.google.com/new_signup.

.. thumbnail:: ../_images/setup/register/gee_landing.png
    :title: Request access to GEE.
    :align: center

For first-time users of SEPAL, select **Use without a cloud project** (for non-commercial users of GEE; the link between GEE and Google Cloud Projects [GCPs] is evolving and SEPAL will continue to develop in order to make use of GCPs correctly – but for now, use SEPAL without a GCP).

.. thumbnail:: ../_images/setup/register/gee_gcp_declaration.png
    :title: Use GEE without a cloud project.
    :align: center

Once you have a GEE account, access the **Earth Engine Code Editor** by going to https://code.earthengine.google.com.

.. thumbnail:: ../_images/setup/register/gee_code.png
    :title: GEE Code Editor
    :align: center

.. tip::

    When you first connect to **Earth Engine Code Editor**, the SEPAL team recommends taking the tour of its features provided in the interface.

    .. thumbnail:: ../_images/setup/gee/editor_tour.png
        :title: GEE Code Editor tour
        :align: center
        :width: 40%

.. tip::

    If you experience trouble while linking your Google account to GEE, `ask the community <https://groups.google.com/g/sepal-users>`__.

Initialize the **Home** folder
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To use your GEE account in the SEPAL interface, set up the **Home** folder, where all your **Assets** (i.e. **Vectors**, **Rasters**, **Collections**, **Mosaics** and **Classifications**) will be exported. Failing to set up this folder will prevent you from successfully executing export requests.

1. To set up the **Home** folder, go to the **Earth Engine Code Editor**.

.. thumbnail:: ../_images/setup/gee/gee_code.png
    :title: GEE Code Editor
    :align: center

The page is subdivided into three zones and a map:

**Zone 1**: Provides you with access to your GEE account information, subdivided into three panes:

    -   **Assets**: Displays all of assets in your account.
    -   **Scripts**: Displays all scripts available with your account (shared and written).
    -   **Doc**: Displays documentation of the GEE JavaScript API (GEE JS API), if you need to code in this editor.

**Zone 2**: Allows advanced users to code their own scripts using the GEE JS API.

**Zone 3**: Displays information about current processes, divided into three panes:

    -   **Inspector**: Transforms the arrow of the mouse into a pointer, allowing you to click anywhere on the map to view information about what you are displaying.
    -   **Tasks**: Displays all of the tasks of your account, as well as their statuses (i.e. **Running**, **Finished** or **Failed**).
    -   **Console**: Displays the console panel of running scripts.

2. Go to **Zone 1** > Select **Assets** > Select **Create** Home **folder**.

.. thumbnail:: ../_images/setup/gee/create_home.png
    :title: GEE asset creation
    :align: center
    :width: 60%

3. Select the name of the folder (this can only be set once and never changed; if you're not satisfied with the suggested name, you can create your own as long as there are no spaces or special characters).

.. thumbnail:: ../_images/setup/gee/home_pop_up.png
    :title: GEE pop-up window for **Home** folder creation
    :align: center
    :width: 50%

4. When you return to your list of **Assets** (located in the **Zone 1** panel), you should see the name you provided as the first folder at the root of the **Asset** tree. 

In our example, we used **galatheetest**:

.. thumbnail:: ../_images/setup/gee/asset_tree.png
    :title: Asset tree
    :align: center
    :width: 60%

.. note::

    After initializing your GEE account, start the connection process between GEE and SEPAL.

Connection between GEE and SEPAL
--------------------------------

SEPAL can work without being connected to your GEE account, but you will miss numerous opportunities to leverage the platform's potential.

In this subsection, we present the connection procedure between GEE and SEPAL.

Connection
^^^^^^^^^^

1. Go to `sepal.io <https://sepal.io>`__ and sign in.

2. Select your **Username** in the lower-right side of the window (e.g. (:code:`prambaud`) in red in the image below).

.. thumbnail:: ../_images/setup/gee/sepal_landing.png
    :title: SEPAL landing
    :align: center

3. Next to the Google logo (:icon:`fa-brands fa-google`) in the upper-right corner of the **User details** pop-up window, the status of the connection between your GEE and SEPAL accounts is displayed (if you have not connected your accounts, it will read **Disconnected**).

.. thumbnail:: ../_images/setup/gee/user_interface_disconnected.png
    :title: SEPAL disconnected
    :align: center
    :width: 40%

4. Select **Google account** in the lower section of the pop-up window (if your GEE account is disconnected, you will see text that reminds you what functionalities are unavailable without a custom GEE account).

.. thumbnail:: ../_images/setup/gee/gee_disconnected.png
    :title: Connection pop-up window
    :align: center
    :width: 40%

5. Select **Connect your Google account** in the pop-up window that appears. Choose the account associated with GEE in the list.

.. thumbnail:: ../_images/setup/gee/gee_credential.png

.. Note::

    You will see a message requesting your permission to authorize SEPAL's access to your Google Drive, as well as your **Assets** folder and **Home** folder to export recipes and module results.

6. After the connection process is complete, you will be redirected to the SEPAL website. If you open **User details** again, the pop-up window will display *Connected* in green in the upper-right corner.

.. thumbnail:: ../_images/setup/gee/user_interface_connected.png
    :title: SEPAL and GEE connected
    :align: center
    :width: 50%

Disconnection
^^^^^^^^^^^^^

If you want to change accounts or disconnect your GEE and SEPAL accounts:

1. Open **User details** and select **Google account**. You should see the following window:

.. thumbnail:: ../_images/setup/gee/gee_connected.png
    :title: GEE connected
    :align: center
    :width: 40%

2. Select **Disconnect your Google account**.

Upload files to GEE
-------------------

When you use SEPAL recipes and modules, you'll be asked to use GEE assets to provide rasters (:code:`ee.Image`) or vectors (:code:`ee.FeatureCollection`) to the core GEE-based algorithm. 

These assets can be either:

-   public assets that someone shared with you; or 
-   assets that you created yourself and would like to use.

.. tip::

    For vector files, SEPAL provides an interface to upload them from your computer to the platform and eventually to GEE. This process allows you to deal with the full process directly from SEPAL without going to the **Earth Engine Code Editor** (for more information, see :doc:`../modules/dwn/vector_manager`).

1. Go to **Assets** in the **Zone 1** panel in the **Earth Engine Code Editor**.

.. thumbnail:: ../_images/setup/gee/gee_asset_list.png
    :title: GEE asset list
    :align: center
    :width: 50%

2. Select **New**. You will have several choices, including **Raster**, **Shape** and **Table**, which will be described in the following subsections.

Raster
^^^^^^

If you need to upload a raster image:

1. Select **Image**.
2. In the pop-up window, select the file you want to upload from your computer (compatible formats include :code:`.tiff`, :code:`.tif`, :code:`.json`, :code:`.tfrecord` or :code:`.tfrecord.gz`; the name of your asset can be changed in the next text field).

.. tip::

    By default, the asset will be named after the basename.

.. thumbnail:: ../_images/setup/gee/upload_image.png
    :title: Upload image
    :align: center
    :width: 50%

Shape
^^^^^

If you need to upload a shape as a :code:`ee.FeatureCollection`:

1. Select **Shape upload**.
2. In the pop-up window, select the file you want to upload from your computer (note: compatible formats include :code:`.shp`, :code:`.zip`, :code:`.dbf`, :code:`.prj`, :code:`.shx`, :code:`.cpg`, :code:`.fix`, :code:`.qix`, :code:`.sbn` or :code:`.shp.xml`; if you didn't compress the file, a :code:`.shp` alone is not sufficient and must be accompanied with other files describing the shape as in the example in the image below).

.. thumbnail:: ../_images/setup/gee/upload_shape.png
    :title: Upload .shp
    :align: center
    :width: 50%

Table
^^^^^

If you need to upload a table as a :code:`ee.FeatureCollection`:

1. Select **csv file upload**.
2. In the pop-up window that appears, select the file you want to upload from your computer (note: compatible formats include :code:`.csv`, :code:`.json`).

.. thumbnail:: ../_images/setup/gee/upload_csv.png
    :title: Upload .csv
    :align: center
    :width: 50%

Use your GEE assets in SEPAL
----------------------------

Once you've uploaded your assets, you can use them in SEPAL by copying and pasting the name of each whenever an asset name is requested from the interface.

To find the asset name, go back to **Assets** in the **Zone 1** pane and select any asset in the list. The following pop-up window will appear:

.. thumbnail:: ../_images/setup/gee/asset_popup.png
    :title: Asset pop-up window
    :align: center
    :width: 80%

If you select **Copy link**, the link will be copied to the clipboard and you can paste it into SEPAL or send it to someone for authorized use. 

Alternatively, you can select **Share** and choose between the different sharing options.
