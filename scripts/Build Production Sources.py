# MenuTitle: Build Production Sources
from pathlib import Path

from GlyphsApp import Glyphs

__doc__ = (
    "Split the design source Glyphs file into separate production source "
    "Glyphs files: Sudo Mono Roman, Sudo Mono Italic, Sudo UI Roman, "
    "Sudo UI Italic, and save them next to the original Glyphs file."
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
    all_glyph_names = set(f.glyphs.keys())
    replace_names = {}
    # kill_names = {}
    for g in f.glyphs:
        if name in g.name:
            target_name = g.name.replace(name, "")
            replace_names[g.name] = target_name
            if target_name in all_glyph_names:
                dead_name = f"{target_name}.kill"
                replace_names[target_name] = dead_name
                # kill_names[dead_name] = target_name
    for g in f.glyphs:
        if g.name in replace_names:
            g.name = replace_names[g.name]
            g.updateGlyphInfo()
        for l in g.layers:
            for c in l.components:
                if c.componentName in replace_names:
                    c.componentName = replace_names[c.componentName]
    # print(kill_names)
    # print(replace_names)
    # collect_and_delete_glyphs(f, ".kill")
    disable_glyphs_by_name(f, ".kill")


def disable_glyphs_by_name(f, name):
    for g in f.glyphs:
        if name in g.name:
            g.export = False


def add_and_save_font(source_font, f, suffix):
    Glyphs.fonts.append(f)
    font_path = Path(source_font.filepath).with_suffix(suffix)
    f.save(str(font_path), formatVersion=3)


def build_mono_roman(design_source):
    f = design_source.copy()
    collect_and_delete_glyphs(f, ".ss20")
    collect_and_delete_glyphs(f, ".italic")
    f.updateFeatures()
    f.kerning.clear()
    add_and_save_font(design_source, f, ".mr.glyphspackage")


def build_mono_italic(design_source):
    f = design_source.copy()
    collect_and_delete_glyphs(f, ".ss20")
    collect_and_switch_glyphs(f, ".italic")
    f.updateFeatures()
    f.kerning.clear()
    add_and_save_font(design_source, f, ".mi.glyphspackage")


def build_prop_roman(design_source):
    f = design_source.copy()
    collect_and_switch_glyphs(f, ".ss20")
    collect_and_delete_glyphs(f, ".italic")
    f.updateFeatures()
    add_and_save_font(design_source, f, ".pr.glyphspackage")


def build_prop_italic(design_source):
    f = design_source.copy()
    collect_and_switch_glyphs(f, ".ss20")
    collect_and_switch_glyphs(f, ".italic")
    f.updateFeatures()
    add_and_save_font(design_source, f, ".pi.glyphspackage")


f = Glyphs.font
# build_mono_roman(f)
# build_mono_italic(f)
build_prop_roman(f)
# build_prop_italic(f)
