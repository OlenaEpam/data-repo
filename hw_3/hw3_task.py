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
c = text_lower.split()
# check every word is it is equal to 'iz' and replace it to 'is'
for i in c:
    if i == 'iz':
        index_of_iz = c.index(i)
        c[index_of_iz] = 'is'
# join all words into new string
string_new = ' '.join(c)
# split this new string into sentences
string_newest = string_new.split('.')
last_words = []
# further split sentences into list of words and retrive last word from element in the list
for i in string_newest:
    if i:
        words = i.split()
        last_word = words[-1]
        last_words.append(last_word)
# join all words received and capitalize the sentence
new_sentence = ' '.join(last_words).capitalize()
# every sentence strip of spaces and capitalize the sentence (if not to strip, we can by index
# take 2nd element and capitalize this element only)
for i in string_newest:
    b = i.strip().capitalize()
    # replace sentences from small letter to sentences from big letter
    index_of_sentence = string_newest.index(i)
    string_newest[index_of_sentence] = b
# join all sentences
string_super = '. '.join(string_newest)
# create a final string containing newly formed sentence too
final_string = string_super + new_sentence + '.'
print(string_super)
print(new_sentence)
# count all True (1) values for whitespaces in final string
whitespace_count = sum(c.isspace() for c in final_string)
print(final_string)
print(whitespace_count)
