ARCHIVE = sudo.zip
DISTDIR = dist
FONTDIR = sudo
WEBDIR = ~/Sites/kuti/download/


all: $(FONTDIR) $(DISTDIR)/$(ARCHIVE)


$(FONTDIR):
	$(MAKE) -C $@


$(DISTDIR)/$(ARCHIVE): $(FONTDIR)
	rm -f $(DISTDIR)/$(ARCHIVE)
	zip -r $(DISTDIR)/$(ARCHIVE) $(FONTDIR)/ --exclude "*.DS_Store" "*Makefile"
	if test -e $(WEBDIR); then \
		cp $(DISTDIR)/$(ARCHIVE) $(WEBDIR)/$(ARCHIVE); \
	fi


clean:
	$(MAKE) -C $(FONTDIR) clean


.PHONY: all clean $(FONTDIR)
