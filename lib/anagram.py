class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, possible_anagrams):
        matches = []

        for wrd in possible_anagrams:
            if sorted(self.word) == sorted(wrd):
                matches.append(wrd)
        return matches
