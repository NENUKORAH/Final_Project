# Final_Project

Final project of the data incites group - University of Toronto Data Analytics Bootcamp
 
## Project Background 

The selected project topic for this group is **Stock price Predictor**

**Data source**: [Tesla Stock Price](https://www.kaggle.com/timoboz/tesla-stock-data-from-2010-to-2020) 

**Google Slide Link**: [Presentation](https://docs.google.com/presentation/d/1gQCpkDp3MEN7LO5x0zF8KAiiKE5SD2Ak3EJYs237JpY/edit?usp=sharing)

**Team Members**

* [Nnaemeka Enukorah](https://github.com/NENUKORAH)

* [Frank Brumwell](https://github.com/ftrbrum)

* [Azuka Obasuyi](https://github.com/aobasuyi)

* [Barnett Bullock](https://github.com/bnbullock)

We highlighted 15 ideas to be considered as the final project for this group and casted votes to determine which project idea should be considered.

This was done using the [miro app](https://miro.com/app/dashboard/) 

![Voting](https://user-images.githubusercontent.com/81701640/131906240-17a3607b-f0a1-4e0a-926a-06a49a8aa31a.png)

We had a tie on three projects, but decided to go with the stock price prediction project idea.

## Project Overview

The purpose of this project is to analyse the stock price of Tesla and predict future pricing using moving averages, linear regression and machine learning.

### Reason for Project Idea

Firstly, the reason the group chose this project idea is because we believe this model can be used in analyzing various stock prices.

Secondly, the dataset mainly contains numerical values and it is easily readable.

Thirdly, the stock market is being considered as major investment portfolio by indiduals and businesses, the model developed in this analysis will help individuals and businesses in making a business decision.

Finally, our passion for numerical analysis and data manipulation is a core reason for choosen this project idea.

### Question to be answered

Using machine learning algorithms we will train a regression model using historic pricing data and technical indicators to make predictions on future prices.

What we seek to achieve with the data set is to identify trends in the stock market using charts and statistical figures.

The model will help in making an investment decision.

### Data Source

The source of data is obtained from kaggle [Tesla Stock Price](https://www.kaggle.com/timoboz/tesla-stock-data-from-2010-to-2020).

This data consists of 2416 rows and 7 columns with historical trading data from 2010 - 2020.

There are multiple variables in the dataset – date, Opening price, Highest price that day, Lowest price that day, Adjusted closing price and Trading volume.

The columns Open and Close represent the starting and final price at which the stock is traded on a particular day.

High, Low and Last represent the maximum, minimum, and last price of the share for the day.

Trading volume is the number of shares bought or sold in the day.

We will use Pandas to clean the dataset and perform an exploratory analysis.

### Machine Learning Model

The first review of the data was done using excel to access the data characteristics.

We will load historic pricing data into a Pandas’ DataFrame for the Linear Regression model.

We will train a simple linear regression model using moving average as a predictor for the closing price.

We will analyze the accuracy of our model, plot the results, and consider the magnitude of our errors.

We will be using python and scikit-learn to present a provisional machine learning model that stands in for the final machine learning model.

This model will take data from the provisional database and output labels for input data.

### Database

For the purpose of this project, we will be using the AWS database and Postgres admin database to store the data.

We will present a provisional database that stands for the final database which will store sample data and used for the machine learning model.

### Technologies Utilized

* Visual Code Studio
* Python
* Flask
* HTML
* Javascript
* PostgreSQL
* PGadmin
* Plotly
* CSS
* AWS
* Jupyter Notebook
* Google Colab
* Machine learning
* Microsoft Excel
* Anaconda
* Pandas

### Project Dashboard

We will be presenting an interactive dashboard that shows our result at the end of the project.

The final project result will be hosted on the web using plotly.