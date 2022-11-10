SELECT COUNT(*) as ' total number of references not tracked in the app but present in the shop assortment' FROM 'retailer' WHERE 'retailer'.EAN NOT IN (SELECT reference_id FROM 'references');
