# The Sudo font family

[![][Fontbakery]](https://jenskutilek.github.io/sudo-font.git/fontbakery/fontbakery-report.html)
[![][Universal]](https://jenskutilek.github.io/sudo-font.git/fontbakery/fontbakery-report.html)
[![][GF Profile]](https://jenskutilek.github.io/sudo-font.git/fontbakery/fontbakery-report.html)
[![][Shaping]](https://jenskutilek.github.io/sudo-font.git/fontbakery/fontbakery-report.html)

[Fontbakery]: https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fjenskutilek%2Fsudo-font.git%2Fgh-pages%2Fbadges%2Foverall.json
[GF Profile]: https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fjenskutilek%2Fsudo-font.git%2Fgh-pages%2Fbadges%2FGoogleFonts.json
[Outline Correctness]: https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fjenskutilek%2Fsudo-font.git%2Fgh-pages%2Fbadges%2FOutlineCorrectnessChecks.json
[Shaping]: https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fjenskutilek%2Fsudo-font.git%2Fgh-pages%2Fbadges%2FShapingChecks.json
[Universal]: https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fjenskutilek%2Fsudo-font.git%2Fgh-pages%2Fbadges%2FUniversal.json

<img src="https://raw.github.com/jenskutilek/sudo-font/master/images/sudo-monospaced-ui-font.png">

Sudo is a font designed for terminals, programming, and user interfaces. Use at 16 pixels size for optimal results. It has a monospaced variant, simply called _Sudo,_ and a proportional variant, called _Sudo UI._ A Variable Font version is available. It has an extra variation axis to modify the length of descenders.

Sudo decidedly has no ligatures, but supports all common [Powerline](https://github.com/powerline/powerline) glyphs out of the box.

Find out more about the fonts at https://www.kutilek.de/sudo-font/ or download the [latest release](https://github.com/jenskutilek/sudo-font/releases/latest/download/sudo.zip).

<img src="https://raw.github.com/jenskutilek/sudo-font/master/images/sudo.png">

<img src="https://raw.github.com/jenskutilek/sudo-font/master/images/sudo-textmate-py.png">

Sudo Regular and Bold in TextMate

<img src="https://raw.github.com/jenskutilek/sudo-font/master/images/sudo-light-powerline.png">

Sudo Light in vim on macOS with [Powerline](https://github.com/powerline/powerline)


## About

Sudo was designed by [Jens Kutílek](https://www.kutilek.de/), a graphic and type designer and font engineer based in Berlin.


## Installation


### Arch Linux

Sudo is available in the [Arch User Repository](https://wiki.archlinux.org/index.php/Arch_User_Repository) as [ttf-sudo](https://aur.archlinux.org/packages/ttf-sudo).


### Debian and Ubuntu Linux

You can use my private apt repository to install and update the fonts.

See the [Debian README](README-Debian.md) for details.

### FreeBSD

Sudo is available in the FreeBSD Ports Collection.

```sh
pkg install sudo-font
```

### macOS

Download the [latest release](https://github.com/jenskutilek/sudo-font/releases/latest/download/sudo.zip) and copy the TTF files into `/Library/Fonts` or `~/Library/Fonts`.

Sudo is also available as a [Homebrew](https://brew.sh/) package.

```sh
brew install --cask font-sudo
```


## Building

If you want to modify the fonts, be aware that unlike in most in other font projects, this is a two-part process.

Any design changes should be made in the main design file `sources-design/Sudo.glyphspackage`, which contains both the monospaced (Sudo) and proportional (Sudo UI) subfamilies including Italics in one file.

To prepare the production sources in the `sources` directory, run the script `scripts/Build Production Sources.py` **inside Glyphs** while the design source file is open. This will split the design source file into two files, one for the monospaced and one for the proportional family, and save them in the `sources` directory.

The fonts are built from the sources in `sources` automatically by GitHub Actions - take a look in the "Actions" tab for the latest build.

If you want to build the fonts manually on your own computer:

* `make build` will produce font files.
* `make test` will run [FontBakery](https://github.com/googlefonts/fontbakery)'s quality assurance tests.
* `make proof` will generate HTML proof files.

The proof files and QA tests are also available automatically via GitHub Actions - look at https://jenskutilek.github.io/sudo-font.git.


## Changelog

See [FONTLOG](sudo/FONTLOG.txt).


## License

This Font Software is licensed under the SIL Open Font License, Version 1.1.
This license is available with a FAQ at
https://scripts.sil.org/OFL


## Repository Layout

This font repository structure is inspired by [Unified Font Repository v0.3](https://github.com/unified-font-repository/Unified-Font-Repository), modified for the Google Fonts workflow.
