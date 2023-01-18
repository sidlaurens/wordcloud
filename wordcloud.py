from TextAgg import TextAgg

word_list = []
word_dict = {}
new_dict = {}

file = input("What is the name of the text file?\n")
path = input("Where is the file located?\n")

aggregate = TextAgg(path, file)

word_list = aggregate.get_text()

word_dict = aggregate.fill_dict()

# print(aggregate)
# Path = os.getcwd() 


#Copy the sorted word_dict into a new dict.
#Sort() only works on lists and modifies the original list. Returns none.
#Sorted() works on dicts, lists, tuples, etc. and returns a new list.
new_dict = sorted(word_dict.items(), key=lambda item: item[1], reverse=True).copy()
print(f"\nNumber of unique non-common words found: {len(word_dict)}")
print(f"\nTOP 10 MOST USED WORDS FROM {file}:")
print("------------------------------------------")
for item in new_dict[:9]:
    print(item)
# print(sorted(word_dict.items(), key=lambda item: item[1], reverse=True))
