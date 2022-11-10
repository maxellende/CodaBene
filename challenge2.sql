SELECT COUNT(CASE WHEN expiry_date<'2021-10-20' THEN 1 ELSE NULL END) as 'expired products', 
       COUNT(CASE WHEN '2021-10-20'<expiry_date AND expiry_date<'2021-10-25' THEN 1 ELSE NULL END) as 'endangered products', 
       COUNT(CASE WHEN '2021-10-25'<expiry_date THEN 1 ELSE NULL END) as 'safe products'
FROM 'references' ;