#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:ts=4:et:sw=4

class Vertex(object):
    def __init__(self, node, *nodeList):
        self.i = node
        self.nodeList = list(nodeList)

    def __hash__(self):
        return self.i

    def reaches(self, vertex):
        ''' Can receive an integer or a Vertex
        '''
        if isinstance(vertex, int):
            return vertex in self.nodeList

        return self.reaches(vertex.i)

    def __str__(self):
        return '< ' + str(self.i) + '>'

    def __repr__(self):
        return self.__str__()


class Graph(object):
    def __init__(self):
        self.vList = {}

    def add(self, node, *nodeList):
        vertex = Vertex(node, *nodeList)
        self.vList[node] = vertex

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

def createNodes(graph, board, entrance_index, exit_index):
    row_index = 0
    for row in board:
        col_index = 0
        for col in row:
            current_node = col
            if (row_index > 0):

            # current_row = 
            col_index += 1
        row_index += 1
    
    G.add(1, 2)
    G.add(2, 1)
    G.add(2, 3)
    G.add(3, 2, 4)
    G.add(4, 3, 1)

if __name__ == '__main__':
    
    puzzle_board = producePuzzleBoard(3)

    G = Graph() 

    createNodes(G, puzzle_board, 0, 8)

    # G.add(1, 2)
    # G.add(2, 1, 3)
    # G.add(3, 2, 4)
    # G.add(4, 3)
    print G.hamiltonian()