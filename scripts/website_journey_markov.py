"""
E-commerce Website Journey as Markov Chain
Shows user progression through website states with clear funnel visualization
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch
from matplotlib.patches import Wedge

plt.rcParams["font.family"] = "serif"


def make_website_journey_gif(filename="website_journey_markov.gif"):
    """
    Website journey with clear hierarchical funnel layout.
    Shows conversion funnel: Home → Product → Cart → Purchase / Exit
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
        # Purchase  (absorbing)
        [0.00, 0.00, 0.00, 0.90, 0.10],
        # Exit      (absorbing)
        [0.00, 0.00, 0.00, 0.00, 1.00],
    ])

    n_steps = 50

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
    # 3. Improved funnel layout (left to right flow)
    # -------------------------

    # Vertical funnel positions - clear hierarchy
    positions = {
        "Home":     (0.15, 0.75),
        "Product":  (0.35, 0.75),
        "Cart":     (0.55, 0.75),
        "Purchase": (0.75, 0.85),  # Success path (higher)
        "Exit":     (0.75, 0.40),  # Drop-off path (lower)
    }
    
    # Box colors - green for conversion, red for exit
    colors = {
        "Home": "#e8f4f8",
        "Product": "#c8e6f0",
        "Cart": "#a8d8e8",
        "Purchase": "#90ee90",  # Light green (success!)
        "Exit": "#ffcccb",  # Light red (failure)
    }
    
    # Box sizes (wider = earlier in funnel)
    box_sizes = {
        "Home": (0.12, 0.12),
        "Product": (0.12, 0.12),
        "Cart": (0.12, 0.12),
        "Purchase": (0.13, 0.10),
        "Exit": (0.13, 0.10),
    }

    # -------------------------
    # 4. Set up figure with legend
    # -------------------------

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_xlim(0, 1)
    ax.set_ylim(0.2, 1.0)
    ax.axis("off")

    # Title
    title = ax.text(
        0.5,
        0.97,
        "E-commerce Conversion Funnel",
        ha="center",
        va="top",
        fontsize=15,
        weight="bold"
    )
    
    # Subtitle showing current state
    subtitle = ax.text(
        0.5,
        0.92,
        "Customer Journey: Step 0",
        ha="center",
        va="top",
        fontsize=11,
        color="#555"
    )

    # Draw state boxes with labels and conversion rates
    boxes = {}
    texts = {}
    for state, (x, y) in positions.items():
        w, h = box_sizes[state]
        
        box = FancyBboxPatch(
            (x - w/2, y - h/2),
            w,
            h,
            boxstyle="round,pad=0.015",
            edgecolor="black",
            facecolor=colors[state],
            linewidth=2.5,
            zorder=2
        )
        ax.add_patch(box)
        boxes[state] = box
        
        # State label
        text = ax.text(x, y + 0.02, state, ha="center", va="center",
                      fontsize=12, weight="bold", zorder=3)
        texts[state] = text
        
        # Add step number for main funnel
        if state in ["Home", "Product", "Cart"]:
            step_num = ["Home", "Product", "Cart"].index(state) + 1
            ax.text(x, y - 0.06, f"Step {step_num}", ha="center", va="center",
                   fontsize=9, style="italic", color="#666", zorder=3)

    # Draw funnel flow arrows (main path)
    arrow_pairs = [
        ("Home", "Product", "70%"),
        ("Product", "Cart", "30%"),
        ("Cart", "Purchase", "30%"),
    ]
    
    arrows = []
    for start, end, label in arrow_pairs:
        x1, y1 = positions[start]
        x2, y2 = positions[end]
        
        # Calculate arrow start and end to connect boxes
        w1, _ = box_sizes[start]
        w2, _ = box_sizes[end]
        arrow_start = (x1 + w1/2, y1)
        arrow_end = (x2 - w2/2, y2)
        
        arrow = FancyArrowPatch(
            arrow_start, arrow_end,
            arrowstyle='->,head_width=0.4,head_length=0.3',
            mutation_scale=20,
            linewidth=2.5,
            color='#2e7d32',
            alpha=0.6,
            zorder=1
        )
        ax.add_patch(arrow)
        arrows.append(arrow)
        
        # Add conversion rate label
        mid_x = (arrow_start[0] + arrow_end[0]) / 2
        mid_y = (arrow_start[1] + arrow_end[1]) / 2 + 0.08
        ax.text(mid_x, mid_y, label, ha="center", va="bottom",
               fontsize=9, weight="bold", color="#2e7d32",
               bbox=dict(boxstyle="round,pad=0.3", facecolor="white", 
                        edgecolor="#2e7d32", linewidth=1.5))

    # Draw exit paths (drop-off arrows)
    exit_arrows = []
    exit_paths = [
        ("Home", "Exit", "20%", 0.15),
        ("Product", "Exit", "15%", 0.35),
        ("Cart", "Exit", "10%", 0.55),
    ]
    
    for start, end, label, x_pos in exit_paths:
        _, y1 = positions[start]
        _, y2 = positions[end]
        
        # Curved arrow pointing down
        arrow = FancyArrowPatch(
            (x_pos, y1 - 0.06), (0.75 - 0.065, y2 + 0.05),
            arrowstyle='->,head_width=0.3,head_length=0.2',
            mutation_scale=15,
            linewidth=1.5,
            color='#c62828',
            alpha=0.4,
            connectionstyle="arc3,rad=-.3",
            zorder=1
        )
        ax.add_patch(arrow)
        exit_arrows.append(arrow)

    # Moving user indicator (larger, more visible)
    user_dot = Circle((0.15, 0.75), radius=0.025, 
                     color="orange", edgecolor="black", 
                     linewidth=2, zorder=10)
    ax.add_patch(user_dot)
    
    # User trail
    trail, = ax.plot([], [], "o-", color="orange", alpha=0.3, 
                    markersize=5, lw=2, zorder=9)

    # Legend
    legend_y = 0.25
    ax.text(0.05, legend_y, "Legend:", fontsize=10, weight="bold")
    ax.text(0.05, legend_y - 0.04, "→ Conversion Flow", fontsize=9, color="#2e7d32", weight="bold")
    ax.text(0.05, legend_y - 0.07, "→ Drop-off", fontsize=9, color="#c62828", weight="bold")
    ax.text(0.28, legend_y - 0.04, "● Current Position", fontsize=9, color="orange", weight="bold")

    # Stats counter
    stats_text = ax.text(0.65, legend_y - 0.01, "", ha="left", va="top",
                        fontsize=9, family="monospace",
                        bbox=dict(boxstyle="round,pad=0.4", 
                                facecolor="white", edgecolor="gray"))

    def update(frame: int):
        step = min(frame, len(path_idx) - 1)
        state_name = states[path_idx[step]]
        x, y = positions[state_name]

        # Update user position
        user_dot.center = (x, y)

        # Update trail (show last 8 positions)
        trail_length = min(8, step + 1)
        xs = [positions[states[path_idx[max(0, step - trail_length + i + 1)]]][0] 
             for i in range(trail_length)]
        ys = [positions[states[path_idx[max(0, step - trail_length + i + 1)]]][1] 
             for i in range(trail_length)]
        trail.set_data(xs, ys)

        # Update subtitle
        subtitle.set_text(f"Customer Journey: Step {step} → {state_name}")
        
        # Highlight current box
        for state, box in boxes.items():
            if state == state_name:
                box.set_linewidth(4)
                box.set_edgecolor("orange")
            else:
                box.set_linewidth(2.5)
                box.set_edgecolor("black")
        
        # Update stats
        visited_states = [states[i] for i in path_idx[:step+1]]
        purchases = visited_states.count("Purchase")
        exits = visited_states.count("Exit")
        in_progress = state_name not in ["Purchase", "Exit"]
        
        stats_text.set_text(
            f"Visits: {step}\n"
            f"Purchases: {purchases}\n"
            f"Exits: {exits}\n"
            f"Status: {'Active' if in_progress else 'Complete'}"
        )

        return [user_dot, trail, subtitle, stats_text] + list(boxes.values())

    # Add pause
    animated_frames = n_steps
    pause_frames = 16  # 2 seconds at 8fps
    total_frames = animated_frames + pause_frames
    
    def update_with_pause(frame):
        actual_frame = min(frame, animated_frames - 1)
        return update(actual_frame)
    
    anim = FuncAnimation(
        fig,
        update_with_pause,
        frames=total_frames,
        interval=200,
        blit=True,
    )

    writer = PillowWriter(fps=8)
    anim.save(filename, writer=writer)
    plt.close(fig)
    print(f"Saved {filename}")


if __name__ == "__main__":
    print("Creating improved website journey visualization...")
    make_website_journey_gif()
    print("Done!")
