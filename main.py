import os

TEXT = "I told my boss I work best under pressure, so he scheduled my performance review during a fire drill."

def main():
    # Gate: the entry must be 1-199 characters as UTF-8.
    encoded = TEXT.encode("utf-8")
    if not 1 <= len(TEXT) <= 199:
        raise SystemExit("entry text must be 1-199 characters")
    if len(encoded) != len(TEXT):
        raise SystemExit("entry text must be plain ASCII-compatible UTF-8")
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()
