
# coding: utf-8

# In[56]:

# remove n ints to get the min coordinates
coordinates = "706209249"
remove = 3


# In[57]:

def iid(coordinates, remove):
    if remove == 0:
        return coordinates
    c = [int(x) for x in list(coordinates)]
    if remove >= len(c):
        return '0'
    
    keep = len(c) - remove
    res = []
    s = sorted(c)
    i = 0
    while keep > 0:
        if s[i] in c:
            idm = c.index(s[i])
            if len(c) - idm > keep:
                res.append(c[idm])
                c = c[(idm+1):]
                keep-=1
                i = 0
                continue
            elif len(c) - idm == keep:
                res.extend(c[idm:])
                keep = 0
        i+=1
    return ''.join([str(i) for i in res])


# In[58]:

iid(c,r)


# In[46]:

c = "64738929"
r = 0


# In[48]:

c = "12345"
r = 6

