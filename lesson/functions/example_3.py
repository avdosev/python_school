def func(a):
    res = a*a + a*3
    return res

if __name__ == "__main__":
    line_with_numbers = input("Ввeдите числа через пробел: ")
    numbers = line_with_numbers.split(' ')
    sum_number = 0
    for num in numbers:
        function_res = func(int(num))
        print(function_res)