from PIL import Image, ImageFilter, ImageEnhance
import tkinter as tk

IMAGE_PATH = "image.png"
PIXEL_ART_WIDTH =400
PIXEL = 5
COLOR_LIMIT = 16

SATURATION = 1.5
CONTRAST = 1.2
SHARPNESS = 10

img = Image.open(IMAGE_PATH).convert("RGB")

aspect = img.height / img.width
PIXEL_ART_HEIGHT = int(PIXEL_ART_WIDTH * aspect)

img = img.resize((PIXEL_ART_WIDTH, PIXEL_ART_HEIGHT), Image.LANCZOS)

img = ImageEnhance.Color(img).enhance(SATURATION)
img = ImageEnhance.Contrast(img).enhance(CONTRAST)
img = ImageEnhance.Sharpness(img).enhance(SHARPNESS)

img = img.quantize(
    colors=COLOR_LIMIT,
    method=Image.Quantize.MEDIANCUT,
    dither=Image.Dither.NONE
).convert("RGB")

SPRITE_WIDTH, SPRITE_HEIGHT = img.size

def symbol(n):
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    base = len(chars)

    out = ""
    while True:
        out = chars[n % base] + out
        n = n // base - 1
        if n < 0:
            break
    return out

palette = {}
sprite = []

for y in range(SPRITE_HEIGHT):
    row = []

    for x in range(SPRITE_WIDTH):
        color = img.getpixel((x, y))

        if color not in palette:
            palette[color] = symbol(len(palette))

        row.append(palette[color])

    sprite.append(row)

colors = {
    s: "#{:02x}{:02x}{:02x}".format(*c)
    for c, s in palette.items()
}

root = tk.Tk()
root.title("Pixel Art")

canvas = tk.Canvas(
    root,
    width=SPRITE_WIDTH * PIXEL,
    height=SPRITE_HEIGHT * PIXEL,
    bg="black",
    highlightthickness=0
)
canvas.pack()

for y, row in enumerate(sprite):
    for x, sym in enumerate(row):
        c = colors[sym]

        canvas.create_rectangle(
            x * PIXEL,
            y * PIXEL,
            (x + 1) * PIXEL,
            (y + 1) * PIXEL,
            fill=c,
            outline=c
        )


root.mainloop()

