import numpy as np
from pathlib import Path
from PIL import Image, ImageDraw


def u(x: float, y: float) -> float | None:
    r2 = x * x + y * y
    if r2 <= 0.03:
        return None
    return x * y / r2


def project(x: float, y: float, z: float) -> tuple[float, float]:
    xp = 430 + 125 * (x - y)
    yp = 355 - 68 * (x + y) - 230 * z
    return xp, yp


def main() -> None:
    chapter_dir = Path(__file__).resolve().parent
    output_path = chapter_dir / "images" / "exercise_xy_over_x2_plus_y2_surface.png"

    grid = np.linspace(-2.0, 2.0, 90)
    image = Image.new("RGB", (860, 680), "white")
    draw = ImageDraw.Draw(image)

    cells: list[tuple[float, list[tuple[float, float]], tuple[int, int, int]]] = []

    for i in range(len(grid) - 1):
        for j in range(len(grid) - 1):
            x1, x2 = grid[i], grid[i + 1]
            y1, y2 = grid[j], grid[j + 1]
            corners = [(x1, y1), (x2, y1), (x2, y2), (x1, y2)]
            values = [u(x, y) for x, y in corners]
            if any(v is None for v in values):
                continue

            avg_z = sum(values) / 4.0
            t = (avg_z + 0.5) / 1.0
            color = (
                int(35 + 180 * t),
                int(80 + 110 * (1 - abs(2 * t - 1))),
                int(210 - 160 * t),
            )
            polygon = [project(x, y, z) for (x, y), z in zip(corners, values)]
            depth = sum(x + y for x, y in corners) / 4.0
            cells.append((depth, polygon, color))

    for _, polygon, color in sorted(cells, key=lambda item: item[0]):
        draw.polygon(polygon, fill=color, outline=(120, 120, 120))

    for axis in [
        (project(-2, -2, -0.6), project(2, -2, -0.6)),
        (project(-2, -2, -0.6), project(-2, 2, -0.6)),
        (project(-2, -2, -0.6), project(-2, -2, 0.6)),
    ]:
        draw.line(axis, fill=(40, 40, 40), width=3)

    ox, oy = project(0, 0, 0)
    draw.ellipse((ox - 7, oy - 7, ox + 7, oy + 7), fill="crimson", outline="crimson")

    image.save(output_path)


if __name__ == "__main__":
    main()
