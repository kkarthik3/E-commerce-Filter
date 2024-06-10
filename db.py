import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('ornaments_db.db')
cursor = conn.cursor()

# Create the ornaments table if it doesn't exist
create_table_query = """
CREATE TABLE IF NOT EXISTS ornaments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price INTEGER NOT NULL,
    material TEXT NOT NULL,
    product_type TEXT NOT NULL,
    weight INTEGER NOT NULL,
    occasion TEXT NOT NULL,
    URL TEXT NOT NULL
);
"""
cursor.execute(create_table_query)

# Insert sample data into the ornaments table
insert_data_query = """
INSERT INTO ornaments (name, price, material, product_type, weight, occasion, URL)
VALUES 
    ('Gold Necklace', 50000, 'Gold', 'Necklace', 50, 'Party', 'https://ranialankar.com/wp-content/uploads/2022/01/20220130_182022.jpg'),
    ('Silver Ring', 8000, 'Silver', 'Ring', 10, 'Daily', 'https://m.media-amazon.com/images/I/51vtC0tJdxL._AC_UY1100_.jpg'),
    ('Platinum Bracelet', 75000, 'Platinum', 'Bracelet', 30, 'Office', 'https://www.byenzojewelry.com/wp-content/uploads/2023/04/015-12-04-1.jpg.webp'),
    ('Diamond Earrings', 120000, 'Diamond', 'Earrings', 20, 'Party', 'https://image.brilliantearth.com/media/product_images/25/BE304RD400_white_top.jpg'),
    ('Gold Bracelet', 30000, 'Gold', 'Bracelet', 25, 'Daily', 'https://i.ebayimg.com/images/g/pzQAAOSwa0xlFUOf/s-l1200.webp'),
    ('Silver Necklace', 20000, 'Silver', 'Necklace', 40, 'Office', 'https://uk.cherrypick.city/cdn/shop/files/silver-necklace-ruby-oxidised-silver-92-5-silver-necklace-140287-36094169022620.jpg?v=1702614712'),
    ('Gold Ring', 15000, 'Gold', 'Ring', 15, 'Party', 'https://bawajewels.com/wp-content/uploads/452-3.jpg'),
    ('Platinum Ring', 55000, 'Platinum', 'Ring', 5, 'Daily', 'https://static.malabargoldanddiamonds.com/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/f/r/frgen13025_c.jpg'),
    ('Diamond Necklace', 200000, 'Diamond', 'Necklace', 60, 'Party', 'https://beauvince.com/cdn/shop/products/925N-4_800x.jpg?v=1702474628'),
    ('Silver Earrings', 12000, 'Silver', 'Earrings', 12, 'Daily', 'https://i.etsystatic.com/5588694/r/il/8acea6/2411693361/il_fullxfull.2411693361_8iuy.jpg'),
    ('Gold Earrings', 30000, 'Gold', 'Earrings', 18, 'Office', 'https://static.malabargoldanddiamonds.com/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/e/g/egdsno102_c.jpg'),
    ('Platinum Necklace', 85000, 'Platinum', 'Necklace', 45, 'Party', 'https://www.rangasjewellery.com/img/p/1/1/11-large_default.jpg'),
    ('Gold Anklet', 25000, 'Gold', 'Others', 20, 'Daily', 'https://rukminim2.flixcart.com/image/850/1000/xif0q/anklet/l/l/j/na-na-2-vs-0012-gold-payal-golden-diva-original-imagmzx4qzujegzv.jpeg?q=90&crop=false'),
    ('Silver Bracelet', 18000, 'Silver', 'Bracelet', 28, 'Office', 'https://m.media-amazon.com/images/I/61qEaJh9NVL._AC_UY1000_.jpg'),
    ('Diamond Ring', 110000, 'Diamond', 'Ring', 7, 'Party', 'https://www.nektanewyork.com/cdn/shop/products/10-carat-princess-cut-diamond-engagement-ring-28999330988206_2000x.jpg?v=1643652837'),
    ('Gold Pendant', 22000, 'Gold', 'Others', 12, 'Office', 'https://5.imimg.com/data5/SELLER/Default/2023/7/325276443/FJ/IG/SB/192607587/gold-pendant-4gm.png'),
    ('Silver Anklet', 15000, 'Silver', 'Others', 18, 'Daily', 'https://silverpalace.in/uploads/products/img-13228624006218c4b33962f9.72190808.jpg'),
    ('Platinum Earrings', 67000, 'Platinum', 'Earrings', 22, 'Party', 'https://rukminim2.flixcart.com/image/850/1000/xif0q/earring/l/p/t/-original-imahyjf6seqdsf6c.jpeg?q=90&crop=false'),
    ('Diamond Bracelet', 130000, 'Diamond', 'Bracelet', 35, 'Office', 'https://image.brilliantearth.com/media/product_images/00/BE5D100TB_white_top.jpg'),
    ('Gold Necklace', 52000, 'Gold', 'Necklace', 48, 'Daily', 'https://ranialankar.com/wp-content/uploads/2022/01/20220130_182022.jpg'),
    ('Silver Pendant', 9000, 'Silver', 'Others', 8, 'Office', 'https://www.proclamationjewelry.com/cdn/shop/products/mens_silver_pendant_stchristopher_necklace_2048x.jpg?v=1680106184'),
    ('Platinum Ring', 60000, 'Platinum', 'Ring', 10, 'Party', 'https://static.malabargoldanddiamonds.com/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/f/r/frgen13025_c.jpg'),
    ('Diamond Anklet', 140000, 'Diamond', 'Others', 25, 'Daily', 'https://i.ebayimg.com/images/g/S-kAAOSwcC9ic67s/s-l1200.jpg'),
    ('Gold Earrings', 28000, 'Gold', 'Earrings', 16, 'Office', 'https://static.malabargoldanddiamonds.com/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/e/g/egdsno102_c.jpg'),
    ('Silver Ring', 7500, 'Silver', 'Ring', 9, 'Party', 'https://m.media-amazon.com/images/I/51vtC0tJdxL._AC_UY1100_.jpg'),
    ('Gold Bracelet', 32000, 'Gold', 'Bracelet', 26, 'Daily', 'https://i.ebayimg.com/images/g/pzQAAOSwa0xlFUOf/s-l1200.webp'),
    ('Platinum Necklace', 90000, 'Platinum', 'Necklace', 50, 'Office', 'https://www.rangasjewellery.com/img/p/1/1/11-large_default.jpg'),
    ('Diamond Earrings', 115000, 'Diamond', 'Earrings', 21, 'Party', 'https://image.brilliantearth.com/media/product_images/25/BE304RD400_white_top.jpg'),
    ('Gold Ring', 17000, 'Gold', 'Ring', 12, 'Daily', 'https://bawajewels.com/wp-content/uploads/452-3.jpg'),
    ('Silver Earrings', 11000, 'Silver', 'Earrings', 10, 'Office', 'https://i.etsystatic.com/5588694/r/il/8acea6/2411693361/il_fullxfull.2411693361_8iuy.jpg');
"""

# Execute the query to insert the data
cursor.execute(insert_data_query)

# Commit the changes and close the connection
conn.commit()
conn.close()
