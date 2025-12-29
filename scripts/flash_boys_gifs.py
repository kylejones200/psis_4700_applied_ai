"""
Flash Boys Visualization GIFs
Creates 5 animated visualizations for explaining Flash Boys and the 2010 Flash Crash
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

plt.rcParams["font.family"] = "serif"


def _tufte_axes(ax, xlabel="", ylabel=""):
    """Apply a clean minimalist style to an axis."""
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    # Hide top and right spines
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    # Subtle bracket feel
    ax.spines["left"].set_position(("outward", 5))
    ax.spines["bottom"].set_position(("outward", 5))

    ax.tick_params(direction="out")
    return ax


def make_latency_race_gif(filename="latency_race.gif"):
    """Investor vs HFT race in milliseconds."""

    fig, ax = plt.subplots(figsize=(6, 3))

    # Time in milliseconds
    t = np.linspace(0, 40, 200)
    base_price = 100.0 + 0.02 * t + 0.4 * np.sin(t / 2)

    # Order time
    t_order = 10.0
    order_idx = np.searchsorted(t, t_order)

    # Plot full price path
    ax.plot(t, base_price, alpha=0.3)
    _tufte_axes(ax, xlabel="Time (ms)", ylabel="Price")

    ax.set_xlim(0, 40)
    ax.set_ylim(base_price.min() - 1, base_price.max() + 1)

    # Markers
    investor_dot, = ax.plot([], [], "o", markersize=6, label="Investor")
    hft_dot, = ax.plot([], [], "s", markersize=5, fillstyle="none",
                       label="HFT")

    ax.legend(frameon=False, loc="upper left")

    def init():
        investor_dot.set_data([], [])
        hft_dot.set_data([], [])
        return investor_dot, hft_dot

    def update(frame):
        # Investor submits at order_idx and moves with time
        if frame >= order_idx:
            investor_dot.set_data([t[frame]], [base_price[frame]])
        else:
            investor_dot.set_data([], [])

        # HFT sees order and jumps ahead on price
        if frame >= order_idx + 3:
            # HFT a bit ahead in time and price
            hft_idx = min(len(t) - 1, frame + 10)
            hft_price = base_price[hft_idx] + 0.2
            hft_dot.set_data([t[hft_idx]], [hft_price])
        else:
            hft_dot.set_data([], [])

        return investor_dot, hft_dot

    # Add pause at end
    animated_frames = len(t)
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


def make_liquidity_vanish_gif(filename="liquidity_vanish.gif"):
    """Order book depth thins out and returns."""

    fig, ax = plt.subplots(figsize=(6, 3))

    # Price grid around mid
    x = np.linspace(-5, 5, 21)

    # Initial symmetric depth
    depth0 = np.exp(-x**2 / 6.0) * 100

    # Bars for bids (x < 0) and asks (x > 0)
    bids_mask = x < 0
    asks_mask = x > 0

    bid_bars = ax.bar(
        x[bids_mask],
        depth0[bids_mask],
        width=0.4,
        align="center"
    )
    ask_bars = ax.bar(
        x[asks_mask],
        depth0[asks_mask],
        width=0.4,
        align="center"
    )

    _tufte_axes(ax, xlabel="Price vs mid", ylabel="Depth")
    ax.set_xlim(-5.5, 5.5)
    ax.set_ylim(0, depth0.max() * 1.3)

    # Frames: calm -> thin bids near mid -> shallow book -> recovery
    n_frames = 120

    def depth_at_frame(f):
        # Phase 0–40: normal
        if f < 40:
            return depth0.copy()

        # Phase 40–80: large sell event, bids near mid vanish
        if f < 80:
            frac = (f - 40) / 40.0
            depth = depth0.copy()
            near_mid = np.abs(x) < 2.0
            depth[(x < 0) & near_mid] *= (1.0 - 0.9 * frac)
            depth[(x < 0) & (np.abs(x) >= 2.0)] *= (1.0 - 0.5 * frac)
            return depth

        # Phase 80–120: recovery
        frac = (f - 80) / 40.0
        depth = depth0.copy()
        near_mid = np.abs(x) < 2.0
        depth[(x < 0) & near_mid] *= (0.1 + 0.9 * frac)
        depth[(x < 0) & (np.abs(x) >= 2.0)] *= (0.5 + 0.5 * frac)
        return depth

    def update(frame):
        depth = depth_at_frame(frame)

        for bar, d in zip(bid_bars, depth[bids_mask]):
            bar.set_height(d)

        for bar, d in zip(ask_bars, depth[asks_mask]):
            bar.set_height(d)

        return (*bid_bars, *ask_bars)

    anim = FuncAnimation(
        fig,
        update,
        frames=n_frames,
        blit=True
    )

    anim.save(filename, writer=PillowWriter(fps=20))
    plt.close(fig)


def make_flash_crash_path_gif(filename="flash_crash_path.gif"):
    """Index price path with animated marker."""

    fig, ax = plt.subplots(figsize=(6, 3))

    # Synthetic intraday path that resembles a flash crash
    n = 300
    t = np.linspace(0, 1, n)
    price = 1000 + 10 * np.sin(4 * np.pi * t)

    drop_start = int(0.35 * n)
    drop_end = int(0.55 * n)

    price[drop_start:drop_end] -= np.linspace(0, 200, drop_end - drop_start)
    price[drop_end:] += np.linspace(200, 0, n - drop_end)

    # Static trace
    ax.plot(t, price, alpha=0.3)
    _tufte_axes(ax, xlabel="Time", ylabel="Index level")

    ax.set_xlim(0, 1)
    ax.set_ylim(price.min() - 20, price.max() + 20)

    # Moving marker
    dot, = ax.plot([], [], "o", markersize=5)

    def init():
        dot.set_data([], [])
        return dot,

    def update(frame):
        dot.set_data([t[frame]], [price[frame]])
        return dot,

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


def make_hot_potato_gif(filename="hot_potato.gif"):
    """Hot potato trade across mutual fund, HFT, and market."""

    fig, ax = plt.subplots(figsize=(4, 4))

    _tufte_axes(ax, xlabel="Holder", ylabel="Contracts")

    holders = ["Mutual fund", "HFT firms", "Rest of market"]
    x = np.arange(len(holders))

    # Total contracts
    total = 100.0

    n_frames = 120

    # Precompute trajectories for holdings
    mf = np.zeros(n_frames)
    hft = np.zeros(n_frames)
    rest = np.zeros(n_frames)

    for f in range(n_frames):
        if f < 30:
            # Mutual fund sells steadily
            frac = f / 30.0
            mf[f] = total * (1.0 - frac)
            hft[f] = total * frac * 0.7
            rest[f] = total * frac * 0.3
        elif f < 70:
            # HFT and rest pass contracts in both directions
            frac = (f - 30) / 40.0
            mf[f] = 0.0
            hft[f] = total * (0.7 - 0.4 * frac)
            rest[f] = total - hft[f]
        else:
            # Market settles with rest holding most
            frac = (f - 70) / 50.0
            mf[f] = 0.0
            hft[f] = total * max(0.2 - 0.2 * frac, 0.0)
            rest[f] = total - hft[f]

    bars = ax.bar(x, [mf[0], hft[0], rest[0]])

    ax.set_xticks(x)
    ax.set_xticklabels(holders, rotation=15, ha="right")
    ax.set_ylim(0, total * 1.1)

    def update(frame):
        heights = [mf[frame], hft[frame], rest[frame]]
        for bar, h in zip(bars, heights):
            bar.set_height(h)
        return bars

    # Add pause at end
    animated_frames = n_frames
    pause_frames = 30  # 2 seconds at 15fps
    total_frames = animated_frames + pause_frames
    
    def update_with_pause(frame):
        actual_frame = min(frame, animated_frames - 1)
        return update(actual_frame)
    
    anim = FuncAnimation(
        fig,
        update_with_pause,
        frames=total_frames,
        blit=True
    )

    anim.save(filename, writer=PillowWriter(fps=15))
    plt.close(fig)


def make_speed_bump_gif(filename="speed_bump.gif"):
    """IEX speed bump equalizes a small latency edge."""

    fig, ax = plt.subplots(figsize=(6, 3))

    _tufte_axes(ax, xlabel="Distance to exchange", ylabel="Track")

    ax.set_xlim(0, 1.0)
    ax.set_ylim(-0.5, 1.5)

    # Tracks
    ax.hlines(0.3, 0, 1, alpha=0.3)
    ax.hlines(0.7, 0, 1, alpha=0.3)
    ax.text(0.02, 0.32, "Investor", va="center", ha="left", fontsize=9)
    ax.text(0.02, 0.72, "Fast trader", va="center", ha="left", fontsize=9)

    # Speed bump zone
    bump_start = 0.6
    bump_end = 0.75
    ax.axvspan(bump_start, bump_end, alpha=0.05)
    ax.text(
        (bump_start + bump_end) / 2,
        1.05,
        "IEX speed bump",
        ha="center",
        va="center",
        fontsize=9
    )

    investor_dot, = ax.plot([], [], "o", markersize=5)
    fast_dot, = ax.plot([], [], "s", markersize=5, fillstyle="none")

    n_frames = 120

    def position_without_bump(f):
        """Baseline faster fast-trader."""
        frac = f / (n_frames - 1)
        investor_x = frac
        fast_x = min(1.0, frac * 1.4)
        return investor_x, fast_x

    def position_with_bump(f):
        """Fast-trader slows in bump zone."""
        frac = f / (n_frames - 1)

        # Investor moves at constant speed
        investor_x = frac

        # Fast trader moves fast, then slows in bump region
        raw_fast = frac * 1.4
        if raw_fast <= bump_start:
            fast_x = raw_fast
        elif raw_fast >= bump_end:
            # After bump, rejoin and end at 1.0 with investor
            # Map remaining distance to end
            remaining = raw_fast - bump_end
            total_after = 1.4 - bump_end
            fast_x = bump_end + remaining * (1.0 - bump_end) / total_after
        else:
            # Inside bump: clamp to slow progress
            frac_bump = (raw_fast - bump_start) / (bump_end - bump_start)
            fast_x = bump_start + 0.3 * frac_bump * (bump_end - bump_start)
        fast_x = min(fast_x, 1.0)
        return investor_x, fast_x

    def update(frame):
        # First half: show baseline race
        # Second half: show speed bump effect
        if frame < n_frames // 2:
            local_f = frame * 2
            inv_x, fast_x = position_without_bump(local_f)
        else:
            local_f = (frame - n_frames // 2) * 2
            inv_x, fast_x = position_with_bump(local_f)

        investor_dot.set_data([inv_x], [0.3])
        fast_dot.set_data([fast_x], [0.7])
        return investor_dot, fast_dot

    # Add pause at end
    animated_frames = n_frames
    pause_frames = 40  # 2 seconds at 20fps
    total_frames = animated_frames + pause_frames
    
    def update_with_pause(frame):
        actual_frame = min(frame, animated_frames - 1)
        return update(actual_frame)
    
    anim = FuncAnimation(
        fig,
        update_with_pause,
        frames=total_frames,
        blit=True
    )

    anim.save(filename, writer=PillowWriter(fps=20))
    plt.close(fig)


if __name__ == "__main__":
    print("Creating Flash Boys visualization GIFs...")
    make_latency_race_gif()
    print("  ✓ latency_race.gif")
    make_liquidity_vanish_gif()
    print("  ✓ liquidity_vanish.gif")
    make_flash_crash_path_gif()
    print("  ✓ flash_crash_path.gif")
    make_hot_potato_gif()
    print("  ✓ hot_potato.gif")
    make_speed_bump_gif()
    print("  ✓ speed_bump.gif")
    print("Done!")
