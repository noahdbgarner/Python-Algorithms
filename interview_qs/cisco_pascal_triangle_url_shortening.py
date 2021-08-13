

def pascal_triangle(nrows: int) -> None:
    """
    Description:
        Find and print a specific row of Pascal's Triangle

    Args:
        nrows (int): the row of pascal's triangle to return
    Returns:

    Explanation:

    Edge Cases:

    Complexity Analysis:

    """
    row_list, num = [], 1
    for i in range(1, nrows + 2):
        row_list.append(num)
        num = int(num * (nrows - i + 1) / i)
    print(row_list)


def url_shortening(num: int, frombase: int = 10, base: int = 64) -> None:
    """
    Description:
        Converting a number from any base to any base. Call this a bijective function. This represents how
        URL shortening is actually done

    Args:

    Returns:

    Explanation:

    Edge Cases:

    Complexity Analysis:

    """
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

    url_shortening(10)
    # Prints 'a' Given the alphabet "0123456789abcdefghijklmnoppqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-"
    url_shortening(1010, frombase=2, base=64)
    # Prints 'a' given the alphabet "0123456789abcdefghijklmnoppqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-"

    pascal_triangle(3)