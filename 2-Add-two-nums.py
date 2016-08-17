# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        # Sol 1: 156ms
        flag = 0
        if (l1 == None):
            return l2
        elif (l2 == None):
            return l1

        p1 = l1
        p2 = l2
        p = ListNode(0)
        res = p
        while(p1 != None and p2 != None):
            sum = flag + p1.val + p2.val
            if (sum >= 10):
                flag = 1
                sum -= 10
                p.val = sum
            else:
                flag = 0
                p.val = sum
            if (p1.next == None and p2.next == None):
                if (flag):
                    p.next = ListNode(flag)
                    return res
                else:
                    return res

            p.next = ListNode(0)
            p = p.next
            p1 = p1.next
            p2 = p2.next

        if (p1 == None):
            p1 = p2 # So that p1 points to the long one anyways


        while(p1 != None):
            sum = flag + p1.val
            if (sum >= 10):
                flag = 1
                sum -= 10
                p.val = sum
            else:
                flag = 0
                p.val = sum
            if (p1.next == None):
                if (flag):
                    p.next = ListNode(flag)
                    return res
                else:
                    return res
            p.next = ListNode(0)
            p = p.next
            p1 = p1.next

        return res
        '''
        # Sol 2: 156ms
        p1 = l1; p2 = l2
        while(p1 != None or p2 != None):
            if (p1.next == None and p2.next != None):
                p1.next = ListNode(0)
            elif (p2.next == None and p1.next != None):
                p2.next = ListNode(0)
            p1 = p1.next
            p2 = p2.next


        p = ListNode(0); p1 = l1; p2 = l2; flag = 0
        res = p
        while (p1 != None):
            sum = flag + p1.val + p2.val
            if (sum >= 10):
                sum -= 10
                flag = 1
                p.val += sum
            else:
                p.val += sum
                flag = 0
            if (p1.next == None):
                if (flag):
                    p.next = ListNode(flag)
                    return res
                else:
                    return res
            p.next = ListNode(0)
            p = p.next
            p1 = p1.next
            p2 = p2.next
        return res
        '''
