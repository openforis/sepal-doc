Use Norway’s International Climate and Forests Initiative (NICFI) - Planet Lab data
===================================================================================

Sign up for NICFI and connect with Google Earth Engine (GEE)
------------------------------------------------------------

In this article, you can learn how to:

-   Sign up for NICFI imagery
-   Access NICFI through GEE

.. note:: 

    Adapted from `<https://developers.planet.com/docs/integrations/gee/nicfi/>`_. 
    
Overview
--------

Through NICFI, anyone can now access Planet’s high-resolution, analysis-ready mosaics of the world’s tropics to help reduce and reverse the loss of tropical forests, combat climate change, conserve biodiversity, and facilitate sustainable development.

In support of NICFI’s mission, you can use this data for a number of purposes, including, but not limited to:

- advancing scientific research about the world’s tropical forests and the critical services they provide;
- implementing and improving policies for sustainable forest management and land use in developing tropical forest countries and jurisdictions;
- increasing transparency and accountability in the tropics;
- protecting and improving the rights of Indigenous Peoples and local communities in tropical forest countries; and
- innovating solutions towards reducing pressure on forests from global commodities and financial markets.
    
The NICFI & Planet Basemaps for Tropical Forest Monitoring are now available in Google Earth Engine (GEE) and SEPAL for easy processing. In a few simple steps, you can create your own custom mosaics using the Planet basemaps.

The first step is to make sure you have a GEE account. You can follow `this tutorial <setup/register.html#sign-up-to-gee>` to register for a GEE account if you don’t already have one.

Sign up for NICFI imagery
-------------------------

Sign up for NICFI Planet data access using the same email address associated with your GEE account. To sign up for access to the NICFI data program, go to `<www.planet.com/nicfi/>`_. In the field, **What is your GEE identity?**, enter the email address that has access to GEE. 

.. thumbnail:: ../_images/setup/nicfi/landing.png
   :title: Planet NICFI landing page.
   :group: setup_nicfi
   
.. tip::

    If you are already a NICFI user and would like to access the basemaps in GEE, go to `<www.planet.com/nicfi/?gee=show>`_ to apply for access. 
    
.. note::
    
    Approval for accessing NICFI-Planet Basemaps in GEE can take up to one week.
    
Access NICFI through GEE
------------------------

The NICFI Planet data can also be accessed from GEE, allowing you to use the PlanetLab imagery in SEPAL recipes, such as **Classification** or **Time series**, by authorizing your GEE account to access PlanetLab data. 

1.  Go to the `Planet Platform Explorer <www.planet.com/explorer>`__ and select **My Account** in the upper-right corner. 

.. thumbnail:: ../_images/setup/nicfi/explorer.png
    :title: The platform explorer of the PlanetLab website. The **My account** dropdown menu appears when hovering.
    :group: setup_nicfi
    
2.  Select **All Plans** (2), which should activate NICFI level 1 data access (1). If it does, select **My settings** (3) and scroll down to the bottom of the page. 

.. thumbnail:: ../_images/setup/nicfi/plans.png
    :title: The plans that are linked to your NICFI account.
    :group: setup_nicfi
    
3.  Select **Edit access** (1) in the lower-right. 

4.  Select all of the checkboxes (2) and enter the email address (3) associated with your GEE account. 

5.  Select **Connect to Earth Engine** (4) to finalize the registration.

.. note:: 

    To connect to GEE, your GEE email address must be the same as the email address used for SEPAL.
    
.. thumbnail:: ../_images/setup/nicfi/gee.png
    :title: The registration form to authorize a GEE account to access your Planet product.
    :group: setup_nicfi

The next step is to make sure SEPAL is connected to the same email address that has access to NICFI-Planet Basemaps in GEE using the same process as in GEE.

Note: If you are already connected to a Google account with access to NICFI-Planet Basemaps in GEE, you can skip the next step.

.. figure:: ../_images/setup/gee/user_interface_connected.png
    :alt: SEPAL and GEE connected.
    :align: center
    :width: 50%

If you are either not connected to your Google account or connected via a different email address that does not have access to the NICFI-Planet Basemaps, select **Google account** and choose the email address that has access to NICFI-Planet Basemaps in GEE. 

.. note::

    Allow SEPAL to access your GEE data and Google Drive account, which are required components for processing. 

.. important::

    For additional information that may help when processing the NICFI/Planet high-resolution imagery in SEPAL, please refer to `the section of Planet Academy <https://university.planet.com/path/nicfi>`__ dedicated to NICFI imagery. 


For support, :doc:`ask the community <>` or contact the SEPAL team at SEPAL@fao.org.
