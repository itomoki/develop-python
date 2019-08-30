def search(L, e):
    """Lを,要素が昇順で並んだリストとする
       eがLにあればTrueを.そうでなければFalesを返す"""

    def bSearch(L, e, low, high):
        #high - lowを減少させる
        if high==low:
            return L[low]==e
        mid = (low + high)//2
        if L[mid]==e:
            return True
        elif L[mid]>e:
            if low==mid:#探索対象は残っていない
                return False
            else:
                return bSearch(L, e, low, mid-1)
        else:
            return bSearch(L, e, mid+1, high)

    if len(L)==0:
        return False
    else:
        return bSearch(L,e,0,len(L)-1)
    
