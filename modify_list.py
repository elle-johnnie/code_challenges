arr = [1, 2, 3, 4, -5]

def square(num):
    return num * num
# map operation
print(map(square, arr) ) # => map object
print(list(map(square, arr)))  # => [1, 4, 9, 16, 25]
# list comprehension
print([square(n) for n in arr]) # => [1, 4, 9, 16, 25]

#####
# conditionals
#####
def is_odd(n):
    return n % 2 == 1
# filter operation
print(filter(is_odd, arr))  # filter object
print(list(filter(is_odd, arr))) # =>  [1, 3, -5]
# list comprehension
print([num for num in arr if is_odd(num)])

#####
# matrix
#####
num_cols = 5
num_rows = 3
grid = [[0 for _ in range(num_cols)] for _ in range(num_rows)]
print(grid)
# => [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

arr = list(range(1, 21))
print(max(arr))
print(max(arr, key=lambda x : x ** 2))  # => 20
print(min(arr, key=lambda x : x - 3))  # => 1

