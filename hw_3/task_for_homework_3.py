text_sample = """homEwork:
tHis iz your homeWork, copy these Text to variable.



You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE 
witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, 
but ALL whitespaces. I got 87.
"""

# all text letters make lower-case
text_lower = text_sample.lower()

# split text by words
words_list = text_lower.split()

# check every word is it is equal to 'iz' and replace it to 'is'
for word in words_list:
    if word == 'iz':
        index_of_iz = words_list.index(word)
        words_list[index_of_iz] = 'is'

# join all words into new string
string_new = ' '.join(words_list)

# split this new string into sentences
string_newest = string_new.split('.')

# further split sentences into list of words and retrieve last word from element in the list
last_words = [sentence.split()[-1] for sentence in string_newest if sentence]

# join all words received and capitalize the sentence
new_sentence = ' '.join(last_words).capitalize()

# every sentence strip of spaces and capitalize the sentence
string_newest = [sentence.strip().capitalize() for sentence in string_newest]

# join all sentences
string_super = '. '.join(string_newest)

# create a final string containing newly formed sentence too
final_string = string_super + new_sentence + '.'
print(string_super)
print(new_sentence)

# count all True (1) values for whitespaces in final string
whitespace_count = sum(element.isspace() for element in final_string)
print(final_string)
print(whitespace_count)
