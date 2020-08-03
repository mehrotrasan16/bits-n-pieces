#Problem Statement
# 141. Linked List Cycle

# Given a linked list, determine if it has a cycle in it.

# To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.


# Example 1:

# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where tail connects to the second node.


# Example 2:

# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where tail connects to the first node.


# Example 3:

# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.


# Follow up:

# Can you solve it using O(1) (i.e. constant) memory?

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        try:
            slow = head
            fast = head.next
            while slow is not fast:
                slow = slow.next
                fast = fast.next.next
            return True
        except:
            return False
        
        #presuming the value for each node is unique.
        #list to contain values
        # l = set()
        # while(head is not None):
        #         #if value exists in list, then it has been revisited, therefore there's a cycle
        #         if(head.val in l):
        #             return True
        #         else:
        #             l.add(head.val)
        #         print(l)
        #         head = head.next
        # return False

        #The above presumption is not valid as shown by this test case on LC
        #[-21,10,17,8,4,26,5,35,33,-7,-16,27,-12,6,29,-12,5,9,20,14,14,2,13,-24,21,23,-21,5]
        # -1
        # Output
        # true
        # Expected
        # false

        ## BUUUT IF WE DO THE ABOVE WITH NODES INSTEAD OF VALUES, THEN IT PASSES
        l = set()
        
        current_node = head
        while current_node:
             #if value exists in list, then it has been revisited, therefore there's a cycle
            if current_node in l:
                return True
            else:
                l.add(current_node)
            current_node = current_node.next
            
        return False


        

        
            