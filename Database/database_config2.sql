-- Add Main Tesla record
INSERT INTO company(ticker_id, company_name)
VALUES ('TSLA', 'Tesla, Inc.')
RETURNING *;

--values are in millions $
UPDATE yearly_values SET
	revenue = revenue * 1000,
	net_income = net_income * 1000,
	gross_profit = gross_profit * 1000,
	operating_income = operating_income * 1000,
	ebitda = ebitda * 1000,
	shares = shares * 1000;

--values are in millions $
UPDATE quarterly_values SET
	revenue = revenue * 1000,
	net_income = net_income * 1000,
	gross_profit = gross_profit * 1000,
	operating_income = operating_income * 1000,
	ebitda = ebitda * 1000,
	shares = shares * 1000;

--values are in millions $
UPDATE common_values SET
	revenue = revenue * 1000,
	net_income = net_income * 1000,
	gross_profit = gross_profit * 1000,
	operating_income = operating_income * 1000,
	ebitda = ebitda * 1000,
	shares = shares * 1000

--alter table and add field	
ALTER TABLE daily_values
ADD COLUMN q_key VARCHAR(10);

--alter table and add field	
ALTER TABLE common_values
ADD COLUMN q_id VARCHAR(10) PRIMARY;

--alter table and add FOREIGN KEY
ALTER TABLE daily_values
ADD FOREIGN KEY (q_key) REFERENCES common_values(q_id);
  
-- Query databse to check successful uploads
SELECT * FROM company;
SELECT * FROM daily_values;
SELECT * FROM yearly_values;
SELECT * FROM quarterly_values;
SELECT * FROM common_values;