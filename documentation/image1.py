# This script is meant to be run from the root level
# of your font's git repository. For example, from a Unix terminal:
# $ git clone my-font
# $ cd my-font
# $ python3 documentation/image1.py --output documentation/image1.png

import argparse

# Import moduels from the Python Standard Library: https://docs.python.org/3/library/
import subprocess

# Import moduels from external python packages: https://pypi.org/
from drawbot_skia.drawbot import (
    fill,
    font,
    fontSize,
    fontVariations,
    line,
    lineCap,
    newPage,
    polygon,
    rect,
    saveImage,
    scale,
    stroke,
    strokeWidth,
    text,
    translate,
)
from fontTools.misc.fixedTools import floatToFixedToStr
from fontTools.ttLib import TTFont

# Constants, these are the main "settings" for the image
WIDTH, HEIGHT, MARGIN, FRAMES = 2048, 1024, 48, 1
FONT_PATH = "fonts/variable/Sudo[YTDE,wght].ttf"
FONT2_PATH = "fonts/variable/SudoUI[YTDE,wght].ttf"
FONT_LICENSE = "OFL v1.1"
AUXILIARY_FONT = "fonts/variable/SudoUI[YTDE,wght].ttf"
AUXILIARY_FONT_SIZE = 48

BIG_TEXT = "AaBb"
BIG_TEXT_FONT_SIZE = 150
BIG_TEXT_LINE_HEIGHT = 190
BIG_TEXT_SIDE_MARGIN = MARGIN * 1
BIG_TEXT_BOTTOM_MARGIN = MARGIN * 2

GRID_VIEW = False  # Toggle this for a grid overlay

# Handel the "--output" flag
# For example: $ python3 documentation/image1.py --output documentation/image1.png
parser = argparse.ArgumentParser()
parser.add_argument("--output", metavar="PNG", help="where to write the PNG file")
args = parser.parse_args()

# Load the font with the parts of fonttools that are imported with the line:
# from fontTools.ttLib import TTFont
# Docs Link: https://fonttools.readthedocs.io/en/latest/ttLib/ttFont.html
ttFont = TTFont(FONT_PATH)

# Constants that are worked out dynamically
MY_URL = subprocess.check_output("git remote get-url origin", shell=True).decode()
MY_HASH = subprocess.check_output("git rev-parse --short HEAD", shell=True).decode()
FONT_NAME = ttFont["name"].getDebugName(4)
FONT_VERSION = "v%s" % floatToFixedToStr(ttFont["head"].fontRevision, 16)


# Draws a grid
def grid():
    stroke(1, 0, 0, 0.75)
    strokeWidth(2)
    STEP_X, STEP_Y = 0, 0
    INCREMENT_X, INCREMENT_Y = MARGIN / 2, MARGIN / 2
    rect(MARGIN, MARGIN, WIDTH - (MARGIN * 2), HEIGHT - (MARGIN * 2))
    for x in range(29):
        polygon((MARGIN + STEP_X, MARGIN), (MARGIN + STEP_X, HEIGHT - MARGIN))
        STEP_X += INCREMENT_X
    for y in range(29):
        polygon((MARGIN, MARGIN + STEP_Y), (WIDTH - MARGIN, MARGIN + STEP_Y))
        STEP_Y += INCREMENT_Y
    polygon((WIDTH / 2, 0), (WIDTH / 2, HEIGHT))
    polygon((0, HEIGHT / 2), (WIDTH, HEIGHT / 2))


# Remap input range to VF axis range
# This is useful for animation
# (E.g. sinewave(-1,1) to wght(100,900))
def remap(value, inputMin, inputMax, outputMin, outputMax):
    inputSpan = inputMax - inputMin  # FIND INPUT RANGE SPAN
    outputSpan = outputMax - outputMin  # FIND OUTPUT RANGE SPAN
    valueScaled = float(value - inputMin) / float(inputSpan)
    return outputMin + (valueScaled * outputSpan)


