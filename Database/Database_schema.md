# Database Schema

- One table with attributes defined as follows:

  - hdate - date type
  - hopen - REAL
  - hhigh - REAL
  - hlow - REAL
  - hclose - REAL
  - hadjclose - REAL
  - hvolume - INTEGER
  - PRIMARY KEY hdate

- The date field was chosen as Primary Key and and also assigned a NOT NULL restraint to ensure records must have at least a date value to be part of the dataset.
