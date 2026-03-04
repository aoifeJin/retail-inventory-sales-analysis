import pandas as pd     # used to create the dataset
import numpy as np     # used to generate random values

np.random.seed(42)     # makes sure the random data stays the same every time the code runs

rows = 5000     # dataset will contain 5000 transactions while each row represents one sales record

zones = ["Men", "Women", "Kids"] # store has three main areas

# each zone has different sections
sections = {
    "Men": ["Clothing", "Accessories", "Perfume", "Sportswear"],
    "Women": ["Clothing", "Accessories", "Perfume"],
    "Kids": ["Clothing", "Accessories"]
}

# each section contains product categories
categories = {
    "Clothing": ["Outerwear", "Dresses", "Tops", "Bottoms"],
    "Sportswear": ["Sportswear"],
    "Accessories": ["Accessories", "Footwear"],
    "Perfume": ["Perfume"]
}

# each product type has a price range, generate random prices within these ranges
price_ranges = {
    "Outerwear": (60, 180),
    "Dresses": (30, 90),
    "Tops": (15, 60),
    "Bottoms": (30, 70),
    "Sportswear": (25, 80),
    "Footwear": (40, 130),
    "Accessories": (10, 40),
    "Perfume": (20, 80)
}

data = []     # create an empty list to store data

# the loop runs 5000 times, ach time it creates one transaction
for i in range(rows):
    
    # every row the code randomly generates: zone, section, category, price, stock level, units sold, promotion and date

    zone = np.random.choice(zones)     # randomly selects a store zone from the list 'zone'

    section = np.random.choice(sections[zone])     # randomly picks one section that belongs to the selected zone

    category = np.random.choice(categories[section])     # each section contains different product categories

    low, high = price_ranges[category]     # get the price range for that category
    price = round(np.random.uniform(low, high), 2)     # generate a random price between the minimum and maximum value then round the price to 2 decimal places

    stock_level = np.random.randint(20, 200)     # creates a random inventory level between 20 and 200 units

    # tops and accessories sell faster, outerwear sells slower, and other products sell at normal speed
    if category in ["Tops", "Accessories"]:
        units_sold = np.random.randint(10, 40)
    elif category == "Outerwear":
        units_sold = np.random.randint(2, 15)
    else:
        units_sold = np.random.randint(5, 25)

    promotion = np.random.choice(["Yes", "No"], p=[0.3, 0.7])     # 30% chance item is on promotion and 70% chance no promotion

    random_days = np.random.randint(0, 365)
    date = pd.Timestamp("2025-01-01") + pd.Timedelta(days=random_days)     # creates a random date in the year 2025

    data.append([
        i + 1,
        zone,
        section,
        category,
        price,
        stock_level,
        units_sold,
        promotion,
        date
    ])

# all generated data is stored in a pandas DataFrame
df = pd.DataFrame(data, columns=[
    "transaction_id",
    "zone",
    "section",
    "category",
    "price",
    "stock_level",
    "units_sold",
    "promotion",
    "date"
])

df.to_csv("data/retail_sales.csv", index=False)     # dataset is saved as a CSV file where location within data/
print("Dataset generated: data/retail_sales.csv")     # handy print statement which confirms the dataset has been successfully generated and saved