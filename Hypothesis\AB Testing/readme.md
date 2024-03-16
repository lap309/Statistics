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

All possible samples (with replacement) = $1000^ (50)$ <br>
$1000^(50)$ sample means will be in the distribution for CLT and that distribution will be normally distributed
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
### Z-Test for Population Mean
Assumptions:
Random Sampling was used <br>
Population distribution is normal OR n >=30 <br>
Population standard deviation MUST be known <br> <br>

#### Z Test for Population Proportion
Assumptions: <br>
Random Sampling was used <br>
n*p>= 10 AND n*(p-1)>=10 <br>
If sampling w/o replacement, n is no more than 10! of the population size

### T-Test for Sample Means
Assumptions:
Population distribution is normal OR n >=30 <br>
Population standard deviation is unknown <br> <br>
$$t = \frac{\overline{x} - \mu_{test}}{\left(s\,\big/ \sqrt{n}\right)}$$


## Two Sample
Used when comparing the performance of two samples/groups. Determines whether the data from two sources could have come from the same normal distribution. We compare the mean of two data sets, assume that the variances are equal, and determine whether a single process could have produced both data sets.<br><br>

### Two Sample Independent T-Test
Properties: <br>
* bell shaped and centered at zero (just like z distribution)
* each _t_ distribution is more spread out than the _z_ distribution
* As the number of df increases, the spread of the _t_ distribution decreases and the sequence of _t_ distributions approaches the _z_ distribution<br>
Assumptions: <br>
- Data points in each group are independent of each other 
- Both samples are normally distributed
    - Either the samples themselves are normally distributed (the populations are normally distributed)
    - Or the samples are large enough that the CLT guarantees the sampling distributions are approximately normal ( n>= 30 )
- Data in group A are independent from data in group B
- Variances of both populations are identical (we can test that assumption)<br> <br>
$$t = \frac{(\overline{X}_1 - \overline{X}_2) - (\mu_1 - \mu_2)}{s_p \sqrt{\frac{1}{n_1}+\frac{1}{n_2}}}$$


### Paired Two Sample T-Test:
When the same sample is both the control and test group. They are measured before treatment (control) and then again after treatment (test) to see the impact. <Br>

Assumptions: <br>
- Data points in group A and B are paired/matched
- Sample is normally distributed
    - Either the samples themselves are normally distributed (the populations are normally distributed)
    - Or the samples are large enough that the CLT guarantees the sampling distributions are approximately normal ( n 30)
- Variances of both populations are identical
<Br> 

$$t = \frac{\overline{X_D} - µ_{test}}{\frac{s_D}{\sqrt{n}}}$$

Where $X_D$ is the set of differences between paired samples, $µ_{test}$ is our mean difference that we want to compare to (0 in this case), $s_D$ is difference sample standard deviation, and n is the number of samples.
$$s_p = \sqrt{\frac{(n_1 - 1)s_1^2 + (n_2 - 1)s_2^2}{n_1 + n_2 - 2}}$$

**Quick Summary**:

    Unpaired: testing the differences of means
    Paired: testing the mean of the differences 
  
### $\chi^2$ Chi-Squared Goodness of Fit: determing whether a variable is 
Designed to assess if there's a statistically significant difference between the observed counts/frequency and the expected counts/frequency across a set of mutually exclusive categories.<br>

<br>The test's fundamental premise is that the observed values in your data should be compared to the predicted values that would be present if the null hypothesis were true.<br><br>
The Chi Squared statistic is a measure of bias in our sample. The value itself doesn't carry much meaning unless we convert it into the corresponding p-value.


### $\chi^2$ Chi-Squared Test of Independence: Correlation between 2 categorical variables
Tests whether two vategorical variables are related to each other.
Chi-squared test can answer questions like: <br>
- Are people's favorite color related to their favorite fruit?
- Is there a significant relationship between country of resident and field that they work in?
<br>
Assumptions:<br>
- The data in the cells should be frequencies.
- The levels (or categories) of the variables are mutually exclusive. That is, a particular subject fits into one and only one level of each of the variables.
- Each subject may contribute data to one and only one cell.
- The study groups must be independent.

## Multiple Samples Hypothesis Tests
If we have a lot of samples/subgroups, and we wanted to run each subgroup against the null hypothesis with a significance level of 5%, as we increase the numbe of tests we perform, we increase our risk of incorrectly concluding that we see a significant difference in our data. <br>
To avoid making several false positives (rejecting when we shouldn't), we should alter the threshold for what we consider to be a value of significance. That is to say, we should alter our alpha. <br>

### Bonferroni Correction

With this method, we define a new significance threshold for our hypothesis tests such that:<br>
$$\alpha_{test} = \frac{\alpha_{overall}}{ \text{number of tests}}$$
<br>
When we have many tests, however, the p-values for the individual tests can become very small and cause us to be too strict. This means that we can easily miss cases when we should have rejected the null hypothesis, inflating our type II error. <br>

### Holm-Bonferroni Method**
The significance threshold for each individual test with this method is:<br>
$$\alpha_{test} = \frac{\alpha_{overall}}{ \text{number of tests}-\text{rank number of p-value} +1}$$
<br>
where the rank number of the p-value is the rank when p-values are sorted from smallest to largest. Notice that the individual significance thresholds will be different for every test. <br><br>
To decide whether or not to reject the null hypotheses for each test, we walk down our ranking of p-values until we find the first one whose p-value is _above_ its significance threshold. All hypothesis tests before this point will have their null hypotheses rejected and all others will _not_ have their null hypotheses rejected.<br>
For more information on the Holm-Bonferroni Method, start with the [following link](https://www.statisticshowto.datasciencecentral.com/holm-bonferroni-method/): <br>
  
# P-value
A p-value quantifies the probability of seeing the observed data given that the null hypothesis is true. If the p-value is very low, then seeing the observed data would be very rare if the null hypothesis were true, so we have evidence to reject it. <br>
In the graphical sense, it is the area under the curve.<br>
Note that p-values are currently considered a little controversial in several fields. Many fields also opt for thresholds for p-values that are much lower than 0.05, because they demand much more confidence that they aren't observing their results due to chance before drawing conclusions.<br><br>

# Errors
__Type I Error: alpha/significance level__ <br>
"False Positive". Thought there was an effect when there wasn't one <br>
ex: getting a positive pregnancy test when you're not pregnant <br>

__Type II Error: beta__ <br>
"False Negative": failed to identify an effect/difference between samples. This is considered worse. <Br>
ex: getting a negative pregnancy test when you are in fact pregnant
<br>
Power: 1- (Type II Error): the probability of rejecting the null hypothesis<br>
<br>
| Decision       | $H_0$ true|   $H_0$ false |
| ------------- |:-------------:| -----:|
| Reject $H_0$ | Type I |Correct|
| Do not reject $H_0$  |Correct|Type II|


Use the maximum acceptable value as the level of significance because using a smaller alphs increases beta.<br><br>

__Variables that impact the Power of the Test__<br>
The larger the size of the discrepancy between the hypothesized value and the actual vlaue of the population characteristic, the greater the power<br>
The larger the significance level, alpha, the grater the power of the test <br>
The larger the sample size, the greater the power of the test
