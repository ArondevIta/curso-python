def is_divisible(valor):
    if valor % 3 == 0 and valor % 5 == 0:
        return 'FizzBuzz'
    if valor % 5 == 0:
        return 'Buzz'
    if valor % 3 == 0:
        return 'Fizz'
    else:
        return valor


print(is_divisible(5))
