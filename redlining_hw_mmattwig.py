#
# Name: Melissa Mattwig
# uniquename: mmattwig
#

import requests
import json
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import random as random
from matplotlib.path import Path
import numpy as np
import statistics
import operator


class DetroitDistrict:
    def __init__(self, Coordinates = None, HolcGrade = None, HolcColor = None, name = None, QualitativeDescription = None,
    RandomLat = None, RandomLong = None, MedianIncome = None, CensusTract = None, json = None):
        if (json is None):
            self.Coordinates = Coordinates
            self.HolcGrade = HolcGrade
            self.HolcColor = HolcColor
            self.name = name
            self.QualitativeDescription = QualitativeDescription
            self.RandomLat = RandomLat
            self.RandomLong = RandomLong
            self.MedianIncome = MedianIncome
            self.CensusTract = CensusTract
        
        else:
            self.Coordinates = json["geometry"]['coordinates'][0][0]
            self.HolcGrade = json["properties"]['holc_grade']
            if self.HolcGrade == 'A':
                self.HolcColor = 'darkgreen'
            elif self.HolcGrade == 'B':
                self.HolcColor = 'cornflowerblue'
            elif self.HolcGrade == 'C':
                self.HolcColor = 'gold'
            elif self.HolcGrade == 'D':
                self.HolcColor = 'maroon'
            self.name = json["properties"]['holc_id']
            self.QualitativeDescription = json["properties"]['area_description_data']['8']
            self.RandomLat = RandomLat
            self.RandomLong = RandomLong
            self.MedianIncome = MedianIncome
            self.CensusTract = CensusTract



def redlining_api(data):
    Districts = []
    Districts = [DetroitDistrict(json = x) for x in data['features']]
    return Districts

if __name__ == "__main__":

    ### PART 1

    census_url = 'https://dsl.richmond.edu/panorama/redlining/static/downloads/geojson/MIDetroit1939.geojson'
    RedliningData = json.loads(requests.get(census_url).text)

    ### PART 2 
    Districts  = []
    Districts = redlining_api(RedliningData)
    
    ### PART 3
    fig, ax = plt.subplots()
    for item in Districts: 
        ax.add_patch(
            plt.Polygon(item.Coordinates, facecolor = item.HolcColor, edgecolor = 'black'))
        ax.autoscale()
        plt.rcParams["figure.figsize"] = (15,15)
    plt.show()

### PART 4
random.seed(17)

xgrid = np.arange(-83.5,-82.8,.004)
ygrid = np.arange(42.1, 42.6, .004)
xmesh, ymesh = np.meshgrid(xgrid,ygrid)

points = np.vstack((xmesh.flatten(),ymesh.flatten())).T

for j in Districts:
    p = Path(j.Coordinates)
    grid = p.contains_points(points)
    #print(j," : ", points[random.choice(np.where(grid)[0])])
    point = points[random.choice(np.where(grid)[0])]
    j.RandomLong = point[0]
    j.RandomLat = point[1]


### PART 5
census_url_first = 'https://geo.fcc.gov/api/census/block/find?latitude='
census_url_last = '&censusYear=2020&showall=false&format=json'
for item in Districts:
    latitude = str(item.RandomLat)
    longitude = str(item.RandomLong)
    census_json = requests.get(census_url_first + latitude + '&longitude=' + longitude + census_url_last)
    census = census_json.json()
    item.CensusTract = census['Block']["FIPS"][5:11]


### PART 6
census_key = '9c547db97001307d8ec933426da2e84ea5b47fc5'
acs_url = 'https://api.census.gov/data/2018/acs/acs5?get=NAME,B19013_001E&for=tract:*&in=state:26&key='

response = requests.get(acs_url + census_key)
census_income = response.json()

tract_to_income_dict = {}
for item in census_income:
    tract_to_income_dict[item[-1]] = item[1]

for district in Districts:
    try:
        district.MedianIncome = tract_to_income_dict[district.CensusTract]
    except:
        pass

