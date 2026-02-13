from langdetect import detect

def generate_prompt(category, topic, tone, length, language, audience):
    auto_lang = detect(topic)

    prompt = f"""
You are a world-class AI Prompt Engineer.

Category: {category}
Topic: {topic}
Tone: {tone}
Length: {length}
Language Preference: {language}
Auto-detected Language: {auto_lang}
Target Audience: {audience if audience else "General"}

Instructions:
- Strong hook
- Clear structure
- Professional quality
- High engagement
- Final CTA

Generate premium-level content.
"""
    return prompt.strip()
