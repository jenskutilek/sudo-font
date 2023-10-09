WOF2_CMD=woff2_compress

STYLE_NAMES = Thin ThinItalic Light LightItalic Regular Italic Medium MediumItalic Bold BoldItalic
STYLES = $(patsubst %,Sudo-%.ttf,$(STYLE_NAMES))

WOF2 = $(STYLES:%.ttf=%.woff2)


.PHONY: all
all: build


.PHONY: build
build: webfonts


.PHONY: clean
clean:
	rm -f *.woff2


.PHONY: check-woff2-support
check-woff2-support:
ifeq (, $(shell which $(WOF2_CMD)))
	$(warning "WOFF2 command not found: $(WOF2_CMD)")
else
	HAVE_WOF2_CMD = true
endif


.PHONY: webfonts
webfonts: check-woff2-support woff2 SudoVariable.woff2 SudoUIVariable.woff2


.PHONY: woff
woff: $(WOFF)


.PHONY: woff2
woff2: $(WOF2)


%.woff2: ../%.ttf
ifdef HAVE_WOF2_CMD
	$(WOF2_CMD) $<
	mv $(basename $<).woff2 $@
endif


SudoVariable.woff2: ../SudoVariable.ttf
ifdef HAVE_WOF2_CMD
	$(WOF2_CMD) ../SudoVariable.ttf
	mv ../SudoVariable.woff2 .
endif


SudoUIVariable.woff2: ../SudoUIVariable.ttf
ifdef HAVE_WOF2_CMD
	$(WOF2_CMD) ../SudoUIVariable.ttf
	mv ../SudoUIVariable.woff2 .
endif


.PHONY: install-debian
install-debian:
