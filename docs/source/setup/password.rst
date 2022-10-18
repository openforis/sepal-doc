Reset password
==============

If you have forgotten your log-in password, you can retrieve or reset it by proving you have access to the email address associated with your account. A password may be recovered by submitting a request by following the directions located at one of the website's log-in forms.

.. note::

    Resetting passwords is not possible without knowing and having access to the email address used to log in to the platform. Before requesting a new account with SEPAL, we suggest testing all of your email accounts first.

This password reset and retrieval process will be performed in three steps, as presented on the following page.

Tell us who you are
-------------------

Click the :code:`Forgot password?` link on the SEPAL landing page.

.. thumbnail:: ../_images/setup/password/landing.png
   :title: Landing page of SEPAL where the user can find the "Forgot password?" button.
   :group: setup_password

On the reset password page, enter the email address you used to register for SEPAL, then click :btn:`<fas fa-envelope> Reset password`.

.. thumbnail:: ../_images/setup/password/email-setup.png
   :title: The reset password page where you can insert your email address.
   :group: setup_password

.. note:: 

    If the field becomes red, your email address was not found in our database. Be careful with typos and test multiple addresses, as you may have used another when you registered. 

Once your email address is validated, a confirmation email will be sent from SEPAL to your associated email account. The notification system will display a message containing this information in the upper-right corner of the screen.

.. thumbnail:: ../_images/setup/password/email-confirmation.png
   :title: The confirmation notification that an email to reset your password has been sent to your associated email address.
   :group: setup_password


Email confirmation
------------------

To reset your password, SEPAL uses an email confirmation system because: 

-   Attackers cannot lock the accounts of other users by guessing their usernames and utilizing the forgotten password recovery function.
-   Passwords cannot be read from your email account by potential attackers.
-   The reset links are only temporarily valid.
-   After someone uses a password reset link, it becomes invalid and cannot be accessed again.

For all of these reasons, SEPAL will send you the following email. 

.. thumbnail:: ../_images/setup/password/email.png
   :title: Example of a reset password email.
   :group: setup_password

Click the :code:`This` link. It will open the reset password interface on a new browser page.

Change password
---------------

In the reset password interface, three fields are available:

-   **Username:** The username associated with your email address in the database.
    
    .. note::
    
        Your username cannot be changed.

-   **Password:** Your new password. 
-   **Confirm password:** A security field where you need to provide your new password again.

Provide a password in the :code:`Password` and :code:`Confirm Password` fields. If the two fields are not exactly the same, the form cannot be validated.

Once everything is set, click on :btn:`<fas fa-check> Set password` to validate your new password.

.. thumbnail:: ../_images/setup/password/change-password.png
   :title: The change password interface.
   :group: setup_password

Once validated, the new password will be automatically associated with your account. The user will be authenticated and a notification will be displayed in the upper-right side of the screen.

.. thumbnail:: ../_images/setup/password/change-password-notification.png
   :title: The change password interface.
   :group: setup_password
