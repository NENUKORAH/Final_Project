# Group : Data Incites

Our chosen dataset is located at the link below which has 10 years of historical daily Tesla stock prices.

Dataset : <https://www.kaggle.com/timoboz/tesla-stock-data-from-2010-to-2020>

## Segment 1 Deliverable

Role - Circle -> Database Design and Mockup

## Database table Creation

- The table creation script is included in this folder and is called "table_create_script.sql". This script was loaded into a query window and executed against a PostgreSQL database named "tesla", which was manually created using the pgAdmin interface. We can automate the full database creation using a script as well if that is deemed a neccessity by the team.

## Table Attributes

- An ERD was not specifically created as we only have a singular data table with the following 7 attributes. I have provided a brief description of each below and this information is also contained oin the "database_schema" file in this directory.
  - Date - this is the date of record
  - Open - opening price of stock
  - High - highest price recorded for that date
  - Low - lowest price recorded for that date
  - Close - closing price of stock
  - Adj Close - adjusted close in case of after hours trading
  - Volume - Amount of shares traded for that date

## Sample Data

- From the primary data downloaded from the kaggle site, the data was partitioned for a sample data set containing the top 100 rows from the actual source file including the header details. As such, we will be using real values for testing and preliminary analysis. This data was loaded manually into the database using the import feature of pgAdmin once the table was created as mentioned above. The name of the sample data file is called "tesla100.csv" and loaded using the pgAdmin interface below.

![Image1](images/FileImport.png)

## CRUD Testing

- With the database setup and available, we can now test everything using the CRUD concept reviewed during our course lectures. The file called "CRUD.txt" contains the SQL scripts that were developed to verify proper testing. Below is a screen capture showing the final part of the delete process, however, each aspect of CRUD contains a tested feature.

![Image2](images/CRUD_Test.png)

## Connection to Machine Learning Model

- The machine learning model is able to connect to the database properly, please see screen capture below showing records returned from a query. The code is contained in the "mlm.ipynb" jupyter file in the repository for your reference.

![Image3](images/DB_connect_read.png)