from drawBot.drawBotDrawingTools import _drawBotDrawingTool
from fontTools.pens.cocoaPen import CocoaPen
from fontTools.ttLib import TTFont


def drawGlyph(glyph):
	pen = CocoaPen(glyph._glyphset)
	glyph.draw(pen)
	path = pen.path
	_drawBotDrawingTool.drawPath(path)

_drawBotDrawingTool.drawGlyph = drawGlyph


s = 0.27
text_x = 130

def text_path(t, pos, font_path):
    # Like text, but draws paths of the glyphs
    x, y = pos
    f = TTFont(font_path)
    gs = f.getGlyphSet()
    save()
    translate(x, y)
    for l in t:
        glyph = gs[l]
        drawGlyph(glyph)
        translate(glyph.width)
    restore()
    
def metrics_color():
    fill(None)
    stroke(73/255, 164/255, 39/255, 1)
    strokeWidth(10)

def highlight_color():
    fill(253/255, 95/255, 0, 0.3)

def mono_metrics(text_x, s):
    save()
    metrics_color()
    y = 0
    xmax = width() / s
    line((0, y), (xmax, y))
    y = 448
    line((0, y), (xmax, y))
    y = 640
    line((text_x + 9 * 448, y), (text_x + 10 * 448, y))
    y = -192
    line((text_x + 5 * 448, y), (text_x + 6 * 448, y))
    
    restore()

def legible_metrics():
    save()
    metrics_color()
    y = 0
    line((0, y), (width() / s, y))
    y = 448
    line((0, y), (width() / s, y))
    y = 640
    line((0, y), (width() / s, y))
    restore()

def monospaced():
    line_height = 832
    size(1280, 720)
    
    # Move up
    translate(0, height())
    scale(s)
    fontSize(1024)
    
    # Orange box
    save()
    highlight_color()
    rect(text_x + 1 * 448, 0, 448, -height()/s)
    restore()
    
    # The text lines
    translate(0, -line_height * 0.85)
    mono_metrics(text_x, s)
    font("Sudo Thin")
    text_path("monospaced", (text_x, 0), "../sudo/Sudo-Thin.ttf")
    
    translate(0, -line_height)
    mono_metrics(text_x, s)
    font("Sudo Regular")
    text_path("monospaced", (text_x, 0), "../sudo/Sudo-Regular.ttf")
    
    translate(0, -line_height)
    mono_metrics(text_x, s)
    font("Sudo Bold")
    text_path("monospaced", (text_x, 0), "../sudo/Sudo-Bold.ttf")

def legible():
    line_height = 832
    newPage(1280, 300)
    
    # Move up
    translate(0, height())
    scale(s)
    fontSize(1024)
    translate(0, -line_height)
    
    # Orange boxes
    save()
    highlight_color()
    rect(0, 0, width()/s, 64)
    # rect(text_x + 1 * 448, 0, 448, -height()/s)
    rect(0, 640, text_x + 2 * 448, -64)
    rect(text_x + 2 * 448, 576, 3 * 448, -64)
    rect(text_x + 5 * 448, 640, 3 * 448, -64)
    rect(text_x + 6 * 448, 448, 2 * 448, -64)
    rect(text_x + 8 * 448, 320, 2 * 448, -64)
    restore()
    
    # The text lines
    legible_metrics()
    font("Sudo Regular")
    text_path(["I", "l", "one", "zero", "seven", "O", "o", "n", "plus", "equal"], (text_x, 0), "../sudo/Sudo-Regular.ttf")

def efficient():
    line_height = 832
    newPage(1280, 300)
    
    # Move up
    translate(0, height())
    scale(s)
    fontSize(1024)
    translate(0, -line_height * 1.05)
    
    # Orange boxes
    save()
    highlight_color()
    rect(text_x, -192, text_x + 2 * 448, 1024)
    restore()
    
    # The text lines
    legible_metrics()
    font("Sudo Regular")
    text_path(["Scaron", "p", "a", "c", "e"], (text_x, 0), "../sudo/Sudo-Regular.ttf")
    scale(0.5)
    
    save()
    highlight_color()
    rect(text_x + 12 * 448, -192*2, 2048, 2048)
    restore()
    
    text_path(["Scaron", "p", "a"], (text_x + 12 * 448, 0), "../resources/consola.ttf")

def unique():
    line_height = 832
    newPage(1280, 300)
    
    # Move up
    translate(0, height())
    scale(s)
    fontSize(1024)
    translate(0, -line_height)

    # The text lines
    legible_metrics()
    font("Sudo Regular")
    text_path(["grave", "agrave", "quotesingle", "quotedblright", "asciicircum", "ocircumflex", "greater", "guilsinglright"], (text_x, 0), "../sudo/Sudo-Regular.ttf")
    
def github():
    line_height = 900
    newPage(1280, 640)
    
    # Move up
    translate(0, height())
    s = 0.22
    text_x = 448 + 224
    scale(s)
    #fontSize(620)
    
    # Orange box
    save()
    highlight_color()
    rect(text_x + 1 * 448, 0, 448, -height()/s)
    restore()
    
    # The text lines
    translate(0, -line_height * 0.85)
    mono_metrics(text_x, s)
    font("Sudo Thin")
    # translate(-448, 0)
    text_path("monospaced", (text_x, 0), "../sudo/Sudo-Thin.ttf")
    
    translate(0, -line_height)
    mono_metrics(text_x, s)
    font("Sudo Regular")
    text_path("monospaced", (text_x, 0), "../sudo/Sudo-Regular.ttf")
    
    translate(0, -line_height)
    mono_metrics(text_x, s)
    font("Sudo Bold")
    text_path("monospaced", (text_x, 0), "../sudo/Sudo-Bold.ttf")

monospaced()
saveImage("~/Sites/kuti/src/sudo-font/sudo-monospaced.svg")

legible()
saveImage("~/Sites/kuti/src/sudo-font/sudo-legible.svg")

efficient()
saveImage("~/Sites/kuti/src/sudo-font/sudo-space-saving.svg")

unique()
saveImage("~/Sites/kuti/src/sudo-font/sudo-quotes.svg")

github()
saveImage("../images/sudo.png")