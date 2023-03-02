def main(x):
    """
    Given a two digit integer x, return true if x is palindrome integer.
    An integer is a palindrome, when it reads the same backward as forward.

    Args:
        x(int): parameter x
    Returns:
        bool: answer
    """
    
    x1= x%10
    x = x//10
    
    x2= x%10

    
    x3= x//10
    
    return (x>99 and x1==x2) or ( x<99 and x1==x3)
print(main(787))



















