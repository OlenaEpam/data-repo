# Refactor homeworks from module 2 and 3 using functional approach with decomposition.
text_sample = """homEwork:
tHis iz your homeWork, copy these Text to variable.
You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE 
witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.
it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.
last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, 
but ALL whitespaces. I got 87.
"""
# all text letters make lower-case


def lower_text(text):
    text_lower = text.lower()
    return text_lower



# split text by words
def text_split(text_to_split_by_words):
    c = text_to_split_by_words.split()
    return c


# calling text_split function



# check every word is it is equal to 'iz' and replace it to 'is'
def replace_iz_error(text_to_check):
    for check_word in text_to_check:
        if check_word == 'iz':
            index_of_iz = text_to_check.index(check_word)
            text_to_check[index_of_iz] = 'is'
    # join all words into new string
    string_new = ' '.join(text_to_check)
    return string_new


# calling replace_iz_function



# split this new string into sentences
def text_split_by_sentence(text_to_split_by_sentences):
    string_newest = text_to_split_by_sentences.split('.')
    return string_newest


# calling text split by sentences



def get_last_words(text_for_last_words):
    last_words = []
    # further split sentences into list of words and retrive last word from element in the list
    for i in text_for_last_words:
        if i:
            words = i.split()
            last_word = words[-1]
            last_words.append(last_word)
    # join all words received and capitalize the sentence
    new_sentence = ' '.join(last_words).capitalize()
    return new_sentence


# calling get last words function



# every sentence strip of spaces and capitalize the sentence
def capitalize_sentences(text_lower_case):
    for i in text_lower_case:
        b = i.strip().capitalize()
        # replace sentences from small letter to sentences from big letter
        index_of_sentence = text_lower_case.index(i)
        text_lower_case[index_of_sentence] = b
    # join all sentences
    string_super = '. '.join(text_lower_case)
    return string_super


# call function to capitalize sentences



# create a final string containing newly formed sentence too
def combine_two_strings(string_one, string_two):
    final_string = string_one + string_two + '.'
    print(string_one)
    print(string_two)
    return final_string


# call combine two strings function



# count all True (1) values for whitespaces in final string
def count_whitespaces(text_to_count_in):
    whitespace_count = sum(c.isspace() for c in text_to_count_in)
    return whitespace_count


# calling count_whitespaces function



def print_elements(*args):
    print(args)


# calling function to print
if __name__ == '__main__':
    text_lowered = lower_text(text_sample)
    split_to_words = text_split(text_lowered)
    replaced_iz = replace_iz_error(split_to_words)
    split_by_sentences = text_split_by_sentence(replaced_iz)
    sentence_with_last_words = get_last_words(split_by_sentences)
    capitalized_text = capitalize_sentences(split_by_sentences)
    combined_text = combine_two_strings(capitalized_text, sentence_with_last_words)
    counted_whitespaces = count_whitespaces(combined_text)
    print_elements(combined_text, counted_whitespaces)
