WEBFONTDIR=Webfonts


.PHONY: all
all: $(WEBFONTDIR) # SudoVariable.ttf


.PHONY: $(WEBFONTDIR)
$(WEBFONTDIR):
	$(MAKE) -C $@


.PHONY: clean
clean:
	$(MAKE) -C $(WEBFONTDIR) clean


SudoVariable.ttf: ../patch/SudoVariable.STAT.avar.ttf
	mv ../patch/SudoVariable.STAT.avar.ttf SudoVariable.ttf
	rm -f SudoVariable.ttx
	ttx SudoVariable.ttf
	mv SudoVariable.ttx ../ttf_ttx/SudoVariable.ttx

../patch/SudoVariable.STAT.avar.ttf: ../ttf_ttx/SudoVariable.ttx ../patch/SudoVariable.STAT.avar.ttx
	ttx -m SudoVariable.ttf ../patch/SudoVariable.STAT.avar.ttx
