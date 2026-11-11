# MenuTitle: Set Special Layer Attributes

from GlyphsApp import Glyphs

wd = Glyphs.font.axes[0].id
wt = Glyphs.font.axes[1].id
desc = Glyphs.font.axes[2].id
xtab = Glyphs.font.axes[3].id
xtra = Glyphs.font.axes[4].id
ita = Glyphs.font.axes[5].id


def set_special_layers(l):
    g = l.parent
    for layer in l.parent.layers:
        if layer.layerId == layer.associatedMasterId:
            continue
        m = g.layers[layer.associatedMasterId]
        print(layer.name, m.name)
        # print("   ", layer.attributes)
        curr_coords = layer.attributes["coordinates"]
        coords = {
            wd: 100,
            wt: curr_coords.get(wt),  # Weight
            desc: curr_coords.get(desc),
            ita: curr_coords.get(ita),
        }
        if m.name == "Regular XTAB0 XTRA1":
            coords[xtab] = 404
            coords[xtra] = 366
        elif m.name == "Regular XTAB1 XTRA0":
            coords[xtab] = 538
            coords[xtra] = 243
        elif m.name == "Regular XTAB0 XTRA0":
            coords[xtab] = 404
            coords[xtra] = 243
        else:
            coords[xtab] = 538
            coords[xtra] = 366
        layer.attributes["coordinates"] = coords


for layer in Glyphs.font.selectedLayers:
    set_special_layers(layer)
