# RentStabilization
Python Scraper and Data for the Property Tax Bills to extract rent stabilized units in NYC

This is an extremely simple and updated version of John Krauss's methodology. 
2020 data in the data folder is the tax complied from Nov 2020 tax records. There are approx 8000 less lots in the dataset in comparison with the [2018 dataset](https://qri.cloud/chriswhong/nyc-rent-stabilized-units-2018). I checked a sample of these lots from 2020 returns and they don't seem to contain rent stabilzed units. 

Repo has 3 codes:
1. Download PDF returns: I used the [multi-unit data](https://data.cityofnewyork.us/Housing-Development/Multiple-Dwelling-Registrations/tesw-yqqr) to reduce the scraping.
2. Read PDF returns
3. Compare the different years. This has simple functions for scrape and read together, if you want to seach for units one by one this is more helpful

