from helpers import EncipheredMessage


def run():
    processor = EncipheredMessage()
    print('Hacking message ...')
    processor.getEncipheredMessage()
    processor.hack()
    print(processor.letterMapping)
    print('Received enciphered message: \n' + processor.enciphered_message)
    print('Hacked message:')
    print(processor.decryptWithMapping())


if __name__ == '__main__':
    run()
