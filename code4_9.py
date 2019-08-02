def fib(x):
    """x>=0を整数と仮定
       x番目のフィボナッチ数を返す"""
    global numFibCalls
    numFibCalls =+ 1
    if x == 0 or x ==1:
        return 1
    else:
        return fib(x-1) + fib(x-2)

def textFib(n):
    for i in range(n+1):
        global numFibCalls
        numFibCalls = 0
        print('fib of',i,'=',fib(i))
        print('fib called',numFibCalls,'times.')

textFib(6)
