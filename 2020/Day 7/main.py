from anytree import Node, RenderTree


visited = []  # List to keep track of visited nodes.
queue = []


def file_to_list(filename):
    file = open(filename, 'r')
    return [line.strip() for line in file]


def part_one():
    input_list = file_to_list("input.txt")
    hashtable = dict()
    counter = 0
    for line in input_list:
        parent_bag = line[:line.index(" contain ")-1]
        print("parent : " + parent_bag)
        rest = line[line.index("contain") + 10:]
        print("rest : " + rest)
        child_bag_1 = ""
        child_bag_2 = ""
        if "," in rest:
            child_bag_1 = rest[: rest.index(",")]
            if child_bag_1[len(child_bag_1)-1] == 's':
                child_bag_1 = child_bag_1[:len(child_bag_1)-1]
            child_bag_2 = rest[rest.index(',')+4:rest.index(".")]
        else:
            child_bag_2 = rest[:len(rest)-1]
        if child_bag_2[len(child_bag_2) - 1] == 's':
            child_bag_2 = child_bag_2[:len(child_bag_2) - 1]
        print("child 1 : " + child_bag_1)
        print("child 2 : " + child_bag_2)
        if child_bag_2 == ' other bag':
            hashtable[parent_bag] = []
        else:
            hashtable[parent_bag] = [child_bag_1, child_bag_2]
    print(hashtable)
    return(bfs(visited, hashtable, 'shiny gold bag'))


def bfs(visited, graph, node):
    listi = []
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(1, end = " ")
        listi.append("1")

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
    return len(listi)


if __name__ == '__main__':
    print("final : " + str(part_one()))
    # print("final : " + str(part_two()))
