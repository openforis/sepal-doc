Orfeo Toolbox
=============

Orfeo ToolBox (OTB) is an open-source project for state-of-the-art remote sensing. Built on the shoulders of the open-source geospatial community, it can process high resolution optical, multispectral and radar images at the terabyte scale. A wide variety of applications are available: from ortho-rectification or pansharpening, all the way to classification, SAR processing, and much more!

OTB ships with more than 100 ready to use applications for remote sensing tasks. They usually expose existing processing functions from the underlying C++ library, or integrate them into high level pipelines. OTB applications allow the user to:

- Combine two or more functions from the Orfeo ToolBox,
- Provide a high level interface to handle: input and output data, definition of parameters and communication with the user.

The complete list of applications is described in the `All Applications page <https://www.orfeo-toolbox.org/CookBook/Applications.html#apprefdoc>`__.

All standard applications share the same implementation and automatically expose generated interfaces. However they are accessed in a slightly different way: the command-line interface is prefixed by :code:`otbcli\_`.
