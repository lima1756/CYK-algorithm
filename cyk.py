from binarytree import Node
from colorama import init as colorama, Fore

colorama()
test = None #'aaabbb S->AB|XB T->AB|XB X->AT A->a B->b'

def main():
    data = data_input()
    word = data[0]
    inv_productions = data[1]
    matrix = []
    for i in range(len(word)):
        matrix.append([])
    for char in word:
        generator = inv_productions.get(char, None)
        if generator is not None:
            matrix[0].append(generator)
    for i in range(1, len(word)):
        for j in range(0, len(word) - i):
            matrix[i].append([])
            l = j + 1
            for k in range(0, i):
                for element in get_generated(matrix[k][j], matrix[i-(k+1)][l]):
                    generators = inv_productions.get(element, None)
                    if generators is not None:
                        matrix[i][j] = append_unique_elements(matrix[i][j], generators)
                l += 1
    if len(matrix[len(word) - 1][0]) > 0 and matrix[len(word) - 1][0].count('S'):
        print(Fore.GREEN + "La palabra pertenece a la gramatica")
        print(create_tree(matrix, data[2], word))
    else: 
        print(Fore.RED +"La palabra NO pertenece a la gramatica")

def create_tree(matrix, productions, word):
    head = Node("S")
    create_subtree(head, 0, len(matrix)-1, matrix, productions, word)
    return head

def create_subtree(current, position_x, position_y, matrix, productions, word):
    x = position_y + position_x
    for i in range(position_y-1, -1, -1):
        for symbol in matrix[i][position_x]:
            for curr_prod in productions[current.value]:
                if len(curr_prod)>1 and symbol == curr_prod[0]:
                    for symbol2 in matrix[position_y-1-i][x]:
                        if symbol2 == curr_prod[1]:
                            current.left = Node(symbol)
                            current.right = Node(symbol2)
                            create_subtree(current.left, position_x, i, matrix, productions, word)
                            create_subtree(current.right, x, position_y-1-i, matrix, productions, word)
                            return
        x -= 1
    current.left = Node(word[position_x])

def get_generated(cyk_element1, cyk_element2):
    concat_elements = []
    if len(cyk_element1) > 0 and len(cyk_element2)>0:
        for element in cyk_element1:
            for element2 in cyk_element2:
                concat_elements.append(element+element2)
    return concat_elements

def append_unique_elements(list1, list2):
    l = list1
    for element in list2:
        if list1.count(element) == 0:
            l.append(element)
    return l

def data_input():
    '''Input of the CYK data

    Returns:
    list: first element is the word to process, second element is an inverse productions dictionary, third are the productions dictionary
    '''
    if test is not None:
        data = test.split(' ') #input().split(' ')
    else:
        print("Please input the data in the format: \"word production1 production2 production3 ...\"")
        data = input().split(' ')
    word = data[0]
    inv_productions = {}
    productions = {}
    for i in range(1, len(data)):
        val = data[i].split('->')
        symbols = val[1].split('|')
        productions[val[0]] = symbols
        for symbol in symbols:
            if inv_productions.__contains__(symbol):
                inv_productions[symbol] += val[0]
            else:    
                inv_productions[symbol] = [val[0]]
    return [word, inv_productions, productions]

main()
