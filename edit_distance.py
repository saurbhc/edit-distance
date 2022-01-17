from __future__ import annotations

import argparse
import logging


def levenshteinDistance(s1, s2):
    """
    Source: https://en.wikibooks.org/wiki/Algorithm_Implementation (cont)
    /Strings/Levenshtein_distance#Python
    """
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    distances = range(len(s1) + 1)
    for i2, c2 in enumerate(s2):
        distances_ = [i2+1]
        for i1, c1 in enumerate(s1):
            if c1 == c2:
                distances_.append(distances[i1])
            else:
                distances_.append(
                    1 +
                    min((distances[i1], distances[i1 + 1], distances_[-1])),
                )
        distances = distances_
    return distances[-1]


def check_last_char_is_same(w1, w2, i, last=False):
    try:
        if last:
            w1_c = w1[-i]
            w2_c = w2[-i]
        else:
            w1_c = w1[i]
            w2_c = w2[i]
    except IndexError:
        logging.debug(f"...IndexError {last=}")
        return False

    logging.debug(f"...{w1_c=} {w2_c=} {last=}")
    return w1_c == w2_c


def calculate_distance(word_1, word_2):
    """
    Current Strategy:

    1. If last characters of two strings are same, nothing much to do.
      Ignore last characters and get count for remaining strings.
      So we recur for lengths m-1 and n-1.
    2. Else (If last characters are not same),
      we consider all operations on ‘str1’,
      consider all three operations on last character of first string,
      recursively compute minimum cost for all three operations
      and take minimum of three values.
      Insert: Recur for m and n-1
      Remove: Recur for m-1 and n
      Replace: Recur for m-1 and n-1
    """
    w1_n = len(word_1)
    w2_n = len(word_2)
    min_n = min(w1_n, w2_n)
    total_distance = 0

    for index in range(min_n):
        logging.debug(f"# {index=} 1st Part")
        is_same = check_last_char_is_same(
            w1=word_1, w2=word_2, i=index, last=True,
        )
        logging.debug(f"...{is_same=}")
        if is_same:
            continue

        # TODO: 2nd Part (TBD)
        logging.debug("# 2nd Part (skipped)")
        distance = levenshteinDistance(word_1, word_2)
        total_distance += distance
        logging.debug(f"{distance=}")

    return total_distance


def main():
    p = argparse.ArgumentParser()
    p.add_argument("word_1", help="1st Word", type=str)
    p.add_argument("word_2", help="2nd Word", type=str)
    p.add_argument(
        '--log', default='warning',
        choices=['debug', 'info', 'warning', 'error'],
        help="logging level (defaults to 'warning')",
    )
    args = p.parse_args()
    logging.basicConfig(
        level=getattr(logging, args.log.upper(), None),
        format='%(levelname)s: %(message)s',
    )

    result = calculate_distance(
        word_1=args.word_1,
        word_2=args.word_2,
    )
    print(
        f"Minimum Edit distance b/w {args.word_1} & {args.word_2} is {result}",
    )


if __name__ == "__main__":
    exit(main())
