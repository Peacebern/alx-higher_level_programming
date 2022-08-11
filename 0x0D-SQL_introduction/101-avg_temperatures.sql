-- script that displays the average temperature (Fahrenheit) by ci-- ty ordered -- by temperature (descending).

SELECT `city`, AVG(`value`) AS 'avg_temp'
FROM `temperature`
GROUP BY `city`
ORDER BY `avg_temp` DESC;
