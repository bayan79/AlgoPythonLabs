"""
Сделать:
1) инт такой что 2+2=5
2) лист макс длина = 10
3) лист с уникальными элементами
"""

class MyInt(int):
    def __add__(self, num):
        return 1 + self + num 

class MyList(list):
    def __init__(self, *args, **kwargs):
        self.MAX_SIZE = kwargs.pop("max_size", 0) 
        super().__init__(*args, **kwargs)
        if self.MAX_SIZE:
            del self[self.MAX_SIZE:]

    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        if self.MAX_SIZE:
            del self[self.MAX_SIZE:]

    def __getattribute__(self, attr):
        attribute = super().__getattribute__(attr)
        if attr in ('MAX_SIZE') or not self.MAX_SIZE:
            return attribute
        
        # если встроенная функция и длина больше заданной
        # то заменяем функцию-аттрибут новой, где после выполнения 
        # исходной функции удаляется лишняя часть списка 
        if isinstance(attribute, type([].append)) and len(self) >= self.MAX_SIZE:
            def new_function(*args, **kwargs):
                result = attribute(*args, **kwargs)
                del self[self.MAX_SIZE:]
                return result
            return new_function
        else:
            return attribute

class MySetList(list):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self[:] = list(set(self))

    def __setitem__(self, key, value):
        super().__setitem__(key, [v for v in value if v not in self])

    def __getattribute__(self, attr):
        attribute = super().__getattribute__(attr)

        # если встроенная функция и длина больше заданной
        # то заменяем функцию-аттрибут новой, где после выполнения 
        # исходной функции удаляется лишняя часть списка 
        if isinstance(attribute, type([].append)) and len(self):
            def new_function(*args, **kwargs):
                result = attribute(*args, **kwargs)
                all_keys = slice(None, None, None)
                all_values = list(set(self))
                super(MySetList, self).__setitem__(all_keys, all_values)
                return result
            return new_function
        else:
            return attribute


if __name__ == "__main__":
    a = MyInt(2)
    b = MyInt(2)
    print(f"{a} + {b} = {a+b}")

    print('\n====== MY LIST with capacity ========')
    my_list = MyList(max_size=10)  
    for i in range(15):
        my_list.append(f'app{i}')
        my_list.extend([f'ext{i}'])
        my_list.insert(1, f'i{i}')
        print(my_list)
    print('\n======== MY SET LIST ========')
    my_set_list = MySetList([1,2,3,3,4,5])
    for i in range(10):
        print(f'before append {i}: ', my_set_list)
        my_set_list.append(i)
        print(f'after append {i}: ', my_set_list)
        my_set_list.insert(1, i)
        print(f'after insert {i}: ', my_set_list)
        my_set_list.extend(list(range(i)))
        print(f'after extend {i}: ', my_set_list, '\n')

    my_set_list[10:15] = range(20, 5, -1)
    print(my_set_list)