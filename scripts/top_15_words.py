import argparse
import re
import sys
from collections import Counter


# Keep tokens that are alphabetic words (with optional internal apostrophes/hyphens),
# and discard numeric/alphanumeric IDs such as 000123abc.
WORD_RE = re.compile(r"^[a-z]+(?:['-][a-z]+)*$")


def is_true_word(token, min_length=2):
    if not token:
        return False
    token = token.lower()
    return len(token) >= min_length and bool(WORD_RE.fullmatch(token))


def read_word_counts_from_stream(stream, min_length=2):
    counter = Counter()
    for line in stream:
        try:
            word, count = line.strip().split("\t")
            count = int(count)
        except ValueError:
            continue  # Skip malformed lines

        if is_true_word(word, min_length=min_length):
            counter[word] += count
    return counter


def read_word_counts(filepath, min_length=2):
    if filepath == "-":
        return read_word_counts_from_stream(sys.stdin, min_length=min_length)

    with open(filepath, "r", encoding="utf-8") as f:
        return read_word_counts_from_stream(f, min_length=min_length)


def print_top_n(counter, n=15):
    print(f"\nTop {n} most frequent true words:\n" + "-" * 36)
    for word, count in counter.most_common(n):
        print(f"{word:20} {count}")


def parse_args():
    parser = argparse.ArgumentParser(
        description="Show top N true words from Hadoop word-count output."
    )
    parser.add_argument(
        "--input",
        default="output/part-00000",
        help="Path to Hadoop output file, or '-' to read from stdin (default: output/part-00000)",
    )
    parser.add_argument(
        "--top",
        type=int,
        default=15,
        help="Number of top words to show (default: 15)",
    )
    parser.add_argument(
        "--min-length",
        type=int,
        default=2,
        help="Minimum word length to keep (default: 2)",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    word_counts = read_word_counts(args.input, min_length=args.min_length)
    print_top_n(word_counts, args.top)