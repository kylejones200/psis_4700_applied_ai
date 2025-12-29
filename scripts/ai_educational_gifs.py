"""
AI Educational Visualizations
Creates 10 educational GIFs for teaching AI concepts
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from matplotlib.patches import Circle, FancyBboxPatch, FancyArrowPatch
from matplotlib.collections import LineCollection

plt.rcParams["font.family"] = "serif"


def make_prompt_refinement_gif(filename="prompt_refinement.gif"):
    """Shows how prompts improve iteratively."""
    
    prompts = [
        {"text": "Write essay", "quality": 0.3},
        {"text": "Write essay about AI", "quality": 0.5},
        {"text": "Write 500-word essay\nabout AI ethics", "quality": 0.7},
        {"text": "Write 500-word essay about\nAI ethics with examples\nand citations", "quality": 0.9},
    ]
    
    frames_per_prompt = 20
    n_frames = len(prompts) * frames_per_prompt
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
    
    # Left: prompt text
    ax1.set_xlim(0, 1)
    ax1.set_ylim(0, 1)
    ax1.axis("off")
    ax1.set_title("Prompt Evolution", fontsize=12, weight="bold", pad=10)
    
    prompt_text = ax1.text(0.5, 0.5, "", ha="center", va="center", 
                           fontsize=11, wrap=True,
                           bbox=dict(boxstyle="round,pad=0.8", 
                                   facecolor="lightblue", alpha=0.3))
    
    # Right: quality meter
    ax2.set_xlim(0, 1)
    ax2.set_ylim(0, 1)
    ax2.set_title("Output Quality", fontsize=12, weight="bold", pad=10)
    ax2.set_ylabel("Quality Score", fontsize=10)
    ax2.set_xticks([])
    ax2.spines["top"].set_visible(False)
    ax2.spines["right"].set_visible(False)
    ax2.spines["bottom"].set_visible(False)
    
    bar_container = ax2.bar([0.5], [0], width=0.3, color="green", alpha=0.7)
    quality_text = ax2.text(0.5, -0.1, "0%", ha="center", fontsize=11, weight="bold")
    
    fig.tight_layout()
    
    def update(frame):
        prompt_idx = min(frame // frames_per_prompt, len(prompts) - 1)
        local_frame = frame % frames_per_prompt
        progress = local_frame / frames_per_prompt
        
        current = prompts[prompt_idx]
        prompt_text.set_text(f"v{prompt_idx + 1}\n\n{current['text']}")
        
        # Animate quality bar
        target_quality = current["quality"]
        if prompt_idx > 0:
            prev_quality = prompts[prompt_idx - 1]["quality"]
            animated_quality = prev_quality + (target_quality - prev_quality) * progress
        else:
            animated_quality = target_quality * progress
        
        bar_container[0].set_height(animated_quality)
        quality_text.set_text(f"{int(animated_quality * 100)}%")
        quality_text.set_y(animated_quality + 0.05)
        
        return [prompt_text, bar_container[0], quality_text]
    
    # Add pause at end
    animated_frames = n_frames
    pause_frames = 20  # 2 seconds at 10fps
    total_frames = animated_frames + pause_frames
    
    def update_with_pause(frame):
        actual_frame = min(frame, animated_frames - 1)
        return update(actual_frame)
    
    anim = FuncAnimation(
        fig,
        update_with_pause,
        frames=total_frames, interval=150, blit=True)

    anim.save(filename, writer=PillowWriter(fps=10))
    plt.close(fig)


def make_drift_over_time_gif(filename="drift_over_time.gif"):
    """Shows model performance degrading over time."""
    
    n_points = 50
    time = np.linspace(0, 1, n_points)
    
    # Accuracy starts high, drifts down
    accuracy = 0.95 - 0.3 * (time ** 2) + 0.05 * np.random.randn(n_points)
    accuracy = np.clip(accuracy, 0.5, 1.0)
    
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.set_xlim(0, 1)
    ax.set_ylim(0.4, 1.05)
    ax.set_xlabel("Time", fontsize=11)
    ax.set_ylabel("Model Accuracy", fontsize=11)
    ax.set_title("Model Drift Over Time", fontsize=13, weight="bold", pad=15)
    
    # Threshold line
    ax.axhline(0.8, color="red", linestyle="--", linewidth=2, 
              label="Acceptable threshold", alpha=0.7)
    
    line, = ax.plot([], [], 'b-', linewidth=2, label="Model performance")
    point, = ax.plot([], [], 'ro', markersize=8)
    
    # Warning text
    warning = ax.text(0.5, 0.5, "", ha="center", va="center",
                     fontsize=12, color="red", weight="bold",
                     transform=ax.transAxes, alpha=0)
    
    ax.legend(loc="upper right", frameon=False)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    # Grid removed for cleaner look
    
    def update(frame):
        idx = min(frame, n_points - 1)
        line.set_data(time[:idx+1], accuracy[:idx+1])
        point.set_data([time[idx]], [accuracy[idx]])
        
        # Show warning when below threshold
        if accuracy[idx] < 0.8:
            warning.set_text("⚠ DRIFT DETECTED")
            warning.set_alpha(0.8)
        else:
            warning.set_alpha(0)
        
        return [line, point, warning]
    
    # Add pause at end
    animated_frames = n_points
    pause_frames = 20  # 2 seconds at 10fps
    total_frames = animated_frames + pause_frames
    
    def update_with_pause(frame):
        actual_frame = min(frame, animated_frames - 1)
        return update(actual_frame)
    
    anim = FuncAnimation(
        fig,
        update_with_pause,
        frames=total_frames, interval=100, blit=True)

    anim.save(filename, writer=PillowWriter(fps=10))
    plt.close(fig)


def make_clustering_emergence_gif(filename="clustering_emergence.gif"):
    """Shows data points forming clusters."""
    
    np.random.seed(42)
    n_per_cluster = 30
    
    # Three clusters
    cluster1 = np.random.randn(n_per_cluster, 2) * 0.3 + [2, 2]
    cluster2 = np.random.randn(n_per_cluster, 2) * 0.3 + [5, 3]
    cluster3 = np.random.randn(n_per_cluster, 2) * 0.3 + [3.5, 5]
    
    all_points = np.vstack([cluster1, cluster2, cluster3])
    n_total = len(all_points)
    
    fig, ax = plt.subplots(figsize=(7, 7))
    ax.set_xlim(0, 7)
    ax.set_ylim(0, 7)
    ax.set_xlabel("Feature 1", fontsize=11)
    ax.set_ylabel("Feature 2", fontsize=11)
    ax.set_title("K-Means Clustering", fontsize=13, weight="bold", pad=15)
    ax.set_aspect('equal')
    
    scatter = ax.scatter([], [], c=[], cmap="viridis", s=50, alpha=0.6, edgecolors='black', linewidth=0.5)
    centroids = ax.scatter([], [], c='red', s=200, marker='X', edgecolors='black', linewidth=2, label="Centroids")
    
    ax.legend()
    # Grid removed for cleaner look
    
    def update(frame):
        # Gradually show points and cluster assignment
        show_n = min(int((frame / 60) * n_total), n_total)
        
        if show_n > 0:
            points = all_points[:show_n]
            
            # Assign colors based on which cluster each point belongs to
            colors = np.zeros(show_n)
            colors[:min(show_n, n_per_cluster)] = 0
            colors[n_per_cluster:min(show_n, 2*n_per_cluster)] = 1
            colors[2*n_per_cluster:show_n] = 2
            
            scatter.set_offsets(points)
            scatter.set_array(colors)
            
            # Show centroids after half the animation
            if frame > 30:
                centroids.set_offsets([[2, 2], [5, 3], [3.5, 5]])
        
        return [scatter, centroids]
    
    # Add pause at end
    animated_frames = 60
    pause_frames = 20  # 2 seconds at 10fps
    total_frames = animated_frames + pause_frames
    
    def update_with_pause(frame):
        actual_frame = min(frame, animated_frames - 1)
        return update(actual_frame)
    
    anim = FuncAnimation(
        fig,
        update_with_pause,
        frames=total_frames, interval=100, blit=True)

    anim.save(filename, writer=PillowWriter(fps=10))
    plt.close(fig)


def make_regression_bestfit_gif(filename="regression_bestfit.gif"):
    """Shows line fitting to data."""
    
    np.random.seed(42)
    n_points = 30
    x = np.linspace(0, 10, n_points)
    y_true = 2 * x + 1
    y = y_true + np.random.randn(n_points) * 2
    
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.set_xlim(-0.5, 10.5)
    ax.set_ylim(-2, 23)
    ax.set_xlabel("X", fontsize=11)
    ax.set_ylabel("Y", fontsize=11)
    ax.set_title("Linear Regression", fontsize=13, weight="bold", pad=15)
    
    ax.scatter(x, y, color='blue', s=50, alpha=0.6, label="Data points")
    line, = ax.plot([], [], 'r-', linewidth=2, label="Best fit line")
    
    ax.legend()
    # Grid removed for cleaner look
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    
    def update(frame):
        # Animate line rotating to best fit
        progress = frame / 60
        
        # Start with slope 0, move to optimal slope 2
        slope = 2 * progress
        intercept = 1 + (10 - 1) * (1 - progress)  # Start high, move to 1
        
        y_line = slope * x + intercept
        line.set_data(x, y_line)
        
        return [line]
    
    # Add pause at end
    animated_frames = 60
    pause_frames = 40  # 2 seconds at 20fps
    total_frames = animated_frames + pause_frames
    
    def update_with_pause(frame):
        actual_frame = min(frame, animated_frames - 1)
        return update(actual_frame)
    
    anim = FuncAnimation(
        fig,
        update_with_pause,
        frames=total_frames, interval=50, blit=True)

    anim.save(filename, writer=PillowWriter(fps=20))
    plt.close(fig)


def make_anomaly_detection_gif(filename="anomaly_detection.gif"):
    """Highlights outliers in data."""
    
    np.random.seed(42)
    n_normal = 100
    n_anomalies = 5
    
    # Normal data
    normal = np.random.randn(n_normal, 2) * 1.5 + [5, 5]
    
    # Anomalies
    anomalies = np.array([[1, 1], [9, 9], [1, 9], [9, 1], [10, 5]])
    
    fig, ax = plt.subplots(figsize=(7, 7))
    ax.set_xlim(-1, 11)
    ax.set_ylim(-1, 11)
    ax.set_xlabel("Feature 1", fontsize=11)
    ax.set_ylabel("Feature 2", fontsize=11)
    ax.set_title("Anomaly Detection", fontsize=13, weight="bold", pad=15)
    ax.set_aspect('equal')
    
    normal_scatter = ax.scatter(normal[:, 0], normal[:, 1], 
                               c='blue', s=30, alpha=0.5, label="Normal")
    anomaly_scatter = ax.scatter([], [], c='red', s=100, marker='X', 
                                label="Anomalies", edgecolors='black', linewidth=2)
    
    # Detection circle
    circle = Circle((5, 5), 4, fill=False, edgecolor='green', 
                   linewidth=2, linestyle='--', alpha=0)
    ax.add_patch(circle)
    
    ax.legend()
    # Grid removed for cleaner look
    
    def update(frame):
        if frame < 30:
            # Show normal distribution
            circle.set_alpha(0)
            anomaly_scatter.set_offsets(np.empty((0, 2)))
        elif frame < 50:
            # Show detection boundary
            circle.set_alpha(0.7)
            anomaly_scatter.set_offsets(np.empty((0, 2)))
        else:
            # Highlight anomalies
            circle.set_alpha(0.7)
            show_n = min(frame - 50, n_anomalies)
            anomaly_scatter.set_offsets(anomalies[:show_n])
        
        return [normal_scatter, anomaly_scatter, circle]
    
    # Add pause at end
    animated_frames = 70
    pause_frames = 20  # 2 seconds at 10fps
    total_frames = animated_frames + pause_frames
    
    def update_with_pause(frame):
        actual_frame = min(frame, animated_frames - 1)
        return update(actual_frame)
    
    anim = FuncAnimation(
        fig,
        update_with_pause,
        frames=total_frames, interval=100, blit=True)

    anim.save(filename, writer=PillowWriter(fps=10))
    plt.close(fig)


def make_sequence_vs_random_gif(filename="sequence_vs_random.gif"):
    """Shows pattern vs noise."""
    
    n_points = 50
    t = np.linspace(0, 4*np.pi, n_points)
    
    # Sequence: sine wave
    sequence = np.sin(t)
    
    # Random: noise
    np.random.seed(42)
    random = np.random.randn(n_points) * 0.5
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(9, 6))
    
    # Sequence
    ax1.set_xlim(0, n_points)
    ax1.set_ylim(-1.5, 1.5)
    ax1.set_ylabel("Value", fontsize=10)
    ax1.set_title("Sequence (Predictable Pattern)", fontsize=11, weight="bold")
    line1, = ax1.plot([], [], 'b-', linewidth=2)
    # Grid removed for cleaner look
    ax1.spines["top"].set_visible(False)
    ax1.spines["right"].set_visible(False)
    
    # Random
    ax2.set_xlim(0, n_points)
    ax2.set_ylim(-1.5, 1.5)
    ax2.set_xlabel("Time", fontsize=10)
    ax2.set_ylabel("Value", fontsize=10)
    ax2.set_title("Random Noise (No Pattern)", fontsize=11, weight="bold")
    line2, = ax2.plot([], [], 'r-', linewidth=2)
    # Grid removed for cleaner look
    ax2.spines["top"].set_visible(False)
    ax2.spines["right"].set_visible(False)
    
    fig.tight_layout()
    
    def update(frame):
        idx = min(frame, n_points - 1)
        line1.set_data(range(idx+1), sequence[:idx+1])
        line2.set_data(range(idx+1), random[:idx+1])
        return [line1, line2]
    
    # Add pause at end
    animated_frames = n_points
    pause_frames = 20  # 2 seconds at 10fps
    total_frames = animated_frames + pause_frames
    
    def update_with_pause(frame):
        actual_frame = min(frame, animated_frames - 1)
        return update(actual_frame)
    
    anim = FuncAnimation(
        fig,
        update_with_pause,
        frames=total_frames, interval=100, blit=True)

    anim.save(filename, writer=PillowWriter(fps=10))
    plt.close(fig)


def make_forecast_vs_reality_gif(filename="forecast_vs_reality.gif"):
    """Shows predictions vs actual values."""
    
    n_points = 40
    t = np.linspace(0, 3*np.pi, n_points)
    
    # Reality: actual values
    reality = np.sin(t) + 0.5 * np.sin(2*t)
    
    # Forecast: lagged and smoothed
    forecast = np.roll(reality, 2) * 0.9
    
    # Split point for forecast
    split = 25
    
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.set_xlim(0, n_points)
    ax.set_ylim(-2, 2)
    ax.set_xlabel("Time", fontsize=11)
    ax.set_ylabel("Value", fontsize=11)
    ax.set_title("Forecast vs Reality", fontsize=13, weight="bold", pad=15)
    
    line_history, = ax.plot([], [], 'b-', linewidth=2, label="Historical data")
    line_forecast, = ax.plot([], [], 'g--', linewidth=2, label="Forecast")
    line_reality, = ax.plot([], [], 'r-', linewidth=2, label="Actual")
    
    ax.axvline(split, color='gray', linestyle=':', linewidth=1, alpha=0.5)
    ax.legend(loc='upper right')
    # Grid removed for cleaner look
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    
    def update(frame):
        if frame <= split:
            # Show historical data
            line_history.set_data(range(frame), reality[:frame])
            line_forecast.set_data([], [])
            line_reality.set_data([], [])
        else:
            # Show forecast and reality
            line_history.set_data(range(split), reality[:split])
            line_forecast.set_data(range(split, frame), forecast[split:frame])
            line_reality.set_data(range(split, frame), reality[split:frame])
        
        return [line_history, line_forecast, line_reality]
    
    # Add pause at end
    animated_frames = n_points
    pause_frames = 16  # 2 seconds at 8fps
    total_frames = animated_frames + pause_frames
    
    def update_with_pause(frame):
        actual_frame = min(frame, animated_frames - 1)
        return update(actual_frame)
    
    anim = FuncAnimation(
        fig,
        update_with_pause,
        frames=total_frames, interval=150, blit=True)

    anim.save(filename, writer=PillowWriter(fps=8))
    plt.close(fig)


def make_bias_in_training_gif(filename="bias_in_training.gif"):
    """Shows skewed distribution in training data."""
    
    np.random.seed(42)
    
    # Balanced data
    balanced_a = np.random.randn(50, 2) * 0.5 + [2, 2]
    balanced_b = np.random.randn(50, 2) * 0.5 + [5, 5]
    
    # Biased data (more of class A)
    biased_a = np.random.randn(80, 2) * 0.5 + [2, 2]
    biased_b = np.random.randn(20, 2) * 0.5 + [5, 5]
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 5))
    
    # Balanced
    ax1.set_xlim(0, 7)
    ax1.set_ylim(0, 7)
    ax1.set_xlabel("Feature 1", fontsize=10)
    ax1.set_ylabel("Feature 2", fontsize=10)
    ax1.set_title("Balanced Dataset\n(50% A, 50% B)", fontsize=11, weight="bold")
    ax1.set_aspect('equal')
    scatter1a = ax1.scatter([], [], c='blue', s=40, alpha=0.6, label="Class A")
    scatter1b = ax1.scatter([], [], c='red', s=40, alpha=0.6, label="Class B")
    ax1.legend()
    # Grid removed for cleaner look
    
    # Biased
    ax2.set_xlim(0, 7)
    ax2.set_ylim(0, 7)
    ax2.set_xlabel("Feature 1", fontsize=10)
    ax2.set_ylabel("Feature 2", fontsize=10)
    ax2.set_title("Biased Dataset\n(80% A, 20% B)", fontsize=11, weight="bold", color='red')
    ax2.set_aspect('equal')
    scatter2a = ax2.scatter([], [], c='blue', s=40, alpha=0.6, label="Class A")
    scatter2b = ax2.scatter([], [], c='red', s=40, alpha=0.6, label="Class B")
    ax2.legend()
    # Grid removed for cleaner look
    
    fig.tight_layout()
    
    def update(frame):
        progress = frame / 60
        
        # Balanced
        n1a = int(50 * progress)
        n1b = int(50 * progress)
        scatter1a.set_offsets(balanced_a[:n1a])
        scatter1b.set_offsets(balanced_b[:n1b])
        
        # Biased
        n2a = int(80 * progress)
        n2b = int(20 * progress)
        scatter2a.set_offsets(biased_a[:n2a])
        scatter2b.set_offsets(biased_b[:n2b])
        
        return [scatter1a, scatter1b, scatter2a, scatter2b]
    
    # Add pause at end
    animated_frames = 60
    pause_frames = 20  # 2 seconds at 10fps
    total_frames = animated_frames + pause_frames
    
    def update_with_pause(frame):
        actual_frame = min(frame, animated_frames - 1)
        return update(actual_frame)
    
    anim = FuncAnimation(
        fig,
        update_with_pause,
        frames=total_frames, interval=100, blit=True)

    anim.save(filename, writer=PillowWriter(fps=10))
    plt.close(fig)


def make_human_in_loop_gif(filename="human_in_loop.gif"):
    """Shows human feedback cycle."""
    
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    
    # Nodes
    nodes = {
        "data": (0.5, 0.8),
        "model": (0.2, 0.5),
        "output": (0.5, 0.2),
        "human": (0.8, 0.5),
    }
    
    labels = {
        "data": "Training\nData",
        "model": "AI\nModel",
        "output": "Predictions",
        "human": "Human\nReview",
    }
    
    # Draw nodes
    circles = {}
    texts = {}
    for key, (x, y) in nodes.items():
        circle = Circle((x, y), 0.08, facecolor='lightblue', 
                       edgecolor='black', linewidth=2, alpha=0)
        ax.add_patch(circle)
        circles[key] = circle
        
        text = ax.text(x, y, labels[key], ha='center', va='center',
                      fontsize=10, weight='bold', alpha=0)
        texts[key] = text
    
    # Arrows
    arrows = []
    arrow_pairs = [
        ("data", "model"),
        ("model", "output"),
        ("output", "human"),
        ("human", "data"),  # feedback loop
    ]
    
    for start, end in arrow_pairs:
        x1, y1 = nodes[start]
        x2, y2 = nodes[end]
        arrow = FancyArrowPatch((x1, y1), (x2, y2),
                               arrowstyle='->', mutation_scale=20,
                               linewidth=2, color='green', alpha=0)
        ax.add_patch(arrow)
        arrows.append(arrow)
    
    title = ax.text(0.5, 0.95, "Human-in-the-Loop Learning", 
                   ha='center', fontsize=14, weight='bold')
    
    def update(frame):
        # Show nodes first
        if frame < 20:
            progress = frame / 20
            for circle in circles.values():
                circle.set_alpha(progress)
            for text in texts.values():
                text.set_alpha(progress)
        else:
            for circle in circles.values():
                circle.set_alpha(1)
            for text in texts.values():
                text.set_alpha(1)
            
            # Animate arrows in sequence
            arrow_idx = (frame - 20) // 10
            if arrow_idx < len(arrows):
                arrows[arrow_idx].set_alpha(0.8)
        
        return list(circles.values()) + list(texts.values()) + arrows + [title]
    
    # Add pause at end
    animated_frames = 80
    pause_frames = 20  # 2 seconds at 10fps
    total_frames = animated_frames + pause_frames
    
    def update_with_pause(frame):
        actual_frame = min(frame, animated_frames - 1)
        return update(actual_frame)
    
    anim = FuncAnimation(
        fig,
        update_with_pause,
        frames=total_frames, interval=100, blit=True)

    anim.save(filename, writer=PillowWriter(fps=10))
    plt.close(fig)


def make_cost_vs_value_gif(filename="cost_vs_value.gif"):
    """Shows optimization tradeoff curve."""
    
    # Cost and value curves
    x = np.linspace(0, 10, 100)
    cost = x ** 1.5  # Cost increases rapidly
    value = 10 * (1 - np.exp(-x/2))  # Value plateaus
    
    # Find intersection/optimal point
    net_value = value - cost
    optimal_idx = np.argmax(net_value)
    optimal_x = x[optimal_idx]
    
    fig, ax = plt.subplots(figsize=(9, 6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 15)
    ax.set_xlabel("Model Complexity", fontsize=11)
    ax.set_ylabel("Value ($)", fontsize=11)
    ax.set_title("Cost vs Value Tradeoff", fontsize=13, weight="bold", pad=15)
    
    line_value, = ax.plot([], [], 'g-', linewidth=3, label="Business Value")
    line_cost, = ax.plot([], [], 'r-', linewidth=3, label="Development Cost")
    line_net, = ax.plot([], [], 'b--', linewidth=2, alpha=0.5, label="Net Value")
    
    optimal_line = ax.axvline(optimal_x, color='purple', linestyle=':', 
                              linewidth=2, alpha=0, label="Optimal Point")
    
    ax.legend(loc='upper left', fontsize=10)
    # Grid removed for cleaner look
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    
    def update(frame):
        idx = min(int((frame / 80) * 100), 99)
        
        line_value.set_data(x[:idx], value[:idx])
        line_cost.set_data(x[:idx], cost[:idx])
        line_net.set_data(x[:idx], net_value[:idx])
        
        # Show optimal point after curves are drawn
        if frame > 60:
            optimal_line.set_alpha(0.7)
        
        return [line_value, line_cost, line_net, optimal_line]
    
    # Add pause at end
    animated_frames = 80
    pause_frames = 20  # 2 seconds at 10fps
    total_frames = animated_frames + pause_frames
    
    def update_with_pause(frame):
        actual_frame = min(frame, animated_frames - 1)
        return update(actual_frame)
    
    anim = FuncAnimation(
        fig,
        update_with_pause,
        frames=total_frames, interval=100, blit=True)

    anim.save(filename, writer=PillowWriter(fps=10))
    plt.close(fig)


if __name__ == "__main__":
    print("Creating AI educational GIFs...")
    print("This may take a few minutes...")
    
    make_prompt_refinement_gif()
    print("  ✓ prompt_refinement.gif")
    
    make_drift_over_time_gif()
    print("  ✓ drift_over_time.gif")
    
    make_clustering_emergence_gif()
    print("  ✓ clustering_emergence.gif")
    
    make_regression_bestfit_gif()
    print("  ✓ regression_bestfit.gif")
    
    make_anomaly_detection_gif()
    print("  ✓ anomaly_detection.gif")
    
    make_sequence_vs_random_gif()
    print("  ✓ sequence_vs_random.gif")
    
    make_forecast_vs_reality_gif()
    print("  ✓ forecast_vs_reality.gif")
    
    make_bias_in_training_gif()
    print("  ✓ bias_in_training.gif")
    
    make_human_in_loop_gif()
    print("  ✓ human_in_loop.gif")
    
    make_cost_vs_value_gif()
    print("  ✓ cost_vs_value.gif")
    
    print("\nDone! Created 10 educational GIFs.")
