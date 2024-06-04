# Check if Every Row and Column Contains All Numbers
# An n x n matrix is valid if every row and every column contains all the integers from 1 to n (inclusive).
# Given an n x n integer matrix matrix, return true if the matrix is valid.

# Otherwise, return false.
# Example 1:
# Input: matrix = [|1,2,31,[3, 1,21,[2,3, 1]]
# Output: true
# Explanation: In this case, n = 3, and
# every row and column contains the numbers 1, 2, and 3.
# Hence, we return true.

def solution(matrix):
    for row in matrix:
        if not check_rows(row):
            return False
        
    return True

def check_rows(list):
    validations = [False] * len(list)
    for l in list:
        try:
            if validations[l-1]:
                return False
            validations[l-1] = True
        except:
            return False

    for v in validations:
        if not v:
            return v

    return True


print(solution([[1,2,3],[1,2,3],[1,2,3]]))
print(solution([[4,2,3,1],[1,2,3,4],[1,2,3,4]]))