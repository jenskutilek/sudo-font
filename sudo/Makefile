WEBFONTDIR=Webfonts

STYLE_NAMES = Thin ThinItalic Light LightItalic Regular Italic Medium MediumItalic Bold BoldItalic
STYLES = $(patsubst %,$(WEBFONTDIR)/Sudo-%.ttf,$(STYLE_NAMES))


all: $(WEBFONTDIR)


$(WEBFONTDIR):
	$(MAKE) -C $@


clean:
	$(MAKE) -C $(WEBFONTDIR) clean


.PHONY: all clean $(WEBFONTDIR)
