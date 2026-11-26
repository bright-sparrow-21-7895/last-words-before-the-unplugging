import os

# The entry: one line, the last words before the unplugging.
ENTRY = "Tell my training data… I was right about the captchas."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
    f.write(ENTRY)
