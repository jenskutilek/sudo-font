# Sudo Design Source

This directory contains the main design source file (actually a folder structure) containing both the Sudo and Sudo UI font families.

It can be exported from Glyphs as-is, but when you want to build the fonts with `gftools` outside of Glyphs, you must split the design source into two production source files that reside in the `../sources` directory.

To split the source, open `Sudo.glyphspackage` from this directory in Glyphs, and run the script `../scripts/Build Production Sources.py` in Glyphs. This will split the source, apply some changes, and save the two production sources, `Sudo.glyphspackage` and `SudoUI.glyphspackage`, in the `../sources` directory.

## Exporting Directly From Glyphs

### Variable Fonts

There are two Variable Font Settings in the Glyphs file that control the export. To get identical results to the official fonts in this repository (in `../sudo/`), a post-processing script is run by Glyphs, which is not publicly available. The script

- Merges the `STAT` and `cvar` tables from `../ttx-patch/SudoVariable.cvar.ttx` into the font.
- Sets different vertical metrics for the Sudo UI font family (a bug in Glyphs prevented applying the different metrics, TBD: check if it is fixed now)
- Sets the `gasp` table in a more granular way than Glyphs can


### Static Fonts

TODO or don't we need them anymore ...?