
import numpy as np

def markov_eq(share, trans):
    share = share.T
    n = 0
    while n < 1000:
        newshare = np.dot(share, trans)
        if np.linalg.norm(newshare-share) < 1e-5:
            return np.around(newshare,4)
        share = newshare
        n += 1
    return np.array([0,0])

share = np.array([.4,.6])
switch_prob = np.array([[.8,.2],[.1,.9]])
print(markov_eq(share,switch_prob))

