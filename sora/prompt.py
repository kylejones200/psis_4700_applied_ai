import pandas as pd
import re

STYLE = (
    "anime-inspired, soft realistic style, clean linework, natural daylight lighting, "
    "warm neutral tones, muted but brighter color palette, calm and clear atmosphere, "
    "minimal composition, cinematic framing with gentle negative space, shallow depth of field, "
    "slow subtle motion, grounded real-world setting, no exaggerated expressions, "
    "consistent recurring characters"
)

CHARACTERS = (
    "same learner character with short dark hair, neutral clothing, calm focused demeanor, "
    "same professional character slightly older, composed posture, clean simple clothing"
)

def slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "_", text)
    return text.strip("_")

df = pd.read_csv("scenes.csv")

df["prompt"] = (
    STYLE
    + ", "
    + CHARACTERS
    + ". "
    + df["scene_description"].str.strip()
    + ". Slow camera movement. No text on screen."
)

df["filename"] = df.apply(
    lambda row: f"{int(row['scene_id']):02d}_{slugify(row['scene_title'])}.mp4",
    axis=1,
)

df.to_csv("sora_prompts.csv", index=False)
print(df[["scene_id", "scene_title", "filename"]].to_string(index=False))