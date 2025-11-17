**User Guide to the Hotel DBMS**

**DEPENDENCIES:**
- Python3
- Downloading python should already come with tkinter preinstalled, however, if when running you encounter problems with tkinter, run in the terminal: pip install tkinter.

**HOW TO RUN:** Following these steps will open the GUI and you are now able to use and interact with the app.

Option 1: If you’re using a terminal type (ensure you’re in the directory of where “menuTest.py” is residing):

python3 menuTest.py OR py menuTest.py

Option 2: If you’re using an IDE:

Run the Python file menuTest.py as you would any other python file


**FEATURES:**

Create Predefined Tables
- To create a predefined table, click on the button labeled “Create Tables”, this will automatically create tables which are required for the hotel DBMS.

Create Custom User Defined Tables
- To create custom tables, click on the button labeled “Add Custom Table”, this will open a menu allowing you to create a table for the hotel DBMS. Simply enter the table name and the appropriate SQL code for your table and click “Create Table”.

Delete All Predefined Tables
- To delete a table, click on the button labeled “Drop Tables”, this will only drop all of the tables created by the “Create Predefined Tables” feature.
- Note: The tables must be created for this feature to work.

Add Records to any table
- To add a record to a table, click on the button labeled “Add Record Table”, this will open a menu, allowing you to add a record to a table. Simply select the table you wish to add a record for using the provided drop down menu and in the textbox enter your record.
- Note: The format when entering a record must be values separated by commas with no spaces in between. The order you input your values in will be interpreted as shown by the schema of the table in the menu (top to bottom).
- Note: The tables must be created for this feature to work.

See all information in all predefined Tables
- To see all data in all tables, click on the button labeled “See All Tables”, this will display all data in every table currently in the hotel DBMS (predefined and user defined).
- Note: The tables must be created and populated for this feature to work.

Clear Results
- To clear any results that have been displayed, click on the “Clear Results” button, this will remove any data currently being displayed in the main menu. This does not erase any data.

Check predefined Queries
- To view the predefined queries of the hotel DBMS, click on the “Run Queries” button, this will display all queries that have been predefined in the hotel DBMS.
- Note: The predefined tables must be created and populated for this feature to work.

Populate Tables with predefined values
- To populate the predefined tables with predefined values, click the “Populate Tables” button, this will populate the predefined tables.
- Note: The predefined tables must be created for this feature to work.

Delete a specific Table
- To delete a specific table, click on the “Delete Table” button, this will open a menu to allow the user to drop a table of their choice. Simply select your table from the provided drop down menu and click the “Delete Table” button.
- Note: The tables must be created for this feature to work.

Delete a Record to a Table
- To delete a record from a specific table, click on the “Delete Record Table” button, this will open a menu, allowing the user to delete a record from a table of their choice. Simply select a table from the provided drop down menu and enter the primary key of the record in the textbox (if the primary key is a composite key see the note below), and click on the “Delete Record” button.
- Note: The format when entering a composite key must be values separated by commas with no spaces in between. The order you input your values in will be interpreted as shown by the schema of the table in the menu (top to bottom).
- Note: The tables must be created and populated for this feature to work.

Update a Record to a Table
- To update a record from a specific table, click on the “Update Record Table” button, this will open a menu, allowing the user to update a record from a table of their choice. Simply select a table from the provided drop down menu and enter the updated record in the textbox, and click on the “Update Record” button.
- Note: The format when entering a record must be values separated by commas with no spaces in between. The order you input your values in will be interpreted as shown by the schema of the table in the menu (top to bottom).
- Note: The tables must be created, populated, and the updated record must have a primary key already existing in the table prior to the update for this feature to work.

Search for a specific Record in a Table
- To search for a record from a specific table, click on the “Search Record Table” button, this will open a menu, allowing the user to search for a record from a table of their choice. Simply select a table from the provided drop down menu and enter the primary key of the record you want to search for in the textbox (if the primary key is a composite key see the note below), and click on the “Search Record” button. Upon clicking the button, in the main menu the record will be displayed.
- Note: The format when entering a composite key must be values separated by commas with no spaces in between. The order you input your values in will be interpreted as shown by the schema of the table in the menu (top to bottom).
- Note: The tables must be created and populated for this feature to work.

Exit the app
- To exit the application, click on the “Exit” button, this will close all menus (including the main menu).

