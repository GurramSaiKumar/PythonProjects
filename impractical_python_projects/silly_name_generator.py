import random

first = ('lanja', 'denguta', 'modda', 'puku')
last = ('gudda', 'shiku', 'munda', 'daana', 'kodaka')


def silly_generator():
    first_choice = random.choice(first)
    second_choice = random.choice(last)
    return first_choice + ' ' + second_choice


if __name__ == '__main__':
    while True:
        try_again = input("Press n to exit. Else Enter")
        if try_again.lower() == 'n':
            break
        silly_word = silly_generator()
        print(silly_word)
