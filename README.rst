imshowTk
===============================

.. image:: https://github.com/SciKit-Surgery/imshowTk/raw/master/project-icon.png
   :height: 128px
   :width: 128px
   :target: https://github.com/SciKit-Surgery/imshowTk
   :alt: Logo

|


.. image:: https://github.com/SciKit-Surgery/imshowTk/workflows/.github/workflows/ci.yml/badge.svg
   :target: https://github.com/SciKit-Surgery/imshowTk/actions/
   :alt: GitHub CI test status

.. image:: https://coveralls.io/repos/github/SciKit-Surgery/imshowTk/badge.svg?branch=master&service=github
    :target: https://coveralls.io/github/SciKit-Surgery/imshowTk?branch=master
    :alt: Test coverage

.. image:: https://readthedocs.org/projects/imshowTk/badge/?version=latest
    :target: http://imshowTk.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. image:: https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg
   :target: CODE_OF_CONDUCT.md

.. image:: https://img.shields.io/badge/Cite-SciKit--Surgery-informational
   :target: https://doi.org/10.1007/s11548-020-02180-5
   :alt: The SciKit-Surgery paper

.. image:: https://img.shields.io/twitter/follow/scikit_surgery?style=social
   :target: https://twitter.com/scikit_surgery?ref_src=twsrc%5Etfw
   :alt: Follow scikit_surgery on twitter


Author: Stephen Thompson

imshowTk is a zero dependency alternative to opencv's imshow function. It was developed to allow us to show an image window when using opencv-headless and don't want to use a larger UI library. It uses tkinter which comes as standard in most Python installations.

imshowTk is part of the `SciKit-Surgery`_ software project, developed at the `Wellcome EPSRC Centre for Interventional and Surgical Sciences`_, part of `University College London (UCL)`_.

Basic use case
::

    from from imshowtk.imshowtk import ImshowTk
    imshow = ImshowTk()
    frame = cv2.imread('project-icon.png')
    imshow.imshow(frame)
    del imshow


Developing
----------

Cloning
^^^^^^^

You can clone the repository using the following command:

::

    git clone https://github.com/SciKit-Surgery/imshowTk


Running tests
^^^^^^^^^^^^^
Pytest is used for running unit tests:
::

    pip install pytest
    python -m pytest


Linting
^^^^^^^

This code conforms to the PEP8 standard. Pylint can be used to analyse the code:

::

    pip install pylint
    pylint --rcfile=tests/pylintrc imshowtk


Installing
----------

You can pip install directly from the repository as follows:

::

    pip install git+https://github.com/SciKit-Surgery/imshowTk



Contributing
^^^^^^^^^^^^

Please see the `contributing guidelines`_.


Useful links
^^^^^^^^^^^^

* `Source code repository`_
* `Documentation`_


Licensing and copyright
-----------------------

Copyright 2023 University College London.
imshowTk is released under the BSD-3 license. Please see the `license file`_ for details.


Acknowledgements
----------------

Supported by `Wellcome`_ and `EPSRC`_.


.. _`Wellcome EPSRC Centre for Interventional and Surgical Sciences`: http://www.ucl.ac.uk/weiss
.. _`source code repository`: https://github.com/SciKit-Surgery/imshowTk
.. _`Documentation`: https://imshowTk.readthedocs.io
.. _`SciKit-Surgery`: https://github.com/SciKit-Surgery
.. _`University College London (UCL)`: http://www.ucl.ac.uk/
.. _`Wellcome`: https://wellcome.ac.uk/
.. _`EPSRC`: https://www.epsrc.ac.uk/
.. _`contributing guidelines`: https://github.com/SciKit-Surgery/imshowTk/blob/master/CONTRIBUTING.rst
.. _`license file`: https://github.com/SciKit-Surgery/imshowTk/blob/master/LICENSE

