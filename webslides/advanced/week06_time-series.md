# Week 6 — Time Series and Forecasting
# Focus: Chronos/TinyTimeMixer, Naive vs. Model-Based Comparisons

> Time series forecasting predicts future values based on past observations. This week introduces modern transformer-based forecasters like Chronos and TinyTimeMixer alongside classical approaches.
---

## Time Series Basics

- Ordered observations over time
- **Trends** — long-term direction
- **Seasonality** — regular patterns
- **Noise** — random variation

![](images/crude-oil-price-timeseries.gif)

> Time series basics recognize that data comes in ordered sequences with trends (long-term direction), seasonality (regular patterns), and noise (random variation).
---

## Train/Validation Splits

- Time-aware splits — test data always after training data
- Avoid leakage across time
- Random splitting breaks causality and gives unrealistic estimates

> Training splits for time series must respect temporal ordering - test data always comes after training data. Random splitting breaks causality and gives unrealistic performance estimates.
---

## Baselines

- **Naive** — repeat last value
- **Seasonal naive** — repeat last seasonal value
- **Moving average**
- Complex models should beat these or they're not worth the complexity

![](images/moving_averages_animation.gif)

> Baseline forecasts like naive (repeat last value) or seasonal naive (repeat last seasonal value) provide performance floors. Complex models should beat these simple approaches or they're not worth the complexity.
---

## Error Metrics

- **MAE** — mean absolute error
- **RMSE** — root mean squared error
- **MAPE** — mean absolute percentage error (fails with zero values)
- **sMAPE** — symmetric MAPE
- Scale sensitivity matters

> Error metrics for forecasting include MAE (mean absolute error), RMSE (root mean squared error), MAPE (mean absolute percentage error), and sMAPE (symmetric MAPE). Scale sensitivity matters - MAPE fails with zero values.
---

## Classical Models

- **ARIMA/SARIMA** — encode assumptions about trends and seasonality
- **Exponential smoothing**
- Interpretable models remain valuable despite deep learning

> Classical models like ARIMA/SARIMA and exponential smoothing encode assumptions about trends and seasonality. These interpretable models remain valuable despite newer deep learning approaches.
---

## Feature Engineering

- **Lags** — past values
- **Rolling stats** — moving averages
- **Calendar features** — day of week, holidays

> Feature engineering for time series creates lags (past values), rolling statistics (moving averages), and calendar features (day of week, holidays) that capture temporal patterns.
---

## Global vs. Local Models

- **Global** — one model for all series
- **Local** — per-series training
- Global models share information and handle new series better

> Global models train one model on all time series versus local models trained separately for each series. Global models share information across series and handle new series better.
---

## Chronos/TinyTimeMixer

- Transformer-style global forecasters
- Treat sequences of values like sequences of words in NLP

![](images/regime_switching_animation.gif)

> Chronos and TinyTimeMixer apply transformer architectures to time series, treating sequences of values analogously to sequences of words in NLP.
---

## Cross-Validation for Time Series

- **Rolling-origin evaluation** (walk-forward)
- Repeatedly train on past data, test on immediate future

> Cross-validation for time series uses rolling-origin evaluation (also called walk-forward validation) where the model repeatedly trains on past data and tests on immediate future.
---

## Intermittent Demand

- Series with many zeros (e.g., spare parts inventory)
- **Croston variants** and special handling
- Standard methods fail on sparse demand

> Intermittent demand series with many zeros (like spare parts inventory) require special handling with methods like Croston's approach designed for sparse demand.
---

## Missing Data

- Imputation strategies
- Gap handling
- Irregular intervals
- Missing pattern (random vs. systematic) informs approach

> Missing data in time series requires careful imputation or gap handling. Missing patterns (random versus systematic) inform appropriate strategies.
---

## Multivariate Series

- Exogenous variables (weather, promos)
- External factors improve forecasts when causal relationships exist

![](images/sunspots_forecast.gif)

> Multivariate series incorporate exogenous variables like weather affecting electricity demand or promotions affecting sales. These external factors improve forecasts when causal relationships exist.
---

## Probabilistic Forecasts

- Predict intervals or quantiles
- Quantify uncertainty for decision-making
- Calibration matters — intervals should have correct coverage

> Probabilistic forecasts output intervals or quantiles rather than point predictions. Quantifying uncertainty helps decision-makers plan for ranges of outcomes.
---

## Change Points

- Detect regime shifts where underlying process changes
- Prevent models from assuming stationarity that no longer holds

