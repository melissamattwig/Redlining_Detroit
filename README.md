# Redlining in Detroit for SI 507 (Intermediate Python) at the University of Michigan
A python project that uses a redlining dataset from Detroit in 1936 to create a map based on the district grades. It will also use census data to to find current median income data to determine the redlining legacy in Detroit.

## Table of contents
* [General info](#general-info)
* [Skills gained](#skills-gained)
* [Technologies](#technologies)
* [Expected Outputs](#expectedoutputs)
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

## Expected Outputs
You should have a map that ressembles this:

![image](https://user-images.githubusercontent.com/60607975/228695296-5b17a3a7-c29b-49ae-b5f8-f3690e06d96b.png)

And the following outputs:

79754.14285714286 - Mean income for district grade A

73067.5 - Median income for district grade A

63827.55263157895 - Mean income for district grade B

65259.0 - Median income for district grade B

41673.64150943396 - Mean income for district grade C

36208.0 - Median income for district grade C

31614.979591836734 - Mean income for district grade D

28786 - Median income for district grade D

A most common word: high

B most common word: houses

C most common word: explanation

D most common word: sheet

	
## Setup
To run this project:

Make sure that the JSON Census file is in the same folder as the .py file

```
$ cd ../redlining_detroit
$ python3 redlining_detroit.py
```
