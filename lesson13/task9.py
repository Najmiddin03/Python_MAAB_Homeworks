import re


def find_word_occurrences(text, word):
    pattern = rf'\b{re.escape(word)}\b'
    matches = [m.start() for m in re.finditer(pattern, text, re.IGNORECASE)]
    return matches


def main():
    text = """Artificial intelligence (AI) refers to the capability of computational systems to perform tasks typically associated with human intelligence, such as learning, reasoning, problem-solving, perception, and decision-making. It is a field of research in computer science that develops and studies methods and software that enable machines to perceive their environment and use learning and intelligence to take actions that maximize their chances of achieving defined goals.[1] Such machines may be called AIs.

High-profile applications of AI include advanced web search engines (e.g., Google Search); recommendation systems (used by YouTube, Amazon, and Netflix); virtual assistants (e.g., Google Assistant, Siri, and Alexa); autonomous vehicles (e.g., Waymo); generative and creative tools (e.g., ChatGPT and AI art); and superhuman play and analysis in strategy games (e.g., chess and Go). However, many AI applications are not perceived as AI: "A lot of cutting edge AI has filtered into general applications, often without being called AI because once something becomes useful enough and common enough it's not labeled AI anymore."[2][3]

Various subfields of AI research are centered around particular goals and the use of particular tools. The traditional goals of AI research include learning, reasoning, knowledge representation, planning, natural language processing, perception, and support for robotics.[a] General intelligence—the ability to complete any task performed by a human on an at least equal level—is among the field's long-term goals.[4] To reach these goals, AI researchers have adapted and integrated a wide range of techniques, including search and mathematical optimization, formal logic, artificial neural networks, and methods based on statistics, operations research, and economics.[b] AI also draws upon psychology, linguistics, philosophy, neuroscience, and other fields.[5]"""

    text = re.sub(r'[^\w\s]', ' ', text)

    word = input("Enter a word to find: ")
    occurrences = find_word_occurrences(text, word)

    if occurrences:
        print(f"The word '{word}' was found at positions: {occurrences}")
    else:
        print(f"The word '{word}' was not found in the text.")


if __name__ == "__main__":
    main()
