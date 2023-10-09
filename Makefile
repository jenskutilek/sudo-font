ARCHIVE = sudo.zip
DISTDIR = dist
FONTDIR = sudo


.PHONY: all
all: build dist # update_version


.PHONY: build
build: $(FONTDIR)


.PHONY: clean
clean:
	$(MAKE) -C $(FONTDIR) clean


.PHONY: dist
dist: $(DISTDIR)/$(ARCHIVE)


.PHONY: $(FONTDIR)
$(FONTDIR):
	$(MAKE) -C $@


$(DISTDIR)/$(ARCHIVE): $(FONTDIR)
	if test -e $(DISTDIR); then \
		rm -f $(DISTDIR)/$(ARCHIVE); \
	else \
		mkdir $(DISTDIR); \
	fi
	zip -r $(DISTDIR)/$(ARCHIVE) $(FONTDIR)/ --exclude "*.DS_Store" "*Makefile"


.PHONY: install-debian
install-debian:
	install -m 644 -Dt $(prefix)/share/fonts/truetype/sudo
