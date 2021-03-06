
# Final_Project

Final project of the data incites group - University of Toronto Data Analytics Bootcamp
 
## Project Background 

The selected project topic for this group is **Stock price Predictor**

**Data source**: [Tesla Stock Price](https://finance.yahoo.com/quote/TSLA/history?p=TSLA) , [Tesla Revenue](https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue) , [Tesla EPS](https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue) 

**Google Slide Link**

 [Presentation](https://docs.google.com/presentation/d/1FUG7G955AFw-W6SOV7qHsod4T7I4Npr5Js2dOtEmPR8/edit#slide=id.gf06cb6288e_0_5)

 [Dashboard Blueprint](https://docs.google.com/presentation/d/1gQCpkDp3MEN7LO5x0zF8KAiiKE5SD2Ak3EJYs237JpY/edit#slide=id.p)

 [Final Dashboard](https://teslastockpriceprediction.herokuapp.com/)

**Team Members**

* [Nnaemeka Enukorah](https://github.com/NENUKORAH)

* [Frank Brumwell](https://github.com/ftrbrum)

* [Azuka Obasuyi](https://github.com/aobasuyi)

* [Barnett Bullock](https://github.com/bnbullock)

## Project Idea

We highlighted 15 ideas to be considered as the final project for this group and casted votes to determine which project idea should be considered.

This was done using the [miro app](https://miro.com/app/dashboard/) 

![Voting](https://user-images.githubusercontent.com/81701640/131906240-17a3607b-f0a1-4e0a-926a-06a49a8aa31a.png)

We had a tie on three projects, but decided to go with the stock price prediction project idea.

## Project Overview

The purpose of this project is to analyse the stock price and revenue of Tesla to predict future pricing using moving averages, linear regression and machine learning.

### Reason for Project Idea

Firstly, the reason the group chose this project idea is because we believe this model can be used in analyzing various stock prices.

Secondly, the dataset mainly contains numerical values and it is easily readable.

Thirdly, the stock market is being considered as major investment portfolio by indiduals and businesses, the model developed in this analysis will help individuals and businesses in making a business decision.

Fourthly, our passion for numerical analysis and data manipulation is a core reason for choosen this project idea.

Finally, to understand the relationship between Tesla revenue, stock prices and Earning Per Share (EPS).

### Question to be answered

Using machine learning algorithms we will train a regression model using historic pricing data and technical indicators to make predictions on future prices.

What we seek to achieve with the data set is to identify trends in the stock market using charts and statistical figures.

We would like to know if Tesla stock price will attain $3,000 a share in the near future as stated by Cathie Wood (Founder Ark Invest) in a recent [Interview](https://finance.yahoo.com/news/tesla-stock-is-worth-3000-ark-invests-cathie-wood-201139618.html).

### Data Source

The source of data is obtained from yahoo finance [Tesla Stock Price](https://finance.yahoo.com/quote/TSLA/history?p=TSLA) and macro trends [Tesla Revenue](https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue) , [Tesla EPS](https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue).

This data consists of 2416 rows and 7 columns with historical trading data from 2010 - 2020.

There are multiple variables in the dataset ??? date, Opening price, Highest price that day, Lowest price that day, Adjusted closing price and Trading volume.

The columns Open and Close represent the starting and final price at which the stock is traded on a particular day.

High, Low and Last represent the maximum, minimum, and last price of the share for the day.

Trading volume is the number of shares bought or sold in the day.

Tesla revenue data consist of quarterly Tesla revenue from 2010 - 2020.

Tesla EPS data consist of quarterly Tesla revenue from 2010 - 2020.

We will use Pandas to clean the dataset and perform an exploratory analysis.

### Machine Learning Model

The first review of the data was done using excel to access the data characteristics.

We will load historic pricing data into a Pandas??? DataFrame for the Linear Regression model.

We will train a simple linear regression model using moving average as a predictor for the closing price.

We will analyze the accuracy of our model, plot the results, and consider the magnitude of our errors.

We will be using python and scikit-learn to present a provisional machine learning model that stands in for the final machine learning model.

This model will take data from the provisional database and output labels for input data.

The target is closing stock price, the data split into training and test set (80, 20).

Four models Autoregressive Integrated Moving Average (ARIMA), Facebook Prophet, Long short-term memory (LSTM) and Linear Regression will be used for the machine learning. 

The model with the best result (magnitude of errors, accuracy) will be selected for final deployment.

### Linear Regression Model

![Linear Regression ML](https://user-images.githubusercontent.com/81701640/134269180-939a6eb2-265c-4476-a1be-6013fc2ef350.png)

### Long Short-Term Memory (LSTM)

![LSTM ML](https://user-images.githubusercontent.com/81701640/134269310-68be9245-31ba-4dea-a1e3-07347c6d95a2.png) 

### Autoregressive Integrated Moving Average (ARIMA) 

![ARIMA ML](https://user-images.githubusercontent.com/81701640/134269341-07a43d4c-12c7-49c9-9f5f-077b35cd5972.png)

### Facebook Prophet Model

![FB prophet ML](https://user-images.githubusercontent.com/81701640/134269469-2d9e9868-4cd8-48e5-8383-1c7e46637643.png)

The null values were dropped, and date set as index in the preprocessing phase.

The data was split 80:20 for testing and training.

We selected the Facebook model because it is the only model that could predict stock prices for a longer term with an accuracy score of 80%.

One major limitation of the model is that the accuracy score might not be as high as the other models.

The main benefit of the facebook prophetmodel is that it factors seasonality in the modelling, it is also flexible and easy to use compared to the other models.

### Database  

For the purpose of this project, we will be using the AWS database and Postgres admin database to store the data.

We will present a provisional database that stands for the final database which will store sample data and used for the machine learning model.

### Database table Creation

The table creation script is included in this folder and is called "table_create_script.sql". This script was loaded into a query window and executed against a PostgreSQL database named "tesla", which was manually created using the pgAdmin interface. 
We can automate the full database creation using a script.

### Table Attributes

Below is a brief description of each attribute and this information is also contained in the "database_schema" file in this directory.

* Date - this is the date of record
* Open - opening price of stock
* High - highest price recorded for that date
* Low - lowest price recorded for that date
* Close - closing price of stock
* Adj Close - adjusted close in case of after hours trading
* Volume - Amount of shares traded for that date

### Sample Data and CRUD testing

From the primary data downloaded from the kaggle site, the data was partitioned for a sample data set containing the top 100 rows from the actual source file including the header details. 
As such, we will be using real values for testing and preliminary analysis. This data was loaded manually into the database using the import feature of pgAdmin once the table was created as mentioned above. 
The name of the sample data file is called "tesla100.csv".

With the database setup and available, we can now test everything using the CRUD concept reviewed during our course lectures. The file called "CRUD.txt" contains the SQL scripts that were developed to verify proper testing. 

### Entity Relationship Diagram

The diagram below shows the entity relationship model of the project dataset. 

![ERD Final Project](https://user-images.githubusercontent.com/81701640/133913727-4f35f369-2905-426c-84f6-8c9060a3149e.png)

### Technologies Utilized

The following technologies will be utilized throughout the duration of this project;

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

A demo has been shown in the google slide presentation.
