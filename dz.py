import random
class NumberEncryptor:
    def __init__(self):
        self.number = None
    def encrypt(self, number):
        self.number = number
        self.number += random.randint(1, 10)
    def decrypt(self):
        return self.number - random.randint(1, 10)
if __name__ == "__main__":
    encryptor = NumberEncryptor()
    original_number = 52
    encryptor.encrypt(original_number)
    print("Зашифроване число:", encryptor.number)
    decrypted_number = encryptor.decrypt()
    print("Розшифроване число:", decrypted_number)