from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def isotherm_x(y, temperature):
    theta = np.pi * temperature / 100.0
    return np.arctan((1.0 / np.tan(theta)) * np.tanh(y))


def heat_flow_y(x, radius):
    return np.arcsinh(np.sqrt(np.maximum(0.0, radius**2 - np.sin(x) ** 2)))


def main():
    chapter_dir = Path(__file__).resolve().parent
    output_path = chapter_dir / "images" / "exercise7_isotherms_heatflow_python_static.png"

    x_min = -np.pi / 2
    x_max = np.pi / 2
    y_max = 3.5

    fig, ax = plt.subplots(figsize=(7.2, 8.6), dpi=220)

    # Plate region.
    ax.fill(
        [x_min, x_min, x_max, x_max],
        [0.0, y_max, y_max, 0.0],
        color="#d8e8f7",
        alpha=0.6,
        zorder=0,
    )
    ax.plot([x_min, x_min], [0.0, y_max], color="#1b4fd1", linewidth=2.2, zorder=2)
    ax.plot([x_max, x_max], [0.0, y_max], color="#1b4fd1", linewidth=2.2, zorder=2)
    ax.plot([x_min, x_max], [0.0, 0.0], color="#1b4fd1", linewidth=2.2, zorder=2)

    # Axes.
    ax.axhline(0.0, color="black", linewidth=1.2, zorder=1)
    ax.axvline(0.0, color="black", linewidth=1.0, alpha=0.7, zorder=1)

    # Isotherms u(x, y) = T.
    y_vals = np.linspace(0.0, y_max, 700)
    temperatures = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    for temperature in temperatures:
        x_vals = isotherm_x(y_vals, temperature)
        ax.plot(
            x_vals,
            y_vals,
            color="#444444",
            linewidth=1.45,
            linestyle=(0, (6, 5)),
            zorder=3,
        )

        x_limit = np.pi / 2 - np.pi * temperature / 100.0
        ax.text(
            x_limit,
            y_max + 0.08,
            f"{temperature}\N{DEGREE SIGN}",
            ha="center",
            va="bottom",
            fontsize=10.5,
            color="#333333",
        )

    # Heat-flow curves sin^2 x + sinh^2 y = R^2.
    radii = [0.18, 0.32, 0.52, 0.9, 1.45, 2.1, 3.0]
    for radius in radii:
        if radius <= 1.0:
            x_vals = np.linspace(-np.arcsin(radius), np.arcsin(radius), 700)
        else:
            x_vals = np.linspace(x_min, x_max, 900)
        y_vals_curve = heat_flow_y(x_vals, radius)
        ax.plot(x_vals, y_vals_curve, color="#111111", linewidth=1.85, zorder=4)

    # Boundary labels.
    ax.text(x_min - 0.05, 3.0, "u = 100°", ha="right", va="center", fontsize=13)
    ax.text(x_max + 0.05, 3.0, "u = 0°", ha="left", va="center", fontsize=13)
    ax.text(-0.82, -0.18, "u = 100°", ha="center", va="top", fontsize=13)
    ax.text(0.82, -0.18, "u = 0°", ha="center", va="top", fontsize=13)

    # Title and annotations.
    ax.set_title("Exercise 7: Isotherms and Curves of Heat Flow", fontsize=15, pad=12)

    ax.set_xlim(x_min - 0.2, x_max + 0.2)
    ax.set_ylim(-0.35, y_max + 0.35)
    ax.set_xticks([-np.pi / 2, 0.0, np.pi / 2])
    ax.set_xticklabels([r"$-\pi/2$", r"$0$", r"$\pi/2$"], fontsize=12)
    ax.set_yticks([1.0, 2.0, 3.0])
    ax.set_yticklabels([r"$1$", r"$2$", r"$3$"], fontsize=12)
    ax.set_xlabel(r"$x$", fontsize=14)
    ax.set_ylabel(r"$y$", fontsize=14, rotation=0, labelpad=12)
    ax.grid(True, color="#aeb6bf", linewidth=0.8, alpha=0.6)

    for spine in ("top", "right"):
        ax.spines[spine].set_visible(False)

    fig.subplots_adjust(top=0.93, left=0.14, right=0.90, bottom=0.08)
    fig.savefig(output_path)
    plt.close(fig)


if __name__ == "__main__":
    main()
