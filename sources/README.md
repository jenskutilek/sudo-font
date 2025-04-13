
# Sudo Production Sources

This directory contains the two source files (actually folder structures) from which both font families, Sudo and Sudo UI, will be built.

Any design changes should be done in the design source in the `../sources-design` directory. Please refer to the [README](../sources-design/README.md) there for how to update the production sources.

You can either export the fonts directly from Glyphs, or using the Google Fonts build chain with `gftools`.

## Exporting Directly From Glyphs

The production sources are set up so that the fonts can be built out of the box with `gftools`. If you want to export the fonts manually from Glyphs, you must change the export settings:

- If you want to match the glyph order, under _Font,_ activate the _Custom Parameter_ “glyphOrder”.
- Make sure that under _Exports,_ the last 10 instances starting with “Sudo UI” are not active.
- Activate the appropriate _Variable Font Setting_ in each respective source.
- In each source’s _Variable Font Setting,_, activate those _Custom Parameters:_
  - _Remove Features_
  - _Remove Glyphs_
- Under _Features,_ activate the `rlig` feature.

### Variable Fonts

There are two Variable Font Settings in the Glyphs file that control the export. To get identical results to the official fonts in this repository (in `../sudo/`), a post-processing script is run by Glyphs, which is not publicly available. The script

- Merges the `STAT` and `cvar` tables from `../ttx-patch/SudoVariable.cvar.ttx` into the font.
- Sets different vertical metrics for the Sudo UI font family (a bug in Glyphs prevented applying the different metrics, TBD: check if it is fixed now)
- Sets the `gasp` table in a more granular way than Glyphs can

### Static Fonts

The static TTF fonts in the releases are exported from Glyphs 3.1.2, also with some post-processing to fix some bugs, especially in the TrueType hinting (screen optimization).

#### Sudo

- For each instance, activate those _Custom Parameters:_
  - _Remove Features_
  - _Remove Glyphs_
  - _Remove Classes_
- In each Italic instance, activate the _Rename Glyphs_ _Custom Parameter._

#### Sudo UI

You must activate the last 10 instances under _Exports,_ starting with “Sudo UI”, before exporting, and deactivate the other instances.

- For each instance, activate those _Custom Parameters:_
  - _Remove Features_
- In each Italic instance, activate the _Rename Glyphs_ _Custom Parameter._
