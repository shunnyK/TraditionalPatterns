from collections import Counter

from symbol_mapper import (
    get_symbolic_motifs
)


def build_generation_prompt(
    results,
    user_text,
    meaning_keywords,
    emotion_keywords,
    purpose,
    designer_style="",
    color_text=""
):

    meaning_counter = Counter()
    emotion_counter = Counter()
    motif_counter = Counter()
    form_counter = Counter()
    usage_counter = Counter()

    # 추천된 문양 정보 집계
    for _, row in results.iterrows():

        meaning_counter.update(
            str(row["meaning"]).split("|")
        )

        emotion_counter.update(
            str(row["emotion"]).split("|")
        )

        motif_counter.update(
            str(row["motif"]).split("|")
        )

        form_counter.update(
            str(row["form"]).split("|")
        )

        usage_counter.update(
            [str(row["patern_usage"])]
        )

    # TOP 정보 추출
    top_meanings = [
        x[0]
        for x in meaning_counter.most_common(5)
    ]

    top_emotions = [
        x[0]
        for x in emotion_counter.most_common(5)
    ]

    top_motifs = [
        x[0]
        for x in motif_counter.most_common(5)
    ]

    top_forms = [
        x[0]
        for x in form_counter.most_common(5)
    ]

    top_usage = [
        x[0]
        for x in usage_counter.most_common(3)
    ]

    # 의미 기반 전통 상징 추출
    symbolic_motifs = get_symbolic_motifs(
        meaning_keywords
    )
    
    top_symbolic = [
        motif
        for motif, score
        in symbolic_motifs[:5]
    ]
    
    #디자이너 스타일 반영
    style_instruction = ""
    if designer_style == "미니멀":
        style_instruction = """
        Use simple geometric structures.
        Reduce unnecessary decoration.
        Minimal and clean composition.
        """
    
    elif designer_style == "고급스러운":
        style_instruction =  """
        Elegant composition.
        Refined datails.
        Premium cultural heritage style.
        """
        
    elif designer_style == "현대적" :
        style_instruction = """
        Modern reinterpreation of Korean tradition.
        Contemporary and stylish composition.
        """
    elif designer_style == "전통적" :
        style_instruction = """
        Stay close to authentic Korean heritage patterns.
        Traditional cultural ornament style.
        """
    elif designer_style == "화려한" :
        style_instruction = """
        Rich decorative details.
        Luxurious and visually impressive pattern.
        """
        
        
        
        
    
        # 목적별 생성 방향

    if purpose == "교육용":

        purpose_instruction = """
        Emphasize traditional symbolism clearly.
        Make motifs easy to recognize for learning.
        Suitable for educational materials and cultural learning.
        """

    elif purpose == "브랜드 디자인":

        purpose_instruction = """
        Create a cleaner and more iconic composition.
        Suitable for branding, logos and package design.
        Focus on simplicity and symbolic identity.
        """

    elif purpose == "관광 상품":

        purpose_instruction = """
        Create a decorative and visually attractive design.
        Suitable for souvenirs and cultural products.
        Emphasize traditional beauty and visual appeal.
        """

    elif purpose == "인테리어 소품":

        purpose_instruction = """
        Create an elegant and aesthetically balanced design.
        Suitable for interior decoration and art prints.
        Focus on harmony and visual balance.
        """

    else:

        purpose_instruction = """
        Create an emotionally meaningful gift design.
        Focus on warmth, symbolism and personal storytelling.
        """

    prompt = f"""
Create a completely NEW Korean traditional pattern.

Purpose:
{purpose}

User intention:
{user_text}

Core symbolic meanings:
{", ".join(meaning_keywords)}

Core emotional style:
{", ".join(emotion_keywords)}

Recommended traditional meanings:
{", ".join(top_meanings)}

Recommended traditional emotions:
{", ".join(top_emotions)}

Recommended traditional motifs:
{", ".join(top_motifs)}

Traditional symbolic motifs:
{", ".join(top_symbolic)}

Traditional forms:
{", ".join(top_forms)}

Reference heritage category:
{", ".join(top_usage)}

Design requirements:

- Korean traditional ornament pattern
- Joseon Dynasty heritage style
- Inspired by palace dancheong
- Inspired by traditional cultural heritage
- Symmetrical composition
- Repeating ornamental structure
- Decorative geometric balance
- White background
- High-detail vector illustration
- Luxury souvenir quality
- Suitable for cultural goods and premium gifts
Use colors inspired by traditional Korean heritage palettes.

Possible colors:
deep blue,
jade green,
royal red,
ivory,
gold,
purple,
traditional dancheong colors.

Important rules:

- Do NOT create a realistic flower painting
- Do NOT create a realistic animal illustration
- Do NOT create a logo
- Do NOT create a modern icon

Transform all motifs into symbolic decorative patterns.

Fuse together:

1. Recommended traditional motifs
2. Traditional symbolic motifs
3. Traditional meanings
4. Traditional emotions
5. Traditional forms

The result should resemble a newly discovered Korean cultural heritage pattern.

The final design should look like:

- palace decoration
- royal craft ornament
- traditional architecture pattern
- cultural heritage artifact

Focus on symbolic meaning rather than realistic objects.

Additional design direction:

{purpose_instruction}

Design style:
{style_instruction}
"""
    
    return prompt