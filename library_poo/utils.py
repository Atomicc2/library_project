import json


def check_information(obj):
    #Display information about a book or a member      
    for k, v in obj.__dict__.items():
        print(f"{k}: {v}")


