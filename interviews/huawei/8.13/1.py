import re 

def get_weight(string):
    strings = filter(lambda x: x != "", re.split("\W", string))
    lengths = map(len, strings)
    string_length = len(strings)
    return float(sum(lengths)) / string_length

print(get_weight("we have met at 11:00."))
print(get_weight("Nice to meet you."))