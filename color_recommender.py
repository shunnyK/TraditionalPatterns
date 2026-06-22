from collections import Counter


def recommend_colors(selected_patterns):
    line_counter = Counter()
    background_counter = Counter()

    for _, row in selected_patterns.iterrows():
        line_color = str(row["line_color"]).strip()
        background_color = str(row["background_color"]).strip()

        if line_color and line_color.lower() != "nan":
            line_counter.update([line_color])

        if background_color and background_color.lower() != "nan":
            background_counter.update([background_color])

    top_line_colors = [
        color for color, count in line_counter.most_common(3)
    ]

    top_background_colors = [
        color for color, count in background_counter.most_common(3)
    ]

    return {
        "line_colors": top_line_colors,
        "background_colors": top_background_colors
    }


def format_colors_for_prompt(colors):
    line_colors = colors.get("line_colors", [])
    background_colors = colors.get("background_colors", [])

    return f"""
Recommended traditional line colors:
{", ".join(line_colors)}

Recommended traditional background colors:
{", ".join(background_colors)}
"""