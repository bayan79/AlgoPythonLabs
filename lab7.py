# 1) Описание людей списком и выбор самого старшего
fields = ['name', 'surname', 'age', 'phone']

description_list = [
    ['Kirill', 'Bayandin', 22, "88005553535"],
    ['Ivan', 'Ivanov', 23, "88005551234"],
    ['Peter', 'Peterov', 26, "88005552345"],
    ['Simon', 'Simonov', 25, "88005553456"],
]

# 2) Описание словарем и выбор младшего
description_dict = {man[3]: dict(zip(fields, man)) for man in description_list}


if __name__ == '__main__':
    oldest = sorted([man for man in description_list], key=lambda x: x[2])[-1]
    print('Oldest:', dict(zip(fields, oldest)))

    youngest_key, _ = sorted(description_dict.items(),
                             key=lambda x: x[1]['age'])[0]
    print('Youngest:', description_dict[youngest_key])
