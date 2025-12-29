"""
Helper script to add pause frames at the end of GIF animations
Adds static frames so viewers can see the final state before loop
"""

def add_pause_frames(total_frames, pause_seconds=2, fps=10):
    """
    Calculate total frames including pause.
    
    Args:
        total_frames: Original animation frames
        pause_seconds: Seconds to pause at end (default 2)
        fps: Frames per second (default 10)
    
    Returns:
        Total frames including pause
    """
    pause_frames = int(pause_seconds * fps)
    return total_frames + pause_frames


def should_show_final_frame(frame, total_animated_frames, total_frames_with_pause):
    """
    Determine if we should show the final animated frame (pause period).
    
    Args:
        frame: Current frame number
        total_animated_frames: Number of frames with animation
        total_frames_with_pause: Total frames including pause
    
    Returns:
        True if in pause period, False otherwise
    """
    return frame >= total_animated_frames


def get_frame_index(frame, total_animated_frames):
    """
    Get the actual frame index to render.
    During pause, return the last animated frame.
    
    Args:
        frame: Current frame in the animation loop
        total_animated_frames: Total animated frames
    
    Returns:
        Frame index to use (clamped to last frame during pause)
    """
    return min(frame, total_animated_frames - 1)
