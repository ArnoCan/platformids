# -*- coding: utf-8 -*-
"""Reads the MS-Windows registry by calling a subprocess for reg.exe.

This is a fallback solution when neither *winreg* / *_winreg*, nor in case 
of Jython the Java APIs such as *WindowsPref*, *JNA*, or *JNI* are not
available.
This works also on *Cygwin*, when e.g. the path for *kernel32.dll* does not
match for the *ctypes*.

Avoid using it due to serious performance impact compared to 
the others - but do when nothing else helps and the 
version information matters. 
"""
from __future__ import absolute_import

import re

from subprocess import Popen, PIPE

from platformids import PlatformIDsError
from platformids.dist.windows import VER_NT_SERVER, VER_NT_WORKSTATION, \
    VER_NT_DOMAIN_CONTROLLER, VER_NT_IOT, VER_NT_GENERIC


__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2018 Arno-Can Uestuensoez" \
                " @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.2'
__uuid__ = "7add5ded-c39b-4b6e-8c87-1b3a1c150ee9"

__docformat__ = "restructuredtext en"


class PlatformIDsReadRegExeError(PlatformIDsError):
    pass


class RegistryByExe(object):
    """Registry read access by *reg.exe* to ::

       "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion"

    """

    def __init__(self):
        
        #: used as cache for following calls
        #: the cache represents this platform, so may not be altered
        self.result = {}
        
        # cached product type
        self.product_type = None


    def read_CurrentVersion(self):
        """Reads the constant - thus hardcoded - key from :: 

             "HKLM\Software\Microsoft\Windows NT\CurrentVersion"

        Args:
            None
        
        Returns:
            The dictionary of the *CurrentVersion*.
        
        Raises:
            PlatformIDsReadRegExeError
            
            pass-through
            
        """
        cmd = 'c:\Windows\\system32\\reg.exe query '
        cmd += '"HKLM\Software\Microsoft\Windows NT\CurrentVersion"'

        p = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
        out = p.communicate()
        
        if not out[0]:
            raise PlatformIDsReadRegExeError("read registry failed: " + str(out))
        
        for k,v in re.findall('^ *([^ ]+) *REG_[^ ]* *(.*)[\r][\n]*$',  out[0], flags=re.MULTILINE):  # @UndefinedVariable
            try:
                self.result[k] = int(v)
            except ValueError:
                try:
                    self.result[k] = int(v, 16)
                except ValueError:
                    self.result[k] = v
        
        return self.result


    def get_win32_OSProductInfo(self):   
        """Estimates the product type, because this is a fallback
        when nothing else is available.
         
        Args:
            None
        
        Returns:
            The estimated product type as a reduction of the
            original 
            
                "pdwReturnedProductType"
        
        Raises:
            pass-through

        """
        if not self.result:
            # set cache
            self.read_CurrentVersion()
        
        if self.product_type != None:
            # use cached product type
            return self.product_type
        
        try:
            #
            # for NT >= 6.0
            #
            eid = self.resultp['EditionID']  
            if re.match(r'.*[Ss]erver', eid):
                self.product_type = VER_NT_SERVER  # 0x0000003 #: see wProductType 
                return VER_NT_SERVER
                
            elif self.resultp['InstallationType'] == 'Client':  # has to be present when *EditionID* is
                self.product_type = VER_NT_WORKSTATION  # 0x0000001 #: see wProductType 
                return VER_NT_WORKSTATION

            elif re.match(r'.*[Dd]omain', eid):
                self.product_type = VER_NT_DOMAIN_CONTROLLER  # 0x0000002 #: see wProductType 
                return VER_NT_DOMAIN_CONTROLLER


            elif re.match(r'.*[Ii][Oo][Tt]', eid):
                self.product_type = VER_NT_IOT  # 0x0000004 #: non standard enum 
                return VER_NT_IOT

            else:
                self.product_type = VER_NT_GENERIC  # 0x0000000 #: non standard enum 
                return VER_NT_GENERIC

        except:
            #
            # for NT < 6.0
            #
            # do not want spend much effort for legacy has past EOL, so...
            #
            
            pnam = self.resultp['ProductName']  
            if re.match(r'.*XP', pnam):
                # WindowsXP
                self.product_type = VER_NT_WORKSTATION  # 0x0000001 #: see wProductType 
                return VER_NT_WORKSTATION

            elif re.match(r'.*SERVER', self.resultp['SourcePath']):  # not reliable...
                # WindowsXP
                self.product_type = VER_NT_SERVER  # 0x0000003 #: see wProductType 
                return VER_NT_SERVER
            
            else:
                #
                # may match a lot...
                #
                self.product_type = VER_NT_GENERIC  # 0x0000000 #: non standard enum 
                return VER_NT_GENERIC
            
