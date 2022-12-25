


'''
把每個range(start,end)包成一個Node，以start 放入二元樹

'''


class Calendar(object):

    def __init__(self):
        self.bookings = []

    def book(self, start, end):
        def isOverlap(A, B):

            if B[0] >= A[1] or B[1] <= A[0]:
                return False
            return True

        if not self.bookings:
            self.bookings.append([start, end])
            return True
        else:
            l, h = 0, len(self.bookings) - 1
            while l <= h:
                mid = (l + h) // 2
                if start >= self.bookings[mid][1]:
                    l = mid + 1
                else:
                    h = mid - 1
            if l < len(self.bookings) and isOverlap(self.bookings[l], [start, end]):
                return False
            else:
                self.bookings = self.bookings[:l] + [[start, end]] + self.bookings[l:]
                return True

# class Node:
#
#     def __init__(self, s, e):
#         self.end_ = e
#         self.start_ = s
#         self.left = None
#         self.right = None
#
# class Calendar(object):
#
#     def __init__(self):
#         self.root = None
#
#     def bise(self, s, e, node):
#         if s >= node.end_ :
#             if node.right:
#                 return self.bise(s, e, node.right)
#             else:
#                 node.right = Node(s, e)
#                 return True
#         elif e <= node.start_ :
#             if node.left:
#                 return self.bise(s, e, node.left)
#             else:
#                 node.left = Node(s, e)
#                 return True
#         else:return False
#
#     def book(self, start, end):
#         if not self.root:
#             self.root = Node(start, end)
#             return True
#         return self.bise(start, end, self.root)

if __name__ == "__main__":
    a = Calendar()
    print(a.book(1, 10))
    print(a.book(2, 3))
    print(a.book(3, 4))
    print(a.book(3, 4))
    print(a.book(0, 1))
    print(a.book(1, 2))
    print(a.book(3, 4))
    print(a.book(11, 20))
    print(a.book(11, 12))
    print(a.book(12, 13))
    print(a.book(14, 15))
    print(a.book(11, 12))
    print(a.book(11, 12))
    print(a.book(11, 12))


#     """
#     True
#     False  #[15, 20) is unavailable
#     True
#     False  #[17, 21] is unavailable
#     True
#     False  #[2, 3) is unavailable
#     True
#     """
#
#     a = Calendar()
#     print(a.book(5, 15))
#     print(a.book(0, 18))
#     print(a.book(24, 29))
#     print(a.book(13, 25))
#     print(a.book(18, 22))
#     print(a.book(15, 18))
#     """
#     True
#     False  #[5, 15) is unavailable
#     True
#     False  #[24, 25] is unavailable
#     True
#     True
#     """



