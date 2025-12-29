"""
Health States and Website Journey Markov Chains
Two practical examples of Markov chains for non-technical audiences
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from matplotlib.patches import FancyBboxPatch, Circle

plt.rcParams["font.family"] = "serif"


def make_health_states_gif(filename="health_states_markov.gif"):
    """
    Health states GIF: Healthy, Sick, Recovered.
    The distribution shifts over time as if you had a simple Markov model.
    """
    # -------------------------
    # 1. Define stage-dependent health transitions
    # -------------------------

    n_states = 3
    n_steps = 30
    labels = ["Healthy", "Sick", "Recovered"]

    def T_health(t: int) -> np.ndarray:
        """Transition matrix for health states at step t."""
        if t < 10:
            # Mostly healthy, small chance to get sick
            return np.array([
                [0.90, 0.10, 0.00],
                [0.00, 0.85, 0.15],
                [0.00, 0.00, 1.00],
            ])
        elif t < 20:
            # Higher chance of recovery
            return np.array([
                [0.90, 0.10, 0.00],
                [0.05, 0.20, 0.75],
                [0.00, 0.00, 1.00],
            ])
        else:
            # Recovery dominates
            return np.array([
                [0.95, 0.05, 0.00],
                [0.05, 0.10, 0.85],
                [0.00, 0.00, 1.00],
            ])

    # -------------------------
    # 2. Simulate probability paths
    # -------------------------

    probs = np.zeros((n_steps + 1, n_states))
    probs[0] = np.array([1.0, 0.0, 0.0])  # start fully healthy

    for t in range(n_steps):
        probs[t + 1] = probs[t] @ T_health(t)

    # -------------------------
    # 3. Set up figure
    # -------------------------

    fig, ax = plt.subplots(figsize=(7, 4.5))

    bars = ax.bar(labels, probs[0], width=0.6, edgecolor="black")

    ax.set_ylim(0, 1.0)
    ax.set_ylabel("Probability")
    title = ax.set_title("Health states over time – step 0", pad=20)

    # minimalist style
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_position(("outward", 5))
    ax.spines["bottom"].set_position(("outward", 5))

    # text tag for current dominant state (moved to upper right)
    state_text = ax.text(
        0.98,
        0.95,
        "Most likely: Healthy",
        transform=ax.transAxes,
        ha="right",
        va="top",
        fontsize=9,
        bbox=dict(boxstyle="round,pad=0.4", facecolor="white", edgecolor="gray", alpha=0.8)
    )

    subtitle = ax.text(
        0.5,
        -0.15,
        "Healthy → Sick → Recovered as a Markov process",
        transform=ax.transAxes,
        ha="center",
        va="center",
        fontsize=9,
    )
    
    fig.tight_layout()

    def update(frame: int):
        p = probs[frame]
        for rect, val in zip(bars, p):
            rect.set_height(val)

        # highlight most likely state
        max_idx = int(np.argmax(p))
        for i, rect in enumerate(bars):
            if i == max_idx:
                rect.set_facecolor("tab:green" if labels[i] == "Healthy"
                                   else "tab:red" if labels[i] == "Sick"
                                   else "tab:blue")
            else:
                rect.set_facecolor("0.85")

        title.set_text(f"Health states over time – step {frame}")
        state_text.set_text(f"Most likely: {labels[max_idx]}")

        return list(bars) + [title, state_text, subtitle]

    # Add pause
    animated_frames = n_steps + 1
    pause_frames = 10
    total_frames = animated_frames + pause_frames
    
    def update_with_pause(frame):
        actual_frame = min(frame, animated_frames - 1)
        return update(actual_frame)
    
    anim = FuncAnimation(
        fig,
        update_with_pause,
        frames=total_frames,
        interval=250,
        blit=True,
    )

    writer = PillowWriter(fps=5)
    anim.save(filename, writer=writer)
    plt.close(fig)


def make_website_journey_gif(filename="website_journey_markov.gif"):
    """
    Website journey GIF: Home, Product, Cart, Purchase, Exit.
    A dot walks through the site like a user's session.
    """
    # -------------------------
    # 1. States and transitions
    # -------------------------

    states = ["Home", "Product", "Cart", "Purchase", "Exit"]
    idx = {s: i for i, s in enumerate(states)}

    # Simple transition matrix: rows = from, cols = to
    T = np.array([
        # Home
        [0.10, 0.70, 0.00, 0.00, 0.20],
        # Product
        [0.05, 0.50, 0.30, 0.00, 0.15],
        # Cart
        [0.00, 0.20, 0.40, 0.30, 0.10],
        # Purchase  (absorbing into Purchase or Exit)
        [0.00, 0.00, 0.00, 0.90, 0.10],
        # Exit      (absorbing)
        [0.00, 0.00, 0.00, 0.00, 1.00],
    ])

    n_steps = 40

    # -------------------------
    # 2. Simulate a single user path
    # -------------------------

    path_idx = [idx["Home"]]
    rng = np.random.default_rng(0)

    for _ in range(n_steps - 1):
        current = path_idx[-1]
        probs = T[current]
        next_state = rng.choice(len(states), p=probs)
        path_idx.append(next_state)

    # -------------------------
    # 3. Layout for nodes
    # -------------------------

    # positions on a simple map
    positions = {
        "Home": (0.1, 0.6),
        "Product": (0.35, 0.6),
        "Cart": (0.6, 0.6),
        "Purchase": (0.85, 0.7),
        "Exit": (0.85, 0.5),
    }

    # -------------------------
    # 4. Set up figure
    # -------------------------

    fig, ax = plt.subplots(figsize=(7, 3))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    title = ax.text(
        0.5,
        0.95,
        "Website journey as a Markov chain – step 0",
        ha="center",
        va="top",
        fontsize=13,
    )

    # draw state boxes
    for state, (x, y) in positions.items():
        box = FancyBboxPatch(
            (x - 0.06, y - 0.05),
            0.12,
            0.10,
            boxstyle="round,pad=0.01",
            edgecolor="black",
            facecolor="0.95",
            linewidth=1.2,
        )
        ax.add_patch(box)
        ax.text(x, y, state, ha="center", va="center", fontsize=10)

    # moving user dot
    user_dot = Circle((0.1, 0.6), radius=0.015, color="tab:orange", zorder=5)
    ax.add_patch(user_dot)

    # path trace line
    line, = ax.plot([], [], "o-", color="tab:blue", alpha=0.3, markersize=3, lw=0.8)

    def update(frame: int):
        step = min(frame, len(path_idx) - 1)
        state_name = states[path_idx[step]]
        x, y = positions[state_name]

        user_dot.center = (x, y)

        # trace of visited nodes
        xs = [positions[states[path_idx[i]]][0] for i in range(step + 1)]
        ys = [positions[states[path_idx[i]]][1] for i in range(step + 1)]
        line.set_data(xs, ys)

        title.set_text(f"Website journey – step {step}, at '{state_name}'")

        return user_dot, line, title

    anim = FuncAnimation(
        fig,
        update,
        frames=n_steps,
        interval=300,
        blit=True,
    )

    writer = PillowWriter(fps=5)
    anim.save(filename, writer=writer)
    plt.close(fig)


if __name__ == "__main__":
    print("Creating health and website Markov chain visualizations...")
    make_health_states_gif()
    print("  ✓ health_states_markov.gif")
    make_website_journey_gif()
    print("  ✓ website_journey_markov.gif")
    print("Done!")
