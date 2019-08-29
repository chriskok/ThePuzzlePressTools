#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:ts=4:et:sw=4

class Vertex(object):
    def __init__(self, node, *nodeList):
        self.i = node
        self.nodeList = list(nodeList)

    def add(self, *nodeList):
        # print('adding {} to {}'.format(list(nodeList), self.i))
        self.nodeList.extend(list(nodeList))
    
    def removeNode(self, node):
        if node in self.nodeList:
            self.nodeList.remove(node)

    def __hash__(self):
        return self.i

    def reaches(self, vertex):
        ''' Can receive an integer or a Vertex
        '''
        if isinstance(vertex, int):
            return vertex in self.nodeList

        return self.reaches(vertex.i)

    def printEdges(self):
        return "{}={}".format(self.i, self.nodeList)

    def printNode(self):
        return str(self.i)

    def getAllEdges(self):
        return [int(number) for number in self.nodeList]

    def __str__(self):
        # return '< ' + str(self.i) + '>'
        return self.printEdges()

    def __repr__(self):
        return self.__str__()


class Graph(object):
    def __init__(self):
        self.vList = {}

    def add(self, node, *nodeList):
        if (node in self.vList):
            self.vList[node].add(*nodeList)
        else:
            vertex = Vertex(node, *nodeList)
            self.vList[node] = vertex
    
    def removeNode(self, node):
        if (node in self.vList):
            # print(self.vList[node])
            for connected in self.vList[node].getAllEdges():
                self.vList[connected].removeNode(node)
            del self.vList[node]
    
    def removeEdges(self, node1, node2):
        if (node1 in self.vList and node2 in self.vList):
            self.vList[node1].removeNode(node2)
            self.vList[node2].removeNode(node1)

    def __str__(self):
        return str(self.vList)

    def hamiltonian(self, current = None, pending = None, destiny = None):
        ''' Returns a list of nodes which represent
        a hamiltonian path, or None if not found
        ''' 
        if pending is None:
            pending = self.vList.values()
        
        result = None

        if current is None:
            for current in pending:
                result = self.hamiltonian(current, [x for x in pending if x is not current], current)
                if result is not None:
                    break
        else:
            if pending == []: 
                if current.reaches(destiny):
                    return [current]
                else:
                    return None

            for x in [self.vList[v] for v in current.nodeList]:
                if x in pending:
                    result = self.hamiltonian(x, [y for y in pending if y is not x], destiny)
                    if result is not None:
                        result = [current] + result
                        break    

        # return result
        if result is not None:
            new_list = [int(str(i).split('=')[0]) for i in result]
            return new_list
        else:
            return result

def producePuzzleBoard(number):
    current_board = []
    for i in range(number):
        current_row = []
        for j in range(number):
            current_number = i*number + j 
            current_row.append(current_number)
        current_board.append(current_row)
    
    return current_board

def createNodes(graph, board, entrance_index=-1, exit_index=-1):
    board_size = len(board)
    row_index = 0
    for row in board:
        col_index = 0
        for col in row:
            current_node = col
            if (row_index > 0):
                graph.add(current_node, board[row_index - 1][col_index]) # add top node
            if (col_index < board_size - 1):
                graph.add(current_node, board[row_index][col_index + 1]) # add right node
            if (row_index < board_size - 1):
                graph.add(current_node, board[row_index + 1][col_index]) # add bottom node
            if (col_index > 0):
                graph.add(current_node, board[row_index][col_index - 1]) # add left node
            col_index += 1
        row_index += 1

    if (entrance_index != -1 and exit_index != -1):
        graph.add(entrance_index, exit_index)

if __name__ == '__main__':
    
    puzzle_board = producePuzzleBoard(3)

    G = Graph() 


    createNodes(G, puzzle_board, 1, 6)
    # print(G)

    # G.removeNode(0)
    # print(G)

    # G.removeEdges(1,4)
    # print(G)

    try:
        print (G.hamiltonian())
    except KeyError:
        print("Please enter a valid entrace or exit index.")