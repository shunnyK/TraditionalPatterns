import json


with open(
    "symbol_map.json",
    encoding="utf-8"
) as f:

    SYMBOL_MAP = json.load(f)


def get_symbol_relationships(
    meaning_keywords,
    top_n=5
):

    result = {}

    for meaning in meaning_keywords:

        if meaning not in SYMBOL_MAP:
            continue

        motifs = SYMBOL_MAP[meaning]

        sorted_motifs = sorted(
            motifs.items(),
            key=lambda x: x[1],
            reverse=True
        )[:top_n]

        result[meaning] = sorted_motifs

    return result