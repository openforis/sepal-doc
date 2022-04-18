Use NICFI - Planet Lab data
===========================

.. note:: 

    Adapted from `<https://developers.planet.com/docs/integrations/gee/nicfi/>`_. 
    
Overview
--------

Through Norway’s International Climate & Forests Initiative (NICFI), anyone can now access Planet’s high-resolution, analysis-ready mosaics of the world’s tropics in order to help reduce and reverse the loss of tropical forests, combat climate change, conserve biodiversity, and facilitate sustainable development.

In support of NICFI’s mission, you can use this data for a number of projects including, but not limited to:

-   Advance scientific research about the world’s tropical forests and the critical services they provide.
-   Implement and improve policies for sustainable forest management and land use in developing tropical forest countries and jurisdictions.
-   Increase transparency and accountability in the tropics.
- Protect and improve the rights of indigenous peoples and local communities in tropical forest countries.
- Innovate solutions towards reducing pressure on forests from global commodities and financial markets.
    

The NICFI & Planet Basemaps for Tropical Forest Monitoring are now available in Google Earth Engine and in SEPAL for easy processing. With a few simple steps, you can create your own custom mosaics using the Planet basemaps.

First make sure you have a Google Earth Engine account. Follow _`this tutorial <setup/register.html#sign-up-to-gee>` to apply for a GEE account if you don’t already have one.

Sign-up for NICFI imagery
-------------------------

Sign up for a NICFI Planet data access using the same email address that has access to Google Earth Engine. You can sign up for access to the NICFI data program here: `<https://www.planet.com/nicfi/>`_ and make sure to specify your email address that has access to GEE in the field “What is your GEE identity” 

.. thumbnail:: ../_images/setup/nicfi/landing.png
   :title: planet nicfi landing page
   :group: setup_nicfi
   
.. tip::

    If you are already a NICFI user and would like to access the Basemaps in GEE, you can apply for access using this `sign up page <https://www.planet.com/nicfi/?gee=show>`_. 
    
.. note::
    
    Approval for accessing NICFI-Planet Basemaps in GEE can take up to one week.
    
Access NICFI through Google Earth Engine
----------------------------------------

The NICFI Planet data can also be accessed from Google Earth Engine. In SEPAL, it will allow you to use the PlanetLab imagery in recipes such as classification or time series. To do so you need to authorized your GEE account to access PlanetLab data. 

Go back to the planet `Platform Explorer <https://www.planet.com/explorer>`__ page and click on :guilabel:`My Account` in the top right corner of the page. 

.. thumbnail:: ../_images/setup/nicfi/explorer.png
    :title: The platform explorer of the PlanetLab website. my account dropdown opens itself on hover.
    :group: setup_nicfi
    
On the next page, click on :guilabel:`All Plans` (2), your NICFI level 1 data access should be activated (1). If yes, click on :guilabel:`My settings` (3) and scroll down to the bottom of the page. 

.. thumbnail:: ../_images/setup/nicfi/plans.png
    :title: the plans that are linked to your NICFI account
    :group: setup_nicfi
    
click on :guilabel:`Edit access` (1) at the bottom right side of the page. Check all the checkboxes (2) and fill the email adress (3) you're using in GEE. Click on :guilabel:`Connect to Earth Engine` (4) to finalize the registration.

.. warning:: 

    The provided GEE adress need to be the same as the one provided in SEPAL to connect to GEE.
    
.. thumbnail:: ../_images/setup/nicfi/gee.png
    :title: the registration form to authorized a GEE account to access your Planet product
    :group: setup_nicfi


Next step is to make sure SEPAL is connected to the same email address that has access to NICFI-Planet Basemaps in GEE using the same process as in :code:`gee`.

If you are connected to a Google account and that is the same account that as access to NICFI-Planet Basemaps in GEE, great!

.. figure:: ../_images/setup/gee/user_interface_connected.png
    :alt: sepal and gee connected
    :align: center
    :width: 50%

If you are not connected to your Google account or are connected via a different email that does not have access to the NICFI-Planet Basemaps, click on :btn:`<fab fa-google> Google account` and select the email address that has access to NICFI-Planet Basemaps in GEE. 

.. note::

    Allow SEPAL to access your GEE data and Drive, this is needed for processing. 

.. important::

    Now you are ready to easily access and process the NICFI-Planet Basemaps in SEPAL!!  