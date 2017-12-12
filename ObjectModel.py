"""
Object Model test scripts
"""

def modify(k):
    """
    Modifies the content of my list
    :param k: list
    :return: nothing
    """
    k.append(33)
    print("k=",k)

def replace(g):
    """
    Replace the content of a list
    :param g: list object
    :return: nothing
    """
    g = [17, 36, 22, 33]
    print("g=",g)

def update_info(g):
    """
    increment each member of the list by 1
    :param g: original list
    :return: nothing
    """
    i = 0
    #for number in g:
    while i < len(g):
        g[i] += 1
        i += 1
    print("g=",g)


def banner(message, border='*'):
    """
    Displays message surrounded by border
    :param message: message string
    :param border: border style (char)
    :return: nothing
    """
    i = 0
    top = ""
    while i < len(message)+4:
        top += (border)
        i += 1

    print(top)
    print(border, message, border)
    print(top)

# Always use immutable objects such as integer or strings for default values
def add_spam(menu=None):
    """
    Add spam to my list
    :param menu: Optional list object
    :return: menu
    """
    if menu is None:
        menu = []
    menu.append("spam")
    return menu

def number_info():
    """
    Write a function that prompts the user
    for two integers, then it prints: the sum,
    the difference, the product, the average,
    and the distance(absolute value), the maximum,
    the minimum
    :return: none
    """
    a = float(input("Please enter a number: "))
    b = float(input("Please enter another number: "))
    print("Sum: ", a+b)
    print("Difference: ", a-b)
    print("Product: ", a*b)
    print("Average: ", (a+b)/2)
    print("Distance: ", abs(a-b))
    if a > b:
        print("Max: ", a)
        print("Min: ", b)
    else:
        print("Max: ", b)
        print("Min: ", a)
    ######
    print("%-12s%5d" % ("Sum:", a+b))
    print("%-12s%5d" % ("Difference:", a-b))
    print("%-12s%5d" % ("Product:", a*b))
    print("%-12s%8.2f" % ("Average:", (a+b)/2))
    print("%-12s%5d" % ("Distance:", abs(a-b)))
    print("%-12s%5d" % ("Max:", max(a,b)))
    print("%-12s%5d" % ("Min:", min(a,b)))


def main():
    #m = [9, 12, 45]
    #print("before m=",m)
    #modify(m)
    #print("after m=",m)
    #replace(m)
    #print("after replace m=",m)
    #update_info(m)
    #print("after update_info m=",m)
    #banner("test")
    #banner(border="@", message="Weber State")
    menu = ["eggs"]
    add_spam(menu)
    print(menu)
    add_spam(menu)
    print(menu)
    print(add_spam())
    print(add_spam())
    number_info()







if __name__ == '__main__':
    main()