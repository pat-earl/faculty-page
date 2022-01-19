---
title: "Pandas - Time Series"
subtitle: "CSC223"
author: Patrick Earl
date: 04/19/2021
slideNumber: true
revealjstheme: robot-lung
width: 1600
height: 1000
transition: slide
---

## Time Data in Pandas
* Dates and times are commonly found in datasets and come a few different formats:
    * Timestamps - Reference to a particular moment in time.
    * Time Intervals and Periods - Reference a length of time between a particular beginning and end point.
    * Time Deltas or Durations - Reference an exact length of time.

---

## Date and Time in Python
* Pandas provides tools, but they are related to Python's built-in modules:
    * `datetime`
    * `dateutil`
* To manually build a date and represent it as a Python object:
  
```
from datetime import datetime
datetime(year=2012, month=12, day=21)
```

* `dateutil` can parse dates from strings

```
from dateutil import parser
date = parser.parse('4th of July, 2015')
date
```

---

* `datetime` objects provide useful methods, like getting the day of the week
* [And many more](https://docs.python.org/3/library/datetime.html)

```
date.strftime('%A')
```

---

## NumPy's `datetime64`
* NumPy added a native time series data type. 
    * This dtype encodes dates as 64-bit integers. (Memory & Performance Savings)
* `datetime64` expects dates to be in a specific format (ISO 8601)
    * However the tradeoff allows for very efficient operations
* `timedelta64` provides functionality for keeping an exact length of time.

```
import numpy as np
date = np.array('2012-12-21', dtype=np.datetime64)
date

date + np.arange(12)
```

---

* NumPy's objects are built on a *fundamental time unit* which imposes a limit between time resolution and maximum time span.
    * [Fundamental Time Units](https://numpy.org/doc/stable/reference/arrays.datetime.html#datetime-units)
  
```
# Day based 
np.datetime64('2015-07-04')

# Minute-based
np.datetime64('2015-07-04 12:00')

# Forcing nanosecond
np.datetime64('2015-07-04 12:59:59.50', 'ns')
```

---

## Dates and Times in Pandas
* Pandas adds in a `Timestamp` object which combines the ease-of-use of `datetime` and `dateutil` with the efficient storage and vectorized interface of `numpy.datetime64`.

* Creating a date similar to using the `dateutil` parser and then applying an operation to the date:

```
import pandas as pd
date = pd.to_datetime('4th of July, 2015')
date

date.strftime('%A')

date + pd.to_timedelta(np.arange(12), 'D')
```

---

## Indexing by Time
* Timestamps can be used to index data:

```
index = pd.DatetimeIndex(['2014-07-04', '2014-08-04',
                          '2015-07-04', '2015-08-04'])

data = pd.Series([0, 1, 2, 3], index=index)
data
```

* Any indexing pattern can be used to access information:

```
data['2014-07-04':'2015-07-04']
```

* Additionally, there are date-only index operations. For example, passing a year to obtain a slice of all the data from that year:

```
data.loc["2015"]
```

---

## Time Series Data Structures
* Pandas provides objects (data and indexing) for each of the aforementioned time types.
    * Timestamps - Data: `Timestamp`, Index: `DatetimeIndex`
    * Time Periods - Data: `Period`, Index: `PeriodIndex`
    * Time Deltas or Durations - Data: `Timedelta`, Index: `TimedeltaIndex`

---

## Timestamp
* Typically these objects are created using the `pd.to_datetime()` method.
    * Passing a single date yields a `Timestamp`
    * A series of dates yields a `DatetimeIndex`

```
dates = pd.to_datetime([datetime(2015, 7, 3), '4th of July 2015', '2015-Jul-6', '07-07-2015', '20150708'])
```

## Period
* `DatetimeIndex` can be converted to a `PeriodIndex` using `to_period()`.
    * A frequency code can be used. 

```
dates.to_period('D')
```

## TimedeltaIndex
* `TimedeltaIndex` is created when a date is subtracting one date from another:

```
dates - dates[0]
```

---

## Regular Sequences
* For more convince, data sequences can be created with these Pandas functions:
    * `date_range`
    * `period_range`
    * `timedelta_range()`

```
# Using date_range with a start and stop
pd.date_range('2015-07-03', '2015-07-10')

# Using date_range with a number of periods
pd.date_range('2015-07-03', periods=8)

# The period can be defined by the freq keyword, which defaults to D
pd.date_range('2015-07-03', periods=8, freq='H')
```

---

```
# Sequence of Period
pd.period_range('2015-07', periods=8, freq='M')

# Sequence of durations increasing by an hour:
pd.timedelta_range(0, periods=10, freq='H')
```

---

## Frequencies and Offsets
* Codes can be used to specify any desired frequency spacing.
* [Table from Pandas Doc](https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#dateoffset-objects)
* Codes that mark an end (i.e. `M - Month End`), can be be changed to mark a start by adding an S suffix (i.e. `MS - Month Start`)
* The month used to mark any quarterly or annual code can be changed by adding a three-letter month code suffix:
    * `Q-JAN, BQ-FEB, QS-MAR, BQS-APR`, etc.
    * `A-JAN, BA-FEB, AS-MAR, BAS-APR`, etc.
* The split-point of a weekly frequency can be changed by adding a three-letter weekday code:
    * `W-SUN, W-MON, W-TUE, W-WED`, etc.

---

* Codes can also be combined with numbers to specify other frequencies, such as creating one of 2 hours 30 minutes:

```
pd.timedelta_range(0, periods=9, freq="2H30T")
```

* Business day offsets:

```
from pandas.tseries.offsets import BDay()
pd.date_range('2021-04-15', periods=5, freq=BDay())
```

---

## Resampling, Shifting, and Windowing
* Resample time series data at a higher or low frequency: 
    * `resample`: Data Aggregation
    * `asfreq`: Data Selection
* Shifting data in time:
    * `shift`: Shifts the data
    * `tshift`: Shifts the index
* Rolling statistics are similar to the `groupby` operation on windows of time series data
    * `rolling`