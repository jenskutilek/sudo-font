WOFF_CMD=sfnt2woff-zopfli
WOF2_CMD=woff2_compress

STYLE_NAMES = Thin ThinItalic Light LightItalic Regular Italic Medium MediumItalic Bold BoldItalic
STYLES = $(patsubst %,Sudo-%.ttf,$(STYLE_NAMES))

WOFF = $(STYLES:%.ttf=%.woff)
WOF2 = $(STYLES:%.ttf=%.woff2)

webfonts: woff2 woff

woff: $(WOFF)

woff2: $(WOF2)

%.woff: ../%.ttf
	$(WOFF_CMD) $<
	mv $(basename $<).woff $@

%.woff2: ../%.ttf
	$(WOF2_CMD) $<
	mv $(basename $<).woff2 $@

clean:
	rm -f *.woff
	rm -f *.woff2

.PHONY: clean webfonts woff woff2
