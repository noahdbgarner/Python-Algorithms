# Pascal function using the calculation of the previous row to calculate the current row to print
def pascal_triangle(nrows):
    row_list, num = [], 1
    for i in range(1, nrows + 2):
        row_list.append(num)
        num = int(num * (nrows - i + 1) / i)
    print(row_list)

# URL shortening a number from any base to any base. We will call it a bijective function
def base_n(num, frombase=10, base=64):
    alphabet = "0123456789abcdefghijklmnoppqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-"
    result = ""
    num = int(str(num), frombase)
    if num == 0:
        print(alphabet[num])
    while num > 0:
        result = alphabet[num % base] + result
        num = int(num / base)
    print(result)



if __name__ == "__main__":

    base_n(10)
    # Prints 'a' Given the alphabet "0123456789abcdefghijklmnoppqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-"
    base_n(1010, frombase=2, base=64)
    # Prints 'a' given the alphabet "0123456789abcdefghijklmnoppqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-"



    pascal_triangle(3)


    pass
