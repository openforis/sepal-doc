SMFM BIOTA
==========
*Calculate biomass change over time using ALOS PALSAR data*

The **Biomass Tool for ALOS (BIOTA)** is part of the World Bank's project, `Satellite Monitoring for Forest Management (SMFM) <https://www.smfm-project.com>`_. It was developed by `LTS International <https://ltsi.co.uk/>`_ and the `University of Edinburgh <https://www.ed.ac.uk/geosciences>`_ with an integration in the SEPAL platform developed by the SEPAL developer team. 

The tool relies on the use of JAXA's `ALOS PALSAR <https://www.eorc.jaxa.jp/ALOS/en/about/palsar.htm>`_ L-band mosaics, allowing users to produce outputs of:

-   calibrated Gamma0 backscatter
-   forest cover
-   above ground biomass (AGB)
-   ABG change
-   classified forest change types (e.g. deforestation, degradation)

In this article, you can learn how to use the **BIOTA tool** to calculate AGB in dry forests and savannahs, as well as change maps.

**Objectives**:

Generate maps of: 

-   AGB
-   Gamma0 backscatter
-   forest cover
-   AGB change
-   deforestation risk 
-   change type

**Prerequisites**: 

-   SEPAL account


Navigate to the **Apps** menu by selecting the wrench icon and entering **SMFM** into the search field. Then, select **SMFM Biota**.

.. note::

    Sometimes the tool takes a few minutes to load. Wait until you see the tool's interface. In case the tool fails to load properly (see figure below), close the tab and repeat the aforementioned steps. If this does not work, reload SEPAL.

    .. figure:: https://raw.githubusercontent.com/dfguerrerom/sepal_smfm_biota/main/doc/_img/biota_fail.png
        :alt: Failure of the BIOTA tool
        :align: center
        :width: 600
        
    If none of these steps work, you might need to start another instance. Please see `Introduction to SEPAL <https://docs.sepal.io/en/latest/setup/presentation.html#terminal-tab>`_ for steps on how to use the terminal to start a higher instance (an **m4** instance should be enough). (You should see an interface like the one in the following figure.)

.. figure:: https://raw.githubusercontent.com/dfguerrerom/sepal_smfm_biota/main/doc/_img/biota_interface.png
    :alt: The SMFM BIOTA interface
    :align: center
    :width: 600

.. tip::

    Depending on your computer screen size, the left column may appear on top of the content, as seen in the following figure.

    .. figure:: https://raw.githubusercontent.com/dfguerrerom/sepal_smfm_biota/main/doc/_img/biota_column.png
        :alt: Left column on top of the tool
        :align: center
        :width: 600

    If this is the case, you can either:
    
    -   Adjust your browser's zoom level, or

    .. figure:: https://raw.githubusercontent.com/dfguerrerom/sepal_smfm_biota/main/doc/_img/biota_chrome.png
        :alt: Example of how to adjust the zoom level on Google Chrome
        :align: center
        :width: 600

    -   Keep the zoom level, but click outside of the column to hide it. To open it again, you will need to select the three dots located in the upper right.

    .. figure:: https://raw.githubusercontent.com/dfguerrerom/sepal_smfm_biota/main/doc/_img/biota_three_dots.png
        :alt: How to display the left column again
        :align: center
        :width: 600

Downloading ALOS mosaics
""""""""""""""""""""""""

The first step is to select the parameters for accessing data from ALOS (JAXA). The data is delivered in SEPAL as either 1 x 1 degree tiles or 5 x 5 degree collections of tiles.

Under :code:`Required inputs`, define the latitude and longitude coordinates by clicking on your point of interest on the map that is shown on the right (this will be the upper-left coordinate of the tiles). The default values are -75 degrees for longitude and 0 degrees for latitude. 

For this exercise, we will demonstrate the steps for a point between the Moyowosi Game Reserve and the Kigosi Game Reserve, next to the border of the Getta and Kigoma regions in Tanzania (latitude -2.54, longitude 31.04).

.. figure:: https://raw.githubusercontent.com/dfguerrerom/sepal_smfm_biota/main/doc/_img/biota_map.png
    :alt: Selecting a point on the map
    :align: center
    :width: 600

.. note::

    The **BIOTA tool** was designed for woodlands and dry forests, as it uses a generic equation to calibrate Gamma0 backscatter to forest AGB developed using forest plot data from Malawi, Mozambique and Tanzania in Southern Africa. For global applicability, the tool supports the calibration of country-specific, backscatter–AGB relationships through determined parameters, which will be explained later in this article.

Next, we define the two years of interest. For this exercise, we will leave the default values (2016 for **Year 1** and 2017 for **Year 2**; Year 2 is used for calculating changes).

