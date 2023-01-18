from os import path
import string

class TextAgg:
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]

    def __init__(self, filepath, filename):
        self.filepath = filepath
        self.filename = filename

        # Initialize variables
        self.full_path = ""
        self.frequency_count = {}
        self.word_list = []
        self.extract_string = ""
    
    def __str__(self):
        return "This class takes a given text file and shows the top 10 most used interesting words in it."

    def get_text(self):
        """ 
        1. Checks that the user-given file path is valid.
        2. Opens the file and scrubs any punctuation from each line.
        3. Append each cleaned word to a list. 
        """
        self.full_path = path.join(self.filepath, self.filename)
        try:
            with open(self.full_path, "r", encoding="utf8") as file:
                get_line = file.readlines()
                if not get_line:
                    raise Exception("File is empty")
                for line in get_line:
                    self.extract_string = line
                    self.extract_string = self.extract_string.replace('“','"').replace('”','"')
                    self.extract_string = self.extract_string.translate(str.maketrans('', '', string.punctuation))
                    # for character in string:
                    #     if character in punctuations:
                    #         string = string.replace(character, "")
                    for word in self.extract_string.lower().split():
                        self.word_list.append(word)
        # word_list.append(extract_string.lower().split())
        except OSError as error:
            print(error.strerror)
            print(f"File path given: {self.full_path}")
            raise FileNotFoundError
        
        return self.word_list
    
    def fill_dict(self):
        """ 
        1. Adds word to dictionary if it is not numeric or a common word.
        2. Ups the count of a word if it is repeated.
        """
        for word in self.word_list:
            if not word.isalpha():
                continue
            elif word in self.uninteresting_words:
                continue
            elif word in self.frequency_count.keys():
                self.frequency_count[word]+=1
            else:
                self.frequency_count[word]=1
        
        return self.frequency_count


# word_pile = file_contents.lower().split()


# for word in word_pile:
#     if word.isnumeric():
#         continue
#     while not word.isalpha():
#         for punctuation in punctuations:
#             if punctuation in word:
#                 # print(f"{punctuation} in {word}")
#                 word = word.replace(punctuation, "")
#                 break
#     # print(f"word is now: {word}")
#     if word in uninteresting_words:
#         continue
#     elif word in frequency_count.keys():
#         frequency_count[word]+=1
#     else:
#         frequency_count[word]=1

# print(frequency_count)