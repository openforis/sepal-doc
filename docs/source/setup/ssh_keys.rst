Set up SSH keys
===============
*Connect to SEPAL without entering your account password*

Create an SSH key on your computer and register its public part in SEPAL.
You can then use it with an SSH client, including VS Code.
If you already have a key on your computer, skip the first step.

1. In a **local** terminal (PowerShell on Windows, Terminal on macOS or Linux),
   create a key:

   .. code-block:: console

       ssh-keygen -t ed25519 -C "sepal"

   Accept the default location and choose a passphrase. Do not overwrite an
   existing key. This creates a private key, ``id_ed25519``, and a public key,
   ``id_ed25519.pub``, in your user's ``.ssh`` folder.
2. In SEPAL, open your user menu, select **SSH keys**, then **Add**.
   Select or drop the ``id_ed25519.pub`` file, or paste its contents into
   **Public key**. Give it a recognizable **Name**, then select **Add**.

   .. thumbnail:: ../_images/setup/ssh_keys/ssh-keys.png
       :title: Open SSH keys from your user menu and select Add.
       :alt: SEPAL SSH keys panel with the Add button at the lower left.
       :group: setup_ssh_keys

   .. thumbnail:: ../_images/setup/ssh_keys/add-ssh-key.png
       :title: Select your public key file or paste its contents, then name the key.
       :alt: Add SSH key dialog with public key file, public key and name fields.
       :group: setup_ssh_keys

3. Connect to your SEPAL session using your SSH client. SSH uses the default
   key automatically; you may
   be prompted for its passphrase. If you saved the key elsewhere, add
   ``IdentityFile /path/to/your/private/key`` to the host's SSH configuration.

.. note::

    Upload only the public ``.pub`` file. Keep the private key on your computer.
    On Windows, use the key and configuration belonging to the SSH client
    used by VS Code; keys created inside WSL are stored separately from
    Windows keys.
