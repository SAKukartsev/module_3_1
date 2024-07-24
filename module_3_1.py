colls = 0


def count_colls():
    global colls
    colls += 1


def string_info(string=''):
    count_colls()
    up = string.upper()
    low = string.lower()
    cart = (len(string), up, low)
    return cart


def is_contains(string, list_to_search):
    count_colls()
    for i in range(len(list_to_search)):
        if string.lower() == list_to_search[i].lower():
            return True
    return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(colls)
