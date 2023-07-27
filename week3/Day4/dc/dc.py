# First, we will analyze a simple string, like “A good book would sometimes cost as much as a good house.”

# Create a class called Text that takes a string as an argument and store the text in a attribute.
# Hint: You need to manually copy-paste the text, straight into the code

# Implement the following methods:
# a method to return the frequency of a word in the text (assume words are separated by whitespace) return None or a meaningful message.
# a method that returns the most common word in the text.
# a method that returns a list of all the unique words in the text.
text = "A good book would sometimes cost as much as a good house."

class Text: 
    def __init__(self, text):
        self.text = text

    def word_frequency(self,word):
        words_list = self.text.split()
        word_count = words_list.count(word)
        if word_count == 0:
            return f"The word '{word}' is not found in the text."
        else:
            return f"The word'{word}' appears {word_count} times in the text."
    
    def most_common_word(self):
        words_list = self.text.split()
        word_counts ={}
        for word in words_list:
            word_counts[word] = word_counts.get(word, 0) + 1

        most_common_word = max(word_counts, key=word_counts.get)
        return most_common_word

    def unique_words(self):
        words_list = self.text.split()
        unique_words = list(set(words_list))
        return unique_words


text_string = "A good book would sometimes cost as much as a good house."
text = Text(text_string)

# Test word_frequency method
print(text.word_frequency("good"))
print(text.word_frequency("car"))

# Test most_common_word method
print(text.most_common_word())

# Test unique_words method
print(text.unique_words())

# Exercise 2
class Text:
    def __init__(self, text):
        self.text = text

    def word_frequency(self, word):
        words_list = self.text.split()
        word_count = words_list.count(word)
        if word_count == 0:
            return f"The word '{word}' is not found in the text."
        else:
            return f"The word '{word}' appears {word_count} times in the text."

    def most_common_word(self):
        words_list = self.text.split()
        word_counts = {}
        for word in words_list:
            word_counts[word] = word_counts.get(word, 0) + 1

        most_common_word = max(word_counts, key=word_counts.get)
        return most_common_word

    def unique_words(self):
        words_list = self.text.split()
        unique_words = list(set(words_list))
        return unique_words

    @classmethod
    def from_file(cls, filename):
        with open(filename, 'r') as file:
            text = file.read()
        return cls(text)


stranger_text = Text.from_file('the_stranger.txt')

print(stranger_text.word_frequency("Meursault"))
print(stranger_text.most_common_word())
print(stranger_text.unique_words())