> Change points mark regime shifts where the underlying process changes. Detection and adaptation prevent models from assuming stationarity that no longer holds.
---

## Anomaly Detection

- Forecast residuals (actual minus predicted)
- Threshold rules to flag unusual values
- Contextual anomalies — high sales might be anomalous in January but normal in December

![](images/median_days_on_market.gif)

> Anomaly detection uses forecast residuals (actual minus predicted) with threshold rules to flag unusual values. Contextual anomalies depend on expected patterns (high sales might be anomalous in January but normal in December).
---

## Deployment

- Define update cadence (daily? weekly?)
- Backtesting in production before updates
- Validate performance continuously

> Deployment of forecasting systems requires defining update cadence (daily? weekly?) and implementing backtesting procedures to validate performance before production updates.
---

## Visualization

- **Decomposition plots** — separate trends, seasonality, residuals
- **Forecast vs. actuals** — show where models succeed and fail

> Visualization through decomposition plots separates trends, seasonality, and residuals. Forecast versus actuals plots show where models succeed and fail.
---

## Seasonality Detection

- **STL decomposition**
- **Autocorrelation** and periodograms
- Identify regular patterns at different frequencies

> Seasonality detection uses STL decomposition, autocorrelation functions, and periodograms to identify regular patterns at different frequencies.
---

## Holiday Effects

- Special events cause outliers in business series
- Add regressors or dummy variables for known holidays

> Holiday effects cause outliers in many business time series. Adding regressors or dummy variables for known holidays improves accuracy.
---

## Feature Lags and Windows

- Sliding windows for deep models
- Define (input steps, output steps) pairs for training
- How much history does the model see?

> Feature lags and windows define how much history the model sees. Sliding windows for deep learning create (input steps, output steps) pairs for training.
---

## Cross-Series Learning

- Pool related series to learn shared patterns
- Sales across similar products may have common dynamics

> Cross-series learning pools related time series to learn shared patterns. Sales across similar products may have common dynamics worth sharing.
---

## Hierarchical Forecasting

- Coherence across levels (SKU → category → total)
- Reconciliation methods enforce consistency
- SKU forecasts should sum to category totals

> Hierarchical forecasting maintains coherence across aggregation levels - SKU forecasts should sum to category totals. Reconciliation methods enforce this consistency.
---

## Cold Start Series

- Little history — benefit from meta-learning
- Similarity-based initialization using comparable series

> Cold start series with little history benefit from meta-learning across other series or similarity-based initialization using comparable series.
---

## Regime Shifts

- Detect when underlying dynamics change
- Adapt models (e.g., consumer behavior during economic transitions)

> Regime switching models adapt when the underlying dynamics change, like consumer behavior shifts during economic transitions.
---

## Probabilistic Calibration

- **PIT histograms** — check marginal calibration
- **CRPS** — continuous ranked probability score
- **Coverage diagnostics** — 90% intervals should contain ~90% of actuals

> Probabilistic calibration ensures predicted intervals have correct coverage - 90% prediction intervals should contain actual values roughly 90% of the time.
---

## Backtesting Frameworks

- Rolling windows
- Embargo periods (no peeking)
- Realistic constraints matching deployment conditions

> Backtesting frameworks implement rolling windows, embargo periods (no peeking), and realistic constraints matching deployment conditions.
---

## Production SLAs

- Forecast delivery times
- Fallback baselines if primary model fails to complete in time

> Production SLAs define when forecasts must be delivered, with fallback baselines if the primary model fails to complete in time.
---

## Practical Lab Preview

- Compare naive vs. Chronos/TinyTimeMixer on a dataset
- Demonstrate when complex models justify their cost

> The practical lab compares naive baselines to Chronos/TinyTimeMixer on real time series data, demonstrating when complex models justify their cost.
---

## Reflection Prompt

- What horizon and error metric matter most in your scenario?
- Predicting tomorrow requires different approaches than predicting next year

> Reflect on what forecast horizon matters most in your scenario. Predicting tomorrow requires different approaches than predicting next year.
---

## Reading List

- Forecasting: Principles and Practice
- Chronos / TinyTimeMixer papers

> The reading list includes Forecasting Principles and Practice textbook plus papers on Chronos and TinyTimeMixer architectures.
---

## Assignment Brief

- Build walk-forward evaluation
- Compare baselines and Chronos
- Document when complexity adds value

> Your assignment implements walk-forward evaluation comparing baseline methods to transformer forecasters, documenting when complexity adds value.
