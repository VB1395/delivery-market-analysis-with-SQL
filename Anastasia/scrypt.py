import sqlite3

# Connect to the Deliveroo database
connection = sqlite3.connect("databases/deliveroo.db")

# Create a cursor object
cursor = connection.cursor()

# SQL query for top 10 restaurants by rating
query_restaurants = """
SELECT name, rating
FROM restaurants
ORDER BY rating DESC
LIMIT 10;
"""

# SQL query to analyze price distribution of menu items
query_price_distribution = """
SELECT price
FROM menu_items;
"""

try:
    # Execute the first query (Top 10 restaurants)
    cursor.execute(query_restaurants)
    results = cursor.fetchall()

    # Print results for the first query
    print("Top 10 Restaurants by Rating:")
    for row in results:
        print(f"Name: {row[0]}, Rating: {row[1]}")

    # Execute the second query (Price distribution)
    cursor.execute(query_price_distribution)
    prices = cursor.fetchall()

    # Convert fetched prices to a list of floats (filter invalid entries)
    price_list = []
    for price in prices:
        try:
            price_list.append(float(price[0]))
        except (ValueError, TypeError):
            # Skip invalid entries
            continue

    # Print a summary of price distribution
    print("\nPrice Distribution of Menu Items:")
    print(f"Total items: {len(price_list)}")
    print(f"Minimum price: {min(price_list):.2f}")
    print(f"Maximum price: {max(price_list):.2f}")
    print(f"Average price: {sum(price_list) / len(price_list):.2f}")

except sqlite3.Error as e:
    print(f"Error: {e}")

finally:
    # Close the connection
    connection.close()

