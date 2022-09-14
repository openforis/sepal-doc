Use NICFI - Planet Lab data
===========================

.. note:: 

    Adapted from `<https://developers.planet.com/docs/integrations/gee/nicfi/>`_. 
    
Overview
--------

Through Norway’s International Climate & Forests Initiative (NICFI), anyone can now access Planet’s high-resolution, analysis-ready mosaics of the world’s tropics to help reduce and reverse the loss of tropical forests, combat climate change, conserve biodiversity, and facilitate sustainable development.

In support of NICFI’s mission, you can use this data for a number of purposes, including, but not limited to:

-   advance scientific research about the world’s tropical forests and the critical services they provide;
-   implement and improve policies for sustainable forest management and land use in developing tropical forest countries and jurisdictions;
-   increase transparency and accountability in the tropics;
- protect and improve the rights of indigenous peoples and local communities in tropical forest countries; and
- innovate solutions towards reducing pressure on forests from global commodities and financial markets.
    

The NICFI & Planet Basemaps for Tropical Forest Monitoring are now available in Google Earth Engine (GEE) and SEPAL for easy processing. In a few simple steps, you can create your own custom mosaics using the Planet basemaps.

The first step is to make sure you have a GEE account. You can follow _`This tutorial <setup/register.html#sign-up-to-gee>` to register for a GEE account if you don’t already have one.

Sign up for NICFI imagery
-------------------------

Sign up for NICFI Planet data access using the same email address associated with your GEE account. You can sign up for access to the NICFI data program here: `<https://www.planet.com/nicfi/>`_. Make sure to include your email address that has access to GEE in the field, “What is your GEE identity?”. 

.. thumbnail:: ../_images/setup/nicfi/landing.png
   :title: Planet NICFI landing page.
   :group: setup_nicfi
   
.. tip::

    If you are already a NICFI user and would like to access the Basemaps in GEE, you can apply for access using this `Sign-up page <https://www.planet.com/nicfi/?gee=show>`_. 
    
.. note::
    
    Approval for accessing NICFI-Planet Basemaps in GEE can take up to one week.
    
Access NICFI through GEE
------------------------

The NICFI Planet data can also be accessed from GEE, allowing you to use the PlanetLab imagery in SEPAL recipes, such as the Classification or Time series, by authorizing your GEE account to access PlanetLab data. 

Go back to the Planet `Platform Explorer <https://www.planet.com/explorer>`__ page and click on :guilabel:`My Account` in the upper-right corner of the page. 

.. thumbnail:: ../_images/setup/nicfi/explorer.png
    :title: The platform explorer of the PlanetLab website. My account dropdown appears when hovering.
    :group: setup_nicfi
    
On the next page, click on :guilabel:`All Plans` (2), which should activate your NICFI level 1 data access (1). If it does, click on :guilabel:`My settings` (3) and scroll down to the bottom of the page. 

.. thumbnail:: ../_images/setup/nicfi/plans.png
    :title: The plans that are linked to your NICFI account.
    :group: setup_nicfi
    
Click on :guilabel:`Edit access` (1) on the lower-right side of the page. Select all of the checkboxes (2) and provide the email address (3) associated with your GEE account. Click on :guilabel:`Connect to Earth Engine` (4) to finalize the registration.

.. note:: 

    To connect to GEE, your GEE address must be the same as the email address used for SEPAL.
    
.. thumbnail:: ../_images/setup/nicfi/gee.png
    :title: The registration form to authorize a GEE account to access your Planet product.
    :group: setup_nicfi


The next step is to make sure SEPAL is connected to the same email address that has access to NICFI-Planet Basemaps in GEE using the same process as in :code:`GEE`.

If you are already connected to a Google account with access to NICFI-Planet Basemaps in GEE, you can skip the next step.

.. figure:: ../_images/setup/gee/user_interface_connected.png
    :alt: SEPAL and GEE connected.
    :align: center
    :width: 50%

If you are either not connected to your Google account or connected via a different email that does not have access to the NICFI-Planet Basemaps, click on :btn:`<fab fa-google> Google account` and select the email address that has access to NICFI-Planet Basemaps in GEE. 

.. note::

    Allow SEPAL to access your GEE data and Google Drive account, required components for processing. 

.. important::

    For additional information that may help when processing the NICFI/Planet high resolution imagery in SEPAL, please refer to the section of `Planet academy <https://university.planet.com/path/nicfi>`__ dedicated to NICFI imagery. 
