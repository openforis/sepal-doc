Manage Disk Usage
=================

In SEPAL, efficient storage management is crucial due to the limited storage capacity. We highly recommended to regularly audit and clean your storage space to maintain optimal system functionality and your resources under the limits.

For non-expert users, initiating storage cleanup can seem daunting. It's important to start with directories known for accumulating large files, such as :code:`/var/log` (system logs), :code:`/tmp` (temporary files), and personal directories like :code:`~/Downloads` or :code:`~/module_results`. A conservative estimate for high storage usage in these areas can vary depending on individual use cases and system configurations. However, as a general guideline, any single folder occupying more than 1GB of space warrants a closer look, especially if it's not actively used for current projects.

To make things easier, SEPAL has integrated the command line tool called :code:`ncdu` (NCurses Disk Usage), this is a command-line utility that provides a convenient and efficient way to analyze disk usage on the SEPAL environment. It uses a text-based user interface to navigate through directories and view which files and folders are consuming disk space.

Prerequisites
=============

- Access to a terminal
- Start a new session (it can be a t1)

Usage
=====

After starting a session, you can start analyzing disk usage by simply typing :code:`ncdu` in your terminal:

.. code-block:: bash

   ncdu

If you want to analyze a specific directory, you can specify the directory path as an argument to the command:

.. code-block:: bash

   ncdu /path/to/directory

.. thumbnail:: ../_images/setup/storage/scanning_files.png
    :title: NCDU Dashboard
    :width: 70%
    :align: center


Navigating :code:`ncdu`
-----------------------

- Use the arrow keys (:btn:`<fa-solid fa-square-caret-left>`, :btn:`<fa-solid fa-square-caret-up>`, :btn:`<fa-solid fa-square-caret-right>`, :btn:`<fa-solid fa-square-caret-down>` )  to navigate through the files and directories.
- Press :code:`Enter` to enter a directory.

.. thumbnail:: ../_images/setup/storage/preview.png
    :title: NCDU preview
    :width: 70%
    :align: center

Understanding the Interface
----------------------------

- The size of the files and directories is shown on the left .
- The graphical representation of disk usage is displayed next to the size.
- The percentage of disk space used by each file or directory relative to the parent directory is shown at the beginning of each line.

Advanced Usage
==============

.. Attention::

   Be cautious when deleting files or directories. Deleting system files or directories can cause system instability or data loss.

- Press ``d`` to delete a file or directory (be cautious with this operation).
- Press ``q`` to quit :code:`ncdu`.

.. thumbnail:: ../_images/setup/storage/delete_file_confirm.png
    :title: NCDU delete confirmation
    :width: 70%
    :align: center

.. thumbnail:: ../_images/setup/storage/delete_file_progress.png
    :title: NCDU delete progress
    :width: 70%
    :align: center

To see a list of all available options and features, you can use the ``--help`` option:

.. code-block:: bash

   ncdu --help

Some useful flags include:

- ``-x``: Stay on the filesystem of the directory being scanned.
- ``-q``: Quick mode, doesn't count sizes of subdirectories.
- ``-o``: Export the results to a file.
