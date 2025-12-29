"""
Markov Chain Learning Visualizations
Creates multiple GIFs to help students understand Markov chains and language models
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from matplotlib.patches import FancyBboxPatch, Circle, Rectangle
from matplotlib.patches import FancyBboxPatch

plt.rcParams["font.family"] = "serif"


def make_stage_dependent_markov_gif(filename="stage_dependent_markov.gif"):
    """
    GIF showing how state probabilities evolve in a stage-dependent 
    (time-inhomogeneous) Markov chain.
    """
    # -------------------------
    # 1. Define a stage-dependent Markov chain
    # -------------------------

    n_states = 3
    n_steps = 30

    state_labels = ["S0", "S1", "S2"]

    def transition_matrix(t: int) -> np.ndarray:
        """Return the transition matrix for step t (stage-dependent)."""
        if t < 10:
            # Stage 1: prefers staying in the same state
            return np.array([
                [0.80, 0.15, 0.05],
                [0.10, 0.80, 0.10],
                [0.05, 0.15, 0.80],
            ])
        elif t < 20:
            # Stage 2: prefers moving toward S1
            return np.array([
                [0.20, 0.70, 0.10],
                [0.10, 0.75, 0.15],
                [0.10, 0.70, 0.20],
            ])
        else:
            # Stage 3: prefers moving toward S2
            return np.array([
                [0.10, 0.20, 0.70],
                [0.05, 0.25, 0.70],
                [0.05, 0.25, 0.70],
            ])

    # -------------------------
    # 2. Simulate distribution over time
    # -------------------------

    probs = np.zeros((n_steps + 1, n_states))
    probs[0] = np.array([1.0, 0.0, 0.0])  # start in S0 with prob 1

    for t in range(n_steps):
        T = transition_matrix(t)
        probs[t + 1] = probs[t] @ T  # row vector times transition matrix

    # -------------------------
    # 3. Set up Matplotlib figure for animation
    # -------------------------

    fig, (ax_bar, ax_heat) = plt.subplots(1, 2, figsize=(10, 4))
    
    # Left subplot: probability bars
    bars = ax_bar.bar(state_labels, probs[0], width=0.6)
    ax_bar.set_ylim(0, 1.0)
    ax_bar.set_ylabel("Probability", fontsize=11)
    ax_bar.set_xlabel("State", fontsize=11)
    
    # minimalist style
    ax_bar.spines["top"].set_visible(False)
    ax_bar.spines["right"].set_visible(False)
    ax_bar.spines["left"].set_position(("outward", 5))
    ax_bar.spines["bottom"].set_position(("outward", 5))
    ax_bar.tick_params(direction="out")
    
    # Right subplot: transition matrix heatmap
    T_init = transition_matrix(0)
    im = ax_heat.imshow(T_init, cmap="YlOrRd", vmin=0, vmax=1.0, aspect="auto")
    
    # Add colorbar
    cbar = fig.colorbar(im, ax=ax_heat, fraction=0.046, pad=0.04)
    cbar.set_label("Probability", rotation=270, labelpad=15, fontsize=10)
    
    # Set labels
    ax_heat.set_xticks(range(n_states))
    ax_heat.set_yticks(range(n_states))
    ax_heat.set_xticklabels(state_labels)
    ax_heat.set_yticklabels(state_labels)
    ax_heat.set_xlabel("To State", fontsize=11)
    ax_heat.set_ylabel("From State", fontsize=11)
    ax_heat.set_title("Transition Matrix", fontsize=11, pad=10)
    
    # Add text annotations for each cell
    text_annotations = []
    for i in range(n_states):
        row_texts = []
        for j in range(n_states):
            text = ax_heat.text(j, i, f"{T_init[i, j]:.2f}",
                               ha="center", va="center",
                               color="black" if T_init[i, j] < 0.5 else "white",
                               fontsize=10, weight="bold")
            row_texts.append(text)
        text_annotations.append(row_texts)
    
    # Main title
    fig.suptitle("Stage-dependent Markov Chain – step 0", fontsize=13, weight="bold")
    
    fig.tight_layout()
    fig.subplots_adjust(top=0.92)

    def update(frame: int):
        # frame is the time step
        p = probs[frame]
        for rect, val in zip(bars, p):
            rect.set_height(val)

        T = transition_matrix(max(frame - 1, 0))
        
        # Update heatmap
        im.set_data(T)
        
        # Update text annotations
        for i in range(n_states):
            for j in range(n_states):
                text_annotations[i][j].set_text(f"{T[i, j]:.2f}")
                # Adjust text color based on background
                text_annotations[i][j].set_color("black" if T[i, j] < 0.5 else "white")
        
        # Update title
        fig.suptitle(f"Stage-dependent Markov Chain – step {frame}", 
                    fontsize=13, weight="bold")

        return list(bars) + [im] + [text for row in text_annotations for text in row]

    # Add pause at end
    animated_frames = n_steps + 1
    pause_frames = 10  # 2 seconds at 5fps
    total_frames = animated_frames + pause_frames
    
    def update_with_pause(frame):
        actual_frame = min(frame, animated_frames - 1)
        return update(actual_frame)
    
    anim = FuncAnimation(
        fig,
        update_with_pause,
        frames=total_frames,
        interval=300,
        blit=True,
    )

    # -------------------------
    # 4. Save as GIF
    # -------------------------

    writer = PillowWriter(fps=5)
    anim.save(filename, writer=writer)

    plt.close(fig)


def make_cloze_sentences_gif(filename="markov_stage_cloze.gif"):
    """
    Fill-in-the-blank sentences GIF.
    Shows several examples where blank is filled with colored word.
    """
    examples = [
        {"prefix": "Mary had a little ", "word": "lamb"},
        {"prefix": "United States of ", "word": "America"},
        {"prefix": "Happy birthday to ", "word": "you"},
    ]

    frames_per_example = 30
    reveal_frame = 15          # frame index inside each example when the word appears

    fig, ax = plt.subplots(figsize=(8, 3))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    # Two text objects: prefix (black) and word (orange)
    prefix_text = ax.text(
        0.5,
        0.55,
        "",
        ha="right",
        va="center",
        fontsize=24,
        color="black"
    )
    
    word_text = ax.text(
        0.5,
        0.55,
        "",
        ha="left",
        va="center",
        fontsize=24,
        color="darkorange"
    )

    subtitle = ax.text(
        0.5,
        0.15,
        "Example 1 of {}".format(len(examples)),
        ha="center",
        va="center",
        fontsize=12,
    )

    # clean frame style
    for spine in ["top", "right", "left", "bottom"]:
        ax.spines[spine].set_visible(False)

    def update(frame: int):
        ex_idx = frame // frames_per_example
        step = frame % frames_per_example
        ex = examples[ex_idx]

        if step < reveal_frame:
            prefix_text.set_text(ex["prefix"] + "____")
            word_text.set_text("")
        else:
            prefix_text.set_text(ex["prefix"])
            word_text.set_text(ex["word"])

        subtitle.set_text(f"Example {ex_idx + 1} of {len(examples)}")

        return prefix_text, word_text, subtitle

    total_frames = frames_per_example * len(examples)

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


def make_text_prediction_chain_gif(filename="text_prediction_chain.gif"):
    """
    Text prediction as a Markov-style chain over the next word.
    Shows phrase with blank and bars for candidate words.
    """
    # ---------- 1. Setup ----------

    phrase_blank = "I would like a cup of ____"
    phrase_full = "I would like a cup of coffee"

    candidates = ["tea", "coffee", "water"]

    start_probs = np.array([0.33, 0.34, 0.33])
    end_probs = np.array([0.10, 0.80, 0.10])

    n_frames = 40
    fade_start = 30  # frame where the word in the text begins to appear

    prob_paths = np.array([
        start_probs + (end_probs - start_probs) * (t / (n_frames - 1))
        for t in range(n_frames)
    ])

    # ---------- 2. Figure ----------

    fig, ax = plt.subplots(figsize=(6, 4))
    bars = ax.bar(candidates, prob_paths[0], width=0.6)

    ax.set_ylim(0, 1.0)
    ax.set_ylabel("Probability")
    title = ax.set_title(phrase_blank)

    # minimalist style
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_position(("outward", 5))
    ax.spines["bottom"].set_position(("outward", 5))

    subtitle = ax.text(
        0.5,
        -0.18,
        "Next word prediction as a chain",
        transform=ax.transAxes,
        ha="center",
        va="center",
        fontsize=10,
    )

    for rect in bars:
        rect.set_edgecolor("black")

    # ---------- 3. Update function ----------

    def update(frame: int):
        probs = prob_paths[frame]

        for rect, p in zip(bars, probs):
            rect.set_height(p)

        # highlight the most likely word
        max_idx = int(np.argmax(probs))
        for i, rect in enumerate(bars):
            if i == max_idx:
                rect.set_facecolor("tab:orange")
            else:
                rect.set_facecolor("0.8")

        # update text as the chain gains confidence
        if frame < fade_start:
            title.set_text(phrase_blank)
        else:
            title.set_text(phrase_full)

        return list(bars) + [title, subtitle]

    # ---------- 4. Animation ----------

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
    print("Creating Markov chain learning visualizations...")
    make_stage_dependent_markov_gif()
    print("  ✓ stage_dependent_markov.gif")
    make_cloze_sentences_gif()
    print("  ✓ markov_stage_cloze.gif")
    make_text_prediction_chain_gif()
    print("  ✓ text_prediction_chain.gif")
    print("Done!")
