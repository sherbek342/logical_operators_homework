def main(a):
    """
    Given a three-digit integer a,  check the following statement "All digits sum is odd".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    x1=a%10 # 5
    a=a//10
    x2=a%10 # 4
    x3=a//10
    return  (x1+x2+x3)%2!=0
print(main(123))#