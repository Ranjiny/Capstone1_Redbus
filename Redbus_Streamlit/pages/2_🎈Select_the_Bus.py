#Page 2
#import necessary modules
import streamlit as st
import datetime
from sqlalchemy import create_engine, MetaData, Table, select,func, Column, or_, and_


# Create a connection to the MySQL database
# eg :engine = create_engine('mysql+pymysql://root:12345678@localhost/Capstone')
engine = create_engine('mysql+pymysql://<username>:<password>@<host>/<dbname>') 
connection = engine.connect()

# Define the table and metadata
metadata = MetaData()
table = Table('bus_routes', metadata, autoload=True, autoload_with=engine)

# Query to fetch data for the select box option for routes
query_1 = select([table.c.route_name.distinct()])
options_route=connection.execute(query_1).fetchall()
# Extract distinct values in tuple into a list
select_options_route = [value[0] for value in options_route]

#Select options for starting time
select_options_start_time = [str(datetime.time(hour=h).strftime('%H:%M') )+'-'+str(datetime.time(hour=(h+1)).strftime('%H:%M') ) 
           for h  in range(0, 23)]
select_options_start_time.append('23:00-00:00')

#Select options for Ratings
select_options_Ratings = [str(r-1)+' to '+str(r) for r in range(5,0,-1)]

#Select options for Fare range
select_options_Fare_Range = [str(fare)+' to '+str(fare+100) for fare in range(0,1000,100)]
select_options_Fare_Range.append('Others')

# Create a container for the dropdown boxes
with st.container():
        col1, col2,col3 = st.columns(3)
        option1=col1.selectbox('Select the route',select_options_route,index=None,
                               placeholder='Select route')
        option2=col2.selectbox('Select the Seat Type',('Seater','Sleeper','Others'))
        option3=col3.selectbox('Select the AC Type',('AC','NON AC'))
        col4, col5,col6 = st.columns(3)
        option4=col1.selectbox('Select the Ratings',select_options_Ratings).split()
        option5=col2.selectbox('Select the Starting Time',select_options_start_time).split(':')
        option6=col3.selectbox('Bus Fare Range',select_options_Fare_Range).split(' ')
           
#where clause query conditions
if option2 == 'Seater':
        query_condition_Seater = or_(Column('bustype').like('%Seater%' ),
                                     Column('bustype').like('%SEATER%'))
elif option2 == 'Sleeper':
        query_condition_Seater = or_(Column('bustype').like('%Sleeper%' ),
                                Column('bustype').like('%SLEEPER%'))
else:         
        query_condition_Seater = and_(Column('bustype').notlike('%Seater%' ),
                                     Column('bustype').notlike('%SEATER%'),
                                     Column('bustype').notlike('%Sleeper%' ),
                                      Column('bustype').notlike('%SLEEPER%'))



if option3=='NON AC':
        query_condition_AC = or_(Column('bustype').like('%Non A/C%' ),Column('bustype').like('%Non AC%'),
                              Column('bustype').like('%Non-AC%'),Column('bustype').like('%Non-A/C%'),
                              Column('bustype').like('%NON-A/C%'),Column('bustype').like('%NON AC%' ),
                              Column('bustype').like('%NON A/C%' ),Column('bustype').like('%NON-AC%'))
else: 
        query_condition_AC = and_(Column('bustype').notlike('%Non A/C%' ),Column('bustype').notlike('%Non AC%'),
                              Column('bustype').notlike('%Non-AC%'),Column('bustype').notlike('%Non-A/C%'),
                              Column('bustype').notlike('%NON-A/C%'),Column('bustype').notlike('%NON AC%' ),
                              Column('bustype').notlike('%NON A/C%' ),Column('bustype').notlike('%NON-AC%'))

option4_where1=int(option4[0])
option4_where2=int(option4[-1])


if option6[0] != 'Others':
        option6_where1=int(option6[0])
        option6_where2=int(option6[-1])
        query_condition_fare = Column('price').between(option6_where1,option6_where2)
else:
        query_condition_fare = Column('price') > 1000
           
#Query to extract the data based on the selected conditions

query=select([func.substr(table.c.route_name, 1, func.instr(table.c.route_name, 'to' ) - 1).label('Starting_names'), 
func.substr(table.c.route_name, func.instr(table.c.route_name, 'to') + 3).label('Reaching_names'),
(table.c.busname).label('Names'),(table.c.price).label('Bus_fare'),
(table.c.star_rating).label('Ratings'),(table.c.seats_available).label('Seats'),
(table.c.bustype).label('Bus_type')]).where(table.c.route_name == option1).where(
table.c.star_rating.between(option4_where1,option4_where2)).where(
        query_condition_fare).where(query_condition_AC).where(query_condition_Seater)

# Execute the query and fetch all distinct values
results = connection.execute(query).fetchall()

# Display the distinct values in a Streamlit table
st.dataframe(results)



