-- Find negative prices
SELECT *
FROM menu_items
WHERE price < 0;

-- Update negative prices
UPDATE menu_items
SET price = NULL
WHERE price < 0;
