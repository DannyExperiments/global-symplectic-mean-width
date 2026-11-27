"""Draw orthographic views of the exact area-preserving square example."""

from math import cos, pi, sin
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
WIDTH, HEIGHT = 704, 832
BACKGROUND, PANEL, BORDER = "#101929", "#172439", "#354c6b"
TEXT, MUTED, MINT, BLUE = "#f5f8ff", "#c9d5e7", "#74e9cf", "#bccbff"
PALETTES = (
    ("#237d79", "#246268", "#2d8884", "#53cfbd", "#79e7d5"),
    ("#535da0", "#414b86", "#626bbc", "#8ea7ff", "#c8d3ff"),
)
EDGES = ((0, 1), (1, 2), (2, 3), (3, 0))
FACES = ((0, 1, 5, 4), (1, 2, 6, 5), (2, 3, 7, 6), (3, 0, 4, 7), (4, 5, 6, 7))


def label(draw, x, y, text, size, color=TEXT):
    font = ImageFont.load_default(size=size)
    bounds = draw.textbbox((x, y), text, font=font, anchor="lt")
    assert bounds[0] >= 0 and bounds[2] < WIDTH and bounds[3] < HEIGHT, (text, bounds)
    draw.text((x, y), text, font=font, fill=color, anchor="lt")


def project(point, angle, y0):
    x, y, z = point
    east, north = x * cos(angle) - y * sin(angle), x * sin(angle) + y * cos(angle)
    return (489 + 66 * east, y0 + 36 * north - 66 * z), north + z


def panel(draw, top, title, sizes, width, half, angle, style):
    accent = (MINT, BLUE)[style]
    draw.rounded_rectangle((30, top, 674, top + 238), 20, fill=PANEL, outline=BORDER, width=2)
    label(draw, 53, top + 29, title, 31, accent)
    label(draw, 53, top + 89, sizes, 37)
    label(draw, 53, top + 149, "Mean width", 27, MUTED)
    label(draw, 53, top + 183, width, 38)
    center_y = top + 128
    for i in (-1.8, -0.9, 0, 0.9, 1.8):
        for first, last in (((i, -1.8, -0.19), (i, 1.8, -0.19)), ((-1.8, i, -0.19), (1.8, i, -0.19))):
            p, _ = project(first, angle, center_y)
            q, _ = project(last, angle, center_y)
            draw.line((p, q), fill="#314763", width=2)
    a, b = half
    vertices = ((-a, -b), (a, -b), (a, b), (-a, b))
    points = [project((x, y, z), angle, center_y) for z in (-0.13, 0.13) for x, y in vertices]
    assert all(278 < x < 670 and top + 18 < y < top + 215 for (x, y), _ in points)
    # Side faces are drawn back to front. The top face gives the true rectangle.
    for _, face_index in sorted((sum(points[i][1] for i in face), j) for j, face in enumerate(FACES[:-1])):
        face = FACES[face_index]
        draw.polygon([points[i][0] for i in face], fill=PALETTES[style][face_index % 3], outline="#26384e")
    draw.polygon([points[i][0] for i in FACES[-1]], fill=PALETTES[style][3])
    for i, j in EDGES:
        draw.line((points[i + 4][0], points[j + 4][0]), fill=PALETTES[style][4], width=3)
    for x, y in vertices:
        (px, py), _ = project((x, y, 0.13), angle, center_y)
        draw.ellipse((px - 4, py - 4, px + 4, py + 4), fill=TEXT)


def frame(angle):
    im = Image.new("RGB", (WIDTH, HEIGHT), BACKGROUND)
    draw = ImageDraw.Draw(im)
    label(draw, 33, 33, "LINEAR SYMPLECTIC MAPS", 25, MINT)
    label(draw, 32, 81, "Squeezing a square", 56)
    label(draw, 34, 150, "Stretch one axis, shrink the other.", 31, MUTED)
    panel(draw, 205, "Original square", "2 by 2", "8 / pi", (1, 1), angle, 0)
    panel(draw, 455, "Squeezed image", "4 by 1", "10 / pi", (2, 0.5), angle, 1)
    label(draw, 34, 723, "Area stays 4", 35, MINT)
    label(draw, 34, 776, "Mean width rises by 25%.", 36)
    label(draw, 397, 730, "Common plot scale", 25, MUTED)
    return im


def main():
    count = 72
    angles = [2 * pi * k / count + pi / 12 for k in range(count)]
    swatches = Image.new("RGB", (352, 416 * len(angles[::8])))
    for i, angle in enumerate(angles[::8]):
        swatches.paste(frame(angle).resize((352, 416)), (0, 416 * i))
    palette = swatches.convert("P", palette=Image.Palette.ADAPTIVE, colors=96)
    frames = [frame(angle).quantize(palette=palette, dither=Image.Dither.NONE) for angle in angles]
    frames[0].save(
        HERE / "squeezing-a-square.gif",
        save_all=True, append_images=frames[1:], loop=0, duration=120, optimize=True,
    )
    with ZipFile(HERE / "squeezing-a-square-explorer.zip", "w") as archive:
        for name in ("README.md", "index.html"):
            file = ZipInfo(name, (1980, 1, 1, 0, 0, 0))
            file.create_system = 3
            file.external_attr = 0o100644 << 16
            archive.writestr(file, (HERE / name).read_bytes(), ZIP_DEFLATED, compresslevel=9)


if __name__ == "__main__":
    main()
