WOF2_CMD=woff2_compress

STYLE_NAMES = Thin ThinItalic Light LightItalic Regular Italic Medium MediumItalic Bold BoldItalic
STYLES = $(patsubst %,Sudo-%.ttf,$(STYLE_NAMES))

WOF2 = $(STYLES:%.ttf=%.woff2)


HAVE_WOF2_CMD := $(if $(shell which $(WOF2_CMD)), "", $(warning "WOFF2 command not found: $(WOF2_CMD)"))


.PHONY: all
all: build


.PHONY: build
ifeq ($(HAVE_WOF2_CMD), "")
build: webfonts
	@echo "Running WOFF2 build"
else
build:
endif


.PHONY: clean
clean:
	rm -f *.woff2


ifeq ($(HAVE_WOF2_CMD), "")
.PHONY: webfonts
webfonts: woff2 SudoVariable.woff2 SudoUIVariable.woff2


.PHONY: woff2
woff2: $(WOF2)


%.woff2: ../%.ttf
	$(WOF2_CMD) $<
	mv $(basename $<).woff2 $@


SudoVariable.woff2: ../SudoVariable.ttf
	$(WOF2_CMD) ../SudoVariable.ttf
	mv ../SudoVariable.woff2 .


SudoUIVariable.woff2: ../SudoUIVariable.ttf
	$(WOF2_CMD) ../SudoUIVariable.ttf
	mv ../SudoUIVariable.woff2 .
endif


.PHONY: install-debian
install-debian:
