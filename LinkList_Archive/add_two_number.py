# given two linked lists representing two non-negative numbers. 
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.
#
# Input: (2 -> 4 -> 9) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 4 ->1

class Node:
    def __init__(self, data):
        self.val = data
        self.next = None

class LinkedList:

    def add_numbers(self, num1, num2):
        head_node = Node(0)
        curr, carry = head_node, 0

        while num1 or num2:
            val = carry
            if num1:
                val += num1.val
                num1 = num1.next
            if num2:
                val += num2.val
                num2 = num2.next
            carry, val = val / 10, val % 10
            curr.next = Node(val)
            curr = curr.next

        if carry == 1:
            curr.next = Node(1)

        return head_node.next

# if __name__ == '__main__':
#     num1, num1.next, num1.next.next = Node(2), Node(4), Node(9)
#     num2, num2.next, num2.next.next = Node(5), Node(6), Node(4)
#     result = LinkedList().add_numbers(num1, num2)
# print "{0} -> {1} -> {2} ->{3}".format(result.val, result.next.val, result.next.next.val, result.next.next.next.val)
