# About The Project
This project delves into a comprehensive NASA dataset spanning meteorite landings worldwide from  to 2013. 
Its aim is to uncover insights such as the correlation between meteorite classes and weight, the geographical patterns of meteorite landings, and the annual count of reported meteorite falls. 
Leveraging the findings from our exploratory analysis, we have crafted user-friendly visualizations to effectively showcase the data.


# Required Modules:
Install the following modules prior to running:
  - Pandas
  - SQL Alchemy
  - Flask
  - NumPy
  - Plotly
  - SKLearn
  - GeoPandas

# How To Run:
  1. Install the required modules listed above
  2. Run the Jupyter Notebook file to obtain the clean data filed
  3. Create a database in PostgreSQL called 'meteorite'
  4. Using the table schema in the meteorites_schema.sql file, create a table within the 'meteorite' database
  5. Import the 'clean_meteorite_data.csv' into the newly created table
  6. Within the folder, create a config.py file containing the username and password from your PostgreSQL client
  7. Open the Sqlalchemy_meteorite.py file and run it in the terminal to locally run Flask API
  8. With the API running, open the 'homepage.html' file in an internet browser and enjoy!

# Ethical Considerations
In choosing our dataset, ethical considerations were relatively low as the data did not involve any information related to individuals or potentially sensitive details. 
Nevertheless, we made an effort to consider the dataset's license, although it was unspecified. 
A comparative examination of NASA datasets with similar information revealed that the majority were accessible within the public domain.

# References: 
- Data source:
    - NASA dataset: https://data.nasa.gov/Space-Science/Meteorite-Landings/gh4g-9sfh/about_data
 - References for any code used that was not our own:
    - https://www.kaggle.com/code/godragons6/nasa-meteorites-a-comprehensive-overview/notebook
    - https://www.youtube.com/watch?v=9ZB1EgaJnBU&t=1156s

# Notes:
The 'class_material' folder is strictly content from the development and presentation process of this project needed for grading purposes only. Feel free to take a look if you'd like!
