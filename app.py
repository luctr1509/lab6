def to_jaden_case(string):
    return " ".join(x.capitalize() for x in string.split(' '))


print(to_jaden_case("he isn't"))