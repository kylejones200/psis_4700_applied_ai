"""
Algorithmic Trading Visualization
Creates an animated GIF showing rule-based algorithmic trading with moving averages
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

plt.rcParams["font.family"] = "serif"


def _tufte_axes(ax, xlabel="", ylabel=""):
    """Apply a clean minimalist style to an axis."""
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    ax.spines["left"].set_position(("outward", 5))
    ax.spines["bottom"].set_position(("outward", 5))

    ax.tick_params(direction="out")
    return ax


def make_algorithmic_trading_gif(filename="algorithmic_trading.gif"):
    """Animated price, moving average, and rule-based trades."""

    # Synthetic price: noisy trend
    n = 300
    t = np.linspace(0, 1, n)
    rng = np.random.default_rng(42)
    steps = rng.normal(loc=0.02, scale=0.3, size=n)
    price = 100 + np.cumsum(steps)

    # Moving average
    window = 15
    ma = np.convolve(price, np.ones(window) / window, mode="same")

    # Simple rule: buy when price crosses above MA, sell when crosses below
    buy_idx = []
    sell_idx = []
    for i in range(1, n):
        if price[i - 1] <= ma[i - 1] and price[i] > ma[i]:
            buy_idx.append(i)
        elif price[i - 1] >= ma[i - 1] and price[i] < ma[i]:
            sell_idx.append(i)

    fig, ax = plt.subplots(figsize=(6, 3))
    _tufte_axes(ax, xlabel="Time", ylabel="Price")

    ax.set_xlim(0, 1)
    ax.set_ylim(price.min() - 2, price.max() + 2)

    # Static text with rule
    ax.text(
        0.98,
        0.98,
        "Rule\nBuy: price > MA\nSell: price < MA",
        transform=ax.transAxes,
        va="top",
        ha="right",
        fontsize=8,
        bbox=dict(boxstyle="round,pad=0.5", facecolor="white", edgecolor="gray", alpha=0.8)
    )

    # Lines for price and MA
    price_line, = ax.plot([], [], lw=1.2, label="Price", color="tab:blue")
    ma_line, = ax.plot([], [], lw=1.0, alpha=0.7, label="Moving avg", color="tab:orange")

    # Scatter for trades
    buy_scatter = ax.scatter([], [], marker="^", s=30, color="green", label="Buy")
    sell_scatter = ax.scatter([], [], marker="v", s=30, color="red", label="Sell")

    ax.legend(frameon=False, loc="lower left", fontsize=8, ncol=2)

    def init():
        price_line.set_data([], [])
        ma_line.set_data([], [])
        buy_scatter.set_offsets(np.empty((0, 2)))
        sell_scatter.set_offsets(np.empty((0, 2)))
        return price_line, ma_line, buy_scatter, sell_scatter

    def update(frame):
        # Update lines up to current frame
        price_line.set_data(t[:frame], price[:frame])
        ma_line.set_data(t[:frame], ma[:frame])

        # Show all trades that have occurred so far
        current_buys = [i for i in buy_idx if i <= frame]
        current_sells = [i for i in sell_idx if i <= frame]

        if current_buys:
            buy_points = np.column_stack((t[current_buys], price[current_buys]))
            buy_scatter.set_offsets(buy_points)
        else:
            buy_scatter.set_offsets(np.empty((0, 2)))

        if current_sells:
            sell_points = np.column_stack((t[current_sells], price[current_sells]))
            sell_scatter.set_offsets(sell_points)
        else:
            sell_scatter.set_offsets(np.empty((0, 2)))

        return price_line, ma_line, buy_scatter, sell_scatter

    # Add pause at end
    animated_frames = n
    pause_frames = 50  # 2 seconds at 25fps
    total_frames = animated_frames + pause_frames
    
    def update_with_pause(frame):
        actual_frame = min(frame, animated_frames - 1)
        return update(actual_frame)
    
    anim = FuncAnimation(
        fig,
        update_with_pause,
        frames=total_frames,
        init_func=init,
        blit=True
    )

    anim.save(filename, writer=PillowWriter(fps=25))
    plt.close(fig)


if __name__ == "__main__":
    print("Creating algorithmic trading visualization...")
    make_algorithmic_trading_gif()
    print("  ✓ algorithmic_trading.gif")
    print("Done!")
