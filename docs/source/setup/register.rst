Register to SEPAL
=================

SEPAL is a computing-based platform for autonomous land monitoring, to gain access to the platform you will first have to create an account and, depending on your needs :ref:`request additional resources <request>`. 

In this guide you will learn how to:

- :ref:`Create an account (mandatory) <create>`
- :ref:`Request for additional resources (recommended) <request>`
- :ref:`Register and link with Google Earth Engine (recommended) <gee>`
- :ref:`Register to Collect Earth Online (optional) <ceo>`

.. _create:

Create an account
-----------------

Requesting an account in SEPAL is an automatic process, to start it, use your browser and go to `sepal.io <https://sepal.io/>`_, you will see the landing page (left image below) with two buttons: :btn:`launch` and :btn:`documentation`, click launch button, the splash page (right) with the log-in form will be loaded, locate the green :btn:`Sign up` button and click it.

.. thumbnail:: ../_images/setup/register/sepal_landing.png
    :width: 49%
    :group: landing
    :title: sepal.io landing page

.. thumbnail:: ../_images/setup/register/sepal_splash_page.png
    :width: 49%
    :group: landing
    :title: sepal.io splash page

In the sign-up form, all the fields are mandatories, set a username, your name, email address, and your organization. Note that at this point you do not have to set a password.

.. thumbnail:: ../_images/setup/register/sepal_sign_up.png
    :width: 60%
    :align: center
    :group: register
    :title: sign up form


Click the :btn:`sign-up` button. If all the fields were successfully validated, a popup message will be displayed at the top right corner saying that a confirmation email has been sent to your email.

.. thumbnail:: ../_images/setup/register/sepal_sent_message.png
    :width: 40%
    :align: center
    :group: register
    :title: sign up form


Check your mailbox and click the link inside to validate your account. You will be redirected to the password creation form, fill the fields and click the :btn:`sign-up` button. If everything goes well you will now inside SEPAL.

.. thumbnail:: ../_images/setup/register/sepal_confirmation_email.png
    :width: 80%
    :align: center
    :group: register
    :title: confirmation email

.. tip:: 

    Once you sign up for SEPAL, you can request access to the Sepal Users Google Group by following this `link <https://groups.google.com/g/sepal-users>`_ and clicking on the button, :guilabel:`Ask to join group`. 
    If you need help, navigate to the `GIS.StackExchange <https://gis.stackexchange.com/questions/tagged/sepal>`_ platform and ask a question to the community using the :guilabel:`sepal` tag. Your question might be useful to others! 


With this fresh account, you can perform some basic operations, such as recipes (not retrieve), visualization or navigating through the platform. To get full access, go to :ref:`request access section <request>`.

.. note:: Even though you are now logged into the platform, some of the SEPAL features are not fully available —see the left tabs bar: :btn:`<fas fa-terminal> terminal` and :btn:`<fas fa-wrench> tools` buttons are deactivated, this is because these functions require an instance (check how to instantiate an instance) and a quota (:ref:`see how to request quota resources <request>`).

    .. thumbnail:: ../_images/setup/register/sepal_recent_disabled_buttons.png
        :width: 30%
        :align: center
        :group: register
        :title: Fresh account. Disabled options.

.. _request:

Request resources (quota)
-------------------------

Requesting processing resources will allow you to use all the modules built into SEPAL, development tools as Jupyter or RStudio, as well as access to the command line terminal. 

To request resources, click the quota button that is located in the bottom right corner, and click the green button :btn:`<fas fa-pencil-alt> Request additional resources`, a form asking you for the limits (instance, storing and storage) and a message that will be read by the platform administators. If you are not sure how many resources you will use, please visit the `resource management <resource>`_ section, where more detailed info can be found.

.. thumbnail:: ../_images/setup/register/sepal_request_button.png
    :width: 62%
    :group: request
    :title: Request additional resources

.. thumbnail:: ../_images/setup/register/sepal_request_form.png
    :width: 38%
    :group: request
    :title: Request form

.. note::  Applications are evaluated by the administrators to prevent bots and malicious users from accessing the platform. 

.. _gee:

Sign up for Google Earth Engine (GEE)
-------------------------------------

.. note::

    This step is not required. SEPAL can run computation on its own GEE account on your behalf. However, we highly recommend signing up for this service to improve your experience.

You will need to have a Google email address to sign up for GEE. If you don't have one already, you can sign up here: http://mail.google.com/mail/sign-up. 

With your Google email address, you can request a GEE account by visiting https://earthengine.google.com/new_signup/.

.. image:: ../_images/setup/register/gee_landing.png
   :alt: Request access to Google Earth Engine (GEE).
   :align: center

Once you have a GEE account, you can access the interface here: https://code.earthengine.google.com/.

.. image:: ../_images/setup/register/gee_code.png
   :alt: GEE code editor
   :align: center

.. tip::

    If you experience problems registering with GEE, contact the SEPAL team for assistance.

.. _ceo:

Sign up for Collect Earth Online (CEO)
--------------------------------------

.. note::

    This step is not required. However, to get the most out of our classification and validation tools, we highly recommend using CEO for collecting point-based training and validation data.

You can access CEO in Google Chrome, Mozilla Firefox or Microsoft Edge by navigating to https://collect.earth/ and clicking on :code:`Login/Register` in the upper-right corner. After clicking on :code:`Register a new account` and following the instructions, you can log in with your **email** and **password**.

.. image:: ../_images/setup/register/ceo_landing.png
   :alt: CEO landing page
   :align: center

.. tip::

    If you forget your password, click on :code:`Forgot your password?` and follow the instructions.
