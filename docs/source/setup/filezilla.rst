Exchange files with SEPAL
=========================

Built-in tools 
--------------

To exchange files with SEPAL, there are several built-in tools you can use. 

.. note:: 

    SEPAL's built-in tools for uploading and downloading are limited. Uploading or downloading very large amounts of data is best done using an FTP solution. 

Jupyter Notebook 
^^^^^^^^^^^^^^^^

In the SEPAL application dashboard, open a new Jupyter Notebook app.

The notebook dashboard enables you to work with files and directories on your system. This includes opening, creating, deleting, renaming, downloading, copying and sharing files and directories.

By clicking the :code:`Upload` button, you can upload a file from your computer to the platform.

When selecting a file, use the :code:`Download` button to download it to your computer.

.. note::

    The download button is only available when you click on a single file. (Folders can not be downloaded.)

.. image:: ../_images/setup/filezilla/jupyter-notebook-dashboard.png


Jupyterlab
^^^^^^^^^^

In the SEPAL application dashboard, open a new Jupyterlab app. 

From there, the File browser and File menu enable you to work with files and directories on your system. This includes opening, creating, deleting, renaming, downloading, copying, and sharing files and directories.

Files can be uploaded to the current directory of the file browser by dragging and dropping them, or by clicking the “Upload Files” button at the top of the file browser:

.. youtube:: 1bd2QHqQSH4

Any file in Jupyterlab can be downloaded by right-clicking its name in the file browser and selecting :code:`Download` from the context menu:

.. youtube:: Wl7Ozl6rMcc

.. seealso:: 

    More information about the Jupyterlab interface can be found in the Jupyterlab `documentation <https://Jupyterlab.readthedocs.io/en/stable/getting_started/overview.html>`_.

Rstudio
^^^^^^^

In the SEPAL application dashboard, open a new Rstudio app.

From there, the file menu (in red in the yellow image) enables you to work with files and directories on your system. This includes opening, creating, deleting, renaming and copying.

.. image:: ../_images/setup/filezilla/rstudio_dashboard.png

Using the :code:`Upload` button in the upper-left of the red rectangle, you can upload files from your local computer.

SEPAL file explorer
^^^^^^^^^^^^^^^^^^^

In the SEPAL file explorer, you will be able to work with files and directories on your system. This includes deleting and downloading.

After clicking on a single file, use the :code:`Download` button to download the file to your local folder.

.. image:: ../_images/setup/filezilla/sepal_file_manager.png

.. note::

    You cannot download multiple files or folders directly through this interface.

FTP solution 
------------

SEPAL content can also be accessed via a SSH File Transfer Protocol (FTP). Any FTP solution might work, but in this section we will present it using FileZilla. Adaptation to your favorite FTP solution should be straightforward. 

FileZilla®
^^^^^^^^^

If you don't have any FTP solution installed on your local machine and you don't know what a FTP solution is, this documentation page is here to help you. 

.. seealso::

    An FTP client is software that allows you to connect to an FTP server in order to exchange files. Once connected, you can upload, download, copy or delete files on the remote computer or your local computer.

FileZilla®, is a free FTP solution. The FileZilla Client not only supports FTP, but also FTP over TLS (FTPS) and SFTP, which we are using in SEPAL. It is an open-source software distributed free of charge under the terms of the `GNU General Public License <https://www.gnu.org/licenses/gpl-3.0.en.html>`_.

.. tip:: 

    The software can be downloaded from `here <https://FileZilla-project.org/download.php?type=client>`_


Connect your FTP client to SEPAL
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Accessing files in SEPAL is easy using FileZilla. To use FileZilla, open the application and connect to the SEPAL server by selecting Menu :code:`File -> Site Manager` in the menu tab. 

In the site manager pop-up, click on the :code:`New Site` button. Use the screenshot below as a guide for filling out the form:

-   **Host:** ssh.sepal.io 
-   **Port:** 443
-   **Protocol:** SFTP – SSH File Transfer Protocol
-   **Logon Type:** Normal 
-   **User:** <your SEPAL username>
-   **Password:** <your SEPAL password> 

.. note::

    For :code:`user` and :code:`password`, insert the credentials you use to connect to the platform.

.. image:: ../_images/setup/filezilla/register_new_site.png

By clicking on :code:`Connect`, your SEPAL drive will appear in the right panel. In the left panel, you can find the files and folders of your computer.

Use the FTP client to interact with SEPAL 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The next step is to get familiar with FileZilla's window layout.

Here is a quick introduction:

Below the toolbar (1) and quick connect bar (2), the message log (3) displays messages related to transfers and connection. Below, you can find the file listings. The left column (local pane, 4) displays the local files and directories (e.g. content on the PC you're using FileZilla on). The right column (server pane, 5) displays the files and directories on the server you are connected to. Both columns have a directory tree at the top and a detailed listing of the currently-selected directory's contents at the bottom. You can easily navigate either of the trees and lists by clicking around, like you would in any other file manager. In the lower section of the window, the transfer queue (6) lists the to-be-transferred and already transferred files.

.. image:: ../_images/setup/filezilla/filezilla_panel.png

.. seealso::

    For more information on using FileZilla, navigate to their `wiki page <https://wiki.FileZilla-project.org/FileZilla_Client_Tutorial_(en)>`_. 


