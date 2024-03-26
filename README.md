# About The Project
This project delves into a comprehensive NASA dataset spanning meteorite landings worldwide from 1980 to 2013. 
Its aim is to uncover insights such as the correlation between meteorite classes and weight, the geographical patterns of meteorite landings, and the annual count of reported meteorite falls. 
Leveraging the findings from our exploratory analysis, we have crafted user-friendly visualizations to effectively showcase the data. We hope you enjoy the interactive and accessible webpage we've made to learn more about meteorite landings!


## Required Modules:
Install the following modules prior to running:
  - Pandas
  - SQL Alchemy
  - Flask
  - NumPy
  - Plotly
  - SKLearn
  - GeoPandas
  - Leaflet

## How To Run:
  1. Install the required modules listed above
  2. Clone the repo using the following code:
     - ```
       git clone https://github.com/eholtgrieve/Meteorite_Landing_Analysis_Project.git
       ```
  4. Run the 'meteorite_landings_project' Jupyter Notebook file to obtain the clean data file
  5. Create a database in PostgreSQL called 'meteorite'
  6. Using the table schema in the meteorites_schema.sql file, create a table within the 'meteorite' database
  7. Import the 'clean_meteorite_data.csv' into the newly created table
  8. Within the folder, create a config.py file containing the username and password from your PostgreSQL client
  9. Open the Sqlalchemy_meteorite.py file and run it in the terminal to locally run Flask API
  10. With the API running, open the 'homepage.html' file in an internet browser and enjoy!

#### Ethical Considerations
In choosing our dataset, ethical considerations were relatively low as the data did not involve any information related to individuals or potentially sensitive details. 
Nevertheless, we made an effort to consider the dataset's license, although it was unspecified. 
A comparative examination of NASA datasets with similar information revealed that the majority were accessible within the public domain.

#### References: 
- Data source:
    - NASA dataset: https://data.nasa.gov/Space-Science/Meteorite-Landings/gh4g-9sfh/about_data
 - References for any code used that was not our own:
    - https://www.kaggle.com/code/godragons6/nasa-meteorites-a-comprehensive-overview/notebook
    - https://www.youtube.com/watch?v=9ZB1EgaJnBU&t=1156s
### Authors:
- Emma Holtgrieve: [Github](github.com/eholtgrieve)
- Shruti Deshpande: [Github](github.com/dshruti29)
- Lyudmila Devlysh: [Github](https://github.com/ldevlysh314)
### Notes:
The 'class_material' folder is strictly content from the development and presentation process of this project needed for grading purposes only. Feel free to take a look if you'd like!
