:html_theme.sidebar_secondary.remove:

.. image:: _images/sepal_light.png
    :align: center
    :class: main-logo only-light only-big

.. image:: _images/sepal_dark.png
    :align: center
    :class: main-logo only-dark center only-big

.. image:: _images/logo_light.png
    :align: center
    :class: main-logo only-light only-small

.. image:: _images/logo_dark.png
    :align: center
    :class: main-logo only-dark center only-small

.. The page title must be in rST for it to show in next/prev page buttons.
   Therefore we add a special style rule to only this page that hides h1 tags

.. raw:: html

    <style type="text/css">
        h1 {text-align:center;}
        h2 {text-align:center;}
        h3 {text-align:center;}
        .bd-main .bd-content .bd-article-container {max-width: 100%;}
        .big-font {font-size: var(--pst-font-size-h4); color: var(--pst-color-primary)}
        .video_wrapper.align-center {margin: auto;}
    </style>

Documentation
=============

.. toctree::
   :maxdepth: 1
   :hidden:

   Getting started<setup/index>
   Cookbook<cookbook/index>
   Modules<modules/index>
   CLI<cli/index>
   Workflows<workflows/index>
   Features<feature/index>
    <team/index>

.. rst-class:: text-center

    System for Earth Observation Data Access, Processing and Analysis for Land Monitoring

.. rst-class:: text-center font-weight-bold big-font

    An open-source project and platform empowering people around the world to gain a better understanding of land cover dynamics by facilitating the efficient access and use of Earth observation data – without the need of coding knowledge.

.. youtube:: niOUVE8N7wo
    :align: center
    :width: 60%

Learn how to use the platform with SEPAL documentation
------------------------------------------------------

.. rst-class:: text-center

    The SEPAL team developed this GitHub page to help users get the most out of the interface.

Getting started
^^^^^^^^^^^^^^^

.. grid:: 1 3 3 3
    :gutter: 2

    .. grid-item-card:: :fas:`running` Register to SEPAL
        :link: setup/register.html

        Set up your SEPAL account and request additional resources.

    .. grid-item-card:: :fas:`plug` Connect to GEE
        :link: setup/gee.html

        Register with Google Earth Engine (GEE) and connect your account to SEPAL.

    .. grid-item-card:: :fas:`plug` Connect to NICFI PlanetLab imagery
        :link: setup/nicfi.html

        Sign up to use Norway’s International Climate and Forests Initiative (NICFI) – PlanetLab data and connect your account to GEE.

Recipes and modules
^^^^^^^^^^^^^^^^^^^

.. grid:: 1 3 3 3
    :gutter: 2

    .. grid-item-card:: :fas:`book-open` Start a recipe
        :link: cookbook/index.html

        Run analysis with recipes, the foundation of SEPAL processes.

    .. grid-item-card:: :fas:`cogs` Start a module
        :link: modules/index.html

        Run integrated workflows with modules – no need of coding experience required.

    .. grid-item-card:: :fas:`map` Use the se.plan module
        :link: modules/dwn/seplan.html

        Compute your restoration index with se.plan, a spatially explicit online tool designed to support forest restoration planning decisions by restoration stakeholders.

Other resources
^^^^^^^^^^^^^^^

.. grid:: 1 2 2 2
    :gutter: 2

    .. grid-item-card:: :fas:`rss` SEPAL website
        :link: https://sepal.io/

        Discover the impact of the project.

    .. grid-item-card:: :fas:`rss` Open Foris
        :link: https://openforis.org/

        Browse the Suite of Tools.

SEPAL is always improving
-------------------------

.. rst-class:: center-text

    Our team members are committed to improving the platform and its documentation to enhance user experience.

    Encounter a problem? See an issue?  Need help? Take one of the following actions to make the project better.


.. grid:: 1 2 2 4
    :gutter: 2

    .. grid-item-card:: :fas:`comments` Ask the Google Group community
        :link: https://groups.google.com/g/sepal-users

    .. grid-item-card:: :fab:`github` Use the GitHub Issue Tracker
        :link: https://github.com/openforis/sepal/issues

    .. grid-item-card:: :fab:`stack-exchange` Ask the GIS StackExchange community
        :link: https://gis.stackexchange.com/questions/tagged/sepal

    .. grid-item-card:: :fas:`book-open` Register for an online facilitated course from the FAO elearning Academy
        :link: https://www.fao.org/in-action/sepal/activities/Elearning/en

About the platform
------------------

.. rst-class:: text-center

    SEPAL is part of the `Open Foris <http://www.openforis.org>`__ suite of tools. The platform allows users to query and process satellite data quickly and efficiently, tailor their products for local needs, and produce sophisticated and relevant geospatial analyses quickly. Harnessing cloud-based supercomputers and modern geospatial data infrastructures (e.g. GEE), the interface enables access and processing of historical satellite data as well as newer data from Landsat and higher-resolution data from Europe’s Copernicus program.

    SEPAL is a cloud computing-based platform for autonomous land monitoring using remotely-sensed data. It is a combination of GEE and open-source software such as GDAL, Jupyter, the Open Foris Geospatial Toolkit, ORFEO Toolbox, Python, R, R Shiny Server, R Studio Server and SNAP Toolkit. The platform allows users to access powerful cloud-computing resources to query, access and process satellite data quickly and efficiently for creating advanced analyses.

Suporting institutions
----------------------

.. rst-class:: text-center

    SEPAL is a project of the Forestry Department of the United Nations Food and Agriculture Organization (FAO) funded by the Government of Norway.

.. logos:: funders

.. logos:: institutions
