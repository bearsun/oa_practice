
# coding: utf-8

# In[1]:

import numpy as np


# In[2]:

def tetris(w,h,pieces):
    rect = np.zeros((h,w))
    total = w*h
    pieces = np.array(pieces)
    i = 0
    for p in pieces:
        #pdb.set_trace()
        while i < total:
            m = i % h
            n = i // h
            #pdb.set_trace()
            if rect[m, n] == 0:
                tofill = p + [n,m]
                if np.all((tofill[:,1] < h) * (tofill[:,0] < w)):
                    if not np.any(rect[tofill[:,1],tofill[:,0]]):
                        rect[tofill[:,1],tofill[:,0]] = 1
                        last = m*n
                        #print((n,m))
                        i+=1
                        break
            i+=1
    if np.all(rect):
        return last
    else:
        return -1


# In[3]:

w,h = 6,6
pieces=[
    [(0,0), (1,0), (2,0), (3,0)],
    [(0,0), (1,0), (2,0), (2,1)],
    [(0,0), (1,0), (0,1), (1,1)],
    [(0,0), (1,0), (0,1), (2,0)],
    [(0,0), (1,0), (2,0), (2,-1)],
    [(0,0), (1,0), (1,-1), (2,-1)],
    [(0,0), (1,0), (1,-1), (2,-1)],
    [(0,0), (1,0), (1,-1), (1,-2)],
    [(0,0), (1,0), (1,1), (0,1)]
]
print(tetris(w,h,pieces))

