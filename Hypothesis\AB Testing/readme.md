# Central Limit Theorem

#### Part 1: <br>
The distribution of sample means with replacement (from a greater population) will approximately be normally distributed as the sample size gets larger. This will hold true regardless of whether the source population is normal or skewed, provided the sample size is sufficiently large (usually n > 30). If the population distribution is normal, you don’t need n>30

Ex: 	pop size N = 1000			Sample size n = 50 <br>
    	Pop mean = 150<br>
  	  Pop st_dev = 6<br>

All possible samples (with replacement) = 1000^ 50 <br>
1000 ^ 50 sample means will be in the distribution for CLT and that distribution will be normally distributed
The larger the sample size, the more normally distributed it will be. Why? 
Because if we increase the sample size, we have more values that will kind of even out the sample mean, and will get it closer to the average.

Essentially, everything will average out if you have enough data.

#### Part 2:<br>
The mean of all these sample means, will be the same as the population mean (as the sample size grows larger)

#### Part 3: 

![image](https://github.com/lap309/Statistics/assets/69564111/5047c725-5506-4589-bbe1-7a833ecc406c)


We use this clause to assume that the mean of our sample, should be somewhere in the bell curve of the population parameter.  (null hypothesis)
If this is not the case, then we reject our null hypothesis and can say our data is an outlier of sorts to the population baseline


# Hypothesis Tests
* Z-Test <br>
    n>= 30 <br>
  population standard deviation must be known
* T-Test
* Chi-Squared Test: To determine if the expected and observed results are well-fitted. Chi-square test analyzes the differences between categorical variables from a random sample. The test's fundamental premise is that the observed values in your data should be compared to the predicted values that would be present if the null hypothesis were true.
