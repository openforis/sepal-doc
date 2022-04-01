Reset password
==============

If you have forgotten your log-in password, you might want to retrieve or reset it by proving you have access to the email address of your account. A password may be recovered by submitting a request through one of the website's logon forms.

.. warning::

    Resetting passwords is not possible without the email address used to log in to the platform. Test every email you can think about before going back to the registration form.

This process will be performed in 3 steps presented on the following page.

Tell us who you are
-------------------

In the first step, click the :code:`forgot password?` link on the SEPAL landing page.

.. thumbnail:: ../_images/setup/password/landing.png
   :title: landing page of SEPAL where the user can find the "forgot password" button
   :group: setup_password

Now that you are on the reset password page, enter the email address you used to register on SEPAL in the "email" text field of the page. When you're done click :btn:`<fas fa-envelope> Reset password`.

.. thumbnail:: ../_images/setup/password/email-setup.png
   :title: the reset password page where the user can specify its email adress
   :group: setup_password

.. warning:: 

    If the field becomes red, it means that your email address was not found in our database. Be careful with typos and test multiple addresses —you may have used another when you registered. 

If the email is validated, a confirmation email will be sent from SEPAL to your associated email address. The notification system will display a note of the information on the top right corner of the screen.

.. thumbnail:: ../_images/setup/password/email-confirmation.png
   :title: the confirmation notification that a reset password email have been send to your account
   :group: setup_password


Email confirmation
------------------

To reset your password, SEPAL uses an email confirmation system because: 

-   Attackers cannot lock the accounts of other users by guessing their user names and using the forgotten password recovery function.
-   Passwords cannot be read from the email by potential attackers.
-   The reset links are only valid temporarily.
-   After someone uses a password reset link, it becomes invalid and cannot be accessed again.

For all these reasons, SEPAL will send you the following email. 

.. thumbnail:: ../_images/setup/password/email.png
   :title: example of a reset password email
   :group: setup_password

Clik the :code:`this` link. It will open the reset password interface on a new browser page.

Change password
---------------

In the reset password interface, 3 fields are available:

-   **username:** the username associated with your email address in the database.
    
    .. note::
    
        It cannot be changed

-   **password:** the new password you will set 
-   **confirm password:** a security field where you need to provide the same password

Provide a password in the :code:`password` field and repeat it in the :code:`confirm password`. If the two fields are not exactly the same, the form cannot be validated. 
Once everything is set, click on :btn:`<fas fa-check> Set password` to validate your new password.

.. thumbnail:: ../_images/setup/password/change-password.png
   :title: the change password interface
   :group: setup_password

Once validated, the new password will be automatically associated with your account. The user will be automatically authenticated and a notification will be displayed at the top right side of the screen.

.. thumbnail:: ../_images/setup/password/change-password-notification.png
   :title: the change password interface
   :group: setup_password
