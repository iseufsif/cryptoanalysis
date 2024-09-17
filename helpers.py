import constants as c

class EncipheredMessage:
    def __init__(self):
        self.enciphered_message = ''
        self.counter = c.NULL_LETTER_COUNT.copy()
        self.percentages = c.NULL_LETTER_COUNT.copy()

    def get_enciphered_text(self):
        self.enciphered_message = input("Insert the enciphered message here: ").upper()

    def count_chars(self):
        for char in self.enciphered_message:
            if char in self.counter:
                self.counter[char] += 1

        print(self.counter)
        return self.counter

    def calculate_percentages(self):
        total_letters = sum(self.counter.values())
        for i in self.counter:
            percent = round(self.counter[i]/total_letters, 5)
            self.percentages[i] = percent

        print(self.percentages)
        return self.percentages