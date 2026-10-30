Introduction to SEPAL
=====================
*Learn the basics of the platform and how to access features*

In this article, learn to:

-   navigate the interface
-   use the functionalities of the platform

Prequisities include:

-   internet access
-   SEPAL account (see `Register <https://docs.sepal.io/en/latest/setup/register.html>`_)

Access SEPAL
------------

1.  Go to `sepal.io <https://sepal.io/>`_.
2.  Select **Launch**.
3.  Enter your username and password.
4.  Select :btn:`Login`.

.. thumbnail:: ../_images/setup/presentation/sepal_login.png
   :title: SEPAL login page
   :width: 70%
   :align: center

.. tip::
   When working in SEPAL, do not use your browser's **Back** function. Instead, use the buttons within the SEPAL interface to navigate to previous pages. In some instances, you may find an arrow in the upper-left or upper-right corner of the interface to navigate to a previous window.

Select language preference
--------------------------

Choose a language for your SEPAL environment by following the instructions in the video below.

.. youtube:: Lv0HwPDQx50

.. note::

   Language preferences can always be changed from the platform's `launch page <https://sepal.io/>`_

The default language in SEPAL is English; however, other languages are available (currently French and Spanish).

To change the language to either French or Spanish:

1.  Go to http://sepal.io.
2.  Select :code:`Launch`.
3.  In the upper-right corner, select **EN**, **ES** or **FR** (English, Spanish and French, respectively).

SEPAL interface
---------------

Home
^^^^

After logging in, you will see the following screen.

.. thumbnail:: ../_images/setup/presentation/sepal_home.png
    :title: SEPAL home screen
    :align: center
    :width: 70%


On the left, there are four main navigation buttons in the vertical **Tabs** bar (from top to bottom):

-   **Process**: Select imagery and create mosaics.
-   **Files**: Navigate through your personal SEPAL folders, where you can download, delete and visualize data using the **Data visualization** link.
-   **Terminal**: Access the command line for the LINUX server.
-   **Apps**: Follow links to a variety of preloaded tools.

Below the vertical **Tabs** bar – on the left – is another button:

-   **Tasks**: View a list of currently running tasks.

In the lower-right corner there are four buttons (from right to left):

-   **Log out from SEPAL** (displayed as a door with an arrow)
-   **User details** (displayed as your username)
-   **User report** (displayed as **$ 0/h**)
-   **User messages** (displayed as a bell)

In the **User details** pop-up window, you can:

-   view and edit user account information (e.g. name, password, email, organization; username can not be edited); and
-   link your GEE and SEPAL accounts by selecting **Use my own Google account** and following the instructions.

If your GEE and SEPAL accounts are connected, SEPAL uses your Google Drive as a temporary storage space for data downloaded to your SEPAL workspace (e.g. any imagery tiles or mosaics that you “retrieve to SEPAL workspace” will first be saved to your Google Drive account before being saved in your SEPAL workspace).

If your GEE and SEPAL accounts are not linked, data downloads to your SEPAL workspace will still be possible and the data will pass through SEPAL's Google Drive account.

.. tip::

   Unlinking your GEE and SEPAL accounts for downloading to SEPAL workspace may help if you do not have sufficient space available in your personal Google Drive.

Linking your GEE and SEPAL accounts will allow you to read and write from your GEE assets. To save data created in SEPAL as a GEE asset or to use your existing GEE assets in classifications or further processing in SEPAL, you will need to have your GEE and SEPAL accounts linked.

.. tip::

   Link your SEPAL and GEE accounts in order to read and write to GEE assets from SEPAL.

In the **User report** pop-up window, you can view the status (used/available) of your processing and storage resources:

-    **Instance spending** refers to the resources used/available to start and run cloud computers;
-    **Storage spending** and **Storage space** refer to the resources used/available for storage in your SEPAL workspace; and
-    **Sessions** refers to any processes in your current session, if you are running any.

.. thumbnail:: ../_images/setup/presentation/user_report_panel.png
   :title: User report panel
   :width: 350px
   :align: center

.. note::

   SEPAL should not be used for long-term data storage, as this is costly. The platform is best used by storing only the data necessary for processing. After processing and producing a product, data should be downloaded to your personal computer and deleted from SEPAL storage.


Process
^^^^^^^

In the vertical **Tabs** bar on the left, select the :code:`Process` button.

.. thumbnail:: ../_images/setup/presentation/process_tab_location.png
   :title: Arrow pointing to the process tab location
   :align: center
   :width: 70%

You should now see many options in the centre of the screen:

-   **Optical mosaic**: Create a mosaic using Landsat and/or Sentinel-2 data (for guidance, see **Exercise 1.2**).
-   **Radar mosaic**: Create a mosaic using Sentinel-1 data.
-   **Planet mosaic**: Create a mosaic using NICFI–Planet basemaps (if you have permission from NICFI-Planet).
-   **Classification**: Use a random forest model to classify images from SEPAL or GEE (for guidance, see **Module 2**).
-   **Time series**: Download time series information to your SEPAL storage.
-   **CCDC**: Create a Continuous Change Detection and Classification (CCDC) asset from a time series.
-   **CCDC slice**: Create a slice of a CCDC asset for a specific date or date range.
-   **Class change**: Create a class change map from two categorical images (either SEPAL recipes or GEE assets).
-   **Index change**: Create an index change map from two single-band images (either SEPAL recipes or GEE assets).
-   **Remapping**: Remap categorical or continuous image bands into new categories.

