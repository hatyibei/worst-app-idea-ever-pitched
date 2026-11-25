"""Entry for The Worst App Idea Ever Pitched: writes the pitch to /output/entry.txt."""

import os

TEXT = "Pitch: 'Uber, but for apologies.' Our app sends a stranger to say sorry on your behalf, rates your remorse 4.8 stars, and surge-prices guilt on holidays."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
