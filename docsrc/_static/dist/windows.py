# -*- coding: utf-8 -*-
"""MS-Windows releases for the *WindowsNT* family based on the registry information.
This includes the IoT products, e.g. *Windows-NT-10.0-IoT-core* on the *RaspberryPi*.
"""
from __future__ import absolute_import
from __future__ import print_function

import os
import re

from platformids import _debug, _verbose
from platformids import RTE_NT, RTE_WIN, RTE_WINDOWS, \
    rte2num, num2rte, num2pretty, \
    decode_version_str_to_segments, \
    PlatformIDsError, PlatformIDsFileCheck

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2018 Arno-Can Uestuensoez" \
                " @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.29'
__uuid__ = "7add5ded-c39b-4b6e-8c87-1b3a1c150ee9"

__docformat__ = "restructuredtext en"

if __debug__:

    # this is for unittests only
    class PlatformIDsUnittestTriggered(PlatformIDsError):
        pass

#
# The handled versions are of the "nt' technology, historic pre-versions and others
# are not supported.
#
# set: win32
# currently no sub-categories, some are contained in
# the 'set: generic': drives, shares
#
#
# RTE_DOS = RTE_WIN32 + 1  #: MS-DOS - frozen

#
# dist - the base versions of major and minor numbers
#
RTE_NT35 = RTE_NT + 0x001d0000  # : Windows NT-3.5
RTE_NT40 = RTE_NT + 0x00200000  # : Windows NT-4.0
RTE_NT50 = RTE_NT + 0x00280000  # : Windows NT-5.0 - W2000
RTE_NT51 = RTE_NT + 0x00290000  # : Windows NT-5.1 - WXP - 32bit
RTE_NT52 = RTE_NT + 0x002a0000  # : Windows NT-5.2 - W2003 / 2003 / 2003R2
RTE_NT60 = RTE_NT + 0x00300000  # : Windows NT-6.0 - vista / 2008
RTE_NT61 = RTE_NT + 0x00310000  # : Windows NT-6.1 - win7 / 2008R2
RTE_NT62 = RTE_NT + 0x00320000  # : Windows NT-6.2 - win8 / 2012
RTE_NT63 = RTE_NT + 0x00330000  # : Windows NT-6.3 - win8.1 / 2012R2
RTE_NT100 = RTE_NT + 0x00500000  # : Windows NT-10.0 - win10 / 2016

#
# distrel - some predefined constant values of the complete versions
#
# the values could be easily calculated dynamically by
#  old-scheme: adding the build number
#  new-scheme: adding the date based product version
#
# frozen history
#
RTE_WINNT35 = RTE_NT35 + 807  # : WindowsNT-4.0 Workstation - 32bit
RTE_WINNT40 = RTE_NT40 + 1381  # : WindowsNT-4.0 Workstation - 32bit
RTE_WIN2000 = RTE_NT50 + 2195  # : Windows2000

RTE_WINXP = RTE_NT51 + 2600  # : WindowsXP - 32bit

RTE_WINXP64 = RTE_NT52 + 3790  # : WindowsXP - 64bit
RTE_WIN2003 = RTE_NT52 + 3790  # : Windows2003
RTE_WIN2003R2 = RTE_NT52 + 3790  # : Windows2003R2 - exception: same build as 2003

RTE_WIN2008 = RTE_NT60 + 6001  # : Windows2008 RTM
RTE_WIN2008SP2 = RTE_NT60 + 6002  # : Windows2008 SP1

RTE_WIN7 = RTE_NT61 + 7600  # : Windows7
RTE_WIN2008R2 = RTE_NT61 + 7600  # : Windows2008R2

RTE_WIN7SP1 = RTE_NT61 + 7601  # : Windows7 SP1
RTE_WIN2008R2SP1 = RTE_NT61 + 7601  # : Windows2008R2 SP1

