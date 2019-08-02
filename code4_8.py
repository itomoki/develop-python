def isPalindrome(s):
    """sを文字列と仮定
    sが回分ならTrueを返し、それ以外ならFalseを返す
    ただし句読点、空白、大文字・小文字は無視する"""

    def toChars(s):
        s = s.lower()
        letters = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                letters = letters + c
        return letters

    def isPal(s):
        print('  isPal called with', s)
        if len(s) <= 1:
            print('  About to return True from base case')
            return True
        else:
            answer = s[0] == s[-1] and isPal(s[1:-1])
            print('  About to return', answer, 'for', s)
            return answer

    return isPal(toChars(s))

def testIsPalindrome():
    print('Try dogGod')
    print(isPalindrome('dogGod'))
    print('Try doGood')
    print(isPalindrome('doGood'))

testIsPalindrome()
