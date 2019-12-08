REM 
REM AUTHOR = Arno-Can Uestuensoez
REM AUTHOR_EMAIL = acue_sf2@sourceforge.net
REM LICENSE = Artistic-License-2.0 + Forced-Fairplay-Constraints
REM COPYRIGHT = Copyright (C) 2019 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez
REM UUID = 1ba7bffb-c00b-4691-a3e9-e392f968e437
REM

@ECHO OFF

pushd %~dp0

if "%BUILDDOC%" == "" (
	set BUILDDOC=sphinx-build
)
if "%DOCTYPE%" == "" (
	set DOCTYPE=html
)

REM emulate "make help"
if "%1" == "help" goto help

REM emulate "make help-sphinx"
if "%1" == "help-sphinx" goto help-sphinx

REM emulate "make clean"
if "%1" == "clean" (
	rmdir /Q /S _build\%DOCTYPE%
	exit /b 0
)

REM emulate "make <doctype>"
if "%1" != "" (
	set DOCTYPE=%1
)

%BUILDDOC% >NUL 2>NUL
if errorlevel 9009 (
	echo.
	echo.Missing 'BUILDDOC=%BUILDDOC%' - 'sphinx-build':
	echo.- set BUILDDOC to the full path name of 'sphinx-build'
	echo.- add the directory to PATH
	echo.
	exit /b 1
)

%BUILDDOC% -M %DOCTYPE% . _build %BUILDDOCOPTS%
goto end

:help
	echo.
	echo.Makefile for the call of %BUILDDOC%.
	echo.Provides the interface by environment variables:
	echo.- BUILDDOC:     name of build tool, default 'sphinx-build'
	echo.- DOCTYPE:      type of created document, default 'html'
	echo.
	echo.The call additionally supports the pass-through of additional options 
	echo.to the build tool. 
	echo.- BUILDDOCOPTS: options to be appended to the call of name 'BUILDDOC'.
	echo.
	echo.for help on build tool call 'make help-sphinx'
	echo.
	exit /b 0

:help-sphinx
	%BUILDDOC% -M help . _build %BUILDDOCOPTS%
	exit /b 0

:end
popd
