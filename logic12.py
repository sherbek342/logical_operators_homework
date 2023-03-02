def main(a):
    """
    Given a two-digit integer a,  check the following statement "All digits of the number are the same".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    x = a%10 
    y = ((a-x)/10)
    return x==y
#print(main(77))