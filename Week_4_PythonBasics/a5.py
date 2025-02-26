class StringReverser:
    def __init__(self, string):
        self.string = string

    def reverse_words(self):
        words = self.string.split()
        return " ".join(reversed(words))

reverser = StringReverser("Hello World")
print("Reversed string:", reverser.reverse_words())
