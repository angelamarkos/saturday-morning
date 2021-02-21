import copy
a = 1
b = a
print(a)
print(b)

b = 2

print(a)
print(b)


list_1 = [1, 2, 3]
# list_2 = list_1[:]
# list_2 = list_1.copy()
list_2 = copy.copy(list_1)

print(list_1)
print(list_2)
list_2[1] = 5

print(list_1)
print(list_2)


list_2d_1 = [[1, 2, [1, 2]], [4, 5, 5]]
# list_2d_2 = list(reversed(list(reversed(list_2d_1))))
list_2d_2 = copy.deepcopy(list_2d_1)

print(list_2d_1)
print(list_2d_2)

list_2d_2[0][2][0] = 0

print(list_2d_1)
print(list_2d_2)

class Template:
    def __init__(self, first_item: int, last_item: int, items: list, private_items: list):
        self.first_item = first_item
        self.last_item = last_item
        self.items = items
        self.__private_items = private_items

    def __str__(self):
        return f'{self.first_item} - {self.last_item} \n' \
               f'{self.items}, {self.__private_items}'

    def __copy__(self):
        private_prefix = f'_{str(self.__class__.__name__)}__'
        instance_dict = copy.copy(self.__dict__)
        for k, v in instance_dict.items():
            if private_prefix in k:
                del instance_dict[k]
                k = k.split(private_prefix)[-1]
                instance_dict[k] = None
        return Template(**instance_dict)

    def __deepcopy__(self):
        private_prefix = f'_{str(self.__class__.__name__)}__'
        instance_dict = copy.deepcopy(self.__dict__)
        for k, v in instance_dict.items():
            if private_prefix in k:
                del instance_dict[k]
                k = k.split(private_prefix)[-1]
                instance_dict[k] = v
        return Template(**instance_dict)

    def clone(self, **kwargs):
        private_prefix = f'_{str(self.__class__.__name__)}__'
        instance_dict = copy.deepcopy(self.__dict__)
        for k, v in instance_dict.items():
            if private_prefix in k:
                del instance_dict[k]
                k = k.split(private_prefix)[-1]
                instance_dict[k] = v

        instance_dict.update(**kwargs)
        return Template(**instance_dict)

class CopyManager:
    """
    data_to_copy = {instance1: [kwargs1, kwargs2, kwargs3, ...], instance2: [kwargs21, ... ], ...}
    """
    def __init__(self, data_to_copy: dict):

        self.data_to_copy = data_to_copy

    def add_to_data(self, classname, instance, kwargs):
        self.data_to_copy[classname][instance] = kwargs

    def clone_items(self):
        for instance, kwargs_list in self.data_to_copy.items():
            for kwargs in kwargs_list:
                yield instance.clone(**kwargs)





item = Template(1, 2, [1, 2, 4], [2, 3, 5])
item_copy = copy.copy(item)
print(item)
print(item_copy)
print('------------')
item_copy.first_item = 0
item_copy.items[0] = 0
print(item)
print(item_copy)

copy_manager = CopyManager({item: [{"first_item": 5},
                                   {"last_item": 3, 'items': [1, 2]},
                                   {'first_item': 7, 'private_items': [3, 4]}]})

for item in copy_manager.clone_items():
    print(item)




