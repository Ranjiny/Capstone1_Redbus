# Capstone_Redbus

Aim:Webscrape the Redbus website and store data in SQL DB. Streamlit application to view the filtered. 

Elements used in the project:
* Browser- Chrome
* DB- Mysql
* Webscraping method- Selenium
* APP creation- Streamlit


-->Selenium automation is used to extract data from the redbus website for government and private bus details for all the links for the government state transports.
Keep in mind to curate the webdriver waits/implicit waits.

--> The extracted data is stored in the db for quick querying purpose and multi-app use.
Include appropriate username, db,password , host while connecting to mysql.

While executing the .py for streamlit application in the terminal, make sure to install the necessary modules.

-->pip install streamlit  # This is used to download the streamlit library to create the app

Ensure to keep it up-to-date, if new changes are available. (pip install --upgrade streamlit )

This code uses pymysql to connect to mysql db. Use "pip install PyMySQL" to install it.

Kindly incorporate the appropriate username, db,password , host while creating engine
create_engine('mysql+pymysql://<username>:<password>@<host>/<dbname>') #dialect+driver://username:password@host:port/database

