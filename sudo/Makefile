WEBFONTDIR=Webfonts


.PHONY: all
all: $(WEBFONTDIR)


.PHONY: build
build:
	@echo "Build"
	cho


.PHONY: webfonts
webfonts: $(WEBFONTDIR)


.PHONY: $(WEBFONTDIR)
$(WEBFONTDIR):
	$(MAKE) -C $@


.PHONY: clean
clean:
	$(MAKE) -C $(WEBFONTDIR) clean


.PHONY: install-debian
install-debian:
	install -m 755 -d $(DESTDIR)$(prefix)/share/fonts/truetype/sudo
	install -m 644 -D *.ttf $(DESTDIR)$(prefix)/share/fonts/truetype/sudo
