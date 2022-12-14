import streamlit

streamlit.title('My prents New Healthy Diner')

streamlit.header('Breakfast Favourites')
streamlit.text('๐ฅฃ Omega 3 & Blueberry Oatmeal')
streamlit.text('๐ฅ Kale, Spinach & Rocket Smoothie')
streamlit.text('๐Hard-Boiled Free-Range Egg')
streamlit.text('๐ฅ๐Avacado Toast')

streamlit.header('๐๐ฅญ Build Your Own Fruit Smoothie ๐ฅ๐')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

# Display the table on the page.

streamlit.dataframe(my_fruit_list)

streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

add_my_fruit = streamlit.text_input('What fruit would you like add?','jackfruit')
streamlit.write('Thanks for having ', add_my_fruit)


import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ fruit_choice)


# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)

import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows) 

streamlit.write('Thanks for adding ', add_my_fruit)

my_cur.execute(" insert into fruit_load_list values ('from streamlit')")



