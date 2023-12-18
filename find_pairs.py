# def count_pairs_with_condition(a,n):
#     count = 0
#     for i in range(n):
#         for j in range(n):
#             if i != j:
#                 diff = (a[i] - a[j])
#                 if diff == (i-j):
#                     count += 1
#     return count

# def count_pairs_with_condition(a,n):
#     return sum(1 for i in range(n) for j in range(n) if i!=j and (a[i]-a[j])==(i-j))

# wrong
# def count_pairs_with_condition(a, n):
#     count = 0
#     valueCount = {}

#     for i in range(n):
#         diff = a[i] - i

#         if diff in valueCount:
#             count += valueCount[diff]

#         if diff + 1 in valueCount:
#             count += valueCount[diff + 1]
        
#         if diff - 1 in valueCount:
#             count += valueCount[diff - 1]
        
#         valueCount[diff] = valueCount.get(diff,0) + 1
    
#     return count

# def count_pairs_with_condition(a, n):
#     count = 0
#     valueCount = {}

#     for i in range(n):
#         for j in range(n):


def count_pairs_with_condition(a, n):
    count = 0
    
    i = 0
    while i < n:
        for j in range(n):
            if i != j and (a[i]-a[j]) == (i-j):
                count += 1
        i += 1
    
    return count
                
n = int(input())
arr = [int(num) for num in input().split(" ")]

result = count_pairs_with_condition(arr,n)
print(result)
