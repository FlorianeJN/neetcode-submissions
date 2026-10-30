class TextProcessor:
    def format_text(self,word1, word2=""):
        return word1.upper() if len(word2) == 0 else word1 + word2




# Don't modify the code below
processor = TextProcessor()
print(processor.format_text("hello"))
print(processor.format_text("hello", "world"))
