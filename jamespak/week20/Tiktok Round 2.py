# A: [-5, -2, -1, 1, 4, 7, 9], sorted, find median of squares of all elements in A
# example -> [25, 4, 1, 1, 16, 49, 81], median is 16

# A: [-5, -2, -1], B: [1, 4, 7, 9]
# A: [5, 2, 1], B: 1, 4, 7, 9]
# A[::-1]: [1, 2, 5], B: [1, 4, 7, 9]

def find_median(A):
    def split_array(A):
        for i in range(len(A)):
            if A[i] >= 0:
                break
        return A[:i], A[i:]
    
    A, B = split_array(A)
    if not A:
        pass
        return
    if not B:
        pass
        return
    
    l = len(A) + len(B) - 1
    return find_kth(A, B, l // 2)**2 if l % 2 else (find_kth(A, B, l // 2 - 1) + find_kth(A, B, l // 2 ) / 2)**2
# A[::-1]: [1, 2, 5], B: [1, 4, 7, 9]
"""
# A[::-1]: [1, 2, 5], B: [1, 4, 7, 9]
A: [1, 4, 7, 9], B: [1, 2, 5]
        i            j
l = len(A) + len(B) - 1

i = len(A) // 2
j = k - i

if A[i] > B[j]:
    find_kth(A[:i], B[j:], i)
else:
    find_kth(A[i:], B[:j], j)
"""
def find_kth(A, B, k):
    if not A:
        return B[k]
    
    if len(A) > len(B):
        A, B = B, A
    
    if k == len(A) + len(B) - 1:
        return max(A[-1], B[-1])
    i = len(A) // 2
    j = k - i

    if A[i] > B[j]:
        return find_kth(A[:i], B[j:], i)
    else:
        return find_kth(A[i:], B[:j], j)
    

    
    
    
    
    


print(find_median(A)) # 16