The tool gives you the option to choose a size of either a 1 x 1 degree tile or a 5 x 5 degree tile. We will select the 1 x 1 tile size.

Before selecting :code:`Download images`, we will look into the :code:`Optional inputs` tab.

.. figure:: https://raw.githubusercontent.com/dfguerrerom/sepal_smfm_biota/main/doc/_img/biota_optional_inputs_tab.png
    :alt: Location of the **Optional inputs** tab
    :align: center
    :width: 600

Different parameters can be changed here. These include the parameters that should be calibrated according to your AOI and specific forest characteristics. Default values are specific to Southern African forests.

.. csv-table::
    :header: Parameter, Role

    **Lee filter**, Applies a Lee filter to the data. This reduces inherent speckle noise in Synthetic Aperture Radar (SAR) imagery. Uncheck if you do not want the filter applied.
    **Window size**, Lee filter window size. Defaults to 5 x 5 pixels.
    **Downsample factor**, Applies downsampling to inputs by specifying an integer factor to downsample by. Defaults to 1 (i.e. no downsampling).
    **Forest threshold**, A forest AGB threshold (in tonnes per hectare [tC/ha]) to separate forest from non-forest (specific to your location). Defaults to 10 tC/ha.
    **Area threshold**, A minimum area threshold (in hectares) to be counted as forest (e.g. a forest patch must be greater than 1 ha in size). Defaults to 0 ha.
    **Change area threshold**, A threshold for a minimum change in forest area required to be flagged as a change. Defaults to 2 ha. This is for users who aim to produce change maps. 
    **Change magnitude threshold**, The minimum absolute change in biomass (in tC/ha) to be flagged as a change. Defaults to 15 tC/ha. This is for users who aim to produce change maps.
    **Contiguity**, The criterion of contiguity between two spatial units. The **rook** criterion defines neighbors by the existence of a common edge between two spatial units. The **queen** criterion is somewhat more encompassing and defines neighbours as spatial units sharing a common edge or a common vertex.
    **Polarization**, Which SAR polarization to use. Defaults to HV (referring to horizontal and vertical polarization).

We will leave the parameters with default values.

.. figure:: https://raw.githubusercontent.com/dfguerrerom/sepal_smfm_biota/main/doc/_img/biota_optional_inputs.png
    :alt: Optional parameters screen
    :align: center
    :width: 600

Go back to the :code:`Required inputs` tab and select :code:`Download Images` at the bottom. This will download all ALOS data tiles into your SEPAL account.

.. note::

    Depending on your point coordinates, it may take a significant amount of time before your data finish downloading. For the point in Tanzania, it should take about five minutes.

You can see the status of the downloads at the bottom of the page.

.. figure:: https://raw.githubusercontent.com/dfguerrerom/sepal_smfm_biota/main/doc/_img/biota_download_status.png
    :alt: Download status
    :align: center
    :width: 600

Once the downloads are finalized for both years, you are able to see the downloaded files under SEPAL :code:`Files`. Go to :code:`module_results` > :code:`smfm` > :code:`data`.

.. figure:: https://raw.githubusercontent.com/dfguerrerom/sepal_smfm_biota/main/doc/_img/biota_files.png
    :alt: SEPAL files with downloaded data.
    :align: center
    :width: 600

Here is a demonstration of the above steps:

.. youtube:: d759Aqi85HE
    :height: 315
    :width: 560

Processing the data and producing outputs
"""""""""""""""""""""""""""""""""""""""""

Now that the download has finished, we can process the data to produce the desired outputs.

Select the :code:`Process` tab on the left side.

.. figure:: https://raw.githubusercontent.com/dfguerrerom/sepal_smfm_biota/main/doc/_img/biota_process.png
    :alt: BIOTA Process window
    :align: center
    :width: 600

For **Year 1**, we will choose **Forest property**, which will automatically check all outputs available (**Gamma0**, **Biomass**, **Forest cover**). For **Year 2**, we will choose **Forest change** (changes between 2016 and 2017), which will also select all available outputs (**Biomass change**, **Change type**, **Deforestation risk**). These will be explained later. 

Select :code:`Get outputs` to start the processes.

.. figure:: https://raw.githubusercontent.com/dfguerrerom/sepal_smfm_biota/main/doc/_img/biota_process_get.png
    :alt: Select outputs and start the process by selecting **Get outputs**
    :align: center
    :width: 600

.. note::

    Depending on your point coordinates, it may take a significant amount of time before your data finish downloading (for the point in Tanzania, it should take approximately two minutes).

The tool will show the process status at the bottom. You will also note a change of colour from white to yellow next to each output (white = not started, yellow = processing, green = finalized).

.. figure:: https://raw.githubusercontent.com/dfguerrerom/sepal_smfm_biota/main/doc/_img/biota_output_processing.png
    :alt: Status of outputs
    :align: center
    :width: 600

Once complete, you will see a message similar to the one below, and all outputs will have a green light. 

.. figure:: https://raw.githubusercontent.com/dfguerrerom/sepal_smfm_biota/main/doc/_img/biota_output_done.png
    :alt: Process finalized
    :align: center
    :width: 600

Here is a demonstration of the above steps:

.. youtube:: OMGESeERRGo
    :height: 315
    :width: 560

Displaying your outputs
"""""""""""""""""""""""

