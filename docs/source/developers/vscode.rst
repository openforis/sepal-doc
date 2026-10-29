Connect VS Code to SEPAL
========================
*Edit files and run code on a SEPAL session from your computer*

Connect Visual Studio Code (VS Code) to a running SEPAL session using the
`Remote - SSH extension <https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh>`__.
Your editor stays on your computer; your files and computations stay on SEPAL.

Connect to a session
--------------------

Before starting, install VS Code, the Remote - SSH extension and an
`SSH client <https://code.visualstudio.com/docs/remote/ssh#_getting-started>`__
on your computer.

1. In SEPAL, start a session (for example, by opening **Terminal**), then select
   the hourly-cost button in the lower-right corner and choose **Sessions**.
2. On the session you want to use, select **Copy SSH login**. The copied login
   includes your username and the session name, for example
   ``alice+humble-robin@ssh.sepal.io``.

   .. thumbnail:: ../_images/developers/vscode/sessions.png
       :title: Hover over the copy icon to see the session's SSH login.
       :alt: SEPAL Sessions panel with the Copy SSH login tooltip visible.
       :group: developers_vscode

3. In VS Code, open the Command Palette (**F1**) and select
   **Remote-SSH: Add New SSH Host...**. Paste the copied login. You can also
   enter it as a full command, using port 443 if your network blocks port 22:

   .. code-block:: console

       ssh -p 443 alice+humble-robin@ssh.sepal.io

   Replace the example login with the one you copied from SEPAL.
4. Select the SSH configuration file offered by VS Code, then run
   **Remote-SSH: Connect to Host...** and select the host you just added.
5. Select **Linux** if asked for the remote platform. Confirm the host's
   fingerprint on your first connection after verifying it. Enter your
   **SEPAL password** when prompted, unless you have already registered an
   SSH key (see :doc:`../setup/ssh_keys`). VS Code may ask for the password more than once during setup.
6. Once connected, select **File > Open Folder...** and open your project
   under ``/home/sepal-user``. The status bar shows the SSH connection;
   terminals opened in this window run on SEPAL.

.. important::

    Keep the ``+session-name`` part of the copied login: it directs VS Code
    to the selected session. When that session stops, the connection closes.
    For a new session, copy its login again and update the saved host using
    **Remote-SSH: Open SSH Configuration File...**, or add a new host.

When finished, use **File > Close Remote Connection** in VS Code. Stop the
session in SEPAL when you no longer need it to avoid consuming resources.

For connection problems, check **View > Output > Remote - SSH** and the
`VS Code SSH troubleshooting guide <https://code.visualstudio.com/docs/remote/troubleshooting>`__.
