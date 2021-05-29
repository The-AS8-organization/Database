# Importing some modules and setting up a few properties
import sys
import os
from matplotlib import pyplot as plt
import numpy as np
import csv
from collections import Counter
sys.path.append(os.getcwd())
os.environ["DJANGO_SETTINGS_MODULE"] = "tsdb_app.settings"

import django
django.setup()
from core import backup




def main():
    backup.main()
    organization_location()
    organization_is_club()
    organization_popularity()
    organization_is_active()
    organization_initiatives()
    organization_resources()
    consumer_age()
    consumer_location()
    consumer_profession()
    consumer_institution()


def height_calc(num):
    if num <= 2:
        return 2
    
    elif num <= 5:
        return 4

    elif num <= 10:
        return 7
    
    elif num <= 20:
        return 10

    else:
        return 15


def organization_location():
    with open("backupfiles/OrganizationBUF.csv", "r") as rfile:
        my_reader = csv.reader(rfile)
        location_dict = Counter()

        next(my_reader)
        for line in my_reader:
            location_dict.update([line[4]])   

        temp_tuple_list = sorted(dict(location_dict).items(), key=lambda x:x[1])
        x_value = []
        y_value = []
        for tup in temp_tuple_list:
            x_value.append(tup[0])
            y_value.append(tup[1])
        height_num = len(x_value)

        plt.style.use("seaborn")
        plt.figure(figsize=(10,height_calc(height_num)))
        plt.barh(x_value, y_value , color="#0AB210")

        plt.title("ORGANIZATIONS' LOCATION")
        plt.xlabel("Number Of Organizations")
        plt.ylabel("Location")

        plt.tight_layout()
        plt.savefig("static/images/plots/plot1.png")


def organization_is_club():
    with open("backupfiles/OrganizationBUF.csv", "r") as rfile:
        my_reader = csv.reader(rfile)
        is_club_dict = Counter()

        next(my_reader)
        for line in my_reader:
            is_club_dict.update([line[5]])  

        temp_tuple_list = sorted(dict(is_club_dict).items(), key=lambda x:x[1])
        x_value = []
        y_value = []
        for tup in temp_tuple_list:
            x_value.append(tup[0])
            y_value.append(tup[1])

        colors = ["#0e8f13", "#0AB210"]
        plt.style.use("seaborn")
        plt.figure(figsize=(10,4))
        _, _, autotexts = plt.pie(y_value, labels=x_value , colors=colors, wedgeprops={"edgecolor":"white"}, autopct="%1.1f%%")
        for autotext in autotexts:
            autotext.set_color('white')

        plt.title("ORGANIZATIONS' IS_CLUB")
        plt.tight_layout()
        plt.savefig("static/images/plots/plot2.png")


def organization_popularity():
    with open("backupfiles/OrganizationBUF.csv", "r") as rfile:
        my_reader = csv.reader(rfile)
        popularity_dict = Counter()

        next(my_reader)
        for line in my_reader:
            popularity_dict.update([line[7]])  

        temp_tuple_list = sorted(dict(popularity_dict).items(), key=lambda x:x[1])
        x_value = []
        y_value = []
        for tup in temp_tuple_list:
            x_value.append(tup[0])
            y_value.append(tup[1])

        colors = ["#0e8f13", "#0AB210", "#0AB210"]
        plt.style.use("seaborn")
        plt.figure(figsize=(10,4))
        _, _, autotexts = plt.pie(y_value, labels=x_value , colors=colors, wedgeprops={"edgecolor":"white"}, autopct="%1.1f%%")
        for autotext in autotexts:
            autotext.set_color('white')

        plt.title("ORGANIZATIONS' POPULARITY")
        plt.tight_layout()
        plt.savefig("static/images/plots/plot3.png")


def organization_is_active():
    with open("backupfiles/OrganizationBUF.csv", "r") as rfile:
        my_reader = csv.reader(rfile)
        is_active_dict = Counter()

        next(my_reader)
        for line in my_reader:
            is_active_dict.update([line[8]])  

        temp_tuple_list = sorted(dict(is_active_dict).items(), key=lambda x:x[1])
        x_value = []
        y_value = []
        for tup in temp_tuple_list:
            x_value.append(tup[0])
            y_value.append(tup[1])

        colors = ["#0e8f13", "#0AB210"]
        plt.style.use("seaborn")
        plt.figure(figsize=(10,4))
        _, _, autotexts = plt.pie(y_value, labels=x_value , colors=colors, wedgeprops={"edgecolor":"white"}, autopct="%1.1f%%")
        for autotext in autotexts:
            autotext.set_color('white')

        plt.title("ORGANIZATIONS' IS_ACTIVE")
        plt.tight_layout()
        plt.savefig("static/images/plots/plot4.png")


