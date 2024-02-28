class QueueNode:
    def __init__(self, value=None, next_node=None):
        self.node_value = value
        self.next_node = next_node


class Queue:

    def __init__(self):
        self.queue_head = None
        self.queue_tail = None
        self.queue_length = 0

    def enqueue(self, node):
        if self.queue_length == 0:

            # head and tail are the same, because only 1 node
            self.queue_head = self.queue_tail = node

        else:
            # append the new node to to the tail's next node, then make it the new tail
            self.queue_tail.next_node = node
            self.queue_tail = node

        self.queue_length += 1


    def dequeue(self):

        # nothing to dequeue
        if self.queue_head is None:
            return None
        
        self.queue_length -= 1

        # removing from the head because it's a First In First Out data structure
        dequeued_node = self.queue_head

        # point to next item in list, effectively orphaning the previous head (would free memory in C here)
        self.queue_head = self.queue_head.next_node
        return dequeued_node.node_value

    
    def peek(self):
        if self.queue_head:
            return self.queue_head.node_value
        return None
    
# Example usage
node1 = QueueNode(1)
node2 = QueueNode(2)
node3 = QueueNode(73)


queue = Queue()
queue.enqueue(node1)
queue.enqueue(node2)

print(queue.dequeue())  # Output: 1
print(queue.dequeue())  # Output: 2
print(queue.peek())     # Output: None (queue is empty)

queue.enqueue(node3)
queue.enqueue(node1)
print(queue.peek())     # Output: 73
