# Query for restaurants distribution

query_deliveroo = """
SELECT
    locations.id, locations.name, locations.longitude, locations.latitude,
    COUNT(locations_to_restaurants.location_id) AS count_per_location
FROM
    locations
JOIN locations_to_restaurants ON locations.id = locations_to_restaurants.location_id

GROUP BY
    locations.id
ORDER BY
	locations.name;
"""

query_takeaway = """ 
SELECT
    locations.id, locations.name, locations.longitude, locations.latitude,
    COUNT(locations_to_restaurants.location_id) AS count_per_location
FROM
    locations
JOIN locations_to_restaurants ON locations.id = locations_to_restaurants.location_id

GROUP BY
    locations.id
ORDER BY
	locations.name;
"""
query_ubereatss = """ 
SELECT
    locations.id, locations.name, locations.longitude, locations.latitude,
    COUNT(locations_to_restaurants.location_id) AS count_per_location
FROM
    locations
JOIN locations_to_restaurants ON locations.id = locations_to_restaurants.location_id

GROUP BY
    locations.id
ORDER BY
	locations.name
"""
query_ubereats = """ SELECT title, location__latitude, location__longitude
                     FROM restaurants
                """
# for kalsalons
query_a4_resto_deliveroo = """
SELECT
    restaurants.id, restaurants.name, restaurants.latitude, restaurants.longitude,
    AVG(CASE WHEN menu_items.name LIKE '%kapsalon%' THEN menu_items.price ELSE NULL END) AS avg_kapsalon_price,
    COUNT(CASE WHEN menu_items.name LIKE '%kapsalon%' THEN menu_items.price ELSE NULL END) AS count_kapsalon_options

FROM
    restaurants
JOIN menu_items ON restaurants.id = menu_items.restaurant_id

WHERE
    menu_items.name LIKE '%kapsalon%'
GROUP BY
    restaurants.id
ORDER BY
	avg_kapsalon_price DESC;
"""

query_a4_resto_takeaway = """
    SELECT
        restaurants.primarySlug, restaurants.name, restaurants.latitude, restaurants.longitude,
        AVG(CASE WHEN menuItems.name LIKE '%kapsalon%' THEN menuItems.price ELSE NULL END) AS avg_kapsalon_price,
        COUNT(CASE WHEN menuItems.name LIKE '%kapsalon%' THEN menuItems.price ELSE NULL END) AS count_kapsalon_options
    FROM
        restaurants
    JOIN 
        menuItems ON restaurants.primarySlug = menuItems.primarySlug
    WHERE
        menuItems.name LIKE '%kapsalon%'
    GROUP BY
        restaurants.primarySlug
    ORDER BY
	    avg_kapsalon_price DESC;
"""

query_a4_resto_ubereats = """
SELECT
    restaurants.id, restaurants.title, restaurants.location__latitude AS latitude, restaurants.location__longitude AS longitude,
    (AVG(CASE WHEN menu_items.name LIKE '%kapsalon%' THEN menu_items.price ELSE NULL END)/100) AS avg_kapsalon_price,
    COUNT(CASE WHEN menu_items.name LIKE '%kapsalon%' THEN menu_items.price ELSE NULL END) AS count_kapsalon_options
FROM
    restaurants
JOIN menu_items ON restaurants.id = menu_items.restaurant_id
    
WHERE
    menu_items.name LIKE '%kapsalon%'
GROUP BY
    restaurants.id
ORDER BY
	avg_kapsalon_price DESC;
"""

# query for deals acorss platform

query_deliveroo_deals = """select count (*) from
(SELECT  count(categories.name) as cat_count ,restaurants.id
FROM restaurants 
JOIN categories on restaurants.id = categories.restaurant_id
Where categories.name like '%deal%'
Group by categories.restaurant_id)
;
"""
query_takeaway_deals ="""select count (*) from
(SELECT  count(menuItems.name) as cat_count ,menuItems.primarySlug
FROM menuItems 
Where menuItems.name like '%deal%'
Group by menuItems.primarySlug)
;
"""
query_ubereats_deals = """select count (*) from
(SELECT  count(name) as cat_count ,restaurant_id
FROM menu_items 
Where name like '%deal%'
Group by restaurant_id)
;
"""

