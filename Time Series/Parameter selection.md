### Stationary
When the properties do not depend on the time/point of the series at which the series is observed. <Br>
For a time series to be considered stationary, these conditions should be met: <br>
-Constant mean <br>
-Constant Variance <br>
-Constant autocorrelation structure (current value being dependent on past value) <br>
-No period component (no trend or seasonality)<br>

Most stationary data will be roughly horizontal and will hav eno predictable pattern in the long term. W

### Parameter Overview
- __p__ and seasonal __P__: [PACF Plot] indicate number of autoregressive terms (__lags__ of the stationarized series)
- __d__ and seasonal __D__: [reducing trend] indicate __differencing__ that must be done to stationarize series. Typical range [0,1,2]
- __q__ and seasonal __Q__: [ACF Plot] indicate number of __moving average__ terms (lags of the forecast errors)
- __s__: [seasonal period] indicates __seasonal__ length in the data


##### Differencing:  x_t2 - x_t1
Subtracting the current value of the series from the previous one for from a lagged value. Computing the change between consecutive observations.

It helps stabilize the mean of a time series by removing change in the level of the time series and therefore eliminating/reducing trend and seasonality. The typical tange of d and D is [0,1,2] because second order differencing (d=2) is typically enough to make a series stationary in most cases. If the time series does not reach stationarity by econd order differencing, the data quality should be considered.
![Diffferencing Example Graphs](differencing_graph_examples.png "Differencing Examples")

##### Autocorrelation
The degree of similarity between changes in a successive time intervals. <br>
How Correlated is the time series with itself (all past points)?

##### Partial Autocorrelation
How correlated is one time series point with the previous time series point or previous lag period (only the preveeding point)? 

