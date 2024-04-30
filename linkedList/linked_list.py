import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class Linked_List:
    def __init__(self):
        self.head = None

    def append_node(self,value):
        # a -> b -> c -> None
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                #print(current)
                current = current.next
            current.next = new_node
        return self.head
    
    def print_out_linked_list(self):
        list1 = []
        if self.head == None:
            return
        else:
            current = self.head
            list1.append(current.data)
            while current.next != None:
                current = current.next
                list1.append(current.data)
        return list1 

    def insert_at_index(self,value):
        return self.head  

    def insert_it_beginning(self, value):
        pass 
    def delete_at_index(self, value):
        pass
    # function for reversing a linked list
    def reverse_linked_list(self):
        # a -> b -> c -> d -> None
        # d -> c -> b -> a -> None
        if self.head == None:
            return
        prev = None
        current = self.head
        while current is not None:
            # for first iteration
            next = current.next # b
            current.next = prev # None
            prev = current # a
            current = next # b
        self.head = prev
        return self.head
    
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
        
val2 = Linked_List()
val2.append_node('a')
val2.append_node('b')
val2.append_node('c')
val2.append_node('d')
val2.append_node('e')
val2.append_node('f')
print(val2)
print(val2.print_out_linked_list())
print(val2.reverse_linked_list())
print(val2)