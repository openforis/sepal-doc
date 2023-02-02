.. image:: docs/source/_images/sepal_header.png

sepal-doc
=========

.. image:: https://img.shields.io/badge/License-CC%20BY--SA%204.0-yellow.svg
    :target: LICENSE
    :alt: License: CC BY-SA 4.0

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
   :alt: Black badge

.. image:: https://img.shields.io/readthedocs/sepal-doc/latest?logo=readthedocs&logoColor=white
    :target: https://sepal-doc.readthedocs.io/en/latest/
    :alt: Documentation Status

.. image:: https://img.shields.io/youtube/channel/views/UCtpxScciUj0fjMmhpYsAZbA?color=red&logo=youtube&logoColor=white&style=flat
   :target: https://www.youtube.com/channel/UCtpxScciUj0fjMmhpYsAZbA
   :alt: YouTube Channel Views

.. image:: https://img.shields.io/twitter/follow/openforis?color=%231DA1F2&logo=twitter&logoColor=white&style=flat
   :target: https://twitter.com/openforis
   :alt: Twitter Follow

.. image:: https://img.shields.io/stackexchange/gis/t/sepal?label=GIS.StackExchange&logo=stackexchange&logoColor=white
    :target: https://gis.stackexchange.com/questions/tagged/sepal
    :alt: gis

Translation
-----------

Currently the documentation is available in the following languages:

.. list-table::

   * - English
     - Français
     - Español
   * - .. image:: https://img.shields.io/static/v1?label=en&message=100%&logo=crowdin&logoColor=white&color=blue
     - .. image:: https://img.shields.io/badge/dynamic/json?logoColor=white&label=fr&logo=crowdin&query=%24.progress.1.data.translationProgress&url=https%3A%2F%2Fbadges.awesome-crowdin.com%2Fstats-15322738-562097.json
     - .. image:: https://img.shields.io/badge/dynamic/json?logoColor=white&label=es&logo=crowdin&query=%24.progress.0.data.translationProgress&url=https%3A%2F%2Fbadges.awesome-crowdin.com%2Fstats-15322738-562097.json

You can contribute to the translation effort on our `crowdin project <https://crowdin.com/project/sepal-doc>`__.

Note
----

This folder gather all the documentation material of the sepal platform: `<https://sepal.io>`_

Build
-----

To build the documentation from the files:
1. Clone the repository to your local machine
1. install nox
1. run the nox build

.. code-block:: console

    git clone https://github.com/openforis/sepal-doc
    cd sepal-doc
    pip install nox
    nox -s docs

Contribute
----------

If you want to contribute you can fork the project in you own repository and then use it.
Please follow the `contributing guidelines <https://docs.sepal.io/en/latest/team/contribute.html>`_ if you consider working with us.
Meet our `contributor <https://github.com/openforis/sepal-doc/blob/master/AUTHORS.rst>`_.
