import re

def load_skills(skill_file='skill_list.txt'):
    with open(skill_file, 'r') as f:
        return set(line.strip().lower() for line in f.readlines())

def extract_skills(text):
    skills = load_skills()
    found = set()
    words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
    for i in range(len(words)):
        word = words[i]
        if word in skills:
            found.add(word)
        if i + 1 < len(words):
            phrase = f"{word} {words[i+1]}"
            if phrase in skills:
                found.add(phrase)
    return list(found)
