# Оформить функциями поиск в словаре и списке
from pprint import pprint

from lab2 import fuzzy_compare_int, fuzzy_compare_string
from lab7 import description_list, description_dict

NAME = 0
SURNAME = 1
AGE = 2
PHONE = 3


def get_estimate_function(field, searched_value):
    if isinstance(searched_value, str):
        compare = fuzzy_compare_string
    elif isinstance(searched_value, int):
        compare = fuzzy_compare_int
    else:
        raise ValueError(f'Unable to estimate value: {searched_value}[field: {field}]')

    def _estimate(item):
        return compare(item[field], searched_value)

    return _estimate


def list_fuzzy_search(field: int, searched_value, source_list):
    estimate = get_estimate_function(field, searched_value)
    return sorted(source_list, key=estimate)[-1]


def dict_fuzzy_search(field: str, searched_value, source_dict):
    estimate = get_estimate_function(field, searched_value)
    index = sorted(source_dict.keys(),
                   key=lambda x: estimate(source_dict[x]))[-1]
    return {**source_dict[index], 'phone': index}


if __name__ == "__main__":
    print('Source:')
    pprint(description_list)
    print(
        '[List] Phone ends with ..3535: ',
        list_fuzzy_search(
            PHONE,
            '3535',
            description_list))

    print('Source:')
    pprint(description_dict)
    print(
        '[Dict] Phone ends with ..3535: ',
        dict_fuzzy_search(
            'phone',
            '3535',
            description_dict))
