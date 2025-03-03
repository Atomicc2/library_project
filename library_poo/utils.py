#Functions utilities

def check_information(obj):
        
        for k, v in obj.__dict__.items():
            print(f"{k}: {v}")