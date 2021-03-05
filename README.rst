sepal-doc
=========

.. image:: https://img.shields.io/badge/License-MIT-yellow.svg
    :target: https://opensource.org/licenses/MIT
    :alt: License: MIT
 

This folder gather all the documentation material of the sepal platform: `<https://sepal.io>`_

Note
----

If the modification you're providing are typos, then you don't need to rebuild locally the full documnetation. Just edit the appropiate file.

Build documentation locally
---------------------------

firs pull the repository to your local machine 
.. code-block::
    
    $ git clone https://github.com/openforis/sepal-doc.git

Then install the python librairies related to doc compilation:

.. code-block::

    $ pip install -r sepal-doc/requirements.txt

now move to the `sepal-doc/docs` folder and run 

.. code-block::

    $ make html

The documentation files will be build in the `sepal-doc/build` folder. double click on the index.html file and you should be seeing the landing page in your favorite browser.

Contribute
----------

If you want to contribute you can fork the project in you own repository and then use it. 
Please follow the `contributing guidelines <https://github.com/openforis/sepal-doc/blob/master/CONTRIBUTE.rst>`_ if you consider working with us. 
Meet our `contributor <https://github.com/openforis/sepal-doc/blob/master/AUTHOR.rst>`_. 
