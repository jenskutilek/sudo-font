WEBFONTDIR=Webfonts
WEBFONTDIR2=Webfonts-Split-VF-Italic


.PHONY: all
all: $(WEBFONTDIR) $(WEBFONTDIR2)


.PHONY: build
build:
	@echo "Build"
	cho


.PHONY: webfonts
webfonts: $(WEBFONTDIR) $(WEBFONTDIR2)


.PHONY: $(WEBFONTDIR)
$(WEBFONTDIR):
	$(MAKE) -C $@


.PHONY: $(WEBFONTDIR2)
$(WEBFONTDIR2):
	$(MAKE) -C $@


.PHONY: clean
clean:
	$(MAKE) -C $(WEBFONTDIR) clean
	$(MAKE) -C $(WEBFONTDIR2) clean


.PHONY: install-debian
install-debian:
	install -m 755 -d $(DESTDIR)$(prefix)/share/fonts/truetype/sudo
	install -m 644 -D *.ttf $(DESTDIR)$(prefix)/share/fonts/truetype/sudo
