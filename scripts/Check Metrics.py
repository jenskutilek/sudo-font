# MenuTitle: Check Metrics

xtab1_xtra1 = Glyphs.font.masters[0].id
xtab0_xtra1 = Glyphs.font.masters[1].id
xtab1_xtra0 = Glyphs.font.masters[2].id
xtab0_xtra0 = Glyphs.font.masters[3].id

for g in Glyphs.font.glyphs:
    if g.layers[xtab1_xtra1].width != g.layers[xtab1_xtra0].width:
        print(g.name)
    if g.layers[xtab0_xtra1].width != g.layers[xtab0_xtra0].width:
        print(g.name)
    for layer in g.layers:
        for mid in (xtab1_xtra1, xtab0_xtra1, xtab1_xtra0, xtab0_xtra0):
            if layer.associatedMasterId == mid and g.layers[mid].width != layer.width:
                print(g.name)
