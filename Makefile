ARCHIVE = sudo.zip
DISTDIR = dist
FONTDIR = sudo


all: $(FONTDIR) $(DISTDIR)/$(ARCHIVE)


$(FONTDIR):
	$(MAKE) -C $@


$(DISTDIR)/$(ARCHIVE): $(FONTDIR)
	rm -f $(DISTDIR)/$(ARCHIVE)
	zip -r $(DISTDIR)/$(ARCHIVE) $(FONTDIR)/ --exclude \*.DS_Store Makefile
	mv ~/Sites/kuti/download/sudo.zip ~/Sites/kuti/download/sudo_old.zip
	cp $(DISTDIR)/$(ARCHIVE) ~/Sites/kuti/download/sudo.zip


clean:
	$(MAKE) -C $(FONTDIR) clean


.PHONY: all clean $(FONTDIR)