# Draw the page/frame and a grid if "GRID_VIEW" is set to "True"
def draw_background():
    newPage(WIDTH, HEIGHT)
    fill(0, 78 / 255, 0)
    rect(-2, -2, WIDTH + 4, HEIGHT + 4)
    fill(235 / 255, 235 / 255, 235 / 255)
    rect(WIDTH / 2, -2, WIDTH + 4, HEIGHT + 4)

    # fill(0, 88 / 255, 0)
    # rect(53, 84, WIDTH / 2 - 53, HEIGHT - 53 - 84)

    if GRID_VIEW:
        grid()


# Draw main text
def draw_main_text():
    fill(0, 182 / 255, 0)
    stroke(None)
    font(FONT_PATH)
    fontSize(BIG_TEXT_FONT_SIZE)
    # Adjust this line to center main text manually.
    # TODO: This should be done automatically when drawbot-skia
    # has support for textBox() and FormattedString
    # text(BIG_TEXT, ((WIDTH / 2) - MARGIN * 4.75, (HEIGHT / 2) - MARGIN * 2.5))

    translate(0, HEIGHT)
    translate(0, -176)
    stripchar = " "
    for _ in range(2):
        for weight, s in (
            (200, "Terminal___".strip(stripchar)),
            (300, "Python_____".strip(stripchar)),
            (400, "Ruby(Rails)".strip(stripchar)),
            (600, "Objective-C".strip(stripchar)),
            (700, "PowerShell_".strip(stripchar)),
        ):
            fontVariations(wght=weight)
            text(s, (MARGIN, 0))
            translate(0, -BIG_TEXT_LINE_HEIGHT)
        translate(WIDTH / 2, 5 * BIG_TEXT_LINE_HEIGHT)
        font(FONT2_PATH)
        fill(91 / 255, 91 / 255, 91 / 255)
        stripchar = "_"


# Divider lines
def draw_divider_lines():
    stroke(1)
    strokeWidth(1)
    lineCap("round")
    line((MARGIN, HEIGHT - (MARGIN * 1.5)), (WIDTH - MARGIN, HEIGHT - (MARGIN * 1.5)))
    # line((MARGIN, MARGIN + (MARGIN / 2)), (WIDTH - MARGIN, MARGIN + (MARGIN / 2)))
    line((MARGIN, 84), (WIDTH - MARGIN, 84))
    stroke(None)


# Draw text describing the font and it's git status & repo URL
def draw_auxiliary_text():
    # Setup
    font(AUXILIARY_FONT)
    fontSize(AUXILIARY_FONT_SIZE)
    # POS_TOP_LEFT = (MARGIN, HEIGHT - MARGIN * 1.25)
    POS_TOP_RIGHT = (WIDTH - MARGIN, HEIGHT - MARGIN * 1.25)
    # POS_BOTTOM_LEFT = (MARGIN, MARGIN / 2)
    POS_BOTTOM_RIGHT = (WIDTH - MARGIN * 0.95, MARGIN / 2)
    URL_AND_HASH = MY_URL + "at commit " + MY_HASH
    URL_AND_HASH = URL_AND_HASH.replace("\n", " ")
    # Draw Text
    fill(1)
    fontVariations(wght=600)
    text("Sudo ", (WIDTH / 2, MARGIN / 2), align="right")
    fill(0)
    fontVariations(wght=680)
    text(" Sudo UI", (WIDTH / 2, MARGIN / 2), align="left")
    fill(0.7)
    text(FONT_VERSION, POS_TOP_RIGHT, align="right")
    # text(URL_AND_HASH, POS_BOTTOM_LEFT, align="left")
    text(FONT_LICENSE, POS_BOTTOM_RIGHT, align="right")


# Build and save the image
if __name__ == "__main__":
    draw_background()
    # draw_divider_lines()
    draw_auxiliary_text()
    draw_main_text()
    # Save output, using the "--output" flag location
    saveImage(args.output)
    # Print done in the terminal
    print("DrawBot: Done")
