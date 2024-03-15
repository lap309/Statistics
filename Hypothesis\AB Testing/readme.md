# Central Limit Theorem

#### Part 1: <br>
The distribution of sample means with replacement (from a greater population) will approximately be normally distributed as the number of samples gets larger. This will hold true regardless of whether the source population is normal or skewed, provided the sample size is sufficiently large (usually n > 30). If the population distribution is normal, you don’t need n>30

The central limit theorem states that if we repeatedly take samples from a population with replacement, as we increase the number of samples taken:
- The mean of the sample means will approach that of the population
- The distribution of sample means will be approximately normal
- The standard deviation of the approximately normal distribution will be $\frac{\sigma}{\sqrt{n}}$ where $\sigma$ is the population standard deviation, and $n$ is the number of observations in a sample (for our dice example, it was 2,000, the number of dice we threw). This means that as your sample size increases, the mean of that sample will be a more and more accurate approximation of the true mean

Ex: 	pop size N = 1000			Sample size n = 50 <br>
    	Pop mean = 150<br>
  	  Pop st_dev = 6<br>

All possible samples (with replacement) = 1000^ 50 <br>
1000 ^ 50 sample means will be in the distribution for CLT and that distribution will be normally distributed
The larger the number of samples taken, the more normally distributed it will be. Why? 
Because if we increase the number of samples taken, we have more values that will kind of even out the sample mean, and will get it closer to the average.

Essentially, everything will average out if you have enough data.

#### Part 2:<br>
The mean of all these sample means, will be the same as the population mean (as the sample size grows larger)

#### Part 3: 

![image](https://github.com/lap309/Statistics/assets/69564111/5047c725-5506-4589-bbe1-7a833ecc406c)


We use this clause to assume that the mean of our sample, should be somewhere in the bell curve of the population parameter.  (null hypothesis)
If this is not the case, then we reject our null hypothesis and can say our data is an outlier of sorts to the population baseline


# Hypothesis Tests
### One Sample
Used for when comparing a new hypothesis to an already existing threshold. Compare the mean of a measured group to a known mean <br> <br>
__Z-Test for Population Mean__ <br>
Assumptions:
Random Sampling was used <br>
Population distribution is normal OR n >=30 <br>
Population standard deviation MUST be known <br> <br>

__Z Test for Population Proportion__ <br>
Assumptions: <br>
Random Sampling was used <br>
n*p>= 10 AND n*(p-1)>=10 <br>
If sampling w/o replacement, n is no more than 10! of the population size

__T-Test for Sample Means__ <br>
Assumptions:
Population distribution is normal OR n >=30 <br>
Population standard deviation is unknown <br> <br>


### Two Sample
Used when comparing the performance of two samples/groups. Determines whether the data from two sources could have come from the same normal distribution. We compare the mean of two data sets, assume that the variances are equal, and determine whether a single process could have produced both data sets.<br><br>

__Two Sample Independent T-Test__ <br>
Properties: <br>
* bell shaped and centered at zero (just like z distribution)
* each _t_ distribution is more spread out than the _z_ distribution
* As the number of df increases, the spread of the _t_ distribution decreases and the sequence of _t_ distributions approaches the _z_ distribution<br>
Assumptions: <br>
- Data points in each group are independent of each other 
- The means of both samples come from a normal sampling distribution:
    - Either the samples themselves are normally distributed (the populations are normally distributed)
    - Or the samples are large enough that the CLT guarantees the sampling distributions are approximately normal
- Data in group A are independent from data in group B
- Variances of both populations are identical (we can test that assumption)<br> <br>

__Paired Two Sample T-Test__<br>

  
__Chi-Squared Test:__ <br>
To determine if the expected and observed results are well-fitted. Chi-square test analyzes the differences between categorical variables from a random sample. The test's fundamental premise is that the observed values in your data should be compared to the predicted values that would be present if the null hypothesis were true.

# P-value
A p-value quantifies the probability of seeing the observed data given that the null hypothesis is true. If the p-value is very low, then seeing the observed data would be very rare if the null hypothesis were true, so we have evidence to reject it. <br>
Note that p-values are currently considered a little controversial in several fields. Many fields also opt for thresholds for p-values that are much lower than 0.05, because they demand much more confidence that they aren't observing their results due to chance before drawing conclusions.<br><br>

# Errors
Type I Error: alpha/significance level <br>
Type II Error: beta
Power: 1- (Type II Error): the probability of rejecting the null hypothesis<br>
<br>
Use the maximum acceptable value as the level of significance because using a smaller alphs increases beta.<br><br>
Variables that impact the Power of the Test<br>
The larger the size of the discrepancy between the hypothesized value and the actual vlaue of the population characteristic, the greater the power<br>
The larger the significance level, alpha, the grater the power of the test <br>
The larger the sample size, the greater the power of the test
