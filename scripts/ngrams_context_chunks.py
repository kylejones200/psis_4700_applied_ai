"""
N-grams, Context, and Chunking Visualization
Shows progression from next-word to n-grams to paragraph chunking
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from matplotlib.patches import Rectangle, FancyBboxPatch

plt.rcParams["font.family"] = "serif"


def make_ngrams_context_chunks_gif(filename="ngrams_context_chunks.gif"):
    """
    Create GIF showing three phases:
    1. Simple next-word prediction
    2. N-gram context window sliding across sentence
    3. Paragraph chunking for larger context
    """
    # -------------------------
    # Text content
    # -------------------------

    sentence_words = ["The", "stock", "market", "fell", "sharply", "today"]
    candidates = ["rose", "fell", "stayed"]

    # probabilities for next-word example
    candidate_probs = np.array([0.15, 0.70, 0.15])

    paragraph_lines = [
        "The stock market fell sharply today.",
        "Analysts blamed weak earnings and high rates.",
        "Investors watched central bank signals closely.",
    ]

    # -------------------------
    # Animation config
    # -------------------------

    frames_per_stage = 30
    n_stages = 3
    n_frames = frames_per_stage * n_stages

    # -------------------------
    # Figure setup
    # -------------------------

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    title = ax.text(
        0.5,
        0.97,
        "",
        ha="center",
        va="top",
        fontsize=14,
        weight="bold"
    )

    subtitle = ax.text(
        0.5,
        0.08,
        "",
        ha="center",
        va="center",
        fontsize=10,
    )

    # -------------------------
    # Sentence words (top row)
    # -------------------------

    x_positions = np.linspace(0.1, 0.9, len(sentence_words))
    y_sentence = 0.75

    word_artists = []
    for x, w in zip(x_positions, sentence_words):
        t = ax.text(
            x,
            y_sentence,
            w,
            ha="center",
            va="center",
            fontsize=13,
        )
        word_artists.append(t)

    # context window rectangle for n-gram view
    context_rect = Rectangle(
        (0.0, y_sentence - 0.07),
        0.0,
        0.14,
        linewidth=0,
        edgecolor=None,
        facecolor="tab:blue",
        alpha=0.15,
    )
    ax.add_patch(context_rect)

    # -------------------------
    # Next-word probability bars (bottom)
    # -------------------------

    bar_x = np.linspace(0.25, 0.75, len(candidates))
    bar_width = 0.15
    bar_bottom = 0.25

    bars = ax.bar(
        bar_x,
        candidate_probs,
        width=bar_width,
        color="0.8",
        edgecolor="black",
    )

    for x, label in zip(bar_x, candidates):
        ax.text(
            x,
            bar_bottom - 0.08,
            label,
            ha="center",
            va="center",
            fontsize=11,
        )

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    # -------------------------
    # Paragraph chunking elements (for stage 3)
    # -------------------------

    paragraph_y = [0.65, 0.51, 0.37]
    paragraph_text = []
    for line, y in zip(paragraph_lines, paragraph_y):
        t = ax.text(
            0.15,
            y,
            line,
            ha="left",
            va="center",
            fontsize=10,
            wrap=True,
            alpha=0.0,
        )
        paragraph_text.append(t)

    # chunk box that wraps the paragraph
    chunk_box = FancyBboxPatch(
        (0.12, 0.30),
        0.76,
        0.42,
        boxstyle="round,pad=0.03",
        linewidth=1.0,
        edgecolor="tab:blue",
        facecolor="tab:blue",
        alpha=0.0,
    )
    ax.add_patch(chunk_box)

    # summary box to the right
    summary_box = FancyBboxPatch(
        (0.82, 0.45),
        0.15,
        0.18,
        boxstyle="round,pad=0.03",
        linewidth=1.0,
        edgecolor="black",
        facecolor="0.9",
        alpha=0.0,
    )
    ax.add_patch(summary_box)

    summary_text = ax.text(
        0.895,
        0.54,
        "Summary",
        ha="center",
        va="center",
        fontsize=10,
        alpha=0.0,
    )

    # arrow from chunk to summary
    arrow = ax.annotate(
        "",
        xy=(0.82, 0.54),
        xytext=(0.88, 0.54),
        arrowprops=dict(arrowstyle="<|-", lw=1),
    )
    arrow.set_alpha(0.0)

    # -------------------------
    # Helper functions
    # -------------------------

    def stage_from_frame(frame: int) -> int:
        return min(frame // frames_per_stage, n_stages - 1)

    def update(frame: int):
        stage = stage_from_frame(frame)
        local = frame % frames_per_stage
        frac = local / (frames_per_stage - 1 + 1e-9)

        # Reset visibility defaults
        for w in word_artists:
            w.set_alpha(1.0)
            w.set_color("black")
        context_rect.set_alpha(0.0)

        for b in bars:
            b.set_alpha(0.0)

        for t in paragraph_text:
            t.set_alpha(0.0)
        chunk_box.set_alpha(0.0)
        summary_box.set_alpha(0.0)
        summary_text.set_alpha(0.0)
        arrow.set_alpha(0.0)

        if stage == 0:
            # Next-word prediction
            title.set_text("Next-word prediction")
            subtitle.set_text("Model predicts the next word from recent context")

            # highlight last word as focus
            for i, w in enumerate(word_artists):
                if i == len(word_artists) - 2:
                    w.set_color("tab:blue")
                elif i == len(word_artists) - 1:
                    w.set_color("tab:orange")

            for b, p in zip(bars, candidate_probs):
                b.set_alpha(1.0)
                b.set_height(p)

        elif stage == 1:
            # N-gram context
            title.set_text("N-gram context")
            subtitle.set_text("Model widens the window to capture short sequences")

            for b in bars:
                b.set_alpha(0.0)

            # sliding window over three-word context
            window_size = 3
            max_start = len(sentence_words) - window_size
            window_start = int(round(frac * max_start))
            x_left = x_positions[window_start] - 0.06
            x_right = x_positions[window_start + window_size - 1] + 0.06

            context_rect.set_x(x_left)
            context_rect.set_width(x_right - x_left)
            context_rect.set_alpha(0.18)

            # highlight words inside window
            for i, w in enumerate(word_artists):
                if window_start <= i < window_start + window_size:
                    w.set_color("tab:blue")
                else:
                    w.set_color("black")

        else:
            # Paragraph chunking
            title.set_text("Paragraph chunking")
            subtitle.set_text("Model uses larger chunks for topic and meaning")

            # fade out sentence words
            for w in word_artists:
                w.set_alpha(1.0 - frac)

            # fade in paragraph lines
            for t in paragraph_text:
                t.set_alpha(frac)

            chunk_box.set_alpha(0.1 + 0.4 * frac)
            summary_box.set_alpha(0.2 + 0.6 * frac)
            summary_text.set_alpha(frac)
            arrow.set_alpha(frac)

        return (
            word_artists
            + list(bars)
            + [context_rect]
            + paragraph_text
            + [chunk_box, summary_box, summary_text, arrow, title, subtitle]
        )

    # Add pause
    animated_frames = n_frames
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
    print("Creating n-grams and context visualization...")
    make_ngrams_context_chunks_gif()
    print("  ✓ ngrams_context_chunks.gif")
    print("Done!")
