#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
**best_rgb.py**

**Platform:**
	Windows, Linux, Mac Os X.

**Description:**
	Defines **Color** package *Best RGB* colorspace.

**Others:**

"""

from __future__ import unicode_literals

import numpy

import color.derivation
import color.exceptions
import color.illuminants
import color.verbose
from color.colorspaces.colorspace import Colorspace

__author__ = "Thomas Mansencal"
__copyright__ = "Copyright (C) 2013 - 2014 - Thomas Mansencal"
__license__ = "GPL V3.0 - http://www.gnu.org/licenses/"
__maintainer__ = "Thomas Mansencal"
__email__ = "thomas.mansencal@gmail.com"
__status__ = "Production"

__all__ = ["LOGGER",
		   "BEST_RGB_PRIMARIES",
		   "BEST_RGB_WHITEPOINT",
		   "BEST_RGB_TO_XYZ_MATRIX",
		   "XYZ_TO_BEST_RGB_MATRIX",
		   "BEST_RGB_TRANSFER_FUNCTION",
		   "BEST_RGB_INVERSE_TRANSFER_FUNCTION",
		   "BEST_RGB_COLORSPACE"]

LOGGER = color.verbose.install_logger()

# http://www.hutchcolor.com/profiles/BestRGB.zip
BEST_RGB_PRIMARIES = numpy.matrix([0.73519163763066209, 0.26480836236933797,
								   0.2153361344537815, 0.77415966386554624,
								   0.13012295081967212, 0.034836065573770496]).reshape((3, 2))

BEST_RGB_WHITEPOINT = color.illuminants.ILLUMINANTS.get("Standard CIE 1931 2 Degree Observer").get("D50")

BEST_RGB_TO_XYZ_MATRIX = color.derivation.get_normalized_primary_matrix(BEST_RGB_PRIMARIES, BEST_RGB_WHITEPOINT)

XYZ_TO_BEST_RGB_MATRIX = BEST_RGB_TO_XYZ_MATRIX.getI()

def __best_rgb_transfer_function(RGB):
	"""
	Defines the *Best RGB* colorspace transfer function.

	:param RGB: RGB Matrix.
	:type RGB: Matrix (3x1)
	:return: Companded RGB Matrix.
	:rtype: Matrix (3x1)
	"""

	RGB = map(lambda x: x ** (1 / 2.2), numpy.ravel(RGB))
	return numpy.matrix(RGB).reshape((3, 1))

def __best_rgb_inverse_transfer_function(RGB):
	"""
	Defines the *Best RGB* colorspace inverse transfer function.

	:param RGB: RGB Matrix.
	:type RGB: Matrix (3x1)
	:return: Companded RGB Matrix.
	:rtype: Matrix (3x1)
	"""

	RGB = map(lambda x: x ** 2.2, numpy.ravel(RGB))
	return numpy.matrix(RGB).reshape((3, 1))

BEST_RGB_TRANSFER_FUNCTION = __best_rgb_transfer_function

BEST_RGB_INVERSE_TRANSFER_FUNCTION = __best_rgb_inverse_transfer_function

BEST_RGB_COLORSPACE = Colorspace("Best RGB",
								 BEST_RGB_PRIMARIES,
								 BEST_RGB_WHITEPOINT,
								 BEST_RGB_TO_XYZ_MATRIX,
								 XYZ_TO_BEST_RGB_MATRIX,
								 BEST_RGB_TRANSFER_FUNCTION,
								 BEST_RGB_INVERSE_TRANSFER_FUNCTION)