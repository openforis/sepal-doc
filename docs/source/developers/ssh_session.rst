.. _ssh_session:

Connect to a session over SSH
=============================
*Use a terminal, file transfer tools, local web apps and code editors with a SEPAL session*

Every running SEPAL session has its own **SSH login**. With it, tools on your
computer can connect directly to that session: you work with your local
programs, while your files and computations stay on SEPAL.

With the SSH login you can:

-   open a terminal on the session from your computer;
-   copy files between your computer and the session;
-   open web apps running in the session, such as JupyterLab, in your local
    browser;
-   edit and run code on the session from a code editor, such as VS Code.

Get the SSH login of a session
------------------------------

1. In SEPAL, start a session (for example, by opening **Terminal**). Then select
   the hourly cost button, :btn:`<fa-solid fa-dollar-sign> x.xx/h`, in the
   lower-right corner of the footer and choose **Sessions**.

   .. thumbnail:: ../_images/developers/ssh_session/sessions-menu.png
       :title: Select Sessions in the menu opened by the hourly cost button.
       :alt: Hourly cost menu with the Usage and Sessions options, Sessions highlighted.
       :align: center
       :width: 50%
       :group: developers_ssh_session

2. On the session you want to use, select **Copy SSH login**. The copied login
   includes your username and the session name, for example
   ``alice+humble-robin@ssh.sepal.io``.

   .. thumbnail:: ../_images/developers/ssh_session/sessions.png
       :title: Select the copy icon to copy the session's SSH login.
       :alt: SEPAL Sessions panel with the Copy SSH login button highlighted and its tooltip visible.
       :align: center
       :group: developers_ssh_session

The examples on this page use ``alice+humble-robin@ssh.sepal.io``. Replace it
with the login you copied.

When you connect:

-   **Password or key:** enter your **SEPAL password** when prompted, or register
    an SSH key to connect without it (see :doc:`../setup/ssh_keys`).
-   **Port:** SEPAL accepts SSH connections on port **22** (the default) and port
    **443**. If your network blocks port 22, add ``-p 443`` to ``ssh`` and
    ``sftp`` commands, or ``-P 443`` to ``scp`` commands.
-   **First connection:** your SSH client asks you to confirm the host's
    fingerprint. Confirm it to continue.

.. important::

    The ``+session-name`` part of the login directs the connection to that
    session. When the session stops, the connection closes and the login stops
    working. For a new session, copy its login again.

Open a terminal
---------------

In a terminal on your computer (PowerShell on Windows, Terminal on macOS or
Linux), run:

.. code-block:: console

    ssh alice+humble-robin@ssh.sepal.io

You get a shell on the session, in your home folder ``/home/sepal-user``. Type
``exit`` to close the connection; the session keeps running.

Transfer files
--------------

Use ``scp`` to copy files and folders between your computer and the session.
Run these commands on your computer:

.. code-block:: console

    # Copy a file from your computer to your home folder in SEPAL
    scp data.csv alice+humble-robin@ssh.sepal.io:~/

    # Copy a folder from SEPAL to the current folder on your computer
    scp -r alice+humble-robin@ssh.sepal.io:~/results .

``sftp`` and ``rsync`` work with the same login. For a graphical client, see
:doc:`../setup/filezilla`.

Files copied to your home folder are kept between sessions. Files copied to
``/tmp`` are deleted when the session stops (see :doc:`../setup/session_storage`).

Open web apps in your local browser
-----------------------------------

A web app running in the session, such as JupyterLab, Solara or Streamlit, is
only reachable from inside the session. To open it in your local browser,
forward its port through the SSH connection.

For example, to use JupyterLab:

1. Connect with port forwarding. ``-L 8888:localhost:8888`` forwards port 8888
   of your computer to port 8888 of the session:

   .. code-block:: console

       ssh -L 8888:localhost:8888 alice+humble-robin@ssh.sepal.io

2. In that connection, start JupyterLab without opening a browser:

   .. code-block:: console

       jupyter lab --no-browser --port 8888

3. JupyterLab prints a link that starts with ``http://127.0.0.1:8888/lab?token=``.
   Open it in your local browser.

The app runs until you stop it with :kbd:`Control-c` or close the connection.
To forward another app, replace ``8888`` with its port in both commands.

.. tip::

    SEPAL also runs JupyterLab, Jupyter Notebook and RStudio directly in your
    browser from the **Apps** section, without any setup on your computer.

Connect a code editor
---------------------

Code editors with SSH remote development open files and run terminals,
debuggers and notebooks directly on the session. This section describes
VS Code; other editors with SSH support, such as editors based on VS Code or
`JetBrains Gateway <https://www.jetbrains.com/remote-development/gateway/>`__,
use the same SSH login.

VS Code
^^^^^^^

Before starting, install `VS Code <https://code.visualstudio.com/>`__ and the
`Remote - SSH extension <https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh>`__
on your computer, as well as an
`SSH client <https://code.visualstudio.com/docs/remote/ssh#_getting-started>`__.

1. Open the Command Palette (**F1**) and select
   **Remote-SSH: Add New SSH Host...**. Paste the copied login, or enter it as
   a full command, for example:

   .. code-block:: console

       ssh -p 443 alice+humble-robin@ssh.sepal.io

2. Select the SSH configuration file offered by VS Code, then run
   **Remote-SSH: Connect to Host...** and select the host you just added.
3. Select **Linux** if asked for the remote platform. Enter your
   **SEPAL password** when prompted, unless you have registered an SSH key.
   VS Code may ask for the password more than once during setup.

   .. note::

       The first connection can take several minutes. VS Code installs its
       server, and later the extensions you use remotely, in
       ``~/.vscode-server`` in your home folder. Your home folder is network
       storage, which is slow when writing many small files (see
       :doc:`../setup/session_storage`). Later connections reuse this
       installation and start faster, until VS Code is updated and installs a
       new version of its server.

4. Once connected, select **File > Open Folder...** and open your project
   under ``/home/sepal-user``. The status bar shows the SSH connection;
   terminals opened in this window run on SEPAL.

To open Jupyter notebooks (``.ipynb`` files) in this window, install the
`Jupyter extension <https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter>`__
when VS Code suggests it; notebooks then run on the session.

For a new session, copy its login again and update the saved host using
**Remote-SSH: Open SSH Configuration File...**, or add a new host. When
finished, select **File > Close Remote Connection**.

For connection problems, check **View > Output > Remote - SSH** and the
`VS Code SSH troubleshooting guide <https://code.visualstudio.com/docs/remote/troubleshooting>`__.

Stop the session
----------------

Closing an SSH connection does not stop the session, which keeps consuming
your instance budget until it stops or expires. When you no longer need it,
stop it from **Sessions** in the hourly cost menu, or from the **Terminal**
(see :ref:`the Terminal section <terminal-instances>`).
