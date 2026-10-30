class TextProcessor:
    def format_text(self,word1, word2=""):
        return word1 + word2 if word2 else word1.upper()

# Don't modify the code below
processor = TextProcessor()
print(processor.format_text("hello"))
print(processor.format_text("hello", "world"))
