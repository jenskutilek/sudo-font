WOF2_CMD=woff2_compress

STYLE_NAMES = Thin ThinItalic Light LightItalic Regular Italic Medium MediumItalic Bold BoldItalic
STYLES = $(patsubst %,Sudo-%.ttf,$(STYLE_NAMES)) $(patsubst %,SudoUI-%.ttf,$(STYLE_NAMES)) SudoVariable.ttf SudoUIVariable.ttf

WOF2 = $(STYLES:%.ttf=%.woff2)


.PHONY: all
all: build


.PHONY: build
build: webfonts
	@echo "Running WOFF2 build"


.PHONY: clean
clean:
	rm -f *.woff2


.PHONY: webfonts
webfonts: woff2


.PHONY: woff2
woff2: $(WOF2)


%.woff2: ../%.ttf
	$(WOF2_CMD) $<
	mv $(basename $<).woff2 $@


.PHONY: install-debian
install-debian:
