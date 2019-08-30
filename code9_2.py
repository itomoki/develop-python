def squareRootBi(x, epsilon):
    """xとepsilonを性のfloat型とし、かつepsilon<1であるとする
       y*yとxの誤差がepsilon以内であるようなyを返す"""
    low = 0.0
    high = max(1.0, x)
    ans = (high + low)/2.0
    while abs(ans**2 - x) >= epsilon:
        if ans**2 < x:
            low = ans
        else:
            high = ans
        ans = (high + low)/2.0
    return ans

