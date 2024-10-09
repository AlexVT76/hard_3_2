
summa_ = []
def calculate_structure_sum(*data_structure):
    for element in data_structure:
        if isinstance(element, int):
            summa_.append(element)
        elif isinstance(element, str):
            summa_.append ( len(element))
        elif isinstance(element, dict):
            for i in element:
                key = (i, element[i])
                calculate_structure_sum(*key)
        else:
            calculate_structure_sum(*element)
    return(sum(summa_))

data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calculate_structure_sum(data_structure)
print(result)
