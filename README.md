# Data-Engineering-project
In this folder i created data engineering project to extract, tranform and load the data. Implement webscraping and use APIs to extract data with Python.
working with banks exchange rate data, Movies data, and Country GDP to perform ETL to the data. 

extract_tranform_load(ETL) 

movies_etl: the process of analyzing the HTML code of a web page and how to extract the required information from it using web scraping in Python.
Iterate over the contents of the variable rows.
Check for the loop counter to restrict to 50 entries.
Extract all the td data objects in the row and save them to col.
Check if the length of col is 0, that is, if there is no data in a current row. This is important since, many timesm there are merged rows that are not apparent in the web page appearance.
Create a dictionary data_dict with the keys same as the columns of the dataframe created for recording the output earlier and corresponding values from the first three headers of data.
Convert the dictionary to a dataframe and concatenate it with the existing one. This way, the data keeps getting appended to the dataframe with every iteration of the loop.
Increment the loop counter.
Once the counter hits 50, stop iterating over rows and break the loop

store the required data in a database, you first need to initialize a connection to the database, save the dataframe as a table, and then close the connection.

SQL_lite: Consider a dataset of employee records that is available with an HR team in a CSV file. create the database called STAFF and load the contents of the CSV file as a table called INSTRUCTORS
To create a table in the database, first need to have the attributes of the required table. Attributes are columns of the table.
Now, to read the CSV using Pandas,  use the read_csv() function. Since this CSV does not contain headers, you can use the keys of the attribute_dict dictionary as a list to assign headers to the data. For this, add the commands below to db_code.py.
The pandas library provides easy loading of its dataframes directly to the database.Use the to_sql() method of the dataframe object.
However, while load the data for creating the table,use to_sql() function uses the argument if_exists. The possible usage of if_exists is tabulate.
Now that the data is uploaded to the table in the database, anyone with access to the database can retrieve this data by executing SQL queries.
Some basic SQL queries to test this data are SELECT queries for viewing data, and COUNT query to count the number of entries.
SQL queries can be executed on the data using the read_sql function in pandas.

GDP_etl: creating an automated script that can extract the list of all countries in order of their GDPs in billion USDs (rounded to 2 decimal places), as logged by the International Monetary Fund (IMF). Since IMF releases this evaluation twice a year, this code will be used by the organization to extract the information as it is updated.
The required information needs to be made accessible as a CSV file Countries_by_GDP.csv as well as a table Countries_by_GDP in a database file World_Economies.db with attributes Country and GDP_USD_billion.
To demonstrate the success of this code by running a query on the database table to display only the entries with more than a 100 billion USD economy. Also log in a file with the entire process of execution named etl_project_log.txt.

Write a data extraction function to retrieve the relevant information from the required URL.
Transform the available GDP information into 'Billion USD' from 'Million USD'.
Load the transformed information to the required CSV file and as a database file.
Run the required query on the database.
Log the progress of the code with appropriate timestamps.