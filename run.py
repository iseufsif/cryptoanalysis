from helpers import EncipheredMessage
import constants as c

def run():
    processor = EncipheredMessage()
    processor.get_enciphered_text()
    processor.count_chars()
    processor.calculate_percentages()

if __name__ == '__main__':
    run()