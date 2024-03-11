WOF2_CMD=woff2_compress

STYLES = SudoUIVar-Italic.ttf SudoUIVar-Regular.ttf SudoVar-Italic.ttf SudoVar-Regular.ttf

WOF2 = $(STYLES:%.ttf=%.woff2)


.PHONY: all
all: build


.PHONY: build
build:


.PHONY: clean
clean:
	rm -f *.woff2


.PHONY: webfonts
webfonts: $(WOF2)


%.woff2: ../Split-VF-Italic/%.ttf
	$(WOF2_CMD) $<
	mv $(basename $<).woff2 $@


.PHONY: install-debian
install-debian:
