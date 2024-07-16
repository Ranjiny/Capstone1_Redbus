# Capstone_Redbus
Webscrape the Redbus website and store data in SQL DB. Streamlit application to view the filtered. 



While executing the .py for streamlit application in the terminal, make sure to install the necessary modules.

pip install streamlit  # This is used to download the streamlit library to create the app

Ensure to keep it up-to-date, if new changes are available. (pip install --upgrade streamlit )

This code uses pymysql to connect to mysql db. Use "pip install PyMySQL" to install it.

Kindly incorporate the appropriate username, db,password , host while creating engine
create_engine('mysql+pymysql://<username>:<password>@<host>/<dbname>') #dialect+driver://username:password@host:port/database

