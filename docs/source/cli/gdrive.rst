Google Drive
============


The `drive` CLI is a utility that allows managing the Google Drive account from the SEPAL console, to read the full documentation please refer to the Readme file directly in the GitHub repository https://github.com/odeke-em/drive. 

Usage
-----

Initialize drive connection
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Before running any of the drive commands, you have to start a session, to do so, run the following line:

.. code-block:: bash

    $ drive init

As result, an URL will be displayed in the terminal, visit it by copying and pasting it in your browser. Log-in to your Google account and, "trust the connection" by click the "allow" button. An authorization code will be displayed, copy it and paste it in the Sepal terminal. Now you are ready to use the :code:`drive` CLI tool.

.. note::
    
    The authorization token will expire on every session, this process has to be repeated each time you want to use the :code:`drive` command tool.

Upload files
------------

You can upload files from your SEPAL environment by using the :code:`push` command. 

.. code-block:: bash

    $ drive push /home/username/image_folder/*.tif
    $ # confirm the changes and wait for the transfer.
    
    $ # check additional parameters by using -help flag
    $ drive push -h
    


Download files
--------------

To download files, use the :code:`pull` command. This command will create files that doesn't exist locally but does remotely. 

.. code-block:: bash
    
    $ cd my_folder
    ~/my_folder$ drive pull 
    
    $ # check additional parameters by using -help flag
    $ drive pull -h

This command will syncronize the files that are not present in your sepal session but are present in your Google Drive account folder.

Additional commands
^^^^^^^^^^^^^^^^^^^

.. code-block:: bash


	$ about               # print out information about your Google drive
	$ clashes             # fix clashes by renaming or trashing files
	$ copy                # copy remote paths to a destination
	$ cp                  # copy remote paths to a destination
	$ deinit              # removes the user's credentials and initialized files
	$ del                 # deletes the items permanently. This operation is irreversible
	$ delete              # deletes the items permanently. This operation is irreversible
	$ diff                # compares local files with their remote equivalent
	$ du                  # similar to util `du` gives you disk usage
	$ edit-desc           # edit the attributes of a file
	$ edit-description    # edit the attributes of a file
	$ emptytrash          # permanently cleans out your trash
	$ features            # returns information about the features of your drive
	$ file-id             # retrieve the fileId for the specified paths
	$ help                # Get help for a topic
	$ id                  # retrieve the fileId for the specified paths
	$ index               # fetch indices from remote
	$ init                # initializes a directory and authenticates user
	$ issue               # report an issue to the project's issue tracker
	$ list                # lists the contents of remote path
	$ ls                  # lists the contents of remote path
	$ md5sum              # prints a list compatible with md5sum(1)
	$ move                # move files/folders
	$ mv                  # move files/folders
	$ new                 # create a new file/folder
	$ open                # open a file in the appropriate filemanager or default browser
	$ pub                 # publishes a file and prints its publicly available url
	$ pull                # pulls remote changes from Google Drive
	$ push                # push local changes to Google Drive
	$ qr                  # open up the QR code for specified files
	$ quota               # prints out information related to your quota space
	$ rename              # renames a file/folder
	$ report              # report an issue to the project's issue tracker
	$ report-issue        # report an issue to the project's issue tracker
	$ share               # share files with specific emails giving the specified users specifies roles and permissions
	$ star                # star files
	$ stat                # display information about a file
	$ touch               # updates a remote file's modification time to that currently on the server
	$ trash               # moves files to trash
	$ unpub               # revokes public access to a file
	$ unshare             # revoke a user's access to a file
	$ unstar              # unstar files
	$ untrash             # restores files from trash to their original locations
	$ url                 # returns the remote URL of each file
	$ version             # 0.3.9

