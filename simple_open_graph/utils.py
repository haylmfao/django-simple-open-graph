from itertools import cycle,islice
from collections import OrderedDict

def string_to_dict(string):
    dict = OrderedDict()
    if string:
        string = str(string)
        for arg in string.split(','):
            arg = arg.strip()
            key, value = arg.split('=', 1)

            if key in dict:
                current_value = dict[key]
                if type(current_value) == list:
                    dict[key].append(value)
                else:
                    dict[key] = [current_value, value]                    
            else:
                dict[key] = value
    return dict

def roundrobin(*iterables):    
    # Recipe credited to George Sakkis
    pending = len(iterables)
    nexts = cycle(iter(it).next for it in iterables)
    while pending:
        try:
            for next in nexts:
                yield next()
        except StopIteration:
            pending -= 1
            nexts = cycle(islice(nexts, pending))


