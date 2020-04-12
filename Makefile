SHELL = /bin/sh
BUILDDIR = build
PDFENGINE = xelatex
MAINFONT = Linux Biolinum

PHASE_1_FILES = \
	Project-plan-v0.1.pdf \
	Project-description-v0.1.pdf \
	Team-plan-v0.1.pdf \
	Risk-assessment-v0.1.pdf \
	Team-risk-assessment-v0.1.pdf \
	Feasibility-study-v0.1.pdf

PHASE_2_FILES = \
	Domain-model-v0.1.pdf \
	Use-cases-v0.1.pdf

PHASE_2_FILES_REV = \
	Project-description-v0.2.pdf \
	Team-risk-assessment-v0.2.pdf \
	Risk-assessment-v0.2.pdf 

EXECUTABLES = pandoc
K := $(foreach exec,$(EXECUTABLES),\
        $(if $(shell which $(exec)),some string,$(error "No $(exec) in PATH")))

.PHONY: clean
clean:
	-rm -rf $(BUILDDIR)/*

$(PHASE_1_FILES): %-v0.1.pdf : %.md
	pandoc $< --metadata-file=misc/metadata.yaml -V mainfont='$(MAINFONT)' -V fontsize=12pt --pdf-engine=$(PDFENGINE) -o $(BUILDDIR)/$@

$(PHASE_2_FILES): %-v0.1.pdf : %.md
	pandoc $< --metadata-file=misc/metadata.yaml -V mainfont='$(MAINFONT)' -V fontsize=12pt --pdf-engine=$(PDFENGINE) -o $(BUILDDIR)/$@

$(PHASE_2_FILES_REV): %-v0.2.pdf : %.md
	pandoc $< --metadata-file=misc/metadata.yaml -V mainfont='$(MAINFONT)' -V fontsize=12pt --pdf-engine=$(PDFENGINE) -o $(BUILDDIR)/$@

.PHONY: phase-1
phase-1: $(PHASE_1_FILES)
	@echo
	@echo "Build finished!"

.PHONY: phase-1-zip
phase-1-zip: $(PHASE_1_FILES)
	zip -r $(BUILDDIR)/software-engineering-2020.zip $(addprefix $(BUILDDIR)/, $(PHASE_1_FILES))
	@echo
	@echo "Build finished!"

.PHONY: phase-2
phase-2: $(PHASE_2_FILES) $(PHASE_2_FILES_REV)
	@echo
	@echo "Build finished!"

.PHONY: phase-2-zip
phase-2-zip: $(PHASE_2_FILES) $(PHASE_2_FILES_REV)
	zip -r $(BUILDDIR)/software-engineering-2020.zip $(addprefix $(BUILDDIR)/, $(PHASE_2_FILES))
	@echo
	@echo "Build finished!"