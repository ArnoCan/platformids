# -*- coding: utf-8 -*-
"""Mapping of numeric and symbolic enum strings, optional loaded 
on demand for human display of debug info only.
"""
from __future__ import absolute_import

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2018 Arno-Can Uestuensoez" \
                " @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.28'
__uuid__ = "7add5ded-c39b-4b6e-8c87-1b3a1c150ee9"

__docformat__ = "restructuredtext en"

from platformids import num2enumstr  # @UnusedImport
from platformids import *  # @UnusedWildImport
from platformids.dist import *  # @UnusedWildImport

from platformids.dist.darwin import *  # @UnusedWildImport

#: mapping of the numeric value to it's symbolic representation
num2enumstr.update(
    {
        RTE_OSX105: "RTE_OSX1050",
        RTE_OSX1058: "RTE_OSX1058",
        RTE_OSX1060: "RTE_OSX1060",
        RTE_OSX1068: "RTE_OSX1068",
        RTE_OSX1070: "RTE_OSX1070",
        RTE_OSX1075: "RTE_OSX1075",
        RTE_OSX1080: "RTE_OSX1080",
        RTE_OSX1085: "RTE_OSX1085",
        RTE_OSX1090: "RTE_OSX1090",
        RTE_OSX1095: "RTE_OSX1095",
        RTE_OSX10100: "RTE_OSX10100",
        RTE_OSX10105: "RTE_OSX10105",
        RTE_OSX10110: "RTE_OSX10110",
        RTE_OSX10116: "RTE_OSX10116",
        RTE_OSX10124: "RTE_OSX10124",
        RTE_OSX10126: "RTE_OSX10126",
        RTE_OSX10130: "RTE_OSX10130",
        RTE_OSX10134: "RTE_OSX10134",
        RTE_OSX10136: "RTE_OSX10136",
        RTE_OSX10140: "RTE_OSX10140",
    }
)

