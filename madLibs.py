"""Mad Libs."""


# From https://www.geeksforgeeks.org/print-colors-python-terminal/
# Python program to print colored text and background
def prRed(skk):
    """Red."""
    return("\033[91m {}\033[00m" .format(skk))


def prGreen(skk):
    """Green."""
    return("\033[92m {}\033[00m" .format(skk))


def prYellow(skk):
    """Yellow."""
    return("\033[93m {}\033[00m" .format(skk))


def prLightPurple(skk):
    """Light Purple."""
    return("\033[94m {}\033[00m" .format(skk))


def prPurple(skk):
    """Purple."""
    return("\033[95m {}\033[00m" .format(skk))


def prCyan(skk):
    """Cyan."""
    return("\033[96m {}\033[00m" .format(skk))


def prLightGray(skk):
    """Light Gray."""
    return("\033[97m {}\033[00m" .format(skk))


def prBlack(skk):
    """Black."""
    return("\033[98m {}\033[00m" .format(skk))


noun1 = input(prRed("Enter a noun.: "))  # 0
verbing = input(prGreen('Enter a verb ending in "ing.": '))  # 1
noun2 = input(prYellow("Enter a noun.: "))  # 2
verb1 = input(prLightPurple("Enter a verb.: "))  # 3
adjective1 = input(prPurple("Enter an adjective.: "))  # 4
plural_noun = input(prCyan("Enter plural noun.: "))  # 5
verb2 = input(prLightGray("Enter a verb.: "))  # 6
possesive_noun = input(prBlack("Enter possesive noun.: "))  # 7
adjective2 = input(prRed("Enter an adjective.: "))  # 8

print(prPurple(
    'The {0} was {1} down by the sea when suddenly a {2} fell '
    'from the sky. '"The crash made everyone {3}. "'So {4} was this '
    'unexpected event, that it even made the {5} '
    '{6}.'' By the time everything calmed down, it became clear '
    'that it had only ''happened in {7} dream.'' Upon awakening, the'
    ' {8} day continued normally.'.format(
        noun1, verbing, noun2, verb1, adjective1, plural_noun, verb2,
        possesive_noun, adjective2)))
# Create Input
# def user_inputs():
#    """Create random words."""
#    noun = list()
#    noun.append(input("Enter a noun.: "))
#    verbing = list()
#    verbing.append(input('Enter a verb ending in "ing.": '))
#    noun.append(input("Enter a noun.: "))
#    verb = list()
#    verb.append(input("Enter a past tense verb.: "))
#    adjective = list()
#    adjective.append(input("Enter an adjective.: "))
#    plural_noun = list()
#    plural_noun.append(input("Enter plural noun.: "))
#    past_tense_verb = list()
#    past_tense_verb.append(input("Enter a past tense verb.: "))
#    possesive_noun = list()
#    possesive_noun.append(input("Enter possesive noun.: "))
#    adjective.append(input("Enter an adjective.: "))
#    print(noun[0])
#    print(verbing)
#    print(verb)
#    print(adjective)
#    print(plural_noun)
#    print(past_tense_verb)
#    print(possesive_noun)


# User Input
# def user_input(prompt):
#    """Accept user input."""
# the input function will display a message in the terminal
# and wait for user input.
#    user_input = input(prompt)
#    return user_input
# user_value = user_input("Please Enter a value:")
# print(user_value)


# TEST
# def test():
#    """Test functions."""
#    test()


# print(
#    'The {noun} was {verbing} down by the place when suddenly a {noun} fell '
#    'from the sky.')
# print("The crash made everyone {verb}.")
# print(
#    'So {adjective} was this unexpected event, that it even made the {nouns} '
#    '{past tense verb}.')
# print(
#    'By the time everything calmed down, it became clear that it had only '
#    'happened in {noun’s} dream.')
# print("Upon awakening, the {adjective} day continued normally.")
