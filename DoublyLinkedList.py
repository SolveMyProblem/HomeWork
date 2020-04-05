# Create node
class Node:

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


# Create doubly linked list
class Doubly_Linked_List:
    # Create Constructor
    def __init__(self):
        self.head = None
        self.size = 0

    # Adding new Value into Node
    def push(self, NewVal):
        NewNode = Node(NewVal)
        NewNode.next = self.head
        if self.head is not None:
            self.head.prev = NewNode
        self.head = NewNode
        self.size += 1

    # Define the method to print linked list
    def list_print(self, node):
        count = 0
        while (node is not None):
            print(node.data, end=' ')

            node = node.next
            count += 1
            if count % 50 == 0:
                print()

    # Define the method to append data into linked list
    def append_list(self, data):
        NewNode = Node(data)
        NewNode.next = None
        if self.head is None:
            NewNode.prev = None
            self.head = NewNode
            return
        last = self.head
        while (last.next is not None):
            last = last.next
        last.next = NewNode
        NewNode.prev = last
        self.size += 1
        return

    # Define the method to find first pre maximum
    def find_pre_max(self):
        max = self.head.data
        cur = self.head
        index = None
        while (cur.next is not None):
            if (cur.data > max):
                max = cur.data
                index = cur
            else:
                cur = cur.next
        return index.prev.data

    # Define the method to find the closet number to the maximum number
    def find_closet_max(self):
        if (self.head.data > self.head.next.data):
            max_1 = self.head.data
            max_2 = self.head.next.data
        else:
            max_1 = self.head.next.data
            max_2 = self.head.data

        cur_node = self.head
        while (cur_node.next is not None):
            if (cur_node.data > max_1):
                max_2 = max_1
                max_1 = cur_node.data
            elif (cur_node.data > max_2 and cur_node.data < max_1):
                max_2 = cur_node.data
            else:
                cur_node = cur_node.next

        return max_2
    #Define the method to delete node
    def remove(self, node):
        if self.head and node is None:
            return
        cur_node = self.head
        if cur_node == node :
            self.head = cur_node.next
            self.head.prev = None



# Define reading data from file
def read_file(file_name):
    f = open(file_name, 'r')
    data = []
    for line in f:
        tmp = line.strip()
        arr = tmp.split('\t')
        data.append(arr)
    return data


data = read_file("data.txt")

first_list = Doubly_Linked_List()

for i in range(len(data) - 1):
    for j in range(len(data[i]) - 1):
        first_list.append_list(int(data[i][j]))

first_list.list_print(first_list.head)
print()

Pre = first_list.find_pre_max()
print("\nPrevious of Max is ", Pre)

wait = input("Press any key to continue...")

max_2 = first_list.find_closet_max()
print("\nThe closet numer to the maximum number is", max_2)
first_list.list_print(first_list.head)
