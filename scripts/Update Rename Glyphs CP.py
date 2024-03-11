# MenuTitle: Update “Rename Glyphs” Custom Parameters

from GlyphsApp import Glyphs, GSCustomParameter

all_names = [g.name for g in Glyphs.font.glyphs]
ss20_names = [name for name in all_names if ".ss20" in name]
ital_names = [name for name in all_names if ".italic" in name]
ss20_pairs = []
ital_pairs = []

for ss20_name in ss20_names:
    default_name = ss20_name.replace(".ss20", "")
    if default_name not in all_names:
        print("Missing default glyph for SS20 glyph:", default_name)
        continue
    ss20_pairs.append((default_name, ss20_name))

for ital_name in ital_names:
    default_name = ital_name.replace(".italic", "")
    if default_name not in all_names:
        print("Missing default glyph for italic glyph:", default_name)
        continue
    ital_pairs.append((default_name, ital_name))


def addSRenameParams(i, rename_ss20_pairs, rename_italic_pairs=[]):
    del_cp = []
    for n, cp in enumerate(i.customParameters):
        if cp.name == "Rename Glyphs":
            del_cp.append(n)
    for n in sorted(del_cp, reverse=True):
        del i.customParameters[n]

    if rename_ss20_pairs:
        cp = GSCustomParameter(
            "Rename Glyphs",
            "\n".join([f"{pair[0]}={pair[1]}" for pair in rename_ss20_pairs]),
        )
        i.customParameters.append(cp)

    if rename_italic_pairs:
        cp = GSCustomParameter(
            "Rename Glyphs",
            "\n".join([f"{pair[0]}={pair[1]}" for pair in rename_italic_pairs]),
        )
        i.customParameters.append(cp)


uivar = Glyphs.font.instances[0]  # Sudo UI Var
addSRenameParams(uivar, ss20_pairs)

for n in (10, 11, 12, 13, 14):
    si = Glyphs.font.instances[n]  # Mono Italics
    addSRenameParams(si, [], ital_pairs)

for n in (15, 16, 17, 18, 19):
    si = Glyphs.font.instances[n]  # UI Romans
    addSRenameParams(si, ss20_pairs)

for n in (20, 21, 22, 23, 24):
    si = Glyphs.font.instances[n]  # UI Italics
    addSRenameParams(si, ss20_pairs, ital_pairs)
