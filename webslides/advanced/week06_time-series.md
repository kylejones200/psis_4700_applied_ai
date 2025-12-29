# Week 6 — Time Series and Forecasting
Focus: Chronos/TinyTimeMixer  
Naive vs model-based comparisons

> Time series forecasting predicts future values based on past observations. This week introduces modern transformerbased forecasters like Chronos and TinyTimeMixer alongside classical approaches.
---

## Time Series Basics
Ordered observations  
Trends, seasonality, noise

![](images/crude-oil-price-timeseries.gif)

> Time series basics recognize that data comes in ordered sequences with trends (long-term direction), seasonality (regular patterns), and noise (random variation).
---

## Train/Validation Splits
Time-aware splits  
Avoid leakage across time

> Training splits for time series must respect temporal ordering - test data always comes after training data. Random splitting breaks causality and gives unrealistic performance estimates.
---

## Baselines
Naive/seasonal naive  
Moving average

![](images/moving_averages_animation.gif)

> Baseline forecasts like naive (repeat last value) or seasonal naive (repeat last seasonal value) provide performance floors. Complex models should beat these simple approaches or they're not worth the complexity.
---

## Error Metrics
MAE, RMSE, MAPE, sMAPE  
Scale sensitivity

> Error metrics for forecasting include MAE (mean absolute error), RMSE (root mean squared error), MAPE (mean absolute percentage error), and sMAPE (symmetric MAPE). Scale sensitivity matters - MAPE fails with zero values.
---

## Classical Models
ARIMA/SARIMA  
Exponential smoothing

> Classical models like ARIMA/SARIMA and exponential smoothing encode assumptions about trends and seasonality. These interpretable models remain valuable despite newer deep learning approaches.
---

## Feature Engineering
Lags, rolling stats, calendar features

> Feature engineering for time series creates lags (past values), rolling statistics (moving averages), and calendar features (day of week, holidays) that capture temporal patterns.
---

## Global vs Local Models
One model for all series vs per-series

> Global models train one model on all time series versus local models trained separately for each series. Global models share information across series and handle new series better.
---

## Chronos/TinyTimeMixer
Transformer-style global forecasters

![](images/regime_switching_animation.gif)

> Chronos and TinyTimeMixer apply transformer architectures to time series, treating sequences of values analogously to sequences of words in NLP.
---

## Cross-Validation for TS
Rolling-origin evaluation (walk-forward)

> Cross-validation for time series uses rolling-origin evaluation (also called walk-forward validation) where the model repeatedly trains on past data and tests on immediate future.
---

## Intermittent Demand
Croston variants  
Special handling

> Intermittent demand series with many zeros (like spare parts inventory) require special handling with methods like Croston's approach designed for sparse demand.
---

## Missing Data
Imputation  
Gaps  
Irregular intervals

> Missing data in time series requires careful imputation or gap handling. Missing patterns (random versus systematic) inform appropriate strategies.
---

## Multivariate Series
Exogenous variables (weather, promos)

![](images/sunspots_forecast.gif)

> Multivariate series incorporate exogenous variables like weather affecting electricity demand or promotions affecting sales. These external factors improve forecasts when causal relationships exist.
---

## Probabilistic Forecasts
Predict intervals/quantiles  
Calibration matters

> Probabilistic forecasts output intervals or quantiles rather than point predictions. Quantifying uncertainty helps decision-makers plan for ranges of outcomes.
---

## Change Points
Detect regime shifts  
Model stability

> Change points mark regime shifts where the underlying process changes. Detection and adaptation prevent models from assuming stationarity that no longer holds.
---

## Anomaly Detection
Forecast residuals  
Thresholds  
Contextual anomalies

![](images/median_days_on_market.gif)

> Anomaly detection uses forecast residuals (actual minus predicted) with threshold rules to flag unusual values. Contextual anomalies depend on expected patterns (high sales might be anomalous in January but normal in December).
---

## Deployment
Update cadence  
Backtesting in production

> Deployment of forecasting systems requires defining update cadence (daily? weekly?) and implementing backtesting procedures to validate performance before production updates.
---

## Visualization
Decomposition plots  
Forecast vs actuals

> Visualization through decomposition plots separates trends, seasonality, and residuals. Forecast versus actuals plots show where models succeed and fail.
---

## Practical Lab Preview
Compare naive vs Chronos/TinyTimeMixer on a dataset

> The practical lab compares naive baselines to Chronos/TinyTimeMixer on real time series data, demonstrating when complex models justify their cost.
---

## Reflection Prompt
What horizon and error metric matter most in your scenario?

> Reflect on what forecast horizon matters most in your scenario. Predicting tomorrow requires different approaches than predicting next year.
---

## Seasonality Detection
STL decomposition  
Autocorrelation and periodograms

> Seasonality detection uses STL decomposition, autocorrelation functions, and periodograms to identify regular patterns at different frequencies.
---

## Holiday Effects
Special events  
Add regressors or dummy variables

> Holiday effects cause outliers in many business time series. Adding regressors or dummy variables for known holidays improves accuracy.
---

## Feature Lags and Windows
Sliding windows for deep models  
Input/output steps

> Feature lags and windows define how much history the model sees. Sliding windows for deep learning create (input steps, output steps) pairs for training.
---

## Cross-Series Learning
Pool related series to learn shared patterns

> Cross-series learning pools related time series to learn shared patterns. Sales across similar products may have common dynamics worth sharing.
---

## Hierarchical Forecasting
Coherence across levels (SKU→category→total)

> Hierarchical forecasting maintains coherence across aggregation levels - SKU forecasts should sum to category totals. Reconciliation methods enforce this consistency.
---

## Cold Start Series
Meta-learning  
Similarity-based initialization

> Cold start series with little history benefit from meta-learning across other series or similarity-based initialization using comparable series.
---

## Regime Shifts
Detect and adapt models when dynamics change

> Regime switching models adapt when the underlying dynamics change, like consumer behavior shifts during economic transitions.
---

## Probabilistic Calibration
PIT histograms  
CRPS  
Coverage diagnostics

> Probabilistic calibration ensures predicted intervals have correct coverage - 90% prediction intervals should contain actual values roughly 90% of the time.
---

## Backtesting Frameworks
Rolling windows  
Embargo  
Realistic constraints

> Backtesting frameworks implement rolling windows, embargo periods (no peeking), and realistic constraints matching deployment conditions.
---

## Production SLAs
Forecast delivery times  
Fallback baselines

> Production SLAs define when forecasts must be delivered, with fallback baselines if the primary model fails to complete in time.
---

## Reading List
Forecasting: Principles & Practice  
Chronos/TinyTimeMixer

> The reading list includes Forecasting Principles and Practice textbook plus papers on Chronos and TinyTimeMixer architectures.
---

## Assignment Brief
Build walk-forward evaluation  
Compare baselines and Chronos

> Your assignment implements walk-forward evaluation comparing baseline methods to transformer forecasters, documenting when complexity adds value.