Google Drive
============

The **Drive** CLI is a utility that allows managing a Google Drive account from the SEPAL console (for more information, see the Readme file directly in the GitHub repository https://github.com/odeke-em/drive).

Usage
-----

Initialize drive connection
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Before running any of the **Drive** commands, start a session by running the following line:

.. code-block:: bash

    $ drive init

Copy the URL that is displayed in the terminal and paste it into your browser. Log in to your Google account and "trust the connection" by selecting the "allow" button. An authorization code will be displayed; copy and paste it into the SEPAL terminal. You are now ready to use the :code:`Drive` CLI tool.

.. note::

    Since the authorization token will expire every session, this process has to be repeated each time you want to use the :code:`Drive` command tool.

Upload files
------------

You can upload files from your SEPAL environment by using the :code:`Push` command.

.. code-block:: bash

    $ drive push /home/username/image_folder/*.tif
    $ # confirm the changes and wait for the transfer.

    $ # check additional parameters by using -help flag
    $ drive push -h

Download files
--------------

To download files, use the :code:`Pull` command. This command will create files that don't exist locally but do remotely.

.. code-block:: bash

    $ cd my_folder
    ~/my_folder$ drive pull

    $ # check additional parameters by using -help flag
    $ drive pull -h

This command will syncronize the files that are not present in your SEPAL session but are present in your Google Drive account folder.

Additional commands
^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    $ about               # Print out information about your Google Drive.
    $ clashes             # Fix clashes by renaming or trashing files.
    $ copy                # Copy remote paths to a destination.
    $ cp                  # Copy remote paths to a destination.
    $ deinit              # Removes the user's credentials and initialized files.
    $ del                 # Deletes the items permanently. This operation is irreversible.
    $ delete              # Deletes the items permanently. This operation is irreversible.
    $ diff                # Compares local files with their remote equivalent.
    $ du                  # Similarly to util `du`, gives you disk usage.
    $ edit-desc           # Edit the attributes of a file.
    $ edit-description    # Edit the attributes of a file.
    $ emptytrash          # Permanently cleans out your trash.
    $ features            # Returns information about the features of your Drive.
    $ file-id             # Retrieve the fileID for the specified paths.
    $ help                # Get help on a topic.
    $ id                  # Retrieve the fileID for the specified paths.
    $ index               # Remotely fetch indices.
    $ init                # Initializes a directory and authenticates user.
    $ issue               # Report an issue to the project's issue tracker.
    $ list                # Lists the contents of a remote path.
    $ ls                  # Lists the contents of a remote path.
    $ md5sum              # Prints a list compatible with md5sum(1).
    $ move                # Move files and folders.
    $ mv                  # Move files and folders.
    $ new                 # Create a new file or folder.
    $ open                # Open a file in the appropriate file manager or default browser.
    $ pub                 # Publishes a file and prints its publicly available URL.
    $ pull                # Pulls remote changes from Google Drive.
    $ push                # Push local changes to Google Drive.
    $ qr                  # Open up the QR code for specified files.
    $ quota               # Prints out information related to your quota space.
    $ rename              # Renames a file or folder.
    $ report              # Report an issue to the project's issue tracker.
    $ report-issue        # Report an issue to the project's issue tracker.
    $ share               # Share files with specific email addresses, giving specific users specified roles and permissions.
    $ star                # Star files.
    $ stat                # Display information about a file.
    $ touch               # Updates a remote file's modification time to that currently on the server.
    $ trash               # Moves files to trash.
    $ unpub               # Revokes public access to a file.
    $ unshare             # Revoke a user's access to a file.
    $ unstar              # Unstar files.
    $ untrash             # Restores files from trash to their original locations.
    $ url                 # Returns the remote URL of each file.
    $ version             # 0.3.9
