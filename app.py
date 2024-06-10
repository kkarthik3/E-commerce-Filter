import streamlit as st
import sqlite3
from llm import input_utterance

# Assuming you have a SQLite database named 'ornaments.db'

# Connect to the database
conn = sqlite3.connect('ornaments_db.db')
cursor = conn.cursor()


st.set_page_config("PNG Jwellery")
st.header("PNG jwellery Query extraction")
# Sidebar filters
st.sidebar.header("Filter Options")


def filter(list):
    # Price range slider
    if (list[0] or list[1]) is not None: 
        if list[1] is not None:
            price_range = st.sidebar.slider('Price Range', 0, 200000, step=5000,value=(list[0],list[1]),key="price")
        else:
            price_range = st.sidebar.slider('Price Range', 0, 200000, step=5000,value=(list[0],200000),key="price")

    else:
        price_range = st.sidebar.slider('Price Range', 0, 200000, step=5000,value=(0,200000),key="price")


    # Material select box
    material_options = ['All', 'Gold', 'Silver', 'Platinum', 'Diamond', 'Others']
    if list[3] is not None:
        selected_values = [item.strip() for item in list[3].split(',')]  # Split by comma and strip whitespace
    else:
        selected_values = ["All"]

    material = st.sidebar.multiselect('Material', material_options,default=selected_values,key="material")


    # Product type select box
    product_options = ['All', 'Necklace', 'Ring', 'Bracelet', 'Earrings', 'Others']
    if list[2] is not None:
        selected_values = [item.strip() for item in list[2].split(',')]  # Split by comma and strip whitespace
    else:
        selected_values = ["All"]

    product_type = st.sidebar.multiselect('Product Type', product_options, default=selected_values,key="product")

    # Weight slider

    if (list[5] or list[6]) is not None: 
        if list[6] is not None:
            weight = st.sidebar.slider('Weight (in grams)', 0, 500, step=5,value=(list[5],list[6]),key="weight")
        else:
            weight = st.sidebar.slider('Weight (in grams)', 0, 500, step=5,value=(list[5],500),key="weight")
    else:
        weight = st.sidebar.slider('Weight (in grams)', 0, 500, step=5,value=(0,500),key="weight")
    

    # Occasion multi-select
    occasion_options = ['Daily', 'Office', 'Party']

    if list[4] is not None:
        selected_values = [item.strip() for item in list[4].split(',')]  # Split by comma and strip whitespace
    else:
        selected_values = None  

    occasion = st.sidebar.multiselect('Occasion', occasion_options,default=selected_values,key="occasion")

    return price_range, material, product_type, weight, occasion


def generate_query(price_range, material, product_type, weight, occasion):
    # SQL query construction
    query = "SELECT * FROM ornaments WHERE 1=1"

    # Apply price range filter
    query += f" AND price BETWEEN {price_range[0]} AND {price_range[1]}"

    # Apply material filter
    if 'All' not in material:
        material_str = "','".join(material)
        query += f" AND material IN ('{material_str}')"

    # Apply product type filter
    if 'All' not in product_type:
        product_type_str = "','".join(product_type)
        query += f" AND product_type IN ('{product_type_str}')"

    # Apply weight filter
    query += f" AND weight BETWEEN {weight[0]} AND {weight[1]}"

    # Apply occasion filter
    if occasion:
        occasion_str = "','".join(occasion)
        query += f" AND occasion IN ('{occasion_str}')"
    else:
        query += f" AND occasion IN ('Daily', 'Office', 'Party')"

    # if 'All' not in occasion:
    #     occasion_type_str = "','".join(occasion)
    #     query += f" AND product_type IN ('{occasion_type_str}')"
        
    return query


if input_query := st.text_input("Enter Query"):
    output_list = input_utterance(input_query)
    st.write(output_list)
    st.write(len(output_list))

    price_range, material, product_type, weight, occasion = filter(output_list)

    query = generate_query((price_range[0], price_range[1]), material, product_type, weight, occasion)

    # Execute the query
    cursor.execute(query)
    results = cursor.fetchall()

    # Display the results
    st.write("Filtered Results:", results)

    # Close the database connection
    conn.close()
