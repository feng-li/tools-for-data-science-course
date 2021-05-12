import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
sns.set(rc = {'figure.figsize':(15,5)})
def bond_price(par,coup_rate,r,T,freq=1):
    per_coupon = par * coup_rate / freq
    i = r/freq
    periods = freq * T
    discount_coupon = sum((per_coupon / (1+i) ** t for t in range(1,periods+1)))
    return dicount_coupon + (par / (1+i) ** periods)

par = 1000
coup_rate = 0.06
r = 0.03
T = 50
freq = 1
