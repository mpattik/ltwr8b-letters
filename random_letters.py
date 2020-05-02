# Michael Pattik A15510375

import numpy as np
import pandas as pd

# I used this website to find the proportions for each letter
thanks = 'https://funbutlearn.com/2012/06/which-english-letter-has-maximum-words.html'

# number of letters to generate
num = 100

letters_str = 's,p,c,a,u,t,m,b,d,r,h,i,e,o,f,g,n,l,w,v,k,j,q,z,y,x'
letters = letters_str.split(',')
probs_str = '10.6%10.3%8.37%7.11%6.97%5.47%5.27%4.69%4.68%4.18%3.84%3.72%3.69%3.32%3.01%2.94%2.85%2.66%1.71%1.44%0.94%0.69%0.49%0.40%0.28%0.16%'
probs = probs_str.split('%')[:-1]
probs = np.round((pd.Series(probs).astype(float) / 100).tolist(), 4)
probs[12] += 0.002200000000000202

# change p=probs to p=None to make probability equal for all letters
chosen = np.random.choice(letters, size=num, replace=True, p=probs)

formatted = ''
for i in chosen:
    formatted += i +'\n'

print(formatted)
