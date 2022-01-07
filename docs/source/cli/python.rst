Python
======

Usage
-----

SEPAL instances run on :code:`focal` ubuntu machines and thus provide a fully functional :code:`Pyhton 3.8` environment. This environment is accecible though Jupyter Notebook, JupyterLab or the terminal: 

.. thumbnail:: ../_images/cli/python/jupyter_example.png
    :title: a code run in Jupyterlab
    :group: python_environment
    :width: 32%

.. thumbnail:: ../_images/cli/python/notebook_example.png
    :title: a code run in Jupyter Notebook
    :group: python_environment
    :width: 32%

.. thumbnail:: ../_images/cli/python/terminal_example.png
    :title: a code run in the terminal
    :group: python_environment
    :width: 32%

Description
-----------

The SEPAL python environment is not empty and embed numerous librairies. They are listed here: 

.. code-block:: console

    ########  geospatial data analysis  ########
    scikit-image
    scipy
    shapely
    shapely-geojson
    tqdm
    xarray-leaflet
    GDAL==$GDAL_VERSION
    bqplot
    numpy
    geopandas
    matplotlib
    pandas
    dask[complete]
    planet
    tensorflow-probability
    geeadd

    ########  Google Earthengine  ########
    oauth2client
    google-api-python-client==1.12.8
    git+git://github.com/openforis/earthengine-api.git@v0.1.270#egg=earthengine-api&subdirectory=python

    ########  BFAST dependencies ########
    wget
    Sphinx==2.2.0
    sphinx-bootstrap-theme==0.7.1
    numpydoc
    git+git://github.com/12rambau/bfast.git

    ########  sepal modules  ########
    geemap==0.8.9
    Unidecode
    pyperclip
    python-dateutil
    pytesmo
    Wand
    PyPDF2 # more recent version are avaiable (PyPDF4)
    rasterio==1.1.5
    openpyxl
    sepal_ui
    opensartoolkit

    ########  web api  ########
    falcon
    gunicorn
    pyCrypto
    awscli

    ########  other deps  ########
    requests
    llvmlite==0.31.0
    coverage

    ########  OSK requirements  ########
    descartes
    fiona
    godale
    psycopg2-binary
    imageio
    rtree
    retrying
    Cython
    pyproj==2.6.1 # Require proj update before 3.0.0 can be installed

    ########  Early Warning System for Canopy Disturbances in Ecuador (SATA)  ########
    nose
    nosexcover
    pylint
    click
    dateutils
    boto3

Run :code:`pip freeze | grep <name of your lib>` to check if it's already installed. 


Customization
-------------

The SEPAL environment can be customized to user needs using any third-party librairies and pip. By default installation will be run in :code:`--user` mode and won't affect other SEPAL users. 


.. thumbnail:: ../_images/cli/python/install_sphinx.gif
    :title: a code run in the terminal

.. note:: 

    If you face compatibility issues when customizing your SEPAL environment, please let us know in the `Github issue tracker <https://github.com/openforis/sepal/issues/new/choose>`__.
