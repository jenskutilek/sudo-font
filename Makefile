ARCHIVE = sudo.zip
DISTDIR = dist
FONTDIR = sudo
WEBDIR = ~/Sites/kuti/_site/download/
WEBPAGE = ~/Sites/kuti/src/sudo-font/index.html


.PHONY: all
all: $(FONTDIR) $(DISTDIR)/$(ARCHIVE) update_version


.PHONY: $(FONTDIR)
$(FONTDIR):
	$(MAKE) -C $@


$(DISTDIR)/$(ARCHIVE): $(FONTDIR)
	rm -f $(DISTDIR)/$(ARCHIVE)
	zip -r $(DISTDIR)/$(ARCHIVE) $(FONTDIR)/ --exclude "*.DS_Store" "*Makefile"
	if test -e $(WEBDIR); then \
		cp $(DISTDIR)/$(ARCHIVE) $(WEBDIR)/$(ARCHIVE); \
	fi


.PHONY: clean
clean:
	$(MAKE) -C $(FONTDIR) clean


.PHONY: update_version
update_version: zip_size := $(shell du -h $(DISTDIR)/$(ARCHIVE) | awk '{ sub(",", "."); print $$1"B"; }')
update_version: sudo_version := $(shell git describe --tags)
update_version:
	sed -E "s/(Download Sudo )v[0-9\.]+( for free.<\/a> \()[0-9]+[0-9\.]+ ?[A-Za-z]+( zip file)/\1$(sudo_version)\2$(zip_size)\3/" $(WEBPAGE) \
	> $(WEBPAGE).tmp \
	&& mv $(WEBPAGE).tmp $(WEBPAGE)
