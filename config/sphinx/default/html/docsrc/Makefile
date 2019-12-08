#  
# AUTHOR = Arno-Can Uestuensoez
# AUTHOR_EMAIL = acue_sf2@sourceforge.net
# LICENSE = Artistic-License-2.0 + Forced-Fairplay-Constraints
# COPYRIGHT = Copyright (C) 2019 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez
# UUID = 1ba7bffb-c00b-4691-a3e9-e392f968e437
#

#
# *** verified for GNU-Make ***
#


#
# the build tool
#
ifdef $$BUILDDIR
	BUILDDOC = $${BUILDDOC}
else
	BUILDDOC = sphinx-build
endif

#
# optional comand line parameters - for test only
#
BUILDDOCOPTS   = $${BUILDDOCOPTS}


ifdef ${1}
	DOCTYPE = ${1}
else
	ifdef $$DOCTYPE
		DOCTYPE = $${DOCTYPE}
	else
		DOCTYPE = html
	endif
endif


.PHONY: help help-sphinx Makefile clean


# standard target defined by command line or environment parameter
${DOCTYPE}: Makefile
	@$(BUILDDOC) -M $@ "." "_build" $(BUILDDOCOPTS)

# alternative sildcard-target for anything else - whatsoever
%: Makefile
	@$(BUILDDOC) -M $@ "." "_build" $(BUILDDOCOPTS)


clean:	
	rm -rf _build/${DOCTYPE}
	rm -rf _build/doctrees


help:
	@echo
	@echo Makefile for the call of $(BUILDDOC).
	@echo Provides the interface by environment variables:
	@echo - BUILDDOC:     name of build tool, default 'sphinx-build'
	@echo - DOCTYPE:      type of created document, default 'html'
	@echo 
	@echo The call additionally supports the pass-through of additional options 
	@echo to the build tool. 
	@echo - BUILDDOCOPTS: options to be appended to the call of name 'BUILDDOC'.
	@echo 
	@echo The following are intentionally fixed and cannot be modified by parameters:
	@echo
	@echo - BUILDDIR:     name of target directory for build output, constant '_build'
	@echo - DOCSOURCE:    the document source, constant '.'
	@echo 
	@echo for help on build tool call 'make help-sphinx'
	@echo


help-sphinx:
	@$(BUILDDOC) -M help "." "_build" $(BUILDDOCOPTS)

	