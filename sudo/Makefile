WEBFONTDIR=Webfonts


.PHONY: all
all: $(WEBFONTDIR) SudoVariable.ttf


.PHONY: $(WEBFONTDIR)
$(WEBFONTDIR):
	$(MAKE) -C $@


.PHONY: clean
clean:
	$(MAKE) -C $(WEBFONTDIR) clean


SudoVariable.ttf: ../ttf_ttx/SudoVariable.STAT.avar.ttf
	mv ../ttf_ttx/SudoVariable.STAT.avar.ttf SudoVariable.ttf
	rm -f SudoVariable.ttx
	ttx SudoVariable.ttf
	mv SudoVariable.ttx ../ttf_ttx/SudoVariable.ttx

../ttf_ttx/SudoVariable.STAT.avar.ttf: ../ttf_ttx/SudoVariable.ttx ../ttf_ttx/SudoVariable.STAT.avar.ttx
	ttx -m SudoVariable.ttf ../ttf_ttx/SudoVariable.STAT.avar.ttx
