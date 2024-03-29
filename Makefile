ARCHIVE = sudo.zip
DISTDIR = dist
FONTDIR = sudo
prefix = /usr/local

.PHONY: all
all: build


.PHONY: build
build: $(FONTDIR)


.PHONY: clean
clean:
	$(MAKE) -C $(FONTDIR) clean


.PHONY: dist
dist: webfonts $(DISTDIR)/$(ARCHIVE)


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
	$(MAKE) -C $(FONTDIR) install-debian


.PHONY: webfonts
webfonts:
	$(MAKE) -C $(FONTDIR) webfonts
