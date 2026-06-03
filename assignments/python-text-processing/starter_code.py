#!/usr/bin/env python3
import argparse
import re
from collections import Counter
from pathlib import Path

PUNCT_RE = re.compile(r"[\W_]+", re.UNICODE)

def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")

def count_stats(text: str):
    lines = text.splitlines()
    chars = len(text)
    words = re.findall(r"\b\w+\b", text)
    return {
        "lines": len(lines),
        "words": len(words),
        "chars": chars,
    }

def top_common_words(text: str, n=5):
    words = re.findall(r"\b\w+\b", text.lower())
    words = [PUNCT_RE.sub('', w) for w in words if w]
    return Counter(words).most_common(n)

def clean_text(text: str) -> str:
    # Remove punctuation and normalize whitespace
    cleaned = PUNCT_RE.sub(' ', text)
    cleaned = re.sub(r"\s+", ' ', cleaned).strip()
    return cleaned

def search_replace(text: str, find: str, replace: str) -> str:
    return text.replace(find, replace)

def write_text(path: Path, text: str):
    path.write_text(text, encoding="utf-8")

def main():
    parser = argparse.ArgumentParser(description="Simple text processing utilities")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_stats = sub.add_parser("stats", help="Print basic statistics for a text file")
    p_stats.add_argument("file", type=Path)

    p_top = sub.add_parser("top", help="Show top N common words")
    p_top.add_argument("file", type=Path)
    p_top.add_argument("-n", type=int, default=5)

    p_clean = sub.add_parser("clean", help="Write cleaned text to a new file")
    p_clean.add_argument("file", type=Path)
    p_clean.add_argument("--out", type=Path, required=True)

    p_replace = sub.add_parser("replace", help="Search and replace in a file and write output")
    p_replace.add_argument("file", type=Path)
    p_replace.add_argument("find", type=str)
    p_replace.add_argument("replace", type=str)
    p_replace.add_argument("--out", type=Path, required=True)

    args = parser.parse_args()

    if args.cmd == "stats":
        text = read_text(args.file)
        stats = count_stats(text)
        print(f"Lines: {stats['lines']}")
        print(f"Words: {stats['words']}")
        print(f"Characters: {stats['chars']}")
    elif args.cmd == "top":
        text = read_text(args.file)
        for word, count in top_common_words(text, n=args.n):
            print(f"{word}: {count}")
    elif args.cmd == "clean":
        text = read_text(args.file)
        cleaned = clean_text(text)
        write_text(args.out, cleaned)
        print(f"Wrote cleaned text to {args.out}")
    elif args.cmd == "replace":
        text = read_text(args.file)
        out_text = search_replace(text, args.find, args.replace)
        write_text(args.out, out_text)
        print(f"Wrote replaced text to {args.out}")

if __name__ == "__main__":
    main()
