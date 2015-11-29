import numpy as np
import scipy as sc
import scipy.stats as st
import pandas as pd

def mann_whitney_u_test():
  
  c = [11,15,9,4,34,17,18,14,12,13,26,31]
  d = [34,31,35,29,28,12,18,31,14,22,10]

  cM = np.mean(c)
  dM = np.mean(d)
  
  data = []
  data += c
  data += d
  ranked = st.rankdata(data)
  cR = ranked[:len(c)]
  dR = ranked[len(c):]
  print cR
  print dR
  
  print len(c)*len(d)/2
  
  U, p = st.mannwhitneyu(c, d)
  
  
  return cM, dM, U, p

print mann_whitney_u_test()