RTE_WIN8 = RTE_NT62 + 9200  # : Windows8
RTE_WIN2012 = RTE_NT62 + 9200  # : Windows2012

RTE_WIN81 = RTE_NT63 + 9600  # : Windows81
RTE_WIN2012R2 = RTE_NT63 + 9600  # : Windows2012R2

#
# for generic NT-10.0 releases
# simply add the numeric version to the base value RTE_NT100
#
# RTE_WINNT100_1703 =  RTE_NT100   + 1703           #: NT-10.0 - 2017.03
# RTE_WINNT100_1803 =  RTE_NT100   + 1803           #: NT-10.0 - 2018.03
# RTE_WINNT100_1809 =  RTE_NT100   + 1809           #: NT-10.0 - 2018.09

# : mapping of the rte string and numeric representation to the numeric value
rte2num.update(
    {
        '7 Server': RTE_WIN2008R2,
        '7': RTE_WIN7,
        '8 Server': RTE_WIN2012,
        '8': RTE_WIN8,
        'Blackcomb': RTE_WIN7,
        'Blue Server': RTE_WIN2012R2,
        'Blue': RTE_WIN81,
        'Longhorn Server' : RTE_NT61 + 6002,  # W2008 SP2
        'Threshold 1': RTE_NT100 + 1507,
        'Threshold 2': RTE_NT100 + 1511,
        'Redstone 1': RTE_NT100 + 1607,
        'Redstone 2': RTE_NT100 + 1703,
        'Redstone 3': RTE_NT100 + 1709,
        'Redstone 4': RTE_NT100 + 1803,
        'Redstone 5': RTE_NT100 + 1809,
        'Vienna': RTE_WIN7,
        'winxp': RTE_WINXP,
        'win2000': RTE_WIN2000,
        'winnt40': RTE_WINNT40,
        'win10': RTE_NT100,
        'win7': RTE_WIN7,
        'win8': RTE_WIN8,
        'win81': RTE_WIN81,
        'win2008': RTE_WIN2008,
        'win2008r2': RTE_WIN2008R2,
        'win2012': RTE_WIN2012,
        'win2012r2': RTE_WIN2012R2,
        'win2016': RTE_NT100,
        'win2019': RTE_NT100,
        'win2019se': RTE_NT100,
        RTE_WIN2000: RTE_WIN2000,
        RTE_WIN2008: RTE_WIN2008,
        RTE_WIN2008R2: RTE_WIN2008R2,
        RTE_WIN2012: RTE_WIN2012,
        RTE_WIN2012R2: RTE_WIN2012R2,
        RTE_WIN7: RTE_WIN7,
        RTE_WIN81: RTE_WIN81,
        RTE_WIN8: RTE_WIN8,
        RTE_WINNT40: RTE_WINNT40,
        RTE_WINXP: RTE_WINXP,

        'nt40': RTE_NT40,

        'nt50': RTE_NT50,
        'nt51': RTE_NT51,
        'nt52': RTE_NT52,

        'nt60': RTE_NT60,
        'nt61': RTE_NT61,
        'nt62': RTE_NT62,
        'nt63': RTE_NT63,
        'nt100': RTE_NT100,

        RTE_NT40: RTE_NT40,

        RTE_NT50: RTE_NT50,
        RTE_NT51: RTE_NT51,
        RTE_NT52: RTE_NT52,

        RTE_NT60: RTE_NT60,
        RTE_NT61: RTE_NT61,
        RTE_NT62: RTE_NT62,
        RTE_NT63: RTE_NT63,
        RTE_NT100: RTE_NT100,

    }
)

