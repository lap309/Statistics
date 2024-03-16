import numpy as np
from scipy import stats
from scipy.stats import norm #used for plotting

null_mean = 
test_meannp.mean(data)

################################################################### 
                    #one sample t-test
################################################################### 
one_sample_test = stats.ttest_1samp(null_mean, test_mean)

## alternative
n=40
sample_mean = 4.5
sample_stdev = 1.2/math.sqrt(n)
null_hyp = 5
p_val = scipy.stats.norm(sample_mean, sample_stdev).cdf(null_hyp)

"""in Excel
normdist( sample_mean, null_hyp, sample_stdev, cumulative = True)"""

################################################################### 
                    #proportions Z-test
################################################################### 
from statsmodels.stats.proportion import proportions_ztest
num_success = 
num_trials = 
null_hyp =
proportin_variance = 
#If prop_var is false, then the variance of the proportion estimate is calculated based on the sample proportion. Can use the null hypothesis value if the normaliity conditions are met
#Alternatively, a proportion can be specified to calculate this variance. Common use case is to use the proportion under the Null hypothesis to specify the variance of the proportion estimate. If we omit this, it would be a different test
stat, pvalue = proportions_ztest(num_success, 
                                 num_trials, 
                                 null_hyp, 
                                 'two_sided',   # two-sided, smaller, larger
                                proportion_variance)



################################################################### 
                  #two sample independent t-test
################################################################### 
two_sample_test = stats.ttest_ind(samp_1, samp_2)

################################################################### 
                    #two sample paired t-test
################################################################### 
paired_t_test = stats.ttest_rel(control_data, test_data)

################################################################### 
                  #Chi-Squared Independence Test
################################################################### 
#Create contigency table (table) with the counts/frequency of each event, then run the code on the dataframe
data = {'Web Dev': [100,60], 'UX Design':[150,70], 'Data Science':[75,70]}
contingency_tab_data = pd.DataFrame(data, index=['New York', 'London'])

#Run chi squared test
stats.chi2_contingency(contingency_tab_data)
"""The output returns the stat estimate, p_value, degrees of freedon, and an array of expected values of the events) 

