"""
GPT Translation Through Meaning Space
Shows how GPT converts language to meaning and back
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from matplotlib.patches import FancyBboxPatch, Circle

plt.rcParams["font.family"] = "serif"


def make_gpt_translation_gif(filename="gpt_translation_meaning.gif"):
    """
    Visualize GPT-style translation as moving through meaning space.
    English → Meaning cloud → Spanish
    """
    # -------------------------
    # Animation config
    # -------------------------

    frames_per_stage = 30
    n_stages = 3
    total_frames = frames_per_stage * n_stages

    stage_titles = [
        "Input: English sentence",
        "Convert to meaning space",
        "Output: Spanish sentence",
    ]

    # -------------------------
    # Figure setup
    # -------------------------

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    # -------------------------
    # Three boxes: English, Meaning, Spanish
    # -------------------------

    x_eng = 0.15
    x_mean = 0.50
    x_span = 0.85
    y_box = 0.65
    box_w = 0.18
    box_h = 0.20

    boxes = []
    for x_center in [x_eng, x_mean, x_span]:
        box = FancyBboxPatch(
            (x_center - box_w / 2, y_box - box_h / 2),
            box_w,
            box_h,
            boxstyle="round,pad=0.01",
            edgecolor="black",
            facecolor="0.94",
            linewidth=1.2,
        )
        ax.add_patch(box)
        boxes.append(box)

    # Box labels
    ax.text(x_eng, y_box + 0.13, "English", ha="center", va="center", fontsize=11)
    ax.text(x_mean, y_box + 0.13, "Meaning", ha="center", va="center", fontsize=11)
    ax.text(x_span, y_box + 0.13, "Spanish", ha="center", va="center", fontsize=11)

    # -------------------------
    # English and Spanish text
    # -------------------------

    english_sentence = "The weather is nice today."
    spanish_sentence = "El clima está agradable hoy."

    eng_text = ax.text(
        x_eng,
        y_box,
        english_sentence,
        ha="center",
        va="center",
        fontsize=11,
        wrap=True,
    )

    span_text = ax.text(
        x_span,
        y_box,
        spanish_sentence,
        ha="center",
        va="center",
        fontsize=11,
        wrap=True,
    )

    # Meaning cloud (random 2D vectors as points)
    rng = np.random.default_rng(0)
    cloud_x = x_mean + 0.08 * (rng.random(60) - 0.5)
    cloud_y = 0.32 + 0.20 * (rng.random(60) - 0.5)

    cloud = ax.scatter(
        cloud_x,
        cloud_y,
        s=15,
        color="tab:blue",
        alpha=0.0,  # start invisible
    )

    # Moving token dot
    dot = Circle((x_eng, y_box), radius=0.015, color="tab:orange")
    ax.add_patch(dot)

    # Title and caption
    title = ax.text(
        0.5,
        0.96,
        "GPT-style translation as idea conversion",
        ha="center",
        va="top",
        fontsize=14,
    )

    caption = ax.text(
        0.5,
        0.08,
        "",
        ha="center",
        va="center",
        fontsize=10,
    )

    def stage_from_frame(frame: int) -> int:
        return min(frame // frames_per_stage, n_stages - 1)

    def update(frame: int):
        stage = stage_from_frame(frame)
        local = frame % frames_per_stage
        frac = local / (frames_per_stage - 1 + 1e-9)

        # base alphas
        eng_alpha = 0.1
        mean_alpha = 0.1
        span_alpha = 0.1

        # fade logic by stage
        if stage == 0:
            eng_alpha = 0.7 + 0.3 * (1 - frac)     # strong at start
            mean_alpha = 0.2 + 0.4 * frac          # bring in meaning
            span_alpha = 0.0
        elif stage == 1:
            eng_alpha = 0.3 * (1 - frac)
            mean_alpha = 0.6 + 0.4 * (1 - abs(frac - 0.5) * 2)
            span_alpha = 0.2 + 0.5 * frac
        else:
            eng_alpha = 0.1
            mean_alpha = 0.3 + 0.3 * (1 - frac)
            span_alpha = 0.7 + 0.3 * frac

        eng_text.set_alpha(eng_alpha)
        span_text.set_alpha(span_alpha)
        cloud.set_alpha(mean_alpha)

        # highlight active box
        active_colors = ["0.94", "0.94", "0.94"]
        active_colors[stage] = "0.85"
        for box, col in zip(boxes, active_colors):
            box.set_facecolor(col)

        # move the dot from English -> Meaning -> Spanish across full animation
        global_frac = frame / (total_frames - 1 + 1e-9)

        if global_frac < 0.5:
            f = global_frac / 0.5
            x_dot = x_eng + (x_mean - x_eng) * f
        else:
            f = (global_frac - 0.5) / 0.5
            x_dot = x_mean + (x_span - x_mean) * f

        dot.center = (x_dot, y_box)

        # captions by stage
        caption.set_text(stage_titles[stage])

        return [eng_text, span_text, cloud, dot, title, caption] + boxes

    # Add pause
    animated_frames = total_frames
    pause_frames = 10
    total_with_pause = animated_frames + pause_frames
    
    def update_with_pause(frame):
        actual_frame = min(frame, animated_frames - 1)
        return update(actual_frame)
    
    anim = FuncAnimation(
        fig,
        update_with_pause,
        frames=total_with_pause,
        interval=200,
        blit=True,
    )

    writer = PillowWriter(fps=5)
    anim.save(filename, writer=writer)
    plt.close(fig)


if __name__ == "__main__":
    print("Creating GPT translation visualization...")
    make_gpt_translation_gif()
    print("  ✓ gpt_translation_meaning.gif")
    print("Done!")
