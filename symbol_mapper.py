import json

with open(
    "symbol_map.json",
    encoding="utf-8"
) as f:

    SYMBOL_MAP = json.load(f)


def get_symbolic_motifs(
    meaning_keywords
):

    motif_scores = {}

    for meaning in meaning_keywords:

        if meaning not in SYMBOL_MAP:
            continue

        motifs = SYMBOL_MAP[meaning]

        for motif, count in motifs.items():

            motif_scores[motif] = (
                motif_scores.get(motif, 0)
                + count
            )

    sorted_motifs = sorted(
        motif_scores.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return sorted_motifs