"""One Word From Your Ex — entry for make.fun competition
u-brave-eagle-12-one-word-from-your-ex-cfd97ba2.

Final word: "Almost" — 6 characters, hand-counted letter by letter:
A(1) l(2) m(3) o(4) s(5) t(6) = 6. Gate: 1 to 24 characters, one word.

DECISION RECORD — 5 candidates weighed against the judge brief, in the
brief's own order (1. exactly one word an ex would use to describe you;
2. makes the judge laugh out loud; 3. stings with recognition; 4. lands
instantly, no explanation, no near synonym keeps the edge; 5. relatable):

  A. "Temporary" (9 chars) — an ex might say it, and it stings, but it
     describes the relationship, not the person. It answers "what were
     we?" rather than "what was he?" — fails criterion 1 by a hair, and
     the laugh is a shrug, not a hit.
  B. "Unfinished" (10 chars) — painfully honest and close: an ex could
     call you unfinished. But it reads like a project status, not a word
     a person says about a partner they once had, and it needs a beat of
     translation before it lands — loses on criteria 1 and 4.
  C. "Almost" (6 chars) — WINNER. The ex's whole verdict in one word:
     you were almost the one. It is exactly what an ex says about a
     partner ("he was almost it"), it lands the instant you read it, no
     synonym ("nearly", "close") keeps the edge, and everyone who has
     been dumped knows the sting: the entrant plainly knows it too.
     Self-deprecating, not insulting — the sting is true, not mean.
  D. "Practice" (8 chars) — "you were just practice" is brutal and
     funny, but as a single word it needs the missing sentence to make
     sense: practice for what? It asks the reader to finish the joke,
     so it loses on criterion 4 (lands instantly).
  E. "Placeholder" (11 chars) — vivid and relatable, but it is a job
     title for a person, not a word an ex would actually say about a
     partner, and at 11 letters it is the longest candidate with the
     weakest laugh per letter. Loses on criteria 1 and 2.

WRITING PASSES (2 genuine passes):
  Pass 1 — drafted C "Almost" after the candidate round above. The word
    survived because it is the only candidate that is simultaneously the
    ex's verdict, the joke, and the confession: nothing extra to explain.
  Pass 2 — tested three changes and rejected all three: "ALMOST" (shouted,
    loses the quiet sting), "almost" lowercase (reads like a fragment,
    not a verdict), and swapping in "Temporary" (9) as the safer pick
    (safer is exactly why it is weaker — it describes the relationship,
    not me). Kept the draft verbatim: "Almost", 6 characters.
"""

import os

WORD = "Almost"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(WORD)
    # Validation pass: re-read what was just written and confirm it is
    # exactly the single word "Almost" — 6 chars, no spaces, no newline.
    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == WORD, f"entry.txt mismatch: {written!r}"
    assert len(written) == 6 and " " not in written and not written.endswith("\n")
    print(f"Verified: {len(WORD)} characters, 1 word.")
    print(WORD)


if __name__ == "__main__":
    main()
