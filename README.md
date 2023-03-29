# Redlining in Detroit for SI 507 (Intermediate Python) at the University of Michigan
A python project that uses a redlining dataset (JSON) from Detroit 1936 to create a map based on the district grades. It will also use census data to to find current median income data to determine the redlining legacy in Detroit

## Table of contents
* [General info](#general-info)
* [Skills gained](#skills-gained)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
This project reads Detroit redlining data from 1936 as a JSON from the University of Richmond to create a DetroitDistricts class. It takes the district grades (between A and D), assigns them a color, then plots the map using matplotlib. Then, the program will randomly pick a coorindate from each of the 238 districts and use an API call to the 2010 Census data to find the median household income of that district. It will then create a JSON cache of this information to avoid over using the Census API calls (due to there being a daily limit). Finally, the program will use a list comprehension to find the ten most commons descriptive words used for each district grade.

## Skills gained
* Reading in a JSON from a URL, creating a JSON cache
* Creating a map using matplotlib
* Use of classes, dictionaries, and list comprehensions
* Using an API call to retrieve census data

## Technologies
Project is created with:
* Visual Studio Code version 1.76.2
* Python Version 3.11
	
## Setup
To run this project:

```
$ 
$ 
```
