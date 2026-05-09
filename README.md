# Pixel Art Collection

A collection of Python-based graphical applications built with Tkinter.

This repository contains three independent scripts demonstrating GUI rendering, pixel-art drawing, and image-to-pixel-art conversion.

---

## Requirements

Install dependencies:

```bash
pip install  pillow
```

---

## Project Files

### 1. logo.py

Displays a custom graphical interface containing styled text elements.

Features:
- Tkinter-based GUI
- Fonts : Fixedsys & minesweeper
- Color styling
- Window layout positioning

**Output**

![Logo GUI Result](images/logo.png)


---

### 2. mario_pixel.py

Renders pixel-art using a manually defined sprite matrix.

Features:
- Canvas-based rendering
- Color-mapped sprite generation
- Scalable pixel size

**Output**

![Mario Pixel Art Result](images/mario.png)

---

### 3. pixel_art_auto.py

Converts an input image into pixel art using color quantization and renders it with Tkinter.

Features:
- Image resizing
- Color palette reduction
- Saturation and contrast enhancement
- Sharpness adjustment
- Pixel-art visualization

**Input Image**

![Input Image](images/image.png)

**Output**

![Converted Pixel Art Result](images/pixel_auto.png)



# App

A simple tool for editing and transforming images with real-time controls.

## How to use

You can download and run the application from the **Releases** section of this repository.

##  Features

-  Adjust **color saturation**
- Change **contrast**
-  Reduce colors
-  Set **custom pixel size**
-  Save the processed image to your device



## Repository Structure

```text
.
├── logo.py
├── mario.py
├── pixel_art_auto.py
├── README.md
└── images/
    ├── logo.png
    ├── mario.png
    ├── pixel_auto.png
    └── image.png
```

---

## Notes

For the image conversion script, ensure the input file path matches:

```python
IMAGE_PATH = "images/image.png"
```
