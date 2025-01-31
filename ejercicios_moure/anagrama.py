
def is_anagram(word_one: str, word_two: str) -> bool:
    if word_one.lower() == word_two.lower():
        return False
    return sorted(word_one.lower()) == sorted(word_two.lower())
