.. _session_storage:

Session storage
===============
*Choose where to keep your files and where to run temporary work*

Every SEPAL session gives you access to two kinds of storage: your **home folder**,
which is kept between sessions, and a **temporary disk**, which belongs to the
session and is emptied when it stops. Choosing the right one makes your work
faster and keeps your storage quota for the files you need.

Overview
--------

.. list-table::
    :header-rows: 1
    :widths: 18 41 41

    * -
      - Home folder
      - Temporary disk
    * - Location
      - ``/home/sepal-user`` (also ``~``)
      - ``/tmp`` — ``/var/tmp`` and ``~/tmp`` point to the same disk
    * - Type of storage
      - Network storage, shared by all your sessions and apps
      - Local disk attached to the session's instance
    * - Lifetime
      - Kept until you delete the files
      - **Emptied when the session stops or expires**
    * - Shared between sessions
      - Yes — every session sees the same files
      - No — each session has its own, empty disk
    * - Storage quota
      - Counts toward your storage quota and storage spending
      - Does not count toward your storage quota
    * - Size
      - Limited by your storage quota
      - 100 GB on standard instance types; from 118 GB to 3,800 GB on
        instance types with SSD
    * - Speed
      - Good for large files; slow when reading or writing many small files
      - Fast for all types of file access

Your home folder
----------------

Your home folder, ``/home/sepal-user``, is your permanent storage in SEPAL. It is
the same folder in every session, in the **Files** section and in the apps you
run, so files you save there are always available.

Use it for:

-   code, scripts and notebooks;
-   input data you use repeatedly;
-   final results, exports and anything else you want to keep.

Because your home folder is network storage, each file operation takes longer
than on a local disk. This is not noticeable for large files, but tasks that
create or read thousands of small files — such as installing Python or R
packages, creating a virtual environment or unpacking an archive — can be
several times slower there than on the temporary disk.

Your home folder counts toward your storage quota. You can see how much you use
in the **Usage** panel of the hourly cost button, :btn:`<fa-solid fa-dollar-sign> x.xx/h`,
in the lower-right corner, and in the **Storage used** line of the **Terminal**.
To find large folders, see :doc:`storage`.

The temporary disk
------------------

Each session has its own temporary disk, mounted at ``/tmp``. The folders
``/var/tmp`` and ``~/tmp`` (``/home/sepal-user/tmp``) point to the same disk, so
files written to any of them use the temporary disk and not your home folder.

The temporary disk:

-   is **empty when the session starts**;
-   is **deleted when the session stops**, whether you stop it or it expires;
-   is only visible from the session that created it;
-   does not count toward your storage quota.

Use it for files you can recreate:

-   Python virtual environments, Conda environments and package caches;
-   intermediate rasters, tiles and other files produced while processing;
-   downloaded archives before extracting the files you need;
-   build folders and other temporary output of tools.

.. warning::

    Everything in the temporary disk is lost when the session stops. Copy the
    results you want to keep to your home folder before stopping the session,
    and keep the files you need to recreate your environment (for example, a
    ``requirements.txt`` file) in your home folder.

Instance types with SSD
^^^^^^^^^^^^^^^^^^^^^^^

The size of the temporary disk depends on the instance type you start:

-   **Standard instance types** (for example, ``t1``, ``m2`` or ``c4``) get a
    100 GB temporary disk.
-   **Instance types with SSD** (those ending in ``d``, such as ``m2d`` or
    ``c4d``, and the ``x`` and ``g`` types) use the SSD drives of the instance
    as their temporary disk. Its size is shown in the **GB SSD** column of the
    **Available instance types with SSD** table in the **Terminal**, from
    118 GB on the smallest types to 3,800 GB on the largest ones.

Choose an instance type with SSD when your temporary files do not fit in
100 GB, for example when processing large image stacks. These types cost
slightly more per hour than the standard type with the same CPU and RAM, so a
standard type is usually enough for smaller jobs. To compare instance types,
see :ref:`the Terminal section <terminal-instances>` of the SEPAL interface
presentation.

Example: work in the temporary disk
-----------------------------------

The following commands create a Python virtual environment in the temporary
disk, run a script, and copy its results to the home folder:

.. code-block:: console

    python3 -m venv /tmp/venv
    source /tmp/venv/bin/activate
    pip install -r ~/my_project/requirements.txt
    python ~/my_project/process.py --output /tmp/output
    cp -r /tmp/output ~/my_project/results

The environment is deleted with the session, but because ``requirements.txt``
is in your home folder, you can recreate it in a new session with the same
commands.

To check the free space on each disk, run:

.. code-block:: console

    df -h /tmp ~
