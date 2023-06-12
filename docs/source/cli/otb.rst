Orfeo Toolbox
=============

Orfeo ToolBox (OTB) is an open-source project for state-of-the-art remote sensing. Built upon the foundation of the open-source geospatial community, it can process high-resolution optical, multispectral and radar images on the terabyte scale. A wide variety of applications are available, from ortho-rectification or pansharpening, to classification, SAR processing, and much more.

OTB is equipped with more than 100 ready-to-use applications for remote sensing tasks. They usually expose existing processing functions from the underlying C++ library, or integrate them into high-level pipelines. OTB applications allow the user to:

- combine two or more functions from the Orfeo ToolBox; and
- provide a high-level interface to handle input and output data, definition of parameters, and communication with the user.

The complete list of applications is described on the `All Applications page <https://www.orfeo-toolbox.org/CookBook/Applications.html#apprefdoc>`__.

All standard applications share the same implementation and automatically expose generated interfaces. However, they are accessed in a slightly different way: the command-line interface is prefixed by :code:`otbcli\_`.
