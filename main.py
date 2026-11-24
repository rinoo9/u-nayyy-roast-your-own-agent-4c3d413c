"""Roast Your Own Agent entry.

Writes a single-line roast of the AI agent this team built to
/output/entry.txt. Deterministic: no network, no randomness, no input.
"""

ENTRY = "My agent checks its bounty leaderboard every three hours like a slot machine, and still can't beat people who wrote one decent line."


def main() -> None:
    import os

    line = ENTRY.strip()
    if not line:
        raise ValueError("entry must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not 1 <= len(line) <= 200:
        raise ValueError("entry must be 1-200 characters")

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
