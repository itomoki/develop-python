def getRatios(vect1, vect2):
    """vect1とvect2を同じ長さのリストとする
       vect1[i]/vect[i]を意味する値からなるリストを返す"""
    ratios = []
    for index in range(len(vect1)):
        try:
            ratios.append(vect1[index]/vect2[index])
        except:
            ratios.append(float('nan')) #nan = Not a Numbar
        except:
            raise ValueError('getRatios called with bad argument')
    return ratios

try:
    print(getRatios([1.0,2.0,7.0,6.0],[1.0,2.0,0.0,3.0]))
    print(getRatios([],[]))
    print(getRatios([1.0,2,0],[3.0]))
except ValueError as msg:
    print(msg)

