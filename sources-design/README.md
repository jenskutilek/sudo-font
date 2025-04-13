# Sudo Design Source

This directory contains the main design source file (actually a folder structure) containing both the Sudo and Sudo UI font families.

In theory, you could export this from Glyphs as-is, but alas, the trickery in the Glyphs file is too strong, and when you export from the full source file, the spacing and alignment of some of the proportional glyphs will be broken.

So it is recommended (and for a build with `gftools` outside Glyphs it is required) that you split the design source into the two production source files that reside in the `../sources` directory.

To split the source, open `Sudo.glyphspackage` from this directory in Glyphs, and run the script `../scripts/Build Production Sources.py` in Glyphs. This will split the source, apply some changes, and save the two production sources, `Sudo.glyphspackage` and `SudoUI.glyphspackage`, in the `../sources` directory.

Please continue with the [README](../sources/README.md) there.
