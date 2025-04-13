#!/usr/bin/env python3
import os
import sys

def main():
    if len(sys.argv) != 2:
        print("Welcome to Cheatsheet CLI!\n\nUsage: cheatsheet <topic>")
        return

    topic = sys.argv[1]

    # Path where Homebrew installs shared files
    brew_prefix = os.popen("brew --prefix").read().strip()
    cheat_path = os.path.join(brew_prefix, "share", "cheats", "cheats", f"{topic}.txt")

    if not os.path.exists(cheat_path):
        print(f"No cheat sheet found for '{topic}'.")
        return

    with open(cheat_path) as f:
        print(f.read())

if __name__ == "__main__":
    main()
