Google Drive
============


The `drive` CLI is a utility that allows managing the Google Drive account from the SEPAL console, to read the full documentation please refer to the Readme file directly in the GitHub repository https://github.com/odeke-em/drive. 

Usage
-----

Upload SEPAL files
^^^^^^^^^^^^^^^^^^

Start an authorization token:

.. code-block:: bash


	$ drive init          
	$ # Visit the displayed URL and paste the code.

Select a local folder and use `push` command.

.. code-block:: bash

	$ drive push /home/username/image_folder/*.tif
	$ # Confirm the changes and wait for the transfer.


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