# : mapping of the rte numeric representation to the string value
num2rte.update(
    {
#         RTE_WINNT40: 'winnt40',
#         RTE_WIN2000: 'win2000',
#         RTE_WINXP: 'winxp',
#         RTE_WIN7: 'win7',
#         RTE_WIN81: 'win81',
#         RTE_WIN8: 'win8',
#         RTE_WIN2008: 'win2008',
#         RTE_WIN2008R2: 'win2008r2',  # the release is actually a different NT
#         RTE_WIN2012: 'win2012',
#         RTE_WIN2012R2: 'win2012r2',

        RTE_WINNT40: 'nt401381',
        RTE_WIN2000: 'nt502195',
        RTE_WINXP: 'nt512600',
        RTE_WIN7: 'nt617601',
        RTE_WIN81: 'nt639600',
        RTE_WIN8: 'nt629200',
        RTE_WIN2008: 'nt606002',
        RTE_WIN2008R2: 'nt617601',  # the release is actually a different NT
        RTE_WIN2012: 'nt629200',
        RTE_WIN2012R2: 'nt639600',

        RTE_NT40: 'nt40',
        RTE_NT50: 'nt50',
        RTE_NT51: 'nt51',
        RTE_NT52: 'nt52',
        RTE_NT60: 'nt60',
        RTE_NT61: 'nt61',
        RTE_NT62: 'nt62',
        RTE_NT63: 'nt63',
        RTE_NT100: 'nt100',

    }
)

# : mapping of the rte numeric representation to the pretty string value
num2pretty.update(
    {
        RTE_WIN: 'Windows',
        RTE_WINDOWS: 'Windows',

        RTE_WIN2000: 'Windows 2000',
        RTE_WIN2008: 'Windows Server 2008',
        RTE_WIN2008R2: 'Windows Server 2008R2',
        RTE_WIN2012: 'Windows Server 2012',
        RTE_WIN2012R2: 'Windows Server 2012R2',
        RTE_WIN7: 'Windows 7',
        RTE_WIN81: 'Windows 8.1',
        RTE_WIN8: 'Windows 8',
        RTE_WINNT40: 'WindowsNT-4.0',
        RTE_WINXP: 'Windows XP',

        RTE_NT40: 'NT-4.0',

        RTE_NT50: 'NT-5.0',
        RTE_NT51: 'NT-5.1',
        RTE_NT52: 'NT-5.2',

        RTE_NT60: 'NT-6.0',
        RTE_NT61: 'NT-6.1',
        RTE_NT62: 'NT-6.2',
        RTE_NT63: 'NT-6.3',
        RTE_NT100: 'NT-10.0',

    }
)

versions = {
    RTE_WINNT40: '4.0.1381',
    RTE_WIN2000: '5.0.2195',
    RTE_WINXP: '5.1.2600',
    RTE_WIN7: '6.1.7601',
    RTE_WIN81: '6.3.9600',
    RTE_WIN8: '6.2.9200',

    RTE_WIN2008: '6.0.6002',
    RTE_WIN2008R2: '6.1.7601',
    RTE_WIN2012: '6.2.9200',
    RTE_WIN2012R2: '6.3.9600',

    RTE_NT40: '4.0',

    RTE_NT50: '5.0',
    RTE_NT51: '5.1',
    RTE_NT52: '5.2',

    RTE_NT60: '6.0',
    RTE_NT61: '6.1',
    RTE_NT62: '6.2',
    RTE_NT63: '6.3',
    RTE_NT100: '10.0',

}

#
# Microsoft: OSVERSIONINFOEXA.wProductType
#
VER_NT_GENERIC = 0x0000000  # : non standard enum

VER_NT_WORKSTATION = 0x0000001  # : see wProductType
VER_NT_DOMAIN_CONTROLLER = 0x0000002  # : see wProductType
VER_NT_SERVER = 0x0000003  # : see wProductType

VER_NT_IOT = 0x0000004  # : non standard enum


