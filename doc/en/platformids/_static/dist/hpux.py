# -*- coding: utf-8 -*-
"""HP-UX releases.

**REMARK**: Not yet supported.

"""
from __future__ import absolute_import

from platformids import RTE_UNIX

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2018 Arno-Can Uestuensoez" \
                " @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.29'
__uuid__ = "7add5ded-c39b-4b6e-8c87-1b3a1c150ee9"



RTE_HPUX          = RTE_UNIX     + 0x00080000    #: UNIX/HP-UX, as Posix system [POSIX]_.


dist = ['hpux', '0.0.0', 'HPUX-0.0.0', 'HPUX', (0, 0, 0,), 'hpux']  # defaults
