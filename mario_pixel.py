import tkinter as tk

PIXEL  =40

colors = {
    "R": "#ff2a23",   
    "B": "#8b4513",   
    "S": "#f3c178",   
    "O": "blue",   
    "Y": "#f7db3d",   
    "K": "#000000",   
    ".": None
}
sprite = [
"....RRRRR....",
"...RRRRRRRR...",
"...BBBSKS...",
"..BSBSSKSSS.",
"..BSBBSSBSSS.",
"..BBSSSBBBB..",
"....SSSSS.....",
"...RRORORR....",
"..RRRORORRR...",
".RRRRYOYRRRR..",
".SSROOOOORSS..",
".SSSOOOOOSSS..",
".SSOOOOOOOSS..",
"...OOO.OOO....",
"...BB...BB....",
"..BBB...BBB..."

]


root = tk.Tk()
root.title("Mario")
root.config(bg ="black")

canvas = tk.Canvas(
    root,
    highlightthickness=0,
    width=len(sprite[0]) * PIXEL,
    height=len(sprite) * PIXEL,
    bg="black"
)
canvas.pack(pady=40)

for y, row in enumerate(sprite):
    for x, pixel in enumerate(row):
        color = colors.get(pixel)
        if color:
            canvas.create_rectangle(
                x * PIXEL,
                y * PIXEL,
                (x + 1) * PIXEL,
                (y + 1) * PIXEL,
                fill=color,
                outline=color
            )

root.mainloop()

