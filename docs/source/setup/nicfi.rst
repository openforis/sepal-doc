Use NICFI–PlanetLab data
========================
*Sign up for NICFI and connect with GEE*

.. warning:: Discontinuation of SEPAL-Planet NICFI Connection: We would like to inform you that the connection between SEPAL and Planet NICFI is no longer available because the NICFI Satellite Data Program has ended as of April 1, 2025. This termination means that any prior instructions or configurations for connecting to Planet NICFI are now obsolete. We appreciate your understanding and support during this transition. For any further inquiries or assistance, please visit: https://www.planet.com/tropical-forest-observatory/ for more information on the NICFI Satellite Data Program and its discontinuation.

In this article, learn how to:

-   sign up for NICFI imagery
-   access NICFI through GEE

.. note::

    Adapted from `<https://developers.planet.com/docs/integrations/gee/nicfi>`_.

Overview
--------

Through Norway’s International Climate and Forests Initiative (NICFI), anyone can access Planet’s high-resolution, analysis-ready mosaics of the world’s tropics to help reduce and reverse the loss of tropical forests, combat climate change, conserve biodiversity and facilitate sustainable development.

In support of NICFI’s mission, you can use this data for a number of purposes, such as:

- advancing scientific research about the world’s tropical forests and the critical services they provide;
- implementing and improving policies for sustainable forest management and land use in developing tropical forest countries and jurisdictions;
- increasing transparency and accountability in the tropics;
- protecting and improving the rights of Indigenous Peoples and local communities in tropical forest countries; and
- innovating solutions towards reducing pressure on forests from global commodities and financial markets.

The NICFI and Planet Basemaps for Tropical Forest Monitoring are now available in Google Earth Engine (GEE) and SEPAL for easy processing. In a few simple steps, you can create your own custom mosaics using Planet basemaps.

The first step is to make sure you have a GEE account.

If you don’t have a GEE account, register by following `this tutorial <setup/register.html#sign-up-to-gee>`__.

Sign up for NICFI imagery
-------------------------

Sign up for NICFI–PlanetLab data access using the same email address associated with your GEE account.

To get access to the NICFI data programme, go to `<https://www.planet.com/nicfi>`_.

.. thumbnail:: ../_images/setup/nicfi/nicfi_page.png
   :title: Planet–NICFI landing page
   :group: setup_nicfi


Select the **Sign up** button and fill in the form.

.. thumbnail:: ../_images/setup/nicfi/signup.png
   :title: Sign up form
   :group: setup_nicfi

After submitting the form, an email will be sent with a link to activate your account.
Check your email for an invitation to complete the signup process.

Select the link and a new form will appear. Complete the form and you will receive a success message with a new page to sign in to your account.

.. thumbnail:: ../_images/setup/nicfi/activate_account.png
   :title: Account activation form
   :group: setup_nicfi

.. tip::

    If you are already a NICFI user and would like to access the basemaps in GEE, apply for access by going to `<www.planet.com/nicfi/?gee=show>`_.

.. note::

    Approval for accessing NICFI–Planet Basemaps in GEE can take up to one week.

Access NICFI through GEE
------------------------

NICFI–PlanetLab data can also be accessed from GEE, allowing you to use PlanetLab imagery in SEPAL recipes, such as **Classification** or **Time series**.

To authorize your GEE account to access PlanetLab data:

1.  Go to the `Planet Platform Explorer <www.planet.com/explorer>`__. In the upper-right corner, select **My Account**.

.. thumbnail:: ../_images/setup/nicfi/explorer.png
    :title: The platform explorer of the PlanetLab website; the **My account** dropdown menu appears when hovering
    :group: setup_nicfi

2.  Select **All plans** (see **2** in figure below), which should activate NICFI level 1 data access (**1** in figure below). If it does, select **My settings** (**3** in figure below) and scroll down to the bottom of the page.

.. thumbnail:: ../_images/setup/nicfi/plans.png
    :title: The plans that are linked to your NICFI account
    :group: setup_nicfi

3.  Select **Edit access** (**1**) in the lower right.

4.  Select all checkboxes (**2**) and enter the email address (**3**) associated with your GEE account.

5.  Select **Connect to Earth Engine** (**4**) to finalize registration.

.. note::

    To connect to GEE, your GEE email address must be the same as the email address used for SEPAL.

.. thumbnail:: ../_images/setup/nicfi/gee.png
    :title: The registration form to authorize a GEE account to access your Planet product
    :group: setup_nicfi

The next step is to make sure SEPAL is connected to the same email address that has access to NICFI–Planet Basemaps in GEE using the same process as in GEE.

Note: If you are already connected to a Google account with access to NICFI–Planet Basemaps in GEE, you can skip this step.

.. figure:: ../_images/setup/gee/user_interface_connected.png
    :alt: SEPAL and GEE connected
    :align: center
    :width: 50%

If you are either not connected to your Google account or connected via a different email address that does not have access to NICFI–Planet Basemaps, select **Google account** and choose the email address that has access to NICFI–Planet Basemaps in GEE.

.. note::

    Allow SEPAL to access your GEE data and Google Drive account, which are required components for processing.

.. important::

    For additional information that may help when processing high-resolution NICFI–Planet imagery in SEPAL, refer to `Planet Academy's section dedicated to NICFI imagery <https://university.planet.com/path/nicfi>`__.
