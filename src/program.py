from typing import List

def maxLenChainWithRandomDelete(lst: List[int]) -> int:
    if not lst: return 0
    
    prevChainLen: int = -1
    currChainLen: int = 0

    res: int = 0

    for val in lst:
        if val == 1:
            currChainLen += 1
        else:
            res = max(res, prevChainLen + currChainLen)
            prevChainLen = currChainLen
            currChainLen = 0
    res = max(res, prevChainLen + currChainLen)
        
    return res
    
