create table UserInfo (
    stockSymbol text,
    dateofPurchase text,
    avgPurchasePrice real,
    numOfStocks integer,
    PRIMARY KEY (stockSymbol, dateofPurchase, avgPurchasePrice)
);