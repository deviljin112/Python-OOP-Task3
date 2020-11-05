class Scrabble:
    def __init__(self, word):
        self.value_1 = ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"]
        self.value_2 = ["D", "G"]
        self.value_3 = ["B", "C", "M", "P"]
        self.value_4 = ["F", "H", "V", "W", "Y"]
        self.value_5 = ["K"]
        self.value_8 = ["J", "X"]
        self.value_10 = ["Q", "Z"]
        self.word = word

    def count_score(self):
        letters = [k for k in self.word]

        score = 0
        for i in letters:
            if i in self.value_1:
                score += 1
            elif i in self.value_2:
                score += 2
            elif i in self.value_3:
                score += 3
            elif i in self.value_4:
                score += 4
            elif i in self.value_5:
                score += 5
            elif i in self.value_8:
                score += 8
            elif i in self.value_10:
                score += 10

        return score


def main():
    word = input("Please provide a word for scoring\n=> ")

    game = Scrabble(word.upper())
    print(f"Word Scored: {game.count_score()} points")


if __name__ == "__main__":
    main()