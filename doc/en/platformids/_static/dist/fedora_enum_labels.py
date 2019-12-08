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

from platformids.dist.fedora import *  # @UnusedWildImport

#: mapping of the numeric value to it's symbolic representation
num2enumstr.update(
    {
        RTE_FEDORA19:     "RTE_FEDORA19",
        RTE_FEDORA20:     "RTE_FEDORA20",
        RTE_FEDORA21:     "RTE_FEDORA21",
        RTE_FEDORA25:     "RTE_FEDORA25",
        RTE_FEDORA27:     "RTE_FEDORA27",
        RTE_FEDORA28:     "RTE_FEDORA28",
        RTE_FEDORA29:     "RTE_FEDORA29",
        RTE_FEDORA30:     "RTE_FEDORA30",
        RTE_FEDORA31:     "RTE_FEDORA31",
    }
)

