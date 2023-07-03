def flattenList(nested_List):
    if not (bool(nested_List)):
        return nested_List

    if isinstance(nested_List[0], list):
        return flattenList(*nested_List[:1]) + flattenList(nested_List[1:])

    return nested_List[:1] + flattenList(nested_List[1:])


nested_List = [[10, 90, 10, 60], [1, 8, 0, 5]]
print('Nested List: ', nested_List)
print("Flattened List: ", sorted(flattenList(nested_List)))
