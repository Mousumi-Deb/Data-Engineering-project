import sqlite3
import pandas as pd
conn = sqlite3.connect('STAFF.db')

# create table
table_name = 'INSTRUCTOR'
attribute_list = ['ID', 'FNAME', 'LNAME', 'CITY', 'CCODE']

# now read the csv file
file_path = 'C:/Users/E7440/OneDrive/Desktop/data_engineering/sql_lite/INSTRUCTOR.csv'
df = pd.read_csv(file_path, names=attribute_list)

# load the data to a table
df.to_sql(table_name, conn, if_exists='replace', index=False)
print('Table is ready')

# view all the data in the table
query_statement = f"SELECT * FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

# view only FNAME column of data
query_statement = f"SELECT FNAME FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

# view the total num of entries
query_statement = f"SELECT COUNT(*) FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

# appending dome data to the table
data_dict = {'ID': [100],
             'FNAME': ['John'],
             'LNAME': ['Doe'],
             'CITY': ['Paris'],
             'CCODE': ['FR']}
data_append = pd.DataFrame(data_dict)

data_append.to_sql(table_name, conn, if_exists='append', index=False)
print('Data appended successfully')

# create a 2nd table in the same database
table2 = 'Department'
attribute_list = ['DEPT_ID', 'DEP_NAME', 'MANAGER_ID', 'LOC_ID']

# read the csv file
file_path = 'C:/Users/E7440/OneDrive/Desktop/data_engineering/sql_lite/Departments.csv'
df = pd.read_csv(file_path, names=attribute_list)

df.to_sql(table2, conn, if_exists='replace', index=False)
print('Table is ready')

# view all the data in the table
query1 = f"SELECT * FROM {table2}"
query_output = pd.read_sql(query1, conn)
print(query1)
print(query_output)

# view only DEP_name column of data
query2 = f"SELECT DEP_NAME FROM {table2}"
query_output = pd.read_sql(query2, conn)
print(query2)
print(query_output)

# view the total num of entries
query3 = f"SELECT COUNT(*) FROM {table2}"
query_output = pd.read_sql(query3, conn)
print(query3)
print(query_output)

# appending dome data to the table
data_dict = {'DEPT_ID': [9],
             'DEP_NAME': ['Quality Assurance'],
             'MANAGER_ID': [30010],
             'LOC_ID': ['L0010']}
data_append = pd.DataFrame(data_dict)

data_append.to_sql(table2, conn, if_exists='append', index=False)
print('Data appended successfully')

conn.commit()
conn.close()
