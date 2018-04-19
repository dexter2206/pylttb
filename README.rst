pylttb: downsampling using Largest Triangle Threebuckets algorithm
======================================================================================
|License: MIT|

**pylttb** is an efficient implementation of Largest Triangle Threebuckets algorithm.

The algorithm was described by Sveinn Steinarsson in his master thesis. More info and original
implementation can be found at this `page <https://github.com/sveinn-steinarsson/flot-downsample/>`_. The code in **pylttb** is based on this implementation
but structures computations a bit differently to leverage ``numpy`` 's array arithmetics.

Usage example
-------------
Supposing you have arrays of ``x`` and ``y`` all you need to do to downsample them to given
``threshold`` is:

.. code:: python

   from pylttb import lttb

   down_x, down_y = lttb(x, y, threshold)
   
.. |License: MIT| image:: https://img.shields.io/badge/License-MIT-yellow.svg
   :target: https://opensource.org/licenses/MIT
