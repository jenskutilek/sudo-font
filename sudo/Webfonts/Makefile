WOFF_CMD=sfnt2woff
WOF2_CMD=woff2_compress

STYLE_NAMES = Thin ThinItalic Light LightItalic Regular Italic Medium MediumItalic Bold BoldItalic
STYLES = $(patsubst %,Sudo-%.ttf,$(STYLE_NAMES))

WOFF = $(STYLES:%.ttf=%.woff)
WOF2 = $(STYLES:%.ttf=%.woff2)

.PHONY: webfonts
webfonts: woff2 woff SudoVariable.woff2 SudoUIVariable.woff2

.PHONY: woff
woff: $(WOFF)

.PHONY: woff2
woff2: $(WOF2)

%.woff: ../%.ttf
	$(WOFF_CMD) $<
	mv $(basename $<).woff $@

%.woff2: ../%.ttf
	$(WOF2_CMD) $<
	mv $(basename $<).woff2 $@

SudoVariable.woff2: ../SudoVariable.ttf
	$(WOF2_CMD) ../SudoVariable.ttf
	mv ../SudoVariable.woff2 .

SudoUIVariable.woff2: ../SudoUIVariable.ttf
	$(WOF2_CMD) ../SudoUIVariable.ttf
	mv ../SudoUIVariable.woff2 .

.PHONY: clean
clean:
	rm -f *.woff
	rm -f *.woff2
