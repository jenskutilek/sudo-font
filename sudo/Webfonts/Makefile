WOF2_CMD=woff2_compress

STYLES = SudoVariable.ttf SudoUIVariable.ttf

WOF2 = $(STYLES:%.ttf=%.woff2)


.PHONY: all
all: webfonts


.PHONY: build
build:


.PHONY: clean
clean:
	rm -f *.woff2


.PHONY: webfonts
webfonts: $(WOF2)


%.woff2: ../%.ttf
	$(WOF2_CMD) $<
	mv $(basename $<).woff2 $@


.PHONY: install-debian
install-debian:
