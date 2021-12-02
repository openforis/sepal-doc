Google Earth Engine
===================

The earthengine tool is a utility program that allows you to manage Earth Engine assets and tasks from the command line. It is installed automatically when you install the Python API. To check whether the tool is installed and functioning correctly, type the following on a command line:

.. code-block:: console

    $ earthengine

If the tool is properly installed then it will print out a short summary of available commands. To get help on a specific command, use:

.. code-block:: console

    $ earthengine command -h

When you first install the Python API you will need to log in using the :code:`authenticate` command described below. 

available commands 
------------------

More information on the available command can be found on `Google API website <https://developers.google.com/earth-engine/guides/command_line>`__.

.. code-block:: bash

    $ authenticate          # Prompts the user to authorize access to Earth Engine via OAuth2.
    $ acl                   # Prints or updates the access control list of the specified asset.
    $ asset                 # Prints or updates metadata associated with an Earth Engine asset.
    $ cp                    # Creates a new Earth Engine asset as a copy of another asset.
    $ create                # Creates assets and folders.
    $ ls                    # Prints the contents of a folder or collection.
    $ licenses              # Prints the name and license of all third party dependencies.
    $ du                    # Prints the size and names of all items in a given folder or collection.
    $ mv                    # Moves or renames an Earth Engine asset.
    $ model                 # TensorFlow model related commands.
    $ rm                    # Deletes the specified assets.
    $ set_project           # Sets the default user project to be used for all API calls.
    $ task                  # Prints information about or manages long-running tasks.
    $ unset_project         # UnSets the default user project to be used for all API calls.
    $ upload                # Uploads assets to Earth Engine.
    $ upload_manifest       # Uploads an image to Earth Engine using the given manifest file.
    $ upload_table_manifest # Uploads a table to Earth Engine using the given manifest file.
