LOAD DATA INFILE 'D:\Projects\the-mart-problem\martData.csv'
INTO TABLE `themart`.`martapis_mart`
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;


LOAD DATA INFILE 'D:\Projects\the-mart-problem\skuData.csv'
INTO TABLE `themart`.`martapis_mart`
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;