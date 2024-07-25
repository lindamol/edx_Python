import sys

class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action

class StackFrontier():#LIFO
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node) # Add node to frontier

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0 #To empty

    def remove(self):
        if self.empty():
            raise Exception("Empty Frontier")
        else:
            node = self.frontier(-1) # to get last item in the list LIFO
            self.frontier = self.frontier[:-1] # remove the node now
            return node
class QueueFrontier(StackFrontier): #FIFO
    def remove(self):
        if self.empty():
            raise Exception("Empty Frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node

class Maze():
    def __init__(self, filename):
