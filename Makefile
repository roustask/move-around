SHELL = /bin/sh
BUILDDIR = build
PDFENGINE = xelatex
MAINFONT = Linux Biolinum

PHASE_1_FILES = \
	Project-plan.pdf \
	Project-description.pdf \
	Team-plan.pdf \
	Risk-assessment.pdf \
	Team-risk-assessment.pdf \
	Feasibility-study.pdf

EXECUTABLES = pandoc pdfunite
K := $(foreach exec,$(EXECUTABLES),\
        $(if $(shell which $(exec)),some string,$(error "No $(exec) in PATH")))

.PHONY: clean
clean:
	-rm -rf $(BUILDDIR)/*

$(PHASE_1_FILES): %.pdf : %.md
	pandoc $< -V mainfont='$(MAINFONT)' -V fontsize=12pt --pdf-engine=$(PDFENGINE) -o $(BUILDDIR)/temp_$@
	pdfunite first-page.pdf $(BUILDDIR)/temp_$@ $(BUILDDIR)/$@
	rm $(BUILDDIR)/temp_$@

.PHONY: phase1
phase1: $(PHASE_1_FILES)
	@echo
	@echo "Build finished!"