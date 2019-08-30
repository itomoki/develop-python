def squareRootExhaustive(x, epsilon):
    """xとepsilonを性のfloat型とし、かつepsilon < 1であるとする
       y*yとxのゴザがepsilon以内であるようなyを返す"""
    step = epsilon**2
    ans  = 0.0
    while abs(ans**2 - 2) >= epsilon and ans*ans <= x:
        ans += step
    if ans*ans > x:
        raise ValueError
    return ans

