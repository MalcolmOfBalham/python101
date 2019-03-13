print("Let's practice everything")
print('You\'d need to know \'bout escapes with \\ that do:')
print('\n newlines and \t tabs')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend the passion from intuition
and requires an explanation
\n\t\t where there is none
"""

print("---------------")
print(poem)
print("---------------")

five = (10 - 2 + 3 - 6)
print(f"this should be five: {five}")

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
#it's just like wiht an f"" string"
print(f"We'd have {beans} beans, {jars} jars and {crates} crates")

start_point /= 10

print("We can also do that this way:")
formula = secret_formula(start_point)
print("We'd have {} beans, {} jars and {} crates".format(*formula))

#the following functions are all from ex25 but put them in here
#once done, import the module in a session
#e.g. import ex24
#and then run by creating a sentence and calling the functions

#also after importing, this is helpful - really justifies putting comments for functions..:
#help(ex24)
#help(ex24.break_words)

def break_words(stuff):
    """This function will break up words for us"""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """prints the last word after popping it off."""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Takes in the sorted sentence and returns the sorted words"""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """prints the first and last word of the sentence"""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words and then prints the first and last"""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

