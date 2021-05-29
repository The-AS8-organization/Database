# Importing some modules and setting up a few properties
import sys
import os
import csv
from zipfile import ZipFile
sys.path.append(os.getcwd())
os.environ["DJANGO_SETTINGS_MODULE"] = "tsdb_app.settings"

import django
django.setup()

from core.models import Tag, Organization, Initiative, Resource, Consumer



# Generating BackUp Files (BUF) and zipping them
def main():
    print("Process Started")
    print("................................\n")
    TagBackUp()
    OrganizationBackUp()
    InitiativeBackUp()
    ResourceBackUp()
    ConsumerBackUp()
    Zipper()
    print("\n................................")
    print("Process successfully completed")



def TagBackUp():
    with open("backupfiles/TagBUF.csv", "w", newline="") as wfile:
        my_writer=csv.writer(wfile)
        my_writer.writerow(["value"])

        if len(Tag.objects.all()) != 0:
            for tag in Tag.objects.all():
                my_writer.writerow([tag.value])
            print("Backed Up Tag table")



def OrganizationBackUp():
    with open("backupfiles/OrganizationBUF.csv", "w", newline="") as wfile:
        my_writer=csv.writer(wfile)
        my_writer.writerow(["name", "email", "site", "location", "is_club", "institution", "popularity", "is_active", "related_tag"])

        if len(Organization.objects.all()) != 0:
            for organization in Organization.objects.all():
                
                all_tags_list = []
                for tag in organization.related_tag.all():
                    all_tags_list.append(tag.value)
                all_tags_str = ", ".join(all_tags_list)

                my_writer.writerow([organization.name, organization.email, organization.site, organization.location, organization.is_club, organization.institution, organization.popularity, organization.is_active, all_tags_str])
            print("Backed Up Organization table")
   


def InitiativeBackUp():
    with open("backupfiles/InitiativeBUF.csv", "w", newline="") as wfile:
        my_writer=csv.writer(wfile)
        my_writer.writerow(["name", "date", "site", "parent_org", "related_tag"])

        if len(Initiative.objects.all()) != 0:
            for initiative in Initiative.objects.all():

                all_tags_list = []
                for tag in initiative.related_tag.all():
                    all_tags_list.append(tag.value)
                all_tags_str = ", ".join(all_tags_list)

                if not initiative.parent_org:
                    parent = initiative.parent_org
                else:
                    parent = initiative.parent_org.name

                my_writer.writerow([initiative.name, initiative.date, initiative.site, parent, all_tags_str])
            print("Backed Up Initiative table")



def ResourceBackUp():
    with open("backupfiles/ResourceBUF.csv", "w", newline="") as wfile:
        my_writer=csv.writer(wfile)
        my_writer.writerow(["name", "description", "date", "link", "parent_org", "followed_initiative", "can_display", "related_tag"])

        if len(Resource.objects.all()) != 0:
            for res in Resource.objects.all():
                
                all_initiatives_list = []
                for initiative in res.followed_initiative.all():
                    all_initiatives_list.append(initiative.name)
                all_initiatives_str = ", ".join(all_initiatives_list)

                all_tags_list = []
                for tag in res.related_tag.all():
                    all_tags_list.append(tag.value)
                all_tags_str = ", ".join(all_tags_list)

                if not res.parent_org:
                    parent = res.parent_org
                else:
                    parent = res.parent_org.name

                my_writer.writerow([res.name, res.description, res.date, res.link, parent, all_initiatives_str, res.can_display, all_tags_str])
            print("Backed Up Resource table")




def ConsumerBackUp():
    with open("backupfiles/ConsumerBUF.csv", "w", newline="") as wfile:
        my_writer=csv.writer(wfile)
        my_writer.writerow(["name", "email", "age", "location", "profession", "institution", "social_link"])
        if len(Consumer.objects.all()) != 0:
            for consumer in Consumer.objects.all():
                my_writer.writerow([consumer.name, consumer.email, consumer.age, consumer.location, consumer.profession, consumer.institution, consumer.social_link])
            print("Backed Up Consumer table")



def Zipper():
    with ZipFile('BUF.zip', "w") as zip_obj:
        zip_obj.write("backupfiles/TagBUF.csv")
        zip_obj.write("backupfiles/OrganizationBUF.csv")
        zip_obj.write("backupfiles/InitiativeBUF.csv")
        zip_obj.write("backupfiles/ResourceBUF.csv")
        zip_obj.write("backupfiles/ConsumerBUF.csv")
    print("Zipped all BUF files")



if __name__ == "__main__":
    main()