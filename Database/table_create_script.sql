CREATE TABLE price_history (
 hdate DATE NOT NULL,
 hopen REAL,
 hhigh REAL,
 hlow REAL,
 hclose REAL,
 hadjclose REAL,	
 hvolume INT,
 PRIMARY KEY (hdate)
);

DROP TABLE price_history;
