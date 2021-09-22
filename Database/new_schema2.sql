-- Create Company Table
CREATE TABLE company (
  ticker_id VARCHAR(10) NOT NULL,
  company_name VARCHAR(40) NOT NULL,
  PRIMARY KEY (ticker_id),
  UNIQUE (company_name)
);

-- Create Daily Values Table
CREATE TABLE daily_values (
 ticker VARCHAR(10) NOT NULL,
 hdate DATE NOT NULL,
 hopen REAL,
 hhigh REAL,
 hlow REAL,
 hclose REAL,
 hadjclose REAL,	
 hvolume INT,
 q_key VARCHAR(10),
 FOREIGN KEY (ticker) REFERENCES company (ticker_id),
 FOREIGN KEY (q_key) REFERENCES common_values (q_id),
 PRIMARY KEY (ticker, hdate)
);

-- Create Quarterly Values Table
CREATE TABLE quarterly_values (
  ticker VARCHAR(10) NOT NULL,
  qDate DATE NOT NULL,
  revenue REAL,
  eps REAL,
  net_income REAL,
  gross_profit REAL,
  operating_income REAL,
  ebitda REAL,
  shares INT,
  quarter VARCHAR(4) NOT NULL,
  qyear INT,
  qlabel VARCHAR(10) NOT NULL,
  FOREIGN KEY (ticker) REFERENCES company (ticker_id),
  PRIMARY KEY (ticker, qDate)
);


-- Create Yearly Values Table
CREATE TABLE yearly_values (
  ticker VARCHAR(10) NOT NULL,
  yyear INT NOT NULL,
  revenue REAL,
  eps REAL,
  net_income REAL,
  gross_profit REAL,
  operating_income REAL,
  ebitda REAL,
  shares INT,
  FOREIGN KEY (ticker) REFERENCES company (ticker_id),
  PRIMARY KEY (ticker, yyear)
);

-- Create Common Values Table
CREATE TABLE common_values (
  ticker VARCHAR(10) NOT NULL,
  qDate DATE NOT NULL,
  revenue REAL,
  eps REAL,
  net_income REAL,
  gross_profit REAL,
  operating_income REAL,
  ebitda REAL,
  shares INT,
  quarter VARCHAR(4) NOT NULL,
  qyear INT NOT NULL,
  qlabel VARCHAR(10) NOT NULL,
  share_price REAL,
  q_id VARCHAR(10),
  FOREIGN KEY (ticker) REFERENCES company (ticker_id),
  PRIMARY KEY (q_id)
);
