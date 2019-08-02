def isPal(x):
    """xをリストとする
    そのリストが回分ならばTrue,そうでんbなければFalseを返す"""
    temp = x[:]
    temp.reverse()
    if temp==x:
        return True
    else:
        return False

def silly(n):
    """nを性のint型とする
    ユーザからn個の入力を受ける
    もし入力文字列が回分であれば'Yes'を,
    そうでなければ'No'を出力する"""
    result = []
    for i in range(n):
        elem = input('Enter element: ')
        result.append(elem)
    print(result)
    if isPal(result):
        print('Yes')
    else:
        print('No')

def main():
    n = input('Please enter the word count : ')
    silly(int(n))

main()



