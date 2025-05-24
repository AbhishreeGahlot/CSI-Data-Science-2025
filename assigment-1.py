# lower triangular pattern
n= 5
for i in range(1 , n+1):
    print("*" * i )


# Upper Triangular Pattern
n = 5 
for i in range(n): 
     print(' ' * i + '*' * (n - i))


# Pyramid Pattern
for i in range(1, n + 1):
        spaces = ' ' * (n - i)
        stars = '*' * (2 * i - 1)
        print(spaces + stars)