# MenuTitle: Update “Rename Glyphs” Custom Parameters

from GlyphsApp import Glyphs, GSCustomParameter

all_names = [g.name for g in Glyphs.font.glyphs]
ss20_names = [name for name in all_names if ".ss20" in name]
ital_names = [name for name in all_names if ".italic" in name]
zero_names = [name for name in all_names if ".zero" in name]
ss20_pairs = []
ital_pairs = []
zero_pairs = []


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


for zero_name in zero_names:
    default_name = zero_name.replace(".zero", "")
    if default_name not in all_names:
        print("Missing default glyph for slashed zero glyph:", default_name)
        continue
    zero_pairs.append((default_name, zero_name))


def addSRenameParams(
    i, rename_ss20_pairs, rename_italic_pairs=[], rename_zero_pairs=[]
):
    del_cp = []
    for n, cp in enumerate(i.customParameters):
        if cp.name == "Rename Glyphs":
            del_cp.append(n)
    for n in sorted(del_cp, reverse=True):
        del i.customParameters[n]
    pairs = []

    if rename_ss20_pairs:
        pairs.extend(rename_ss20_pairs)
    if rename_italic_pairs:
        pairs.extend(rename_italic_pairs)
    if rename_zero_pairs:
        pairs.extend(rename_zero_pairs)
    if pairs:
        cp = GSCustomParameter(
            "Rename Glyphs",
            "\n".join([f"{pair[0]}={pair[1]}" for pair in pairs]),
        )
        i.customParameters.append(cp)


uivar = Glyphs.font.instances[0]  # Sudo UI Var
addSRenameParams(uivar, ss20_pairs, rename_zero_pairs=zero_pairs)

for n in (7, 8, 9, 10, 11):
    si = Glyphs.font.instances[n]  # Mono Italics
    addSRenameParams(si, [], ital_pairs)

for n in (12, 13, 14, 15, 16):
    si = Glyphs.font.instances[n]  # UI Romans
    addSRenameParams(si, ss20_pairs, rename_zero_pairs=zero_pairs)

for n in (17, 18, 19, 20, 21):
    si = Glyphs.font.instances[n]  # UI Italics
    addSRenameParams(si, ss20_pairs, ital_pairs, rename_zero_pairs=zero_pairs)
