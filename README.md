# Project Overview
This project delves into a comprehensive NASA dataset spanning meteorite landings worldwide from 861 to 2013. 
Its aim is to uncover insights such as the correlation between meteorite classes and weight, the geographical patterns of meteorite landings, and the annual count of reported meteorite falls. 
Leveraging the findings from our exploratory analysis, we have crafted user-friendly visualizations to effectively showcase the data.

# Instructions:
  - Create a database in PostgreSQL called 'meteorite'
  - Using the table schema in the meteorites_schema.sql file, create a table within the 'meteorite' database
  - Import the 'clean_meteorite_data.csv' into the newly created table
  - Within the folder, create a config.py file containing the username and password from your PostgreSQL client
  - Open the Sqlalchemy_meteorite.py file and run it in the terminal to locally run Flask API
  - Open the 'index01_21' file in an internet browser while the API is running to ensure the links under the 'Plots' category will 

# Ethical Considerations
In choosing our dataset, ethical considerations were relatively low as the data did not involve any information related to individuals or potentially sensitive details. 
Nevertheless, we made an effort to consider the dataset's license, although it was unspecified. 
A comparative examination of NASA datasets with similar information revealed that the majority were accessible within the public domain.

# References: 
- References for the data source(s):
    - NASA dataset: https://data.nasa.gov/Space-Science/Meteorite-Landings/gh4g-9sfh/about_data
 - References for any code used that is not your own:
    - https://www.kaggle.com/code/godragons6/nasa-meteorites-a-comprehensive-overview/notebook
    - https://www.youtube.com/watch?v=9ZB1EgaJnBU&t=1156s