def organization_initiatives():
    with open("backupfiles/InitiativeBUF.csv", "r") as rfile:
        my_reader = csv.reader(rfile)
        org_dict = Counter()

        next(my_reader)
        for line in my_reader:
            org_dict.update([line[4]])   

        temp_tuple_list = sorted(dict(org_dict).items(), key=lambda x:x[1])
        x_value = []
        y_value = []
        for tup in temp_tuple_list:
            if tup[0] == "":
                x_value.append("Others")
            else:
                x_value.append(tup[0])
            y_value.append(tup[1])
        height_num = len(x_value)

        plt.style.use("seaborn")
        plt.figure(figsize=(10,height_calc(height_num)))
        plt.barh(x_value, y_value , color="#0AB210")

        plt.title("ORGANIZATIONS' INITIATIVES")
        plt.xlabel("Number Of Initiatives")
        plt.ylabel("Organization")

        plt.tight_layout()
        plt.savefig("static/images/plots/plot5.png")


def organization_resources():
    with open("backupfiles/ResourceBUF.csv", "r") as rfile:
        my_reader = csv.reader(rfile)
        org_dict = Counter()

        next(my_reader)
        for line in my_reader:
            org_dict.update([line[5]])   

        temp_tuple_list = sorted(dict(org_dict).items(), key=lambda x:x[1])
        x_value = []
        y_value = []
        for tup in temp_tuple_list:
            if tup[0] == "":
                x_value.append("Others")
            else:
                x_value.append(tup[0])
            y_value.append(tup[1])
        height_num = len(x_value)

        plt.style.use("seaborn")
        plt.figure(figsize=(10,height_calc(height_num)))
        plt.barh(x_value, y_value , color="#0AB210")

        plt.title("ORGANIZATIONS' RESOURCES")
        plt.xlabel("Number Of Resources")
        plt.ylabel("Organization")

        plt.tight_layout()
        plt.savefig("static/images/plots/plot6.png")


def consumer_location():
    with open("backupfiles/ConsumerBUF.csv", "r") as rfile:
        my_reader = csv.reader(rfile)
        location_dict = Counter()

        next(my_reader)
        for line in my_reader:
            location_dict.update([line[4]])   

        temp_tuple_list = sorted(dict(location_dict).items(), key=lambda x:x[1])
        x_value = []
        y_value = []
        for tup in temp_tuple_list:
            x_value.append(tup[0])
            y_value.append(tup[1])
        height_num = len(x_value)

        plt.style.use("seaborn")
        plt.figure(figsize=(10,height_calc(height_num)))
        plt.barh(x_value, y_value , color="#0AB210")

        plt.title("CONSUMERS' LOCATION")
        plt.xlabel("Number Of Consumers")
        plt.ylabel("Location")

        plt.tight_layout()
        plt.savefig("static/images/plots/plot7.png")


def consumer_age():
    with open("backupfiles/ConsumerBUF.csv", "r") as rfile:
        my_reader = csv.reader(rfile)
        age_list = []

        next(my_reader)
        for line in my_reader:
            age = int(line[3])
            age_list.append(age)  

        lowest = min(age_list)
        highest = max(age_list)
        bins = [0]

        current = lowest
        while current <= highest:
            bins.append(current)
            current += 5
        bins.append(current)

        plt.style.use("seaborn")
        plt.figure(figsize=(10, 6))
        plt.hist(age_list, bins=bins, color="#0AB210", edgecolor="#ffffff")

        plt.title("CONSUMERS' AGE")
        plt.xlabel("Age")
        plt.ylabel("Number of Consumers")

        plt.tight_layout()
        plt.savefig("static/images/plots/plot8.png")


def consumer_profession():
    with open("backupfiles/ConsumerBUF.csv", "r") as rfile:
        my_reader = csv.reader(rfile)
        profession_dict = Counter()

        next(my_reader)
        for line in my_reader:
            profession_dict.update([line[4]])   

        temp_tuple_list = sorted(dict(profession_dict).items(), key=lambda x:x[1])
        x_value = []
        y_value = []
        for tup in temp_tuple_list:
            x_value.append(tup[0])
            y_value.append(tup[1])
        height_num = len(x_value)

        plt.style.use("seaborn")
        plt.figure(figsize=(10,height_calc(height_num)))
        plt.barh(x_value, y_value , color="#0AB210")

        plt.title("CONSUMERS' PROFESSION")
        plt.xlabel("Number Of Consumers")
        plt.ylabel("Professsion")

        plt.tight_layout()
        plt.savefig("static/images/plots/plot9.png")


def consumer_institution():
    with open("backupfiles/ConsumerBUF.csv", "r") as rfile:
        my_reader = csv.reader(rfile)
        institution_dict = Counter()

        next(my_reader)
        for line in my_reader:
            institution_dict.update([line[4]])   

        temp_tuple_list = sorted(dict(institution_dict).items(), key=lambda x:x[1])
        x_value = []
        y_value = []
        for tup in temp_tuple_list:
            x_value.append(tup[0])
            y_value.append(tup[1])
        height_num = len(x_value)

        plt.style.use("seaborn")
        plt.figure(figsize=(10,height_calc(height_num)))
        plt.barh(x_value, y_value , color="#0AB210")

        plt.title("CONSUMERS' INSTITUTION")
        plt.xlabel("Number Of Consumers")
        plt.ylabel("Institution")

        plt.tight_layout()
        plt.savefig("static/images/plots/plot10.png")