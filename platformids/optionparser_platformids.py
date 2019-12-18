# -*- coding: utf-8 -*-
"""Provides the command  line options for *platformids*.
"""
from __future__ import absolute_import

import sys
import os
import argparse
import platform

from sourceinfo.fileinfo import getcaller_linenumber

from pythonids import PYV35Plus, ISSTR
from platformids import _debug, _verbose
from platformids import RTE , RTE_WIN32, PlatformIDsError
import platformids.dist
import platformids.platforms


if PYV35Plus:
    unicode = str  # @ReservedAssignment

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2017 Arno-Can Uestuensoez" \
                " @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.35'
__uuid__ = "7add5ded-c39b-4b6e-8c87-1b3a1c150ee9"

__docformat__ = "restructuredtext en"

# cached defaults
_verbose = platformids._verbose
_debug = platformids._debug
_header = ''

# pre-fetch debugging
if '--debug' in sys.argv:
    sys.tracebacklimit = 1000
else:
    sys.tracebacklimit = 0


_appname = "rtplatformids"

class FetchOptionsError(PlatformIDsError):
    def __init__(self, *args, **kargs):
        super(FetchOptionsError, self).__init__(*args, **kargs)


#
# buffer for options evaluation
_clibuf = []

#
# early fetch for the parameter of the ArgumentParser constructor
#
if '--fromfile' in sys.argv:
    _fromfile='@'
else:
    _fromfile = None


class FormatTextRaw(argparse.HelpFormatter):
    """Formatter for help."""

    def _split_lines(self, text, width):
        """Customize help format."""
        if text.startswith('@R:'):
            return text[3:].splitlines()
        return argparse.HelpFormatter._split_lines(self, text, width)


