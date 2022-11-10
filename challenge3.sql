SELECT allee as aisle,
       COUNT(CASE WHEN expiry_date<'2021-10-20' THEN 1 ELSE NULL END) as expired_products, 
       COUNT(CASE WHEN '2021-10-20'<expiry_date AND expiry_date<'2021-10-25' THEN 1 ELSE NULL END) as endangered_products, 
       COUNT(CASE WHEN '2021-10-25'<expiry_date THEN 1 ELSE NULL END) as safe_products
FROM 'references' GROUP BY 'references'.allee
ORDER BY endangered_products DESC;

