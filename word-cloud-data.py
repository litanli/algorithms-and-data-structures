# Word Cloud Data
# Given a long string (a few words, a few sentences, a paragraph, etc.) build
# a word cloud using a dictionary. We'll treat words that begin with an upper
# case letter as the same word as their lowercase counterparts. We can assume
# our input contains only words and standard punctuations.

# e.g. input: 'After beating the eggs, Dana read the next step: Add milk and
#              eggs, then add flour and sugar.'
#      output: word_cloud_data = {'after': 1, 'the': 2, ..., 'add': 2}

# We need to break this problem down into subproblems
# 1. Splitting the words from the input string
# 2. Populating the dictionary with each word
# 3. Handling words that are both uppercase and lowercase

# What's rule do we choose for handling words that are both upper case and 
# lower case. E.g. how do we treat words that are capitalized because they 
# start a sentence and its lowercase counterparts. How do we treat the pronoun 
# "Bill" vs. the dollar "bill"? We want our word cloud dictionary to reflect 
# the context in which the word appears in the input string. Here's some rules 
# we can consider. Importantly, none of these rules are perfect.

# 1. Capitalize a word if it always appears capitalized.
#    This will retain pronouns in capitalized form, but for shorter inputs 
#    where words are less likely to be repeated we may get non-pronoun words 
#    that begin a sentence in capitalized form.

# 2. Capitalize a word if it ever appears capitalized in the input string.
#    All pronouns will be capitalized, but all words that start a sentence will 
#    always be included in capitalized form.

# 3. Include every word in lower case, ignoring case entirely.
#    This gives us simplicity but we lose all information case would provide.

# 4. Use an API or other tool that identifies proper nouns.
#    This has potential to give us a high level of accuracy, but we'll give up
#    control of decisions, we'll be relying on code we didn't write, and our
#    practical runtime may be significantly increased

# We'll choose rule option 1. Capitalize a word if it always appears 
# capitalized. We'll use a class so we can call our methods on instances of 
# our class instead of passing references. Instead of using the built-in 
# split(), we'll write our own split word functionality that allows us to split
# the words from the input_string and add to our dictionary immediately.

class WordCloudData:

    def __init__(self, input_string):
        self.words_to_counts = {}
        self.populate_words_to_counts(input_string)

    def populate_words_to_counts(self, input_string):
        # Iterates over each character in the input string, splitting
        # words and passing them to add_word_to_dictionary()
        current_word_start_index = 0
        current_word_length = 0
        
        for i, character in enumerate(input_string):

            # If we reached the end of the string we check if the last
            # character is a letter and add the last word to our dictionary
            if i == len(input_string) - 1:
                if character.isalpha():
                    current_word_length += 1
                if current_word_length > 0:
                    current_word = input_string[current_word_start_index:
                        current_word_start_index + current_word_length]
                    self.add_word_to_dictionary(current_word)

            # If we reach a space or emdash we know we're at the end of a word
            # so we add it to our dictionary and reset our current word
            elif character == ' ' or character == u'\u2014':
                if current_word_length > 0:
                    current_word = input_string[current_word_start_index:
                        current_word_start_index + current_word_length]
                    self.add_word_to_dictionary(current_word)
                    current_word_length = 0

            # We want to make sure we split on ellipses so if we get two periods in
            # a row we add the current word to our dictionary and reset our current word
            elif character == '.':
                if i < len(input_string) - 1 and input_string[i + 1] == '.':
                    if current_word_length > 0:
                        current_word = input_string[current_word_start_index:
                            current_word_start_index + current_word_length]
                        self.add_word_to_dictionary(current_word)
                        current_word_length = 0

            # If the character is a letter or an apostrophe, we add it to our current word
            elif character.isalpha() or character == '\'':
                if current_word_length == 0:
                    current_word_start_index = i
                current_word_length += 1

            # If the character is a hyphen, we want to check if it's surrounded by letters
            # If it is, we add it to our current word
            elif character == '-':
                if i > 0 and input_string[i - 1].isalpha() and \
                        input_string[i + 1].isalpha():
                    if current_word_length == 0:
                        current_word_start_index = i
                    current_word_length += 1
                else:
                    if current_word_length > 0:
                        current_word = input_string[current_word_start_index:
                            current_word_start_index + current_word_length]
                        self.add_word_to_dictionary(current_word)
                        current_word_length = 0


    def add_word_to_dictionary(self, word):
        # If the word is already in the dictionary we increment its count
        if word in self.words_to_counts:
            self.words_to_counts[word] += 1

        # If a lowercase version is in the dictionary, we know our input word must be uppercase
        # but we only include uppercase words if they're always uppercase
        # so we just increment the lowercase version's count
        elif word.lower() in self.words_to_counts:
            self.words_to_counts[word.lower()] += 1

        # If an uppercase version is in the dictionary, we know our input word must be lowercase.
        # since we only include uppercase words if they're always uppercase, we add the
        # lowercase version and give it the uppercase version's count
        elif word.capitalize() in self.words_to_counts:
            self.words_to_counts[word] = 1
            self.words_to_counts[word] += self.words_to_counts[word.capitalize()]
            del self.words_to_counts[word.capitalize()]

        # Otherwise, the word is not in the dictionary at all, lowercase or uppercase
        # so we add it to the dictionary
        else:
            self.words_to_counts[word] = 1
            
# What we learned:
# We saw there were many heuristics that we could use to handle uppercase and
# lowercase versions of words, none of which were perfect. Open-ended questions
# like this can really separate good engineerings from great engineers.
# Good engineers will come up with a solution, but great engineers will come up
# with several solutions, weigh them carefully, and choose the best one for the
# given context (Remember one of Dan Heath's principles of decision making: 
# expand the number of possibilities). As you consider a problem, challenge 
# yourself to see how many possible solutions you can come up with. This will
# grow your ability to quickly see multiple ways to solve a problem so you can
# find the BEST solution.