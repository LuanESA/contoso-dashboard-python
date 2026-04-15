WITH Evolucao AS (
    SELECT 
        d.CalendarYear,
        d.CalendarMonthLabel,
        SUM(fs.SalesAmount) AS Faturamento
    FROM 
        FactSales fs
    JOIN DimDate d 
        ON fs.DateKey = d.DateKey
    GROUP BY
        d.CalendarYear,
        d.CalendarMonthLabel
)

SELECT *,
    Faturamento 
        - LAG(Faturamento) OVER (ORDER BY CalendarYear, CalendarMonthLabel) 
        AS Crescimento_Valor,

    (Faturamento - LAG(Faturamento) OVER (ORDER BY CalendarYear, CalendarMonthLabel)) 
        * 100.0 
        / LAG(Faturamento) OVER (ORDER BY CalendarYear, CalendarMonthLabel) 
        AS Crescimento_Percentual

FROM Evolucao
ORDER BY CalendarYear,CalendarMonthLabel;


-----------------------------------------

SELECT 
    d.CalendarYear,
    d.CalendarMonthLabel,
    
    SUM(fs.SalesAmount) AS Faturamento,
    SUM(fs.TotalCost) AS Custo,

    (SUM(fs.SalesAmount) - SUM(fs.TotalCost)) * 1.0
        / NULLIF(SUM(fs.SalesAmount),0) AS Margem

FROM 
    FactSales fs
JOIN DimDate d 
    ON fs.DateKey = d.DateKey

GROUP BY
    d.CalendarYear,
    d.CalendarMonthLabel

ORDER BY
    d.CalendarYear,
    d.CalendarMonthLabel;



-------------------------------------------------


SELECT 
    d.CalendarYear,
    d.CalendarMonthLabel,
    SUM(fs.SalesAmount) AS Faturamento
FROM 
    FactSales fs
JOIN DimDate d 
    ON fs.DateKey = d.DateKey
GROUP BY
    d.CalendarYear,
    d.CalendarMonthLabel
ORDER BY
    d.CalendarYear,
    d.CalendarMonthLabel;

