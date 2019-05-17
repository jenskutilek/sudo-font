WOFF_CMD=sfnt2woff-zopfli
WOF2_CMD=woff2_compress

# Build the webfonts and pack them
dist: webfonts zip

# Build the webfonts
webfonts: webfont-thin webfont-thinitalic

webfont-thin: sudo/Sudo-Thin.ttf
	cp "sudo/Sudo-Thin.ttf" "sudo/Web Fonts/SudoWeb-Thin.ttf"
	$(WOFF_CMD) "sudo/Web Fonts/SudoWeb-Thin.ttf"
	$(WOF2_CMD) "sudo/Web Fonts/SudoWeb-Thin.ttf"

webfont-thinitalic: sudo/Sudo-ThinItalic.ttf
	cp "sudo/Sudo-ThinItalic.ttf" "sudo/Web Fonts/SudoWeb-ThinItalic.ttf"
	$(WOFF_CMD) "sudo/Web Fonts/SudoWeb-ThinItalic.ttf"
	$(WOF2_CMD) "sudo/Web Fonts/SudoWeb-ThinItalic.ttf"

# msgfmt $$font -o ./sudo/Web\ Fonts/$${font/Sudo/SudoWeb}; \
# Pack all fonts
# zip:
# 	rm ../dist/sudo.zip
# 	cd ..
# 	zip -r dist/sudo.zip sudo/ --exclude \*.DS_Store
# 	mv ~/Sites/kuti/download/sudo.zip ~/Sites/kuti/download/sudo_old.zip
# 	cp dist/sudo.zip ~/Sites/kuti/download/
