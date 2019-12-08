# -*- coding: utf-8 -*-
"""MS-Windows releases for the WindowsNT family.

.. note::

   **ATTENTION**: The ostype == RTE_NT uses for *dist* and *distrel* it's own non-default 
   encoding, while the scheme follows the default record layout, see ':ref:`Windows NT <enumWINNT>`'.
"""
from __future__ import absolute_import

import sys

from platformids import RTE_NT, RTE_WIN, RTE_WINDOWS, \
    rte2num, num2rte, num2pretty

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2018 Arno-Can Uestuensoez" \
                " @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.2'
__uuid__ = "7add5ded-c39b-4b6e-8c87-1b3a1c150ee9"

__docformat__ = "restructuredtext en"


#
# Microsoft: OSVERSIONINFOEXA.wProductType
#
VER_NT_WORKSTATION       = 0x0000001  #: see wProductType
VER_NT_DOMAIN_CONTROLLER = 0x0000002  #: see wProductType
VER_NT_SERVER            = 0x0000003  #: see wProductType

VER_NT_IOT               = 0x0000004  #: non standard enum

#
# platform specific adapters: win/nt and cygwin
#
if sys.platform in ('win32',):
    import ctypes
    kernel32 = ctypes.windll.kernel32  # @UndefinedVariable

elif sys.platform in ('cygwin',):
    import ctypes  # @Reimport
    kernel32 = ctypes.CDLL('kernel32.dll')


def get_win32_OSVersionInfo():   
    try:
        class OSVersionInfo(ctypes.Structure):
            _fields_ = [
                ("dwOSVersionInfoSize" , ctypes.c_int),        # DWORD
                ("dwMajorVersion"      , ctypes.c_int),        # DWORD
                ("dwMinorVersion"      , ctypes.c_int),        # DWORD
                ("dwBuildNumber"       , ctypes.c_int),        # DWORD
                ("dwPlatformId"        , ctypes.c_int),        # DWORD
                ("szCSDVersion"        , ctypes.c_char * 128), # CHAR
            ]
    
        _GetVersionEx = getattr( ctypes.windll.kernel32 , "GetVersionExA")  # @UndefinedVariable
        version  = OSVersionInfo()
        version.dwOSVersionInfoSize = ctypes.sizeof(OSVersionInfo)
        _GetVersionEx( ctypes.byref(version) )    
        return version

    except:
        return
    
def get_win32_OSVersionInfoExa():
    """Retuns a structure OSVERSIONINFOEXA, which contains the value
    for wProductType.
    """
    try:
        class OSVersionInfoExa(ctypes.Structure):
            _fields_ = [
                ("dwOSVersionInfoSize" , ctypes.c_int),        # DWORD
                ("dwMajorVersion"      , ctypes.c_int),        # DWORD
                ("dwMinorVersion"      , ctypes.c_int),        # DWORD
                ("dwBuildNumber"       , ctypes.c_int),        # DWORD
                ("dwPlatformId"        , ctypes.c_int),        # DWORD
                ("szCSDVersion"        , ctypes.c_char * 128), # CHAR

                ("wServicePackMajor"   , ctypes.c_int16),      # WORD
                ("wServicePackMinor"   , ctypes.c_int16),      # WORD
                ("wSuiteMask"          , ctypes.c_int16),      # WORD
                ("wProductType"        , ctypes.c_int8),       # BYTE
                    # wProductType - one of:
                    # - VER_NT_DOMAIN_CONTROLLER
                    # - VER_NT_SERVER
                    # - VER_NT_WORKSTATION
                    #
                ("wReserved"           , ctypes.c_int8),       # BYTE

                ];

        _GetVersionExa = getattr( kernel32 , "GetVersionExA")
        version  = OSVersionInfoExa()
        version.dwOSVersionInfoSize = ctypes.sizeof(OSVersionInfoExa)
        _GetVersionExa( ctypes.byref(version) )
        return version

    except:
        return

def get_win32_OSProductInfo():   

        # BOOL WINAPI GetProductInfo(
        #   _In_  DWORD  dwOSMajorVersion,
        #   _In_  DWORD  dwOSMinorVersion,
        #   _In_  DWORD  dwSpMajorVersion,
        #   _In_  DWORD  dwSpMinorVersion,
        #   _Out_ PDWORD pdwReturnedProductType
        # );

    try:
        class OSProdInfo(ctypes.Structure):
            _fields_ = [
                ("pdwReturnedProductType" , ctypes.c_int),        # PDWORD
                ];

        _GetProductInfo = getattr( kernel32 , "GetProductInfo")
        ptype  = OSProdInfo()
        ptype.dwOSVersionInfoSize = ctypes.sizeof(OSProdInfo)

        osver = get_win32_OSVersionInfoExa()
        _GetProductInfo(
            ctypes.c_int(osver.dwMajorVersion),
            ctypes.c_int(osver.dwMinorVersion),
            ctypes.c_int(osver.wServicePackMajor),
            ctypes.c_int(osver.wServicePackMinor),
            ctypes.byref(ptype) 
            )
        return ptype

    except:
        return

def print_versinfo(vinfo):
    try:
        print("dwOSVersionInfoSize  = " + str(vinfo.dwOSVersionInfoSize))
        print("dwMajorVersion       = " + str(vinfo.dwMajorVersion))
        print("dwMinorVersion       = " + str(vinfo.dwMinorVersion))
        print("dwBuildNumber        = " + str(vinfo.dwBuildNumber))
        print("dwPlatformId         = " + str(vinfo.dwPlatformId))
        print("szCSDVersion         = " + str(vinfo.szCSDVersion))

        print("wServicePackMajor    = " + str(vinfo.wServicePackMajor))
        print("wServicePackMinor    = " + str(vinfo.wServicePackMinor))
        print("wSuiteMask           = " + str(vinfo.wSuiteMask))
        print("wProductType         = " + str(vinfo.wProductType))
        print("wReserved            = " + str(vinfo.wReserved))

    except:
        return


def get_win32_IsWindowsXPSP1OrGreater():   

    try:
        # BOOL WINAPI  IsWindowsXPSP1OrGreater(
        # );

        class OSProdInfo(ctypes.Structure):
            _fields_ = [
                ("pdwReturnedProductType" , ctypes.c_int),        # PDWORD
                ];

        _IsWindowsXPSP1OrGreater = getattr( kernel32 , "IsWindowsXPSP1OrGreater")
        return _IsWindowsXPSP1OrGreater()

    except:
        return
