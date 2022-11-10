SELECT allee as aisle,
       'retailer'.'LibelléSous-Famille',
       COUNT(CASE WHEN expiry_date<'2021-10-20' THEN 1 ELSE NULL END) as expired_products, 
       COUNT(CASE WHEN '2021-10-20'<expiry_date AND expiry_date<'2021-10-25' THEN 1 ELSE NULL END) as endangered_products, 
       COUNT(CASE WHEN '2021-10-25'<expiry_date THEN 1 ELSE NULL END) as safe_products
FROM 'references', 'retailer'
WHERE 'references'.reference_id == 'retailer'.EAN AND LOWER('retailer'."LibelléGroupedeFamille") LIKE '%charcuterie%'
GROUP BY 'references'.allee ,'retailer'.'LibelléSous-Famille'
ORDER BY endangered_products DESC;

