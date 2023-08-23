# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()  # Convert to lowercase for case-insensitive comparison

    def match(self, words):
        return [w for w in words if self.is_anagram(w)]

    def is_anagram(self, candidate):
        candidate_lower = candidate.lower()
        return candidate_lower != self.word and sorted(candidate_lower) == sorted(self.word)