When you select one of these options, a new tab will open with the graphical user interface (GUI) that allows you to specify your desired options.

Files
^^^^^

In the vertical **Tabs** bar on the left, select the :code:`Files` button to display all files stored in your SEPAL workspace.

For example, select the :code:`Downloads` folder to display the folders containing any of the data you have downloaded in SEPAL. If you have not downloaded mosaics in SEPAL yet, this folder will be empty.

.. thumbnail:: ../_images/setup/presentation/files_menu.png
    :title: The Files menu
    :align: center
    :width: 50%

In the upper right, there are four buttons (from left to right; the three right-most buttons will be inactive until you select a file):

-   The first button will show hidden files (files and folder names starting with **.**).
-   The second button will download selected data to your local computer.
-   The third button will delete the selected folder or file.
-   The last button will clear your selection.

Terminal
^^^^^^^^

In the vertical **Tabs** bar on the left, select the :code:`Terminal` button.

This links you to the Linux command line that you can use in a variety of ways to manage data, load data from an outside location or process data using a series of commands.

.. _terminal-instances:

When you open the **Terminal**, it shows a menu to start, join or stop sessions. A session runs on an **instance**, a cloud computer whose type sets the number of CPUs, the amount of RAM, the temporary disk and the hourly cost.

.. thumbnail:: ../_images/setup/presentation/terminal.png
    :title: The Terminal menu: (1) spending, (2) instance types without SSD, (3) instance types with SSD, (4) active sessions and (5) the selection prompt
    :alt: SEPAL Terminal menu with the spending summary, the instance type tables, the active sessions table and the selection prompt.
    :align: center
    :width: 50%

The menu contains:

1.  Your **Instance spending**, **Storage spending** and **Storage used** for the month, as a percentage of your quotas.
2.  The **Available instance types without SSD** table.
3.  The **Available instance types with SSD** table.
4.  The **Active sessions** table, if you have sessions running, with an **ID** for each session.
5.  The **Select** prompt, where you enter your choice. The value in parentheses is used if you press **Enter** without typing anything.

Both instance type tables have the same columns:

-   **Type**: the name to enter in the prompt (for example, **m2**).
-   **CPU**: the number of virtual CPUs.
-   **GB RAM**: the memory, in GB.
-   **GB SSD**: the size of the SSD storage available under ``/tmp``. Instance types without SSD show **-** and get a 100 GB temporary disk instead.
-   **Perf.**: the CPU performance compared with a **t1** instance (**1.0x**). For example, an instance with **7.0x** processes roughly seven times faster than a **t1**.
-   **USD/h**: the cost per hour, charged to your instance spending while the session runs.

The first letter of the type indicates the balance between CPU and memory: **t** types are the smallest and cheapest, **m** types are general purpose, **c** types have more CPU for the same memory, **r** types have more memory for the same CPU, **x** types have very large amounts of memory, and **g** types include a GPU. Types ending in **d** are the SSD versions of the corresponding type (for example, **m2d** is an **m2** with 118 GB of SSD storage).

To choose an instance type:

-   Start with a small instance, such as **t1** or **m2**; they are enough for most tasks and cost-effective.
-   Choose a type with more **GB RAM** if your processing runs out of memory, or a type with a higher **Perf.** value if it is too slow.
-   Choose a type with SSD (**GB SSD**) if your temporary files do not fit in 100 GB. To learn how to use this storage, see :doc:`session_storage`.

To start a session:

1.  In the **Select** prompt, enter the **Type** of instance you want (for example, **m2**).
2.  Press **Enter** on your keyboard and wait for the instance to start, which can take a few minutes.

To join a running session, enter its **ID** from the **Active sessions** table (for example, **1**) and press **Enter**.

To stop a session:

-   in the **Terminal** menu, enter its **ID** followed by **s** (for example, **1s**) and press **Enter**; or
-   select the hourly cost button, :btn:`<fa-solid fa-dollar-sign> x.xx/h`, in the lower-right corner, choose **Sessions**, then select the trashcan icon of the session.

Once a session has stopped, you can start a new one with a larger or smaller instance type if necessary.

.. note::

    Stopping a session deletes everything stored in its temporary disk (``/tmp``). Files in your home folder are kept. For more information, see :doc:`session_storage`.


Apps
^^^^

In the vertical **Tabs** bar on the left, select the **Apps** button to display applications accessible through SEPAL (for more information about each app, select the rightmost **i** button).

Applications are preprogrammed (typically using R or Python) to perform specific useful tasks, making use of instances (running them will use your SEPAL computing resources).

.. thumbnail:: ../_images/setup/presentation/apps_interface.png
    :title: The Apps interface
    :align: center
    :width: 70%


Some of the apps include:

-   **R Studio**: Provides access to the R environment, where you can run processing scripts and upload data to your SEPAL folder.
-   **JupyterLab**: Provides access to the Python environment where you can run complex data workflows.
-   **BFAST GPU**: Graphics processing unit (GPU) implementation of the Breaks for Additive Season and Trend (BFAST) algorithm to analyse time series.
-   **Deforestation alert analysis**: Retrieves any type of alert on a selected area of interest (AOI).
-   **MGCI**: Calculates Sustainable Development Goal (SDG) 15.4.2: Mountain Green Cover Index (MGCI) at national/subregional scale.
-   **SMFM Biota**: Calculates biomass change over time using ALOS PALSAR data (SMFM refers to Satellite Monitoring for Forest Management).

For more information on available apps, see :doc:`../modules/index`.
