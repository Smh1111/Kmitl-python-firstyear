def find_route(start_node, routes):
    node_list = []
    distance = 0.0

    currentKey = ""
    node_list.append(start_node)
    for key, value in routes.items():
        if key == start_node:
            node_list.append(value[0])
            distance += value[1]
            currentKey = value[0]

    if currentKey:
        
        while currentKey in routes.keys():
            for key, value in routes.items():
                if currentKey == key:
                    node_list.append(value[0])
                    print(value[0], value[1])
                    distance += value[1]
                    currentKey = value[0]

    return node_list, distance

routes_dict = {
    "i": ("j", 4.0), 
    "a": ("b", 3.4),
    "j": ("k", 6.0),
    "c": ("d", 5.6),
    "b": ("c", 4.0)
}

print(find_route("i", routes_dict))