class ActionExt(argparse.Action):
    """Extends the 'argparse.Action'
    """
    def __init__(self, *args, **kwargs):
        super(ActionExt, self).__init__(*args, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        """Adds context help on each option.
        """
        if _debug > 2:
            if values:
                sys.stderr.write(
                    "RDBG:%d:CLI:option: %s=%s\n" %(
                        getcaller_linenumber(),
                        str(option_string),
                        str(values)
                        )
                    )
            else:
                sys.stderr.write(
                    "RDBG:%d:CLI:option: %s\n" %(
                        getcaller_linenumber(),
                        str(option_string)
                        )
                    )

        if values and (values in ("help", "?") or type(values) is list and values[0] in ("help", "?")):
            form = FormatTextRaw('rdbg')
            # print('\n' + str(sys.argv[-2]))
            if self.__doc__:
                print('\n  ' +
                      '\n  '.join(FormatTextRaw._split_lines(
                          form, "@R:" + self.__doc__, 80)) + '\n')
            else:
                print('\n  ' +
                      '\n  '.join(FormatTextRaw._split_lines(
                          form, "No help.", 80)) + '\n')
            sys.exit(0)

        self.call(parser, namespace, values, option_string)

    def get_help_text(self):
        form = FormatTextRaw('rdbg')
        #print('\n' + str(sys.argv[-2]))
        if self.__doc__:
            return '\n  ' + '\n  '.join(FormatTextRaw._split_lines(
                form, "@R:" + self.__doc__, 80)) + '\n'
        else:
            return '\n  ' + '\n  '.join(FormatTextRaw._split_lines(
                form, "No help.", 80)) + '\n'

    def help_option(self):
        print(self.get_help_text())
        sys.exit(0)


class OptActionDebug(ActionExt):
    """Activates debug output including stacktrace, repetition raise level."""

    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        super(OptActionDebug, self).__init__(
            option_strings, dest, nargs, **kwargs)

    def call(self, parser, namespace, values, option_string=None):
        global _debug
        if values == '0':
            platformids._debug = 0
            _debug = platformids._debug
            namespace.debug = _debug
            sys.tracebacklimit = 0
        elif not values:
            platformids._debug += 1
            _debug = platformids._debug
            namespace.debug = _debug
            if _debug > 2:
                sys.tracebacklimit = 1000  # the original default
            else:
                sys.tracebacklimit += 4
        else:
            try:
                platformids._debug = int(values)
                _debug = platformids._debug
                namespace.debug = _debug
                sys.tracebacklimit = 1000  # the original default
            except ValueError:
                raise PlatformIDsError("'--debug' requires 'int', got: " + str(values))


class OptActionDebugOptions(ActionExt):
    """Displays the internal commandline options data with optional output format."""

    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        super(OptActionDebugOptions, self).__init__(
            option_strings, dest, nargs, **kwargs)

    def call(self, parser, namespace, values, option_string=None):
        namespace.debug_options = []
        if values in ('', None, [],):
            namespace.debug_options.append('json')
        elif values[0].lower() in ('json', 'repr', 'str'):
            namespace.debug_options.append(values[0])
            if values[-1].lower() == 'cont':
                namespace.debug_options.append(values[1])
            elif len(values) >1:
                raise PlatformIDsError("invalid value: --debug-options=" + str(values))
        else:
            raise PlatformIDsError("invalid value: --debug-options=" + str(values))

class OptActionEnumerate(ActionExt):
    """Enumerates the known platform entries."""

    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        super(OptActionEnumerate, self).__init__(
            option_strings, dest, nargs, **kwargs)

    def call(self, parser, namespace, values, option_string=None):
        if not values:
            namespace.enumerate = {'type': 'all',}
        else:
            namespace.enumerate = {'type': values.pop(0)}
            if namespace.enumerate['type'] not in ('all', 'category', 'ostype', 'dist', 'distrel'):
                raise PlatformIDsError("Invalid value for enumerate: '" + str(values) + "'")
            
            for x in values:
                if x.startswith('num='):
                    namespace.enumerate['num'] = x[4:]
                    if namespace.enumerate['num'] not in ('int', 'hex', 'bit', 'sym',):
                        raise PlatformIDsError("Invalid value for num='" + str(namespace.enumerate['num']) + "'")
                elif x.startswith('scope='):
                    namespace.enumerate['scope'] = x[6:]
                    if namespace.enumerate['scope'] not in ('all', 'numkey', 'strkey',):
                        raise PlatformIDsError("Invalid value for scope='" + str(namespace.enumerate['scope']) + "'")
                elif x.startswith('pad='):
                    namespace.enumerate['pad'] = x[4:]
                    if namespace.enumerate['pad'] not in ('on', '1', 'true', 'off', '0', 'false',):
                        raise PlatformIDsError("Invalid value for pad='" + str(namespace.enumerate['pad']) + "'")
                elif x.startswith('reverse='):
                    namespace.enumerate['reverse'] = x[8:]
                    if namespace.enumerate['reverse'] not in ('on', '1', 'true', 'off', '0', 'false',):
                        raise PlatformIDsError("Invalid value for reverse='" + str(namespace.enumerate['reverse']) + "'")
                else:
                    raise PlatformIDsError("Invalid option: '" + str(x) + "'")

class OptActionEnvironDetails(ActionExt):
    """Details of runtime environment."""

    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        super(OptActionEnvironDetails, self).__init__(
            option_strings, dest, nargs, **kwargs)

    def call(self, parser, namespace, values, option_string=None):

        print("")
        print("app:                   " + str(_appname))
        print("")
        print("python running rtplatformids:")
        print("  running version:     " + str(platform.python_version()))
        print("  compiler:            " + str(platform.python_compiler()))
        print("  build:               " + str(platform.python_build()))
        print("")
        sys.exit()


class OptActionFromfile(ActionExt):
    """Enables the read of options from an options file."""

    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        super(OptActionFromfile, self).__init__(
            option_strings, dest, nargs, **kwargs)

    def call(self, parser, namespace, values, option_string=None):
        namespace.fromfile = True


class OptActionH(ActionExt):
    """Usage."""

    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        super(OptActionH, self).__init__(
            option_strings, dest, nargs, **kwargs)

    def call(self, parser, namespace, values, option_string=None):
        parser.print_usage()
        sys.exit(0)


class OptActionHelp(ActionExt):
    """This help."""

    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        super(OptActionHelp, self).__init__(
            option_strings, dest, nargs, **kwargs)

    def call(self, parser, namespace, values, option_string=None):
        parser.print_help()
        sys.exit(0)


class OptActionPrintOutFormat(ActionExt):
    """Defines the processed output format.

  --out-format=<format>
    format := (
       'json' | 'raw' | 'repr' | 'str' | 'bashvars'
    )

"""

    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        super(OptActionPrintOutFormat, self).__init__(
            option_strings, dest, nargs, **kwargs)

    def call(self, parser, namespace, values, option_string=None):
        if not values[0]:
            raise  PlatformIDsError("Requires value for'--out-format'")
        elif values[0] in ('json', 'raw', 'repr', 'str', 'basharray' ,'bashvars'):
            namespace.out_format = values[0]
        else:
            raise  PlatformIDsError("Unknown output format:" + str(values))

class OptActionCategory(ActionExt):
    """Display category."""

    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        super(OptActionCategory, self).__init__(
            option_strings, dest, nargs, **kwargs)

    def call(self, parser, namespace, values, option_string=None):
        namespace.category= True
        namespace.selected = True


class OptActionOstype(ActionExt):
    """Display ostype."""

    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        super(OptActionOstype, self).__init__(
            option_strings, dest, nargs, **kwargs)

    def call(self, parser, namespace, values, option_string=None):
        namespace.ostype = True
        namespace.selected = True


class OptActionPlatform(ActionExt):
    """Display parameters from standard library 'platform'."""

    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        super(OptActionPlatform, self).__init__(
            option_strings, dest, nargs, **kwargs)

    def call(self, parser, namespace, values, option_string=None):
        namespace.platform = True
        namespace.selected = True


class OptActionDist(ActionExt):
    """Display distribution."""

    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        super(OptActionDist, self).__init__(
            option_strings, dest, nargs, **kwargs)

    def call(self, parser, namespace, values, option_string=None):
        namespace.dist = True
        namespace.selected = True


class OptActionDistRel(ActionExt):
    """Display release of the distribution."""

    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        super(OptActionDistRel, self).__init__(
            option_strings, dest, nargs, **kwargs)

    def call(self, parser, namespace, values, option_string=None):
        namespace.distrel = True
        namespace.selected = True


class OptActionDistRelName(ActionExt):
    """Display name of the distribution release."""

    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        super(OptActionDistRelName, self).__init__(
            option_strings, dest, nargs, **kwargs)

    def call(self, parser, namespace, values, option_string=None):
        namespace.distrel = True
        namespace.selected = True


class OptActionDistRelKey(ActionExt):
    """Display name of the selection key of the distribution release.
Used for internal mapping-tables to be used as debugging support.
"""

    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        super(OptActionDistRelKey, self).__init__(
            option_strings, dest, nargs, **kwargs)

    def call(self, parser, namespace, values, option_string=None):
        namespace.distrel_key = True
        namespace.selected = True


class OptActionDistVers(ActionExt):
    """Display the version array the distribution release."""

    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        super(OptActionDistVers, self).__init__(
            option_strings, dest, nargs, **kwargs)

    def call(self, parser, namespace, values, option_string=None):
        namespace.distrel_version = True
        namespace.selected = True


class OptActionLoad(ActionExt):
    """Loads additional platform source modules."""

    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        super(OptActionLoad, self).__init__(
            option_strings, dest, nargs, **kwargs)

    def call(self, parser, namespace, values, option_string=None):
        if not values:
            raise PlatformIDsError("Requires value: '--load'")
        else:
            if type(values) is list:
                values = values[0]
            if not os.path.exists(values):
                raise PlatformIDsError("Missing filepathname: --load='" + str(values) + "'")
            if not os.path.isfile(values):
                raise PlatformIDsError("Requires a file: --load='" + str(values) + "'")
            namespace.load.append(values)


class OptActionOstypeId(ActionExt):
    """Display the ID of the OS release."""

    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        super(OptActionOstypeId, self).__init__(
            option_strings, dest, nargs, **kwargs)

    def call(self, parser, namespace, values, option_string=None):
        namespace.ostype_id = True
        namespace.selected = True


class OptActionOstypeVers(ActionExt):
    """Display the version array the OS release."""

    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        super(OptActionOstypeVers, self).__init__(
            option_strings, dest, nargs, **kwargs)

    def call(self, parser, namespace, values, option_string=None):
        namespace.ostype_version = True
        namespace.selected = True


class OptActionDistRelHexversion(ActionExt):
    """Display the release of the distribution including the canonical version as hex-bit-array."""

    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        super(OptActionDistRelHexversion, self).__init__(
            option_strings, dest, nargs, **kwargs)

    def call(self, parser, namespace, values, option_string=None):
        namespace.distrel_hexversion = True
        namespace.selected = True


class OptActionQuiet(ActionExt):
    """Suppress output"""

    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        super(OptActionQuiet, self).__init__(
            option_strings, dest, nargs, **kwargs)

    def call(self, parser, namespace, values, option_string=None):
        namespace.quiet = True


class OptActionRaw(ActionExt):
    """Prints the values as raw type, else symbolic names where suitable."""

    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        super(OptActionRaw, self).__init__(
            option_strings, dest, nargs, **kwargs)

    def call(self, parser, namespace, values, option_string=None):
        namespace.raw = True


class OptActionTerse(ActionExt):
    """Terse, values only."""

    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        super(OptActionTerse, self).__init__(
            option_strings, dest, nargs, **kwargs)

    def call(self, parser, namespace, values, option_string=None):
        namespace.terse = True


class OptActionVerbose(ActionExt):
    """Verbose, repetition raises the level."""

    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        super(OptActionVerbose, self).__init__(
            option_strings, dest, nargs, **kwargs)

    def call(self, parser, namespace, values, option_string=None):
        global _verbose
        if values == '0':
            namespace.verbose = _verbose = platformids._verbose = 0
        elif not values:
            platformids._verbose += 1
            _verbose = platformids._verbose
            namespace.verbose = _verbose
        else:
            try:
                platformids._verbose = int(values)
                _verbose = platformids._verbose
                namespace.verbose = _verbose
            except ValueError:
                raise PlatformIDsError("'--verbose' requires 'int', got: " + str(values))


class OptActionVersion(ActionExt):
    """Current version of 'rtplatformids' - terse."""

    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        super(OptActionVersion, self).__init__(
            option_strings, dest, nargs, **kwargs)

    def call(self, parser, namespace, values, option_string=None):
        sys.stdout.write(str(__version__))
        sys.exit()


class OptActionVersionDetails(ActionExt):
    """Current versions - detailed."""

    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        super(OptActionVersionDetails, self).__init__(
            option_strings, dest, nargs, **kwargs)

    def call(self, parser, namespace, values, option_string=None):
        print("")
        print("app:            " + str(_appname))
        print("id:             " + str(__uuid__))
        print("platformids:    " + str(platformids.__version__))
        print("platforms:      " + str(platformids.platforms.__version__))
#        print("dist:           " + str(platformids.dist.__version__))
        print("rtplatformids:  " + str(__version__))
        print("")
        print("Project:        " + 'https://multiconf.sourceforge.net/')
        print("SCM:            " + 'https://github.com/ArnoCan/multiconf/')
        print("package:        " + 'https://pypi.python.org/pypi/multiconf/')
        print("docs:           " + 'https://pythonhosted.org/multiconf/')
        print("")
        print("author:         " + str(platformids.__author__))
        print("author-www:     " + 'https://arnocan.wordpress.com')
        print("")
        print("copyright:      " + str(platformids.__copyright__))
        print("license:        " + str(platformids.__license__))
        print("")
        sys.exit()

class OptionsNamespace(object):
    """Namespace object for parameter passing.
    """
    def __init__(self, argv, optargs, env=None):
        self._argv = argv  #: The original argv
        self.optargs = optargs  #: the result formatted as JSON compatible
        self.rdbgenv = env  #: FIXME:
        self.selected = False

    def get_optvalues(self):
        """Gets the resulting command line parameters."""
        return self.optargs

#
# option parser/scanner
#
class OptionsParser(object):

    def __init__(self, argv=None, *args, **kargs):
        """
        Args:
            argv:
                call options

        Returns:
            (opts, unknown, args)

        Raises:
            pass-through
        """
        # prep argv
        if argv and type(argv) in ISSTR:
            self.argv = argv.split()
        elif argv and type(argv) in (list,):
            self.argv = argv[:]
        elif argv is None:
            self.argv = sys.argv[:]
        else:
            self.argv = argv

        self.optargs = {}  #: resulting options and arguments'--

    def get_options(self):

        _myspace = OptionsNamespace(self.argv, self.optargs)

        # set and call parser
        self.parser = argparse.ArgumentParser(
            prog='rtplatformids',
            add_help=False,
            description="""
The 'rtplatformids' command line interface provides basic
dialogue access to the library modules of 'platformids'.

""",
            formatter_class=FormatTextRaw,
            fromfile_prefix_chars=_fromfile  # from early fetch
        )

        group_options = self.parser.add_argument_group(
            'Parameter:',
            'When at least one is active the selected are displayed only, else all.'
        )
        group_options.add_argument(
            '--category',
            '-category',
            nargs=0,
            default=False,
            action=OptActionCategory,
            help="@R:" + OptActionCategory.__doc__
        )
        group_options.add_argument(
            '--ostype',
            '-ostype',
            nargs=0,
            default=False,
            action=OptActionOstype,
            help="@R:" + OptActionOstype.__doc__
        )
        group_options.add_argument(
            '--dist',
            '-dist',
            nargs=0,
            default=False,
            action=OptActionDist,
            help="@R:" + OptActionDist.__doc__
        )
        group_options.add_argument(
            '--distrel',
            '-distrel',
            nargs=0,
            default=False,
            action=OptActionDistRel,
            help="@R:" + OptActionDistRel.__doc__
        )
        group_options.add_argument(
            '--distrel-name',
            '-distrel-name',
            nargs=0,
            default=False,
            action=OptActionDistRelName,
            help="@R:" + OptActionDistRelName.__doc__
        )
        group_options.add_argument(
            '--distrel-key',
            '-distrel-key',
            nargs=0,
            default=False,
            action=OptActionDistRelKey,
            help="@R:" + OptActionDistRelKey.__doc__
        )
        group_options.add_argument(
            '--distrel-version',
            '-distrel-version',
            '--dist-vers',
            '-dist-vers',
            nargs=0,
            default=False,
            action=OptActionDistVers,
            help="@R:" + OptActionDistVers.__doc__
        )
        group_options.add_argument(
            '--distrel-hexversion',
            '-distrel-hexversion',
            nargs=0,
            default=False,
            action=OptActionDistRelHexversion,
            help="@R:" + OptActionDistRelHexversion.__doc__
        )
        group_options.add_argument(
            '--ostype-id',
            '-ostype-id',
            nargs=0,
            default=False,
            action=OptActionOstypeId,
            help="@R:" + OptActionOstypeId.__doc__
        )
        group_options.add_argument(
            '--ostype-version',
            '-ostype-version',
            nargs=0,
            default=False,
            action=OptActionOstypeVers,
            help="@R:" + OptActionOstypeVers.__doc__
        )
        group_options.add_argument(
            '--platform',
            '-platform',
            nargs=0,
            default=False,
            action=OptActionPlatform,
            help="@R:" + OptActionPlatform.__doc__
        )
        group_options.add_argument(
            '--raw',
            '-raw',
            nargs=0,
            default=False,
            action=OptActionRaw,
            help="@R:" + OptActionRaw.__doc__
        )

        group_options = self.parser.add_argument_group(
            'Developer Options:',
            'For details refer to the manual.'
        )
        group_options.add_argument(
            '--debug',
            '-debug',
            '-d',
            nargs='?',
            type=int,
            default=0,
            const=None,
            action=OptActionDebug,
            help="@R:" + OptActionDebug.__doc__
        )
        group_options.add_argument(
            '--debug-options',
            '-debug-options',
            nargs='*',
            #type=str,
            default=[],
            #const=[ 'json', 'break',],
            action=OptActionDebugOptions,
            help="@R:" + OptActionDebugOptions.__doc__
        )
        group_options.add_argument(
            '--enumerate',
            '-enumerate',
            nargs='*',
            type=str,
            default={},
            const={'all', 'num=int', 'scope=strkey', 'pad=on', 'reverse=false'},
            action=OptActionEnumerate,
            help="@R:" + OptActionEnumerate.__doc__
        )
        group_options.add_argument(
            '--environ', 
            '-environ', 
            '--env',
            '-env',
            nargs=0,
            action=OptActionEnvironDetails,
            default=None,
            const=None,
            help="@R:" + OptActionEnvironDetails.__doc__
        )
        group_options.add_argument(
            '--fromfile',
            '-fromfile',
            nargs=0,
            action=OptActionFromfile,
            help="@R:" + OptActionFromfile.__doc__
        )
        group_options.add_argument(
            '--load',
            '-load',
            nargs=1,
            type=str,
            default=[],
            const=[],
            action=OptActionLoad,
            help="@R:" + OptActionLoad.__doc__
        )


        group_options = self.parser.add_argument_group(
            'Generic Support Options:',
            ''
        )
        group_options.add_argument(
            '--out-format',
            '-out-format',
            nargs=1,
            type=str,
            default='str',
            const='json',
            action=OptActionPrintOutFormat,
            help="@R:" + OptActionPrintOutFormat.__doc__
        )
        group_options.add_argument(
            '--quiet',
            '-quiet',
            '-q',
            nargs=0,
            default=False,
            action=OptActionQuiet,
            help="@R:" + OptActionQuiet.__doc__
        )
        group_options.add_argument(
            '--terse',
            '-terse',
            '-X', 
            nargs=0,
            default=False,
            action=OptActionTerse,
            help="@R:" + OptActionTerse.__doc__
        )
        group_options.add_argument(
            '--verbose',
            '-verbose',
            '-v', 
            nargs='?',
            type=int,
            action=OptActionVerbose,
            default=0,
            const=0,
            help="@R:" + OptActionVerbose.__doc__
        )
        group_options.add_argument(
            '--version',
            '-version',
            nargs=0,
            action=OptActionVersion,
            default=None,
            help="@R:" + OptActionVersion.__doc__
        )
        group_options.add_argument(
            '--Version',
            '-Version',
            nargs=0,
            action=OptActionVersionDetails,
            default=None,
            help="@R:" + OptActionVersionDetails.__doc__
        )
        group_options.add_argument(
            '--help',
            '-help',
            nargs=0,
            action=OptActionHelp,
            default=None,
            help="@R:" + OptActionHelp.__doc__
        )
        group_options.add_argument(
            '-h',
            nargs=0,
            action=OptActionH,
            default=None,
            help="@R:" + OptActionH.__doc__
        )


        # defined args
        # a little extra
        if self.argv == sys.argv:
            argv = self.argv[1:]
        else:
            argv = self.argv

        # group_result = self.parser.add_argument_group(  # @UnusedVariable
        #     'RESULT:',
        #     """
        #     Success: '0', 
        #     else:    != '0'.
        #     """
        # )

        group_see = self.parser.add_argument_group(  # @UnusedVariable
            'SEE ALSO:',
            """
            https://pypi.org/project/platformids/
            https://platformids.sourceforge.io/
            """
        )

        group_copyright = self.parser.add_argument_group(  # @UnusedVariable
            'COPYRIGHT:',
            """Arno-Can Uestuensoez (C)2008-2018 @Ingenieurbuero Arno-Can Uestuensoez""",
        )

        # defined args
        if "--" in argv:
            idx = argv.index('--')
            opts, unknown = self.parser.parse_known_args(argv, namespace=_myspace)
            args = argv[idx + 1:]
        else:
            opts, unknown = self.parser.parse_known_args(argv, namespace=_myspace)
            args = []
            # args = opts.ARGS

        # for later post-processing
        self.opts = _myspace
        self.args = args
        self.unknown = unknown

        if unknown:
            raise PlatformIDsError("Unknown options:" + str(unknown))

        if platformids._debug:
            if RTE & RTE_WIN32:
                sys.stderr.write("DBG:PLATFORMIDS:CLI:PID=%d\n" % (os.getpid(),))
            else:
                sys.stderr.write(
                    "DBG:PLATFORMIDS:CLI:PID=%d, PPID=%d\n" % (
                        os.getpid(), os.getppid(),)  # @UndefinedVariable
                    )

        if _myspace.debug_options:
            if self.opts.debug_options[0] == 'str':
                for k,v, in self.get_items():
                    print("%-20s: %s" % (k, v,))
            elif self.opts.debug_options[0] == 'repr':
                print(repr(self.get_JSON_bin()))
            elif self.opts.debug_options[0] == 'json':
                import jsondata.jsondata
                print(str(jsondata.jsondata.JSONData(self.get_JSON_bin())))
            else:
                raise  PlatformIDsError("Output format not supported for options print:" + str(self.opts.out_format))

            if len(self.opts.debug_options) == 1:
                sys.exit(0)

        return opts, unknown, args

    def get_JSON_bin(self):
        """Provides structured data of the compile task in-memory in
        JSON format. ::

           result := {
              'params': {
                  'category': '',
                  'dist': '',
                  'distrel_version': '',
                  'distrel': '',
                  'distrel_key': '',
                  'distrel_name': '',
                  'distrel_hexversion': '',
                  'ostype_hexversion': '',
                  'ostype': ''
               },
              'selected': '',
              'load': ''
              'enumerate': ''
              'platform': ''
              'raw': ''

              'debug': '',
              'debug_options': '',
              'outform': {
                  'out_format': '',
              },
              'quiet': '',
              'terse': ''
              'verbose': '',

              'args': [],
           }
        """
        j =  {}
        j['params'] =  {}
        j['params']['category'] =  self.opts.category
        j['params']['dist'] =  self.opts.dist
        j['params']['distrel_version'] =  self.opts.distrel_version
        j['params']['distrel'] =  self.opts.distrel
        j['params']['distrel_hexversion'] =  self.opts.distrel_hexversion
        j['params']['distrel_key'] =  self.opts.distrel_key
        j['params']['distrel_name'] =  self.opts.distrel_name
        j['params']['ostype_version'] =  self.opts.ostype_version
        j['params']['ostype'] =  self.opts.ostype
        j['selected'] =  self.opts.selected

        j['load'] =  self.opts.load
        j['enumerate'] =  self.opts.enumerate
        j['platform'] =  self.opts.platform
        j['raw'] =  self.opts.platform

        j['debug'] =  self.opts.debug
        j['debug_options'] =  self.opts.debug_options
        j['outform'] =  {}
        j['outform']['out_format'] =  self.opts.out_format
        j['quiet'] =  self.opts.quiet
        j['terse'] =  self.opts.terse
        j['verbose'] =  self.opts.verbose

        j['args'] =  self.args

        return j

    def get_items(self):
        """Provides a list of flat str-value tuples ::

           result := [
            ('category', ''),
            ('dist', ''),
            ('distrel_version', ''),
            ('distrel', ''),
            ('distrel_key', ''),
            ('distrel_name', ''),
            ('hexversion', ''),
            ('ostype_version', ''),
            ('ostype', ''),
            ('selected', ''),

            ('load', ''),
            ('enumerate', ''),
            ('platform', ''),
            ('raw', ''),

            ('debug', ''),
            ('debug_options', ''),
            ('out_format', ''),
            ('quiet', ''),
            ('terse', ''),
            ('verbose', ''),
           ]
        """
        return [
            ('category',  self.opts.category),
            ('dist',  self.opts.dist),
            ('distrel_version',  self.opts.distrel_version),
            ('distrel',  self.opts.distrel),
            ('distrel_key',  self.opts.distrel_key),
            ('distrel_name',  self.opts.distrel_name),
            ('hexversion',  self.opts.hexversion),
            ('ostype_version',  self.opts.ostype_version),
            ('ostype',  self.opts.ostype),
            ('selected',  self.opts.selected),

            ('load',  self.opts.load),
            ('enumerate',  self.opts.enumerate),
            ('platform',  self.opts.platform),
            ('raw',  self.opts.raw),

            ('debug', self.opts.debug),
            ('debug_options', self.opts.debug_options),
            ('out_format', self.opts.out_format),
            ('quiet', self.opts.quiet),
            ('terse', self.opts.terse),
            ('verbose', self.opts.verbose),
        ]

    def print_usage(self, *args):
        self.parser.print_usage(*args)

    def print_help(self, *args):
        self.parser.print_help(*args)
