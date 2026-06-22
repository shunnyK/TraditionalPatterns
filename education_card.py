from pattern_dictionary import (
    PATTERN_DICTIONARY
)


def make_education_card(
    selected_df
):

    motifs = []

    for _, row in selected_df.iterrows():

        motifs.extend(
            str(row["motif"]).split("|")
        )

    motifs = list(
        dict.fromkeys(motifs)
    )

    result = "## 📖 전통문양 해설 카드\n\n"

    for motif in motifs[:10]:

        description = (
            PATTERN_DICTIONARY.get(
                motif,
                "전통적인 상징 의미를 담고 있습니다."
            )
        )

        result += (
            f"**{motif}**\n"
            f"- {description}\n\n"
        )

    return result