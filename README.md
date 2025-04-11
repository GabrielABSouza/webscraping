# webscraping
This is a webscraping project which includes collecting data from a website, transforin the data into a SQLite database and turning it into some useful dashboards

To guide you through the project here are some tips:

- start by the extraction file (src -> extraction -> spiders -> notebook.py) , which includes all the code needed to access the website and collect the data needed to solve the business problem
- now we move to the transform file (src -> transform -> main.py), where we use mainly pandas to treat this json data, make it more readable and connect to a SQLite database
- finally we go to the dashboard file (src -> dashboard -> app.py), this code includes connection to the sqlite data base and some streamlit commands in order to create the needed dashboards to analyze the required KPIs
