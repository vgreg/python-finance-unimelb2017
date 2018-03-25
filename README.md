# Python for financial research (2017 workshop)

[Vincent Grégoire](http://www.vincentgregoire.com), University of Melbourne

This repository contains material for a Python for financial research workshop I taught to honours and Ph.D. students at the University of Melbourne in 2017.

**NOTE: This stuff is in part already outdated. The most significant change is that I am now using Python 3.6 instead of 2.7. See the [2018 workshop](https://github.com/vgreg/python-finance-unimelb2018) for up-to-date examples.**


## Outline


The boot camp is divided into four blocks of three hours each:

**1. Introduction to Python programming**

We will discuss what Python is and you will learn the basic structure of the
language. You will also learn your way around the programming environment,
including the two main editors for scientific Python, Spyder, and Jupyter.

**2.    Introduction to data analysis using pandas and matplotlib**

You will learn how to import, export and transform data using pandas, the
panel data package for Python. You will also learn how to explore the data
by generating summary statistics and plotting graphs using matplotlib.

**3.    More data analysis using pandas and statsmodels**

You will learn more advanced features of Python and pandas, including dealing
with timestamps and estimating measures from daily and intraday data. You
will also learn how to estimate OLS and panel regressions using statsmodels.

**4.    Other topics**

In this block, you will be introduced briefly to other python packages that
can be helpful for research. The list of topics is not yet finalized, but
will likely include text analysis, web scraping, network analysis and
symbolic algebra.

## Software


I recommend the [Anaconda distribution](https://www.anaconda.com/download/),
which is available for Windows, Mac OS and  Linux. We are using the Python
2.7 version for the boot camp. **Note: for the 2018 workshop I am now using Python 3.6**.


## Material


### Slides

- [Python for Financial Research (PDF)](https://github.com/vgreg/python-finance-unimelb2017/blob/master/slides/PythonBootcampMarch2017.pdf)
- [Introduction to Web Scraping with Python (PDF)](https://github.com/vgreg/python-finance-unimelb2017/blob/master/slides/WebScrapingPythonMarch2017.pdf)


### Code


**Note**: this code is for illustrative purpose, and does not necessarily show
the *correct* or *best* way to do something, the main goal is to illustrate
the Python language, its libraries, and some common use cases in research.

**Block 1:**

- [PythonIntro.py](https://github.com/vgreg/python-finance-unimelb2017/blob/master/listings/PythonIntro.py): Introduction to the Python language.
- [TurtleTutorial.py](https://github.com/vgreg/python-finance-unimelb2017/blob/master/listings/TurtleTutorial.py): Some exercises with the turtle package.

**Block 2:**

- [Introduction to pandas](notebooks/introduction-to-pandas.ipynb): Short intro to pandas using Yahoo Finance data.
- [CRSP Example - Dividends](notebooks/crsp-example-dividends.ipynb): A quick event study around dividends announcements

**Block 3:**

- [Introduction to empirical market microstructure in Python](notebooks/introduction-to-empirical-market-microstructure-in-python.ipynb): Intro to using pandas with intraday data.
- [Estimating standard errors in Python](https://github.com/vgreg/python-se): Using statsmodels and pandas for panel regressions.

**Block 4:**

- [Trump's tweets and the stock market](https://github.com/vgreg/python-finance-unimelb2017/blob/master/notebooks/trump-tweets-and-the-stock-market.ipynb): Merge and analyze twitter data, apply textual (sentiment) analysis and process intraday stock market data.
- [DownloadEdgar.py](https://github.com/vgreg/python-finance-unimelb2017/blob/master/listings/DownloadEdgar.py): Batch downloading 10-Ks from EDGAR.