class WinVersion(object):

    def __init__(self, *args, **kargs):

        self.ntmajor = self.ntminor = self.release = self.build = 0
        self.editionid = self.installationtype = self.sourcepath = self.productname = ''
        self.productcategory = VER_NT_GENERIC  # 0x0000000  #: non standard enum
        self.sp = self.ubr = None

        self.raw = {}
        self.fetch_current_version_raw()

        pass  # 4debugging

    def  fetch_current_version_raw(self, **kargs):

        use_nt_native = kargs.get('usetest', 255)  # : for unittests only
        
        if os.name == 'java':
            # it is Jython - use Java for access to native system data

            try:
                if __debug__:
                    # this is for unittests only
                    if (use_nt_native & 1) == 0:
                        raise PlatformIDsUnittestTriggered('use_nt_native_1(%d)' % (use_nt_native) )

                #
                # 1. try JNA
                if _verbose:
                    print("VERB:platformids:scan:try:JNA:jy.platformids.dist.nt.Kernel32GetProductInfo")
                from jy.platformids.dist.nt import Kernel32GetProductInfo  # @UnresolvedImport

                if _verbose:
                    print("VERB:platformids:scan:try:JNA:jy.platformids.dist.nt.Advapi32GetCurrentVersion")
                from jy.platformids.dist.nt import Advapi32GetCurrentVersion  # @UnresolvedImport

                if _verbose:
                    print("VERB:platformids:scan:JNA:LOADED")

                currentversion = Advapi32GetCurrentVersion().getCurrentVersionValues()
                for k, v in currentversion.items():
                    self.raw[k] = v

            except Exception as e:
                if _debug:
                    print("VERB:platformids:scan:JNA:failed with:" + str(e))

                try:
                    if __debug__:
                        # this is for unittests only
                        if (use_nt_native & 2) == 0:
                            raise PlatformIDsUnittestTriggered('use_nt_native_2(%d)' % (use_nt_native) )

                    #
                    # 2. try java.util.WindowsPreferences...
                    #
                    if _verbose:
                        print("VERB:platformids:scan:try:WindowsPreferences:jy.platformids.dist.nt.ReadCurrentVersionWinPrefs")
                    from jy.platformids.dist.nt import ReadCurrentVersionWinPrefs  # @UnresolvedImport

                    if _verbose:
                        print("VERB:platformids:scan:WindowsPreferences:LOADED")

                    currentversion = ReadCurrentVersionWinPrefs()
                    for k, v in currentversion:
                        self.raw[k] = v

                except Exception as e:
                    if _debug:
                        print("VERB:platformids:scan:WindowsPreferences:failed with:" + str(e))

                    #
                    # 4. try JNI next... coming soon
                    #
                    
                    try:
                        if __debug__:
                            # this is for unittests only
                            if (use_nt_native & 8) == 0:
                                raise PlatformIDsUnittestTriggered('use_nt_native_8(%d)' % (use_nt_native) )

                        #
                        # 8. try REG.EXE next...
                        #
                        if _verbose:
                            print("VERB:platformids:scan:try:platformids.dist.nt.RegistryByExe")
                        from platformids.dist.nt.windows_subprocess_reg_exe import RegistryByExe  # @UnresolvedImport
                        if _verbose:
                            print("VERB:platformids:scan:RegistryByExe:LOADED")

                        currentversion = RegistryByExe().read_CurrentVersion()
                        for k, v in currentversion.items():
                            self.raw[k] = v

                    except:
                        if __debug__:
                            # this is for unittests only
                            if (use_nt_native & 16) == 0:
                                raise PlatformIDsUnittestTriggered('use_nt_native_16(%d)' % (use_nt_native) )

                        #
                        # 16. try min-info
                        #
                        import platform
                        self.raw['ProductName'] = platform.System.getProperty('os.name').lower()  # @UndefinedVariable  # seems 2.0+
                        self.raw['CurrentMajorVersionNumber'], self.raw['CurrentMajorVersionNumber'], self.raw['CurrentMajorVersionNumber'] = decode_version_str_to_segments(
                            platform.System.getProperty('os.version').lower())  # @UndefinedVariable

        elif os.name == 'posix':
            # for document generation by introspection on posix platform
            # avoids exception with generator error for sphinx-apidoc
            pass

        else:

            #
            # read registry
            #

            # use standard libs _winreg / winreg
            try:
                import winreg  # @UnresolvedImport @UnusedImport
                validxError = WindowsError  # @UndefinedVariable
            except:
                import _winreg as winreg  # @UnresolvedImport @Reimport
                validxError = OSError

            hklm = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)  # @UndefinedVariable  - win32 only

            # rnumerate CurrentVersion attribute values
            curvers_key = winreg.OpenKey(hklm, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion")  # @UndefinedVariable  - win32 only
            for i in range(1024):
                try:
                    n, v, t = winreg.EnumValue(curvers_key, i)  # @UndefinedVariable  - win32 only @UnusedVariable
                    self.raw[n] = v
                except validxError:
                    break

            winreg.CloseKey(curvers_key)  # @UndefinedVariable  - win32 only

            #
            # fetch product category
            #
            try:
                #
                # use API
                #

                # post winxp supports simple access to product type
                from platformids.dist.nt.windows_kernel32dll import get_win32_OSProductInfo, get_win32_OSVersionInfoExa
                from platformids.dist.nt.windows_products import prod_ext, prod_type_categories

                osver = get_win32_OSVersionInfoExa()
                pinfo = get_win32_OSProductInfo()
                self.productcategory = pinfo.pdwReturnedProductType

                # TODO: check it
                if self.raw['InstallationType'].startswith('IoT'):
                    # superposes others if defined as IoT
                    self.productcategory = VER_NT_IOT

            except:
                #
                # estimate by data - default is GENERIC
                #
                try:
                    if self.raw['InstallationType'].startswith('Client'):
                        self.productcategory = VER_NT_WORKSTATION

                    elif self.raw['InstallationType'].startswith('Server'):
                        self.productcategory = VER_NT_SERVER

                    elif self.raw['InstallationType'].startswith('IoT'):
                        self.productcategory = VER_NT_IOT

                    elif re.match(r'.*omain.*', self.raw['InstallationType'], flags=re.MULTILINE):  # @UndefinedVariable
                        self.productcategory = VER_NT_DOMAIN_CONTROLLER

                    else:
                        # matches for almost all systems, which in nowadays
                        # could be used in multiple roles - without variation
                        self.productcategory = VER_NT_GENERIC

                except:
                    self.productcategory = VER_NT_GENERIC  # should already be from init

        self.raw['productcategory'] = self.productcategory

        return self.raw

    def readout_versioninfo_ext(self):

        #
        # Major-Minor-Version
        #
        try:
            # >= Win10
            self.ntmajor = int(self.raw['CurrentMajorVersionNumber'])  # REG_SZ    17763
            self.ntminor = int(self.raw['CurrentMinorVersionNumber'])  # REG_DWORD    0xa
            self.release = int(self.raw['ReleaseId'])  # REG_SZ    1511
            self.build = self.raw['CurrentBuildNumber']  # REG_DWORD    0x0

        except KeyError:
            # < Win10
            try:
                self.ntmajor, self.ntminor = self.raw['CurrentVersion'].split('.')  # REG_SZ    6.3
                self.ntmajor = int(self.ntmajor)
                self.ntminor = int(self.ntminor)
            except KeyError:
                # ooops...
                pass

            try:
                self.release = self.build = int(self.raw['CurrentBuildNumber'])  # REG_DWORD    0x0
            except:
                pass

            try:
                # WinXP < x < Win10
                self.sp = re.sub(r'^[^0-9]*', '', self.raw['CSDVersion'])  # REG_SZ
                self.sp = int(self.sp)
            except KeyError:
                pass

        try:
            self.ubr = int(self.raw['UBR'])  # REG_DWORD    0x6b
        except KeyError:
            pass

        try:
            self.editionid = self.raw['EditionID']  # REG_SZ    IoTUAP
        except KeyError:
            self.editionid = ''

        try:
            self.installationtype = self.raw['InstallationType']  # REG_SZ    IoTUAP
        except KeyError:
            self.installationtype = ''

            try:
                #
                # a weak criteria as the last resort,
                # the installation source path with some encoding
                # into the path name, e.g.:
                #
                #   D:\GERMAN\WIN2000\SERVER\I386
                #   D:\GERMAN\WINXP\PRO\I386
                #
                self.sourcepath = self.raw['SourcePath']  # REG_SZ D:\GERMAN\WINXP\PRO\I386
                self.sourcepath = re.sub(r'', r'', self.sourcepath)
            except KeyError:
                self.sourcepath = ''

        try:
            self.productname = self.raw['ProductName']  # REG_SZ    IoTUAP
        except:
            pass

        ret = {
            "ntmajor":          self.ntmajor,
            "ntminor":          self.ntminor,
            "release":          self.release,

            "build":            self.build,

            "productcategory":  self.productcategory,

            "InstallationType": self.installationtype,
            "ProductName":      self.productname,
            "EditionID":        self.editionid
        }

        if self.sp != None:
            ret["sp"] = self.sp

        if self.ubr != None:
            ret["ubr"] = self.ubr

        return ret

    def readout_distribution(self):

        self.readout_versioninfo_ext()
        return [
            'nt%d%d%d' % (self.ntmajor, self.ntminor, self.release),
            '%d.%d.%d' % (self.ntmajor, self.ntminor, self.release),
            'NT-%d.%d.%d' % (self.ntmajor, self.ntminor, self.release),
            'NT',
             (self.ntmajor, self.ntminor, self.release),
             'nt'
        ]

    def __str__(self):
        try:
            res = ''
            res += "ntmajor          = %s\n" % (str(self.ntmajor))
            res += "ntminor          = %s\n" % (str(self.ntminor))
            res += "release          = %s\n" % (str(self.release))
            res += "build            = %s\n" % (str(self.build))

            res += "productcategory  = %s\n" % (str(self.productcategory))

            try:
                res += "sp               = %s\n" % (str(self.sp))
            except AttributeError:
                res += "ubr              = %s\n" % (str(self.ubr))

            res += "InstallationType = %s\n" % (str(self.installationtype))
            res += "EditionID        = %s\n" % (str(self.editionid))
            res += "ProductName      = %s\n" % (str(self.productname))

            return res
        except:

            return

    def __repr__(self):
        try:
            res = "{"
            res += "ntmajor: %s, " % (str(self.ntmajor))
            res += "ntminor: %s, " % (str(self.ntminor))
            res += "release: %s, " % (str(self.release))
            res += "build: %s, " % (str(self.build))

            res += "productcategory: %s, " % (str(self.productcategory))

            try:
                res += "sp: %s, " % (str(self.sp))
            except AttributeError:
                res += "ubr: %s, " % (str(self.ubr))

            res += "InstallationType: %s, " % (str(self.installationtype))
            res += "EditionID: %s, " % (str(self.editionid))
            res += "ProductName: %s, " % (str(self.productname))
            res += "}"

            return res

        except:
            return

dist = ['', '', '', 'NT', '', '']

try:
    WINVERSION = WinVersion()
    WINVERSION.fetch_current_version_raw()
    dist = WINVERSION.readout_distribution()

except PlatformIDsFileCheck:
    # not on MS-Windows platform, so scan will fail
    pass    


if dist[5] != 'nt':
    # does not actually match MS-Windows
    dist = ['nt', '0.0.0', 'NT-0.0.0', 'NT', (0, 0, 0,), 'nt']


if __name__ == "__main__":
    winv = WinVersion()
    vinfo = winv.readout_versioninfo_ext()
    print(vinfo)

