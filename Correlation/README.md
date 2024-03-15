## Types of Correlation

#### Covariance(x,y) / Covariance Matrix
Relationship between 2 variables, unless using the covariance matrix <br>
df.cov() <br>
Covariance is very sensitive to scaling and does not suitable for comparison across different units. Ex: covariance of a dataset measured in inches compared to a covariance of the same dataset measured in feet would result in 12x as much, even though they are measuring the same thing. Even though they are measuring the same thing, the covariance would be a product of 12 because of the difference in unit of measurement. For this reason, correlation might be better. <br><br>

#### Pearson's Correlation Coefficient: Linear
Normalized version of the covariance (follows a similar formula to z-score) that measure LINEAR DEPENDENCE between 2 variables.<br>
It measure the strength of linear association <br>
Note: Having a correlation of 0 does not rule out Non-linear relations/patterns between the variables. 
df.corr() <br><br>

#### Spearman's Rank Correlation: Non-linear / non-parametric
Non-parametric measure of rank correlation. This would be like ranking the x values, ranking the y values, then taking the correlation of the new rank columns. This is helpful to identify NON-LINEAR RELATIONSHIPS

#### Phi Coefficient: Binary Categorical Variables
Based off of Pearsons but called MCC(Mathew's Correlation Coefficient) in Machine Learning <br>
Used to evaluate predictions by a binary classifier <br><br>

#### Point Biserial Correlation: Binary category and Continuous variable
Based off of Pearsons
