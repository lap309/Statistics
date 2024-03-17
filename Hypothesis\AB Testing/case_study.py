""" Finding the distributions, probabilityes, and proportions of different scenarios in a case study
ex: based on how we were performing before the test, was this change in strategy effective?
     if the null hypothesis is correct, how likely is it that we would have had x amount of conversions, etc...
    what value would be good enough
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import math



null =     # expected value from past strategies ,year ago etc
alt =      # current data value
n=
p_val= .5

from scipy.stats import binom
# cdf returns the probability up until that value on a normal distribution
#alternative hypothesis: less than or equal
prob = binom.cdf( alt ,n,p_val)

#alternative hypothesis: less than
prob = binom.cdf( alt-1 ,n,p_val)

#alternative hypothesis: greater than
prob = 1-binom.cdf( alt ,n,p_val)    # all values up until that value

#alternative hypothes: not equal to
prob = (binom.cdf( alt ,n,p_val))/2


# Question: How many conversions would we need to see from the campaign in order for the test to have been significant/have an affect?
#ppt returns the value necessary in the current disttribution to be at the specified percentage
binom.ppt(0.95, n, p_val)
binom.ppt(0.05, n, p_val)
binom.ppt(0.025, n, p_val)
binom.ppt(0.975, n, p_val)
#this will tell us the value we need to get in order to reject the null hypothesis




