from pathlib import Path

from GlyphsApp import INSTANCETYPEVARIABLE, TTF, VARIABLE, Glyphs, GSCustomParameter

sources_path = Path.home() / "Documents" / "Schriften" / "Sudo" / "sources"


def activate_cp(parent, name):
    for cp in parent.customParameters:
        if cp.name == name:
            if Glyphs.buildNumber == 3151:
                newcp = GSCustomParameter(cp.name, cp.value)
                parent.customParameters.append(newcp)
                return
            else:
                cp.active = True


def export_vf(sources_path, file_name, instance_index):
    source_path = sources_path / file_name
    out_path = sources_path.parent / "sudo"
    font = Glyphs.open(str(source_path), showInterface=True)
    if font is None:
        print(f"Could not open file: '{source_path}'")
        return

    font.disableUpdateInterface()
    # Set up the source for export
    activate_cp(font, "glyphOrder")
    inst = font.instances[instance_index]
    inst.active = True
    activate_cp(inst, "Remove Features")
    activate_cp(inst, "Remove Glyphs")
    font.features["rlig"].active = True
    font.enableUpdateInterface()
    result = inst.generate(VARIABLE, str(out_path), autoHint=False, removeOverlap=False)
    if not result:
        print(f"Export of font '{file_name}' failed.")
    # font.close()


def export_static_mono(sources_path, file_name):
    if Glyphs.buildNumber != 3151:
        print(
            "Warning: It is recommended to export the static fonts "
            "with Glyphs build 3151."
        )
    source_path = sources_path / file_name
    out_path = sources_path.parent / "sudo"
    font = Glyphs.open(str(source_path), showInterface=True)
    if font is None:
        print(f"Could not open file: '{source_path}'")
        return

    font.disableUpdateInterface()
    activate_cp(font, "glyphOrder")
    for inst in font.instances:
        if inst.type == INSTANCETYPEVARIABLE:
            inst.active = False
            continue
        if inst.familyName == "Sudo":
            inst.active = True
        if inst.familyName == "Sudo UI":
            inst.active = False
            continue
        activate_cp(inst, "Remove Features")
        activate_cp(inst, "Remove Glyphs")
        if "Italic" in inst.name:
            activate_cp(inst, "Rename Glyphs")
    font.enableUpdateInterface()
    for inst in font.instances:
        if not inst.active:
            continue
        result = inst.generate(TTF, str(out_path), False, True)
        if not result:
            print(f"Export of static mono fonts from '{file_name}' failed.")


def export_static_prop(sources_path, file_name):
    if Glyphs.buildNumber != 3151:
        print(
            "Warning: It is recommended to export the static fonts "
            "with Glyphs build 3151."
        )
    source_path = sources_path / file_name
    out_path = sources_path.parent / "sudo"
    font = Glyphs.open(str(source_path), showInterface=True)
    if font is None:
        print(f"Could not open file: '{source_path}'")
        return

    font.disableUpdateInterface()
    activate_cp(font, "glyphOrder")
    for inst in font.instances:
        if inst.type == INSTANCETYPEVARIABLE:
            inst.active = False
            continue
        if inst.familyName == "Sudo UI":
            inst.active = True
        if inst.familyName == "Sudo":
            inst.active = False
            continue
        activate_cp(inst, "Remove Features")
        # activate_cp(inst, "Remove Glyphs")
        if "Italic" in inst.name:
            activate_cp(inst, "Rename Glyphs")
    font.enableUpdateInterface()
    for inst in font.instances:
        if not inst.active:
            continue
        result = inst.generate(TTF, str(out_path), False, True)
        if not result:
            print(f"Export of static mono fonts from '{file_name}' failed.")


if Glyphs.buildNumber != 3151:
    export_vf(sources_path, "SudoUI.glyphspackage", 0)
    export_vf(sources_path, "Sudo.glyphspackage", 1)

if Glyphs.buildNumber == 3151:
    export_static_prop(sources_path, "SudoUI.glyphspackage")
    export_static_mono(sources_path, "Sudo.glyphspackage")

print("Done.")