With the outputs processed, we can now visualize the results.

In the same window, under :code:`Display outputs`, you can choose the process to display by selecting the dropdown **Select process** option.

Select **Biomass**. Then, press :code:`Display`. You will see the map appear on your screen (see figure below).

.. figure:: https://raw.githubusercontent.com/dfguerrerom/sepal_smfm_biota/main/doc/_img/biota_display.png
    :alt: Biomass map
    :align: center
    :width: 600

This is showing AGB in tonnes per hectare (tC/ha) for the 1 x 1 degree tile in Tanzania. To go back to the interface and select the other outputs, click anywhere on the screen outside of the map and do the same for the other results.

If you followed these exact steps, your outputs should look similar to the ones in the figure below. 

.. figure:: https://raw.githubusercontent.com/dfguerrerom/sepal_smfm_biota/main/doc/_img/biota_all.png
    :alt: BIOTA outputs for Tanzania
    :align: center
    :width: 600

A summary of each output is described in the table below.

.. csv-table::
    :header: Output, Description

    **Gamma0**, Gamma0 backscatter in decibels for the polarization specified
    **Biomass**, Biomass in tonnes per hectare
    **Forest/woody cover**, Binary classification of forested (1) and non-forested (0) areas
    **Change type**, Change described in seven different types (specified below)
    **Biomass change**, Change in biomass in tonnes per hectare
    **Deforestation risk**, Risk of deforestation from low (1) to high (3) 
    
There are seven change types described in the **BIOTA tool**, each of which is defined as a number (0 to 6) and colour-coded on the map. Change types include:

.. csv-table::
    :header: Change class, Pixel value, Description

    **Deforestation**, 1, A loss of AGB that crosses the ``forest_threshold``.
    **Degradation**, 2, A loss of AGB in a location above the ``forest_threshold`` in both images.
    **Minor loss**, 3, A loss of AGB that does not cross the ``change_area_threshold`` or ``change_magnitude_threshold``.
    **Minor gain**, 4, A gain of AGB that does not cross the ``change_area_threshold`` or ``change_magnitude_threshold``.
    **Growth**, 5, A gain of AGB in a location above the ``forest_threshold`` in both images.
    **Afforestation**, 6, A gain of AGB that crosses the ``forest_threshold``.
    **Non-forest**, 0, Below the ``forest_threshold`` in both images.

You can also use the :code:`Write raster` option to save this map into your SEPAL account. Once you select **Write raster**, you should see a message in green informing you that your export has been completed.

.. figure:: https://raw.githubusercontent.com/dfguerrerom/sepal_smfm_biota/main/doc/_img/biota_export.png
    :alt: Map export complete for the **Change type** output.
    :align: center
    :width: 600

The file will then be located in your SEPAL **Files**. You can download this map by selecting it and selecting the **Download** button in the upper-right corner. This will download the output as a .tif file that can be used in GIS software.

.. figure:: https://raw.githubusercontent.com/dfguerrerom/sepal_smfm_biota/main/doc/_img/biota_export_file.png
    :alt: Exported map in **Files**
    :align: center
    :width: 600

Here is a demonstration of the above steps:

.. youtube:: my8U5TaV9IU
    :height: 315
    :width: 560

Additional resources
""""""""""""""""""""

On the left side, you can access:

-   **Source code**: The source code of the tool, which is a GitHub repository.
-   **Wiki**: The README file of the tool, where you can find additional information and instructions about how to use the tool.
-   **Bug report**: The issue creation page on the GitHub repository of the tool, where you can report a bug or issue with using the tool.

.. figure:: https://raw.githubusercontent.com/dfguerrerom/sepal_smfm_biota/main/doc/_img/biota_resources.png
    :alt: Additional resources
    :align: center
    :width: 600

.. custom-edit:: https://raw.githubusercontent.com/sepal-contrib/sepal_smfm_biota/release/doc/en.rst
