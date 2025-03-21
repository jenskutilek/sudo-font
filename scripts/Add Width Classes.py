# MenuTitle: Add Width Classes

__doc__ = (
    "Add glyph classes to the current font that are used to contextually substitute a "
    "matching alternate of lowlinecomb"
)

from GlyphsApp import Glyphs, GSClass

# Remove any existing classes
old_classes = [
    i for i, c in enumerate(Glyphs.font.classes) if c.name.startswith("width_")
]
for i in sorted(old_classes, reverse=True):
    del Glyphs.font.classes[i]

# Add new classes
width_classes = {}

for glyph in Glyphs.font.glyphs:
    if not glyph.export:
        continue
    if glyph.category != "Letter":
        continue
    w = int(glyph.layers[0].width)
    if w == 448:
        continue
    if w not in width_classes:
        width_classes[w] = set()
    width_classes[w].add(glyph.name)

for w in sorted(width_classes):
    Glyphs.font.classes.append(
        GSClass(f"width_{w}", "\n".join(sorted(width_classes[w])))
    )
