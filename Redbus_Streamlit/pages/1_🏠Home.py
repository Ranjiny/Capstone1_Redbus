import streamlit as st
from sqlalchemy import create_engine, MetaData, Table, select

st.write("""
         # Welcome to the bus selection app #
         #
         You can book your tickets using the following links
         
         *To check the availability of buses use '🎈Select_the_Bus' page* """)

# Create a connection to the MySQL database
engine = create_engine('mysql+pymysql://root:12345678@localhost/Capstone')
connection = engine.connect()

# Define the table and metadata
metadata = MetaData()
table = Table('route_details', metadata, autoload=True, autoload_with=engine)

# Select distinct values from two columns
query = select([table.c.route_name.distinct(), table.c.route_link])

# Execute the query and fetch all distinct values
results = connection.execute(query).fetchall()

# Display the distinct values in a Streamlit table
st.dataframe(results)