### PART 7
district_list = []
for district in Districts:
    district_dict = {
        "Coordinates": district.Coordinates,
        "Holc_grade": district.HolcGrade,
        "Holc_color": district.HolcColor,
        "Name": district.name,
        "Qualitative_description": district.QualitativeDescription,
        "Census_tract": district.CensusTract,
        "Latitude": district.RandomLat,
        "Longitude": district.RandomLong,
        "Median_income": district.MedianIncome
    }
    district_list.append(district_dict)
    
final_obj = {'Districts':district_list}
out_file = open("myfile.json", "w")
json.dump(final_obj, out_file)
out_file.close()


### PART 8
A_list = [int(x.MedianIncome) for x in Districts if x.HolcGrade == "A" if x.MedianIncome != None]
#print(A_list)
B_list = [int(x.MedianIncome) for x in Districts if x.HolcGrade == "B" if x.MedianIncome != None]
#print(B_list)
C_list = [int(x.MedianIncome) for x in Districts if x.HolcGrade == "C" if x.MedianIncome != None]
#print(C_list)
D_list = [int(x.MedianIncome) for x in Districts if x.HolcGrade == "D" if x.MedianIncome != None]
#print(D_list)

A_mean_income = sum(A_list) / len(A_list)
A_median_income = statistics.median(A_list)
print(A_mean_income)
print(A_median_income)
B_mean_income = sum(B_list) / len(B_list)
print(B_mean_income)
B_median_income = statistics.median(B_list)
print(B_median_income)
C_mean_income = sum(C_list) / len(C_list)
print(C_mean_income)
C_median_income = statistics.median(C_list)
print(C_median_income)
D_mean_income = sum(D_list) / len(D_list)
print(D_mean_income)
D_median_income = statistics.median(D_list)
print(D_median_income)


### PART 9
A_word_count_dict = {}
B_word_count_dict = {}
C_word_count_dict = {}
D_word_count_dict = {}
common_words = ["the", "an", "a", 'and', "if", "but", "is", "isn't", "isnt", "will", "are",
                "of", "there", "for", "at", "on", "may", "which", "that", "in", "not", "to",
                "this", "from", "have", "*See", "area", "Area", "with", "The", "A"]

for district in Districts:
    if district.HolcGrade == "A":
        A_word_list_all = district.QualitativeDescription.split()
        A_word_list = [x for x in A_word_list_all if (x not in common_words)]
        for word in A_word_list:
            if word in A_word_count_dict.keys():
                A_word_count_dict[word] += 1
            else:
                A_word_count_dict[word] = 1
    elif district.HolcGrade == "B":
        B_word_list_all = district.QualitativeDescription.split()
        B_word_list = [x for x in B_word_list_all if (x not in common_words)]
        for word in B_word_list:
            if word in B_word_count_dict.keys():
                B_word_count_dict[word] += 1
            else:
                B_word_count_dict[word] = 1
    elif district.HolcGrade == "C":
        C_word_list_all = district.QualitativeDescription.split()
        C_word_list = [x for x in C_word_list_all if (x not in common_words)]
        for word in C_word_list:
            if word in C_word_count_dict.keys():
                C_word_count_dict[word] += 1
            else:
                C_word_count_dict[word] = 1
    elif district.HolcGrade == "D":
        D_word_list_all = district.QualitativeDescription.split()
        D_word_list = [x for x in D_word_list_all if (x not in common_words)]
        for word in D_word_list:
            if word in D_word_count_dict.keys():
                D_word_count_dict[word] += 1
            else:
                D_word_count_dict[word] = 1

A_most_common_word = max(A_word_count_dict.items(), key = operator.itemgetter(1))[0]
B_most_common_word = max(B_word_count_dict.items(), key = operator.itemgetter(1))[0]
C_most_common_word = max(C_word_count_dict.items(), key = operator.itemgetter(1))[0]
D_most_common_word = max(D_word_count_dict.items(), key = operator.itemgetter(1))[0]
print("A most common word: " + A_most_common_word)
print("B most common word: " + B_most_common_word)
print("C most common word: " + C_most_common_word)
print("D most common word: " + D_most_common_word)

