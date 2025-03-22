# MenuTitle: Build Production Sources
from pathlib import Path

from GlyphsApp import VARIABLE, Glyphs, GSClass

__doc__ = (
    "Split the design source Glyphs file into separate production source "
    "Glyphs files, Sudo.glyphspackage and SudoUI.glyphspackage, and save them"
    "in the sources directory. The script must be run inside Glyphs while the design "
    "source (/sources-design/Sudo.glyphspackage) is open."
)


def collect_and_delete_glyphs(f, name):
    delete_glyphs = []
    for g in f.glyphs:
        if name in g.name:
            delete_glyphs.append(g.name)
        for layer in g.layers:
            for c in layer.components:
                if name in c.componentName:
                    c.decompose()
    for name in delete_glyphs:
        del f.glyphs[name]


def collect_and_switch_glyphs(f, name):
    # print(f"collect_and_switch_glyphs: {name}")
    replace_names = {}
    for g in f.glyphs:
        if name in g.name:
            target_name = g.name.replace(name, "")
            replace_names[g.name] = target_name
            if target_name in f.glyphs.keys():
                dead_name = f"{target_name}.kill"
                replace_names[target_name] = dead_name
    actual_renamed = {}
    for g in f.glyphs:
        if g.name in replace_names:
            target_name = replace_names[g.name]
            i = 1
            while target_name in f.glyphs.keys():
                target_name = f"{replace_names[g.name]}.{i}"
                i += 1
            # print(f"    {g.name} -> {target_name}")
            actual_renamed[g.name] = target_name
            g.name = target_name
    for g in f.glyphs:
        for l in g.layers:
            for c in l.components:
                if c.componentName in actual_renamed:
                    c.componentName = actual_renamed[c.componentName]
    # collect_and_delete_glyphs(f, ".kill")
    disable_glyphs_by_name(f, ".kill")
    for g in f.glyphs:
        g.updateGlyphInfo()


def delete_italic_exports(f):
    delete = []
    for i, export in enumerate(f.instances):
        if "Italic" in export.name:
            delete.append(i)
    for i in sorted(delete, reverse=True):
        del f.instances[i]


def delete_roman_exports(f):
    delete = []
    for i, export in enumerate(f.instances):
        if "Italic" not in export.name:
            delete.append(i)
    for i in sorted(delete, reverse=True):
        del f.instances[i]


def delete_masters(f, master_indexes):
    for master_index in sorted(master_indexes, reverse=True):
        del f.masters[master_index]


def disable_glyphs_by_name(f, name):
    for g in f.glyphs:
        if name in g.name:
            g.export = False


def disable_cp(f, name):
    # Disable export-level custom parameters by name
    for export in f.instances:
        for cp in export.customParameters:
            if cp.name == name:
                cp.active = False


def disable_cps(f, names):
    # Disable export-level custom parameters by name
    for name in names:
        disable_cp(f, name)


def disable_feature(f, tag):
    for feature in f.features:
        if feature.name == tag:
            feature.active = False


def disable_features(f, tags):
    for tag in tags:
        disable_feature(f, tag)


def disable_font_cps(f, names):
    # Disable font-level custom parameters by name
    for name in names:
        disable_font_cp(f, name)


def disable_font_cp(f, name):
    # Disable font-level custom parameters by name
    for cp in f.customParameters:
        if cp.name == name:
            cp.active = False


def disable_export_settings(f):
    for export in f.instances:
        if export.type == VARIABLE:
            export.active = False
        elif export.familyName == "Sudo UI":
            export.active = False


def add_and_save_font(source_font, f, file_name):
    Glyphs.fonts.append(f)
    font_path = Path(source_font.filepath).parent.parent / "sources" / file_name
    print(f"Saving file to {font_path}")
    f.save(str(font_path), formatVersion=3)


def remove_width_classes(f):
    # Remove any existing classes
    old_classes = [i for i, c in enumerate(f.classes) if c.name.startswith("width_")]
    for i in sorted(old_classes, reverse=True):
        del f.classes[i]


def update_width_classes(f):
    remove_width_classes(f)
    # Add new classes
    width_classes = {}

    for glyph in f.glyphs:
        if glyph.name in ("ordfeminine", "ordmasculine"):
            continue
        if ".ss20" in glyph.name or ".sups" in glyph.name:
            continue
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

    rclt_code = ""
    for w in sorted(width_classes):
        f.classes.append(GSClass(f"width_{w}", "\n".join(sorted(width_classes[w]))))
        rclt_code += f"sub @width_{w} lowlinecomb' by lowlinecomb.{w};\n"

    found_rclt = False
    for fea in f.features:
        if fea.tag() == "rclt":
            fea.code = rclt_code
            found_rclt = True
    if not found_rclt:
        print(f"Could not find rclt feature to update in {f}")


# Each source's configuration


def build_mono_roman(design_source):
    f = design_source.copy()
    collect_and_delete_glyphs(f, ".ss20")
    # disable_glyphs_by_name(f, "lowlinecomb.")
    remove_width_classes(f)
    disable_font_cps(f, ("glyphOrder",))
    disable_cps(
        f, ("Remove Features", "Remove Glyphs", "Replace Feature", "Rename Glyphs")
    )
    disable_features(f, ("rlig",))
    disable_export_settings(f)
    f.updateFeatures()
    f.kerning.clear()
    add_and_save_font(design_source, f, "Sudo.glyphspackage")


def build_prop_roman(design_source):
    f = design_source.copy()
    collect_and_switch_glyphs(f, ".ss20")
    disable_font_cps(f, ("glyphOrder", "postscriptIsFixedPitch"))
    disable_cps(
        f, ("Remove Features", "Remove Glyphs", "Replace Feature", "Rename Glyphs")
    )
    disable_features(f, ("rlig",))
    disable_export_settings(f)
    update_width_classes(f)
    f.updateFeatures()
    add_and_save_font(design_source, f, "SudoUI.glyphspackage")


f = Glyphs.font
build_mono_roman(f)
build_prop_roman(f)
