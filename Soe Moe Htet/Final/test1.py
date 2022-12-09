distance = 0.0

def find_route(start_node, routes):
    global distance

    if start_node in routes:
        next_node = routes[start_node][0]

        distance += routes[start_node][1]

        return find_route(next_node, routes)
    else:
        return distance

routes_dict = {
    "i": ("j", 4.0), 
    "a": ("b", 3.4),
    "j": ("k", 6.0),
    "c": ("d", 5.6),
    "b": ("c", 4.0)
}

print(find_route("q", routes_dict))