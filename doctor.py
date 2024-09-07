import datetime
import time
import os
from tkinter import *
from PIL import ImageTk, Image
from tkinter.font import Font
import sqlite3
from tkinter import messagebox
import boto3
import json

global formatted_date
current_date = datetime.date.today()

# Format the current date as 'DD-MM-YYYY'
formatted_date = current_date.strftime("%d-%m-%Y")

def new6():
    tab4 = Toplevel()
    tab4.title("MediSense System")
    tab4.geometry(root.geometry())
    back1_label = Label(tab4, image=back1)
    back1_label.place(x=0, y=0, relwidth=1, relheight=1)
    value1=checkbox_var1.get()
    value2=checkbox_var2.get()
    value3=checkbox_var3.get()
    value4=checkbox_var4.get()
    print(value1)
    print(value2)
    print(value3)
    print(value4)

    #arun

    if name=="arun":
        # name

        # Define your AWS credentials and region
        aws_access_key_id = 'AKIAZKHZJ4ZMCFFSCZDJ'
        aws_secret_access_key = 'KpEu2hZOKXGUoDe5EO+U717siLmXdIRq5AOsT5Iu'

        s3 = boto3.client('s3', region_name='Stockholm')


        s3 = boto3.client('s3', 
                        aws_access_key_id=aws_access_key_id, 
                        aws_secret_access_key=aws_secret_access_key)

        # Specify the bucket name and the folder (prefix) you want to create
        bucket_name = 'trial14567543'
        folder_name = "who"
        helo=str(formatted_date)


        # Create a sample JSON data
        json_data = {"name":"arun"
                    
        
        }

        # Convert the JSON data to string
        json_string = json.dumps(json_data)

        # Specify the file name for the JSON file
        file_name = folder_name+helo+".json"
        print(file_name)

        # Upload the JSON file to S3
        s3.put_object(Bucket=bucket_name, Key=file_name, Body=json_string)

        #availability
        # Define your AWS credentials and region
        aws_access_key_id = 'AKIAZKHZJ4ZMCFFSCZDJ'
        aws_secret_access_key = 'KpEu2hZOKXGUoDe5EO+U717siLmXdIRq5AOsT5Iu'

        s3 = boto3.client('s3', region_name='Stockholm')


        s3 = boto3.client('s3', 
                        aws_access_key_id=aws_access_key_id, 
                        aws_secret_access_key=aws_secret_access_key)

        # Specify the bucket name and the folder (prefix) you want to create
        bucket_name = 'trial14567543'
        folder_name = "arun"
        helo=str(formatted_date)


        # Create a sample JSON data
        json_data = {"a0":value1,
                     "b0":value2,
                     "c0":value3,
                     "d0":value4                    
                     }

        # Convert the JSON data to string
        json_string = json.dumps(json_data)

        # Specify the file name for the JSON file
        file_name = folder_name+helo+".json"
        print(file_name)

        # Upload the JSON file to S3
        s3.put_object(Bucket=bucket_name, Key=file_name, Body=json_string)

    #paul

    if name=="paul":
        # name

        # Define your AWS credentials and region
        aws_access_key_id = 'AKIAZKHZJ4ZMCFFSCZDJ'
        aws_secret_access_key = 'KpEu2hZOKXGUoDe5EO+U717siLmXdIRq5AOsT5Iu'

        s3 = boto3.client('s3', region_name='Stockholm')


        s3 = boto3.client('s3', 
                        aws_access_key_id=aws_access_key_id, 
                        aws_secret_access_key=aws_secret_access_key)

        # Specify the bucket name and the folder (prefix) you want to create
        bucket_name = 'trial14567543'
        folder_name = "who"
        helo=str(formatted_date)


        # Create a sample JSON data
        json_data = {"name":"paul"
                    
        
        }

        # Convert the JSON data to string
        json_string = json.dumps(json_data)

        # Specify the file name for the JSON file
        file_name = folder_name+helo+".json"
        print(file_name)

        # Upload the JSON file to S3
        s3.put_object(Bucket=bucket_name, Key=file_name, Body=json_string)

        #availability
        # Define your AWS credentials and region
        aws_access_key_id = 'AKIAZKHZJ4ZMCFFSCZDJ'
        aws_secret_access_key = 'KpEu2hZOKXGUoDe5EO+U717siLmXdIRq5AOsT5Iu'

        s3 = boto3.client('s3', region_name='Stockholm')


        s3 = boto3.client('s3', 
                        aws_access_key_id=aws_access_key_id, 
                        aws_secret_access_key=aws_secret_access_key)

        # Specify the bucket name and the folder (prefix) you want to create
        bucket_name = 'trial14567543'
        folder_name = "paul"
        helo=str(formatted_date)


        # Create a sample JSON data
        json_data = {"a1":value1,
                     "b1":value2,
                     "c1":value3,
                     "d1":value4                    
                     }

        # Convert the JSON data to string
        json_string = json.dumps(json_data)

        # Specify the file name for the JSON file
        file_name = folder_name+helo+".json"
        print(file_name)

        # Upload the JSON file to S3
        s3.put_object(Bucket=bucket_name, Key=file_name, Body=json_string)

    #karan

    if name=="karan":
        # name

        # Define your AWS credentials and region
        aws_access_key_id = 'AKIAZKHZJ4ZMCFFSCZDJ'
        aws_secret_access_key = 'KpEu2hZOKXGUoDe5EO+U717siLmXdIRq5AOsT5Iu'

        s3 = boto3.client('s3', region_name='Stockholm')


        s3 = boto3.client('s3', 
                        aws_access_key_id=aws_access_key_id, 
                        aws_secret_access_key=aws_secret_access_key)

        # Specify the bucket name and the folder (prefix) you want to create
        bucket_name = 'trial14567543'
        folder_name = "who"
        helo=str(formatted_date)


        # Create a sample JSON data
        json_data = {"name":"karan"
                    
        
        }

        # Convert the JSON data to string
        json_string = json.dumps(json_data)

        # Specify the file name for the JSON file
        file_name = folder_name+helo+".json"
        print(file_name)

        # Upload the JSON file to S3
        s3.put_object(Bucket=bucket_name, Key=file_name, Body=json_string)

        #availability
        # Define your AWS credentials and region
        aws_access_key_id = 'AKIAZKHZJ4ZMCFFSCZDJ'
        aws_secret_access_key = 'KpEu2hZOKXGUoDe5EO+U717siLmXdIRq5AOsT5Iu'

        s3 = boto3.client('s3', region_name='Stockholm')


        s3 = boto3.client('s3', 
                        aws_access_key_id=aws_access_key_id, 
                        aws_secret_access_key=aws_secret_access_key)

        # Specify the bucket name and the folder (prefix) you want to create
        bucket_name = 'trial14567543'
        folder_name = "karan"
        helo=str(formatted_date)


        # Create a sample JSON data
        json_data = {"a2":value1,
                     "b2":value2,
                     "c2":value3,
                     "d2":value4                    
                     }

        # Convert the JSON data to string
        json_string = json.dumps(json_data)

        # Specify the file name for the JSON file
        file_name = folder_name+helo+".json"
        print(file_name)

        # Upload the JSON file to S3
        s3.put_object(Bucket=bucket_name, Key=file_name, Body=json_string)

    #kishore

    if name=="kishore":
        # name

        # Define your AWS credentials and region
        aws_access_key_id = 'AKIAZKHZJ4ZMCFFSCZDJ'
        aws_secret_access_key = 'KpEu2hZOKXGUoDe5EO+U717siLmXdIRq5AOsT5Iu'

        s3 = boto3.client('s3', region_name='Stockholm')


        s3 = boto3.client('s3', 
                        aws_access_key_id=aws_access_key_id, 
                        aws_secret_access_key=aws_secret_access_key)

        # Specify the bucket name and the folder (prefix) you want to create
        bucket_name = 'trial14567543'
        folder_name = "who"
        helo=str(formatted_date)


        # Create a sample JSON data
        json_data = {"name":"kishore"
                    
        
        }

        # Convert the JSON data to string
        json_string = json.dumps(json_data)

        # Specify the file name for the JSON file
        file_name = folder_name+helo+".json"
        print(file_name)

        # Upload the JSON file to S3
        s3.put_object(Bucket=bucket_name, Key=file_name, Body=json_string)

        #availability
        # Define your AWS credentials and region
        aws_access_key_id = 'AKIAZKHZJ4ZMCFFSCZDJ'
        aws_secret_access_key = 'KpEu2hZOKXGUoDe5EO+U717siLmXdIRq5AOsT5Iu'

        s3 = boto3.client('s3', region_name='Stockholm')


        s3 = boto3.client('s3', 
                        aws_access_key_id=aws_access_key_id, 
                        aws_secret_access_key=aws_secret_access_key)

        # Specify the bucket name and the folder (prefix) you want to create
        bucket_name = 'trial14567543'
        folder_name = "kishore"
        helo=str(formatted_date)


        # Create a sample JSON data
        json_data = {"a3":value1,
                     "b3":value2,
                     "c3":value3,
                     "d3":value4                    
                     }

        # Convert the JSON data to string
        json_string = json.dumps(json_data)

        # Specify the file name for the JSON file
        file_name = folder_name+helo+".json"
        print(file_name)

        # Upload the JSON file to S3
        s3.put_object(Bucket=bucket_name, Key=file_name, Body=json_string)

    #raj

    if name=="raj":
        # name

        # Define your AWS credentials and region
        aws_access_key_id = 'AKIAZKHZJ4ZMCFFSCZDJ'
        aws_secret_access_key = 'KpEu2hZOKXGUoDe5EO+U717siLmXdIRq5AOsT5Iu'

        s3 = boto3.client('s3', region_name='Stockholm')


        s3 = boto3.client('s3', 
                        aws_access_key_id=aws_access_key_id, 
                        aws_secret_access_key=aws_secret_access_key)

        # Specify the bucket name and the folder (prefix) you want to create
        bucket_name = 'trial14567543'
        folder_name = "who"
        helo=str(formatted_date)


        # Create a sample JSON data
        json_data = {"name":"raj"
                    
        
        }

        # Convert the JSON data to string
        json_string = json.dumps(json_data)

        # Specify the file name for the JSON file
        file_name = folder_name+helo+".json"
        print(file_name)

        # Upload the JSON file to S3
        s3.put_object(Bucket=bucket_name, Key=file_name, Body=json_string)

        #availability
        # Define your AWS credentials and region
        aws_access_key_id = 'AKIAZKHZJ4ZMCFFSCZDJ'
        aws_secret_access_key = 'KpEu2hZOKXGUoDe5EO+U717siLmXdIRq5AOsT5Iu'

        s3 = boto3.client('s3', region_name='Stockholm')


        s3 = boto3.client('s3', 
                        aws_access_key_id=aws_access_key_id, 
                        aws_secret_access_key=aws_secret_access_key)

        # Specify the bucket name and the folder (prefix) you want to create
        bucket_name = 'trial14567543'
        folder_name = "raj"
        helo=str(formatted_date)


        # Create a sample JSON data
        json_data = {"e0":value1,
                     "f0":value2,
                     "g0":value3,
                     "h0":value4                    
                     }

        # Convert the JSON data to string
        json_string = json.dumps(json_data)

        # Specify the file name for the JSON file
        file_name = folder_name+helo+".json"
        print(file_name)

        # Upload the JSON file to S3
        s3.put_object(Bucket=bucket_name, Key=file_name, Body=json_string)

    #kajal

    if name=="kajal":
        # name

        # Define your AWS credentials and region
        aws_access_key_id = 'AKIAZKHZJ4ZMCFFSCZDJ'
        aws_secret_access_key = 'KpEu2hZOKXGUoDe5EO+U717siLmXdIRq5AOsT5Iu'

        s3 = boto3.client('s3', region_name='Stockholm')


        s3 = boto3.client('s3', 
                        aws_access_key_id=aws_access_key_id, 
                        aws_secret_access_key=aws_secret_access_key)

        # Specify the bucket name and the folder (prefix) you want to create
        bucket_name = 'trial14567543'
        folder_name = "who"
        helo=str(formatted_date)


        # Create a sample JSON data
        json_data = {"name":"kajal"
                    
        
        }

        # Convert the JSON data to string
        json_string = json.dumps(json_data)

        # Specify the file name for the JSON file
        file_name = folder_name+helo+".json"
        print(file_name)

        # Upload the JSON file to S3
        s3.put_object(Bucket=bucket_name, Key=file_name, Body=json_string)

        #availability
        # Define your AWS credentials and region
        aws_access_key_id = 'AKIAZKHZJ4ZMCFFSCZDJ'
        aws_secret_access_key = 'KpEu2hZOKXGUoDe5EO+U717siLmXdIRq5AOsT5Iu'

        s3 = boto3.client('s3', region_name='Stockholm')


        s3 = boto3.client('s3', 
                        aws_access_key_id=aws_access_key_id, 
                        aws_secret_access_key=aws_secret_access_key)

        # Specify the bucket name and the folder (prefix) you want to create
        bucket_name = 'trial14567543'
        folder_name = "kajal"
        helo=str(formatted_date)


        # Create a sample JSON data
        json_data = {"e1":value1,
                     "f1":value2,
                     "g1":value3,
                     "h1":value4                    
                     }

        # Convert the JSON data to string
        json_string = json.dumps(json_data)

        # Specify the file name for the JSON file
        file_name = folder_name+helo+".json"
        print(file_name)

        # Upload the JSON file to S3
        s3.put_object(Bucket=bucket_name, Key=file_name, Body=json_string)

    #kapoor

    if name=="kapoor":
        # name

        # Define your AWS credentials and region
        aws_access_key_id = 'AKIAZKHZJ4ZMCFFSCZDJ'
        aws_secret_access_key = 'KpEu2hZOKXGUoDe5EO+U717siLmXdIRq5AOsT5Iu'

        s3 = boto3.client('s3', region_name='Stockholm')


        s3 = boto3.client('s3', 
                        aws_access_key_id=aws_access_key_id, 
                        aws_secret_access_key=aws_secret_access_key)

        # Specify the bucket name and the folder (prefix) you want to create
        bucket_name = 'trial14567543'
        folder_name = "who"
        helo=str(formatted_date)


        # Create a sample JSON data
        json_data = {"name":"kapoor"
                    
        
        }

        # Convert the JSON data to string
        json_string = json.dumps(json_data)

        # Specify the file name for the JSON file
        file_name = folder_name+helo+".json"
        print(file_name)

        # Upload the JSON file to S3
        s3.put_object(Bucket=bucket_name, Key=file_name, Body=json_string)

        #availability
        # Define your AWS credentials and region
        aws_access_key_id = 'AKIAZKHZJ4ZMCFFSCZDJ'
        aws_secret_access_key = 'KpEu2hZOKXGUoDe5EO+U717siLmXdIRq5AOsT5Iu'

        s3 = boto3.client('s3', region_name='Stockholm')


        s3 = boto3.client('s3', 
                        aws_access_key_id=aws_access_key_id, 
                        aws_secret_access_key=aws_secret_access_key)

        # Specify the bucket name and the folder (prefix) you want to create
        bucket_name = 'trial14567543'
        folder_name = "kapoor"
        helo=str(formatted_date)


        # Create a sample JSON data
        json_data = {"e2":value1,
                     "f2":value2,
                     "g2":value3,
                     "h2":value4                    
                     }

        # Convert the JSON data to string
        json_string = json.dumps(json_data)

        # Specify the file name for the JSON file
        file_name = folder_name+helo+".json"
        print(file_name)

        # Upload the JSON file to S3
        s3.put_object(Bucket=bucket_name, Key=file_name, Body=json_string)

    #hari

    if name=="hari":
        # name

        # Define your AWS credentials and region
        aws_access_key_id = 'AKIAZKHZJ4ZMCFFSCZDJ'
        aws_secret_access_key = 'KpEu2hZOKXGUoDe5EO+U717siLmXdIRq5AOsT5Iu'

        s3 = boto3.client('s3', region_name='Stockholm')


        s3 = boto3.client('s3', 
                        aws_access_key_id=aws_access_key_id, 
                        aws_secret_access_key=aws_secret_access_key)

        # Specify the bucket name and the folder (prefix) you want to create
        bucket_name = 'trial14567543'
        folder_name = "who"
        helo=str(formatted_date)


        # Create a sample JSON data
        json_data = {"name":"hari"
                    
        
        }

        # Convert the JSON data to string
        json_string = json.dumps(json_data)

        # Specify the file name for the JSON file
        file_name = folder_name+helo+".json"
        print(file_name)

        # Upload the JSON file to S3
        s3.put_object(Bucket=bucket_name, Key=file_name, Body=json_string)

        #availability
        # Define your AWS credentials and region
        aws_access_key_id = 'AKIAZKHZJ4ZMCFFSCZDJ'
        aws_secret_access_key = 'KpEu2hZOKXGUoDe5EO+U717siLmXdIRq5AOsT5Iu'

        s3 = boto3.client('s3', region_name='Stockholm')


        s3 = boto3.client('s3', 
                        aws_access_key_id=aws_access_key_id, 
                        aws_secret_access_key=aws_secret_access_key)

        # Specify the bucket name and the folder (prefix) you want to create
        bucket_name = 'trial14567543'
        folder_name = "hari"
        helo=str(formatted_date)


        # Create a sample JSON data
        json_data = {"e3":value1,
                     "f3":value2,
                     "g3":value3,
                     "h3":value4                    
                     }

        # Convert the JSON data to string
        json_string = json.dumps(json_data)

        # Specify the file name for the JSON file
        file_name = folder_name+helo+".json"
        print(file_name)

        # Upload the JSON file to S3
        s3.put_object(Bucket=bucket_name, Key=file_name, Body=json_string)

    #sanjay

    if name=="sanjay":
        # name

        # Define your AWS credentials and region
        aws_access_key_id = 'AKIAZKHZJ4ZMCFFSCZDJ'
        aws_secret_access_key = 'KpEu2hZOKXGUoDe5EO+U717siLmXdIRq5AOsT5Iu'

        s3 = boto3.client('s3', region_name='Stockholm')


        s3 = boto3.client('s3', 
                        aws_access_key_id=aws_access_key_id, 
                        aws_secret_access_key=aws_secret_access_key)

        # Specify the bucket name and the folder (prefix) you want to create
        bucket_name = 'trial14567543'
        folder_name = "who"
        helo=str(formatted_date)


        # Create a sample JSON data
        json_data = {"name":"sanjay"
                    
        
        }

        # Convert the JSON data to string
        json_string = json.dumps(json_data)

        # Specify the file name for the JSON file
        file_name = folder_name+helo+".json"
        print(file_name)

        # Upload the JSON file to S3
        s3.put_object(Bucket=bucket_name, Key=file_name, Body=json_string)

        #availability
        # Define your AWS credentials and region
        aws_access_key_id = 'AKIAZKHZJ4ZMCFFSCZDJ'
        aws_secret_access_key = 'KpEu2hZOKXGUoDe5EO+U717siLmXdIRq5AOsT5Iu'

        s3 = boto3.client('s3', region_name='Stockholm')


        s3 = boto3.client('s3', 
                        aws_access_key_id=aws_access_key_id, 
                        aws_secret_access_key=aws_secret_access_key)

        # Specify the bucket name and the folder (prefix) you want to create
        bucket_name = 'trial14567543'
        folder_name = "sanjay"
        helo=str(formatted_date)


        # Create a sample JSON data
        json_data = {"i0":value1,
                     "j0":value2,
                     "k0":value3,
                     "l0":value4                    
                     }

        # Convert the JSON data to string
        json_string = json.dumps(json_data)

        # Specify the file name for the JSON file
        file_name = folder_name+helo+".json"
        print(file_name)

        # Upload the JSON file to S3
        s3.put_object(Bucket=bucket_name, Key=file_name, Body=json_string)

    #sundhar

    if name=="sundhar":
        # name

        # Define your AWS credentials and region
        aws_access_key_id = 'AKIAZKHZJ4ZMCFFSCZDJ'
        aws_secret_access_key = 'KpEu2hZOKXGUoDe5EO+U717siLmXdIRq5AOsT5Iu'

        s3 = boto3.client('s3', region_name='Stockholm')


        s3 = boto3.client('s3', 
                        aws_access_key_id=aws_access_key_id, 
                        aws_secret_access_key=aws_secret_access_key)

        # Specify the bucket name and the folder (prefix) you want to create
        bucket_name = 'trial14567543'
        folder_name = "who"
        helo=str(formatted_date)


        # Create a sample JSON data
        json_data = {"name":"sundhar"
                    
        
        }

        # Convert the JSON data to string
        json_string = json.dumps(json_data)

        # Specify the file name for the JSON file
        file_name = folder_name+helo+".json"
        print(file_name)

        # Upload the JSON file to S3
        s3.put_object(Bucket=bucket_name, Key=file_name, Body=json_string)

        #availability
        # Define your AWS credentials and region
        aws_access_key_id = 'AKIAZKHZJ4ZMCFFSCZDJ'
        aws_secret_access_key = 'KpEu2hZOKXGUoDe5EO+U717siLmXdIRq5AOsT5Iu'

        s3 = boto3.client('s3', region_name='Stockholm')


        s3 = boto3.client('s3', 
                        aws_access_key_id=aws_access_key_id, 
                        aws_secret_access_key=aws_secret_access_key)

        # Specify the bucket name and the folder (prefix) you want to create
        bucket_name = 'trial14567543'
        folder_name = "sundhar"
        helo=str(formatted_date)


        # Create a sample JSON data
        json_data = {"i1":value1,
                     "j1":value2,
                     "k1":value3,
                     "l1":value4                    
                     }

        # Convert the JSON data to string
        json_string = json.dumps(json_data)

        # Specify the file name for the JSON file
        file_name = folder_name+helo+".json"
        print(file_name)

        # Upload the JSON file to S3
        s3.put_object(Bucket=bucket_name, Key=file_name, Body=json_string)

    #madhu

    if name=="madhu":
        # name

        # Define your AWS credentials and region
        aws_access_key_id = 'AKIAZKHZJ4ZMCFFSCZDJ'
        aws_secret_access_key = 'KpEu2hZOKXGUoDe5EO+U717siLmXdIRq5AOsT5Iu'

        s3 = boto3.client('s3', region_name='Stockholm')


        s3 = boto3.client('s3', 
                        aws_access_key_id=aws_access_key_id, 
                        aws_secret_access_key=aws_secret_access_key)

        # Specify the bucket name and the folder (prefix) you want to create
        bucket_name = 'trial14567543'
        folder_name = "who"
        helo=str(formatted_date)


        # Create a sample JSON data
        json_data = {"name":"madhu"
                    
        
        }

        # Convert the JSON data to string
        json_string = json.dumps(json_data)

        # Specify the file name for the JSON file
        file_name = folder_name+helo+".json"
        print(file_name)

        # Upload the JSON file to S3
        s3.put_object(Bucket=bucket_name, Key=file_name, Body=json_string)

        #availability
        # Define your AWS credentials and region
        aws_access_key_id = 'AKIAZKHZJ4ZMCFFSCZDJ'
        aws_secret_access_key = 'KpEu2hZOKXGUoDe5EO+U717siLmXdIRq5AOsT5Iu'

        s3 = boto3.client('s3', region_name='Stockholm')


        s3 = boto3.client('s3', 
                        aws_access_key_id=aws_access_key_id, 
                        aws_secret_access_key=aws_secret_access_key)

        # Specify the bucket name and the folder (prefix) you want to create
        bucket_name = 'trial14567543'
        folder_name = "madhu"
        helo=str(formatted_date)


        # Create a sample JSON data
        json_data = {"i2":value1,
                     "j2":value2,
                     "k2":value3,
                     "l2":value4                    
                     }

        # Convert the JSON data to string
        json_string = json.dumps(json_data)

        # Specify the file name for the JSON file
        file_name = folder_name+helo+".json"
        print(file_name)

        # Upload the JSON file to S3
        s3.put_object(Bucket=bucket_name, Key=file_name, Body=json_string)

    #dharun

    if name=="dharun":
        # name

        # Define your AWS credentials and region
        aws_access_key_id = 'AKIAZKHZJ4ZMCFFSCZDJ'
        aws_secret_access_key = 'KpEu2hZOKXGUoDe5EO+U717siLmXdIRq5AOsT5Iu'

        s3 = boto3.client('s3', region_name='Stockholm')


        s3 = boto3.client('s3', 
                        aws_access_key_id=aws_access_key_id, 
                        aws_secret_access_key=aws_secret_access_key)

        # Specify the bucket name and the folder (prefix) you want to create
        bucket_name = 'trial14567543'
        folder_name = "who"
        helo=str(formatted_date)


        # Create a sample JSON data
        json_data = {"name":"dharun"
                    
        
        }

        # Convert the JSON data to string
        json_string = json.dumps(json_data)

        # Specify the file name for the JSON file
        file_name = folder_name+helo+".json"
        print(file_name)

        # Upload the JSON file to S3
        s3.put_object(Bucket=bucket_name, Key=file_name, Body=json_string)

        #availability
        # Define your AWS credentials and region
        aws_access_key_id = 'AKIAZKHZJ4ZMCFFSCZDJ'
        aws_secret_access_key = 'KpEu2hZOKXGUoDe5EO+U717siLmXdIRq5AOsT5Iu'

        s3 = boto3.client('s3', region_name='Stockholm')


        s3 = boto3.client('s3', 
                        aws_access_key_id=aws_access_key_id, 
                        aws_secret_access_key=aws_secret_access_key)

        # Specify the bucket name and the folder (prefix) you want to create
        bucket_name = 'trial14567543'
        folder_name = "dharun"
        helo=str(formatted_date)


        # Create a sample JSON data
        json_data = {"i3":value1,
                     "j3":value2,
                     "k3":value3,
                     "l3":value4                    
                     }

        # Convert the JSON data to string
        json_string = json.dumps(json_data)

        # Specify the file name for the JSON file
        file_name = folder_name+helo+".json"
        print(file_name)

        # Upload the JSON file to S3
        s3.put_object(Bucket=bucket_name, Key=file_name, Body=json_string)

    #rahul

    if name=="rahul":
        # name

        # Define your AWS credentials and region
        aws_access_key_id = 'AKIAZKHZJ4ZMCFFSCZDJ'
        aws_secret_access_key = 'KpEu2hZOKXGUoDe5EO+U717siLmXdIRq5AOsT5Iu'

        s3 = boto3.client('s3', region_name='Stockholm')


        s3 = boto3.client('s3', 
                        aws_access_key_id=aws_access_key_id, 
                        aws_secret_access_key=aws_secret_access_key)

        # Specify the bucket name and the folder (prefix) you want to create
        bucket_name = 'trial14567543'
        folder_name = "who"
        helo=str(formatted_date)


        # Create a sample JSON data
        json_data = {"name":"rahul"
                    
        
        }

        # Convert the JSON data to string
        json_string = json.dumps(json_data)

        # Specify the file name for the JSON file
        file_name = folder_name+helo+".json"
        print(file_name)

        # Upload the JSON file to S3
        s3.put_object(Bucket=bucket_name, Key=file_name, Body=json_string)

        #availability
        # Define your AWS credentials and region
        aws_access_key_id = 'AKIAZKHZJ4ZMCFFSCZDJ'
        aws_secret_access_key = 'KpEu2hZOKXGUoDe5EO+U717siLmXdIRq5AOsT5Iu'

        s3 = boto3.client('s3', region_name='Stockholm')


        s3 = boto3.client('s3', 
                        aws_access_key_id=aws_access_key_id, 
                        aws_secret_access_key=aws_secret_access_key)

        # Specify the bucket name and the folder (prefix) you want to create
        bucket_name = 'trial14567543'
        folder_name = "rahul"
        helo=str(formatted_date)


        # Create a sample JSON data
        json_data = {"m0":value1,
                     "n0":value2,
                     "o0":value3,
                     "p0":value4                    
                     }

        # Convert the JSON data to string
        json_string = json.dumps(json_data)

        # Specify the file name for the JSON file
        file_name = folder_name+helo+".json"
        print(file_name)

        # Upload the JSON file to S3
        s3.put_object(Bucket=bucket_name, Key=file_name, Body=json_string)

    #ram

    if name=="ram":
        # name

        # Define your AWS credentials and region
        aws_access_key_id = 'AKIAZKHZJ4ZMCFFSCZDJ'
        aws_secret_access_key = 'KpEu2hZOKXGUoDe5EO+U717siLmXdIRq5AOsT5Iu'

        s3 = boto3.client('s3', region_name='Stockholm')


        s3 = boto3.client('s3', 
                        aws_access_key_id=aws_access_key_id, 
                        aws_secret_access_key=aws_secret_access_key)

        # Specify the bucket name and the folder (prefix) you want to create
        bucket_name = 'trial14567543'
        folder_name = "who"
        helo=str(formatted_date)


        # Create a sample JSON data
        json_data = {"name":"ram"
                    
        
        }

        # Convert the JSON data to string
        json_string = json.dumps(json_data)

        # Specify the file name for the JSON file
        file_name = folder_name+helo+".json"
        print(file_name)

        # Upload the JSON file to S3
        s3.put_object(Bucket=bucket_name, Key=file_name, Body=json_string)

        #availability
        # Define your AWS credentials and region
        aws_access_key_id = 'AKIAZKHZJ4ZMCFFSCZDJ'
        aws_secret_access_key = 'KpEu2hZOKXGUoDe5EO+U717siLmXdIRq5AOsT5Iu'

        s3 = boto3.client('s3', region_name='Stockholm')


        s3 = boto3.client('s3', 
                        aws_access_key_id=aws_access_key_id, 
                        aws_secret_access_key=aws_secret_access_key)

        # Specify the bucket name and the folder (prefix) you want to create
        bucket_name = 'trial14567543'
        folder_name = "ram"
        helo=str(formatted_date)


        # Create a sample JSON data
        json_data = {"m1":value1,
                     "n1":value2,
                     "o1":value3,
                     "p1":value4                    
                     }

        # Convert the JSON data to string
        json_string = json.dumps(json_data)

        # Specify the file name for the JSON file
        file_name = folder_name+helo+".json"
        print(file_name)

        # Upload the JSON file to S3
        s3.put_object(Bucket=bucket_name, Key=file_name, Body=json_string)

    #sara

    if name=="sara":
        # name

        # Define your AWS credentials and region
        aws_access_key_id = 'AKIAZKHZJ4ZMCFFSCZDJ'
        aws_secret_access_key = 'KpEu2hZOKXGUoDe5EO+U717siLmXdIRq5AOsT5Iu'

        s3 = boto3.client('s3', region_name='Stockholm')


        s3 = boto3.client('s3', 
                        aws_access_key_id=aws_access_key_id, 
                        aws_secret_access_key=aws_secret_access_key)

        # Specify the bucket name and the folder (prefix) you want to create
        bucket_name = 'trial14567543'
        folder_name = "who"
        helo=str(formatted_date)


        # Create a sample JSON data
        json_data = {"name":"sara"
                    
        
        }

        # Convert the JSON data to string
        json_string = json.dumps(json_data)

        # Specify the file name for the JSON file
        file_name = folder_name+helo+".json"
        print(file_name)

        # Upload the JSON file to S3
        s3.put_object(Bucket=bucket_name, Key=file_name, Body=json_string)

        #availability
        # Define your AWS credentials and region
        aws_access_key_id = 'AKIAZKHZJ4ZMCFFSCZDJ'
        aws_secret_access_key = 'KpEu2hZOKXGUoDe5EO+U717siLmXdIRq5AOsT5Iu'

        s3 = boto3.client('s3', region_name='Stockholm')


        s3 = boto3.client('s3', 
                        aws_access_key_id=aws_access_key_id, 
                        aws_secret_access_key=aws_secret_access_key)

        # Specify the bucket name and the folder (prefix) you want to create
        bucket_name = 'trial14567543'
        folder_name = "sara"
        helo=str(formatted_date)


        # Create a sample JSON data
        json_data = {"m2":value1,
                     "n2":value2,
                     "o2":value3,
                     "p2":value4                    
                     }

        # Convert the JSON data to string
        json_string = json.dumps(json_data)

        # Specify the file name for the JSON file
        file_name = folder_name+helo+".json"
        print(file_name)

        # Upload the JSON file to S3
        s3.put_object(Bucket=bucket_name, Key=file_name, Body=json_string)

        #rahul

    if name=="vasan":
        # name

        # Define your AWS credentials and region
        aws_access_key_id = 'AKIAZKHZJ4ZMCFFSCZDJ'
        aws_secret_access_key = 'KpEu2hZOKXGUoDe5EO+U717siLmXdIRq5AOsT5Iu'

        s3 = boto3.client('s3', region_name='Stockholm')


        s3 = boto3.client('s3', 
                        aws_access_key_id=aws_access_key_id, 
                        aws_secret_access_key=aws_secret_access_key)

        # Specify the bucket name and the folder (prefix) you want to create
        bucket_name = 'trial14567543'
        folder_name = "who"
        helo=str(formatted_date)


        # Create a sample JSON data
        json_data = {"name":"vasan"
                    
        
        }

        # Convert the JSON data to string
        json_string = json.dumps(json_data)

        # Specify the file name for the JSON file
        file_name = folder_name+helo+".json"
        print(file_name)

        # Upload the JSON file to S3
        s3.put_object(Bucket=bucket_name, Key=file_name, Body=json_string)

        #availability
        # Define your AWS credentials and region
        aws_access_key_id = 'AKIAZKHZJ4ZMCFFSCZDJ'
        aws_secret_access_key = 'KpEu2hZOKXGUoDe5EO+U717siLmXdIRq5AOsT5Iu'

        s3 = boto3.client('s3', region_name='Stockholm')


        s3 = boto3.client('s3', 
                        aws_access_key_id=aws_access_key_id, 
                        aws_secret_access_key=aws_secret_access_key)

        # Specify the bucket name and the folder (prefix) you want to create
        bucket_name = 'trial14567543'
        folder_name = "vasan"
        helo=str(formatted_date)


        # Create a sample JSON data
        json_data = {"m3":value1,
                     "n3":value2,
                     "o3":value3,
                     "p3":value4                    
                     }

        # Convert the JSON data to string
        json_string = json.dumps(json_data)

        # Specify the file name for the JSON file
        file_name = folder_name+helo+".json"
        print(file_name)

        # Upload the JSON file to S3
        s3.put_object(Bucket=bucket_name, Key=file_name, Body=json_string)
    
    response=messagebox.askyesno("Availability","Your availability is updated  ")
    if response:
         root.quit()






def new4():
    tab4 = Toplevel()
    tab4.title("MediSense System")
    tab4.geometry(root.geometry())
    back1_label = Label(tab4, image=back1)
    back1_label.place(x=0, y=0, relwidth=1, relheight=1)
    label1=Label(tab4, text="Choose Availability:",font=custom_font1,bg="#9ee8f0", fg="#111212",height=1,width=20)
    label1.place(relx=0.50, rely=0.10, anchor="center")
    global value1,value2,value3,value4,checkbox_var1,checkbox_var2,checkbox_var3,checkbox_var4
    #arun
    if name=="arun":
        checkbox_var1 = IntVar()
        checkbox = Checkbutton(tab4, text="9:00", variable=checkbox_var1)
        checkbox.place(relx=0.40, rely=0.30, anchor="center")
        
 


        checkbox_var2 = IntVar()
        checkbox = Checkbutton(tab4, text="9:30", variable=checkbox_var2)
        checkbox.place(relx=0.55, rely=0.30, anchor="center")
        


        checkbox_var3 = IntVar()
        checkbox = Checkbutton(tab4, text="10:00", variable=checkbox_var3)
        checkbox.place(relx=0.40, rely=0.50, anchor="center")
        

        checkbox_var4 = IntVar()
        checkbox = Checkbutton(tab4, text="10:30", variable=checkbox_var4)
        checkbox.place(relx=0.55, rely=0.50, anchor="center")
        

        button2 = Button(tab4, text="Submit", font=custom_font1, bg="#9ee8f0", fg="#111212", command=new6, width=15, height=1)
        button2.place(relx=0.5, rely=0.80, anchor="center")
    
    #paul

    if name=="paul":
        checkbox_var1 = IntVar()
        checkbox = Checkbutton(tab4, text="11:00", variable=checkbox_var1)
        checkbox.place(relx=0.40, rely=0.30, anchor="center")
        
 


        checkbox_var2 = IntVar()
        checkbox = Checkbutton(tab4, text="11:30", variable=checkbox_var2)
        checkbox.place(relx=0.55, rely=0.30, anchor="center")
        


        checkbox_var3 = IntVar()
        checkbox = Checkbutton(tab4, text="12:00", variable=checkbox_var3)
        checkbox.place(relx=0.40, rely=0.50, anchor="center")
        

        checkbox_var4 = IntVar()
        checkbox = Checkbutton(tab4, text="12:30", variable=checkbox_var4)
        checkbox.place(relx=0.55, rely=0.50, anchor="center")
        

        button2 = Button(tab4, text="Submit", font=custom_font1, bg="#9ee8f0", fg="#111212", command=new6, width=15, height=1)
        button2.place(relx=0.5, rely=0.80, anchor="center")
    
    #karan
    if name=="karan":
        checkbox_var1 = IntVar()
        checkbox = Checkbutton(tab4, text="2:00", variable=checkbox_var1)
        checkbox.place(relx=0.40, rely=0.30, anchor="center")
        
 


        checkbox_var2 = IntVar()
        checkbox = Checkbutton(tab4, text="2:30", variable=checkbox_var2)
        checkbox.place(relx=0.55, rely=0.30, anchor="center")
        


        checkbox_var3 = IntVar()
        checkbox = Checkbutton(tab4, text="3:00", variable=checkbox_var3)
        checkbox.place(relx=0.40, rely=0.50, anchor="center")
        

        checkbox_var4 = IntVar()
        checkbox = Checkbutton(tab4, text="3:30", variable=checkbox_var4)
        checkbox.place(relx=0.55, rely=0.50, anchor="center")
        

        button2 = Button(tab4, text="Submit", font=custom_font1, bg="#9ee8f0", fg="#111212", command=new6, width=15, height=1)
        button2.place(relx=0.5, rely=0.80, anchor="center")

    #kishore
    if name=="kishore":
        checkbox_var1 = IntVar()
        checkbox = Checkbutton(tab4, text="4:00", variable=checkbox_var1)
        checkbox.place(relx=0.40, rely=0.30, anchor="center")
        
 


        checkbox_var2 = IntVar()
        checkbox = Checkbutton(tab4, text="4:30", variable=checkbox_var2)
        checkbox.place(relx=0.55, rely=0.30, anchor="center")
        


        checkbox_var3 = IntVar()
        checkbox = Checkbutton(tab4, text="5:00", variable=checkbox_var3)
        checkbox.place(relx=0.40, rely=0.50, anchor="center")
        

        checkbox_var4 = IntVar()
        checkbox = Checkbutton(tab4, text="5:30", variable=checkbox_var4)
        checkbox.place(relx=0.55, rely=0.50, anchor="center")
        

        button2 = Button(tab4, text="Submit", font=custom_font1, bg="#9ee8f0", fg="#111212", command=new6, width=15, height=1)
        button2.place(relx=0.5, rely=0.80, anchor="center")

    #raj
    if name=="raj":
        checkbox_var1 = IntVar()
        checkbox = Checkbutton(tab4, text="9:00", variable=checkbox_var1)
        checkbox.place(relx=0.40, rely=0.30, anchor="center")
        
 


        checkbox_var2 = IntVar()
        checkbox = Checkbutton(tab4, text="9:30", variable=checkbox_var2)
        checkbox.place(relx=0.55, rely=0.30, anchor="center")
        


        checkbox_var3 = IntVar()
        checkbox = Checkbutton(tab4, text="10:00", variable=checkbox_var3)
        checkbox.place(relx=0.40, rely=0.50, anchor="center")
        

        checkbox_var4 = IntVar()
        checkbox = Checkbutton(tab4, text="10:30", variable=checkbox_var4)
        checkbox.place(relx=0.55, rely=0.50, anchor="center")
        

        button2 = Button(tab4, text="Submit", font=custom_font1, bg="#9ee8f0", fg="#111212", command=new6, width=15, height=1)
        button2.place(relx=0.5, rely=0.80, anchor="center")

    #kajal
    if name=="kajal":
        checkbox_var1 = IntVar()
        checkbox = Checkbutton(tab4, text="11:00", variable=checkbox_var1)
        checkbox.place(relx=0.40, rely=0.30, anchor="center")
        
 


        checkbox_var2 = IntVar()
        checkbox = Checkbutton(tab4, text="11:30", variable=checkbox_var2)
        checkbox.place(relx=0.55, rely=0.30, anchor="center")
        


        checkbox_var3 = IntVar()
        checkbox = Checkbutton(tab4, text="12:00", variable=checkbox_var3)
        checkbox.place(relx=0.40, rely=0.50, anchor="center")
        

        checkbox_var4 = IntVar()
        checkbox = Checkbutton(tab4, text="12:30", variable=checkbox_var4)
        checkbox.place(relx=0.55, rely=0.50, anchor="center")
        

        button2 = Button(tab4, text="Submit", font=custom_font1, bg="#9ee8f0", fg="#111212", command=new6, width=15, height=1)
        button2.place(relx=0.5, rely=0.80, anchor="center")

    #kapoor
    if name=="kapoor":
        checkbox_var1 = IntVar()
        checkbox = Checkbutton(tab4, text="2:00", variable=checkbox_var1)
        checkbox.place(relx=0.40, rely=0.30, anchor="center")
        
 


        checkbox_var2 = IntVar()
        checkbox = Checkbutton(tab4, text="2:30", variable=checkbox_var2)
        checkbox.place(relx=0.55, rely=0.30, anchor="center")
        


        checkbox_var3 = IntVar()
        checkbox = Checkbutton(tab4, text="3:00", variable=checkbox_var3)
        checkbox.place(relx=0.40, rely=0.50, anchor="center")
        

        checkbox_var4 = IntVar()
        checkbox = Checkbutton(tab4, text="3:30", variable=checkbox_var4)
        checkbox.place(relx=0.55, rely=0.50, anchor="center")
        

        button2 = Button(tab4, text="Submit", font=custom_font1, bg="#9ee8f0", fg="#111212", command=new6, width=15, height=1)
        button2.place(relx=0.5, rely=0.80, anchor="center")

    #hari
    if name=="hari":
        checkbox_var1 = IntVar()
        checkbox = Checkbutton(tab4, text="4:00", variable=checkbox_var1)
        checkbox.place(relx=0.40, rely=0.30, anchor="center")
        
 


        checkbox_var2 = IntVar()
        checkbox = Checkbutton(tab4, text="4:30", variable=checkbox_var2)
        checkbox.place(relx=0.55, rely=0.30, anchor="center")
        


        checkbox_var3 = IntVar()
        checkbox = Checkbutton(tab4, text="5:00", variable=checkbox_var3)
        checkbox.place(relx=0.40, rely=0.50, anchor="center")
        

        checkbox_var4 = IntVar()
        checkbox = Checkbutton(tab4, text="5:30", variable=checkbox_var4)
        checkbox.place(relx=0.55, rely=0.50, anchor="center")
        

        button2 = Button(tab4, text="Submit", font=custom_font1, bg="#9ee8f0", fg="#111212", command=new6, width=15, height=1)
        button2.place(relx=0.5, rely=0.80, anchor="center")

    #sanjay
    if name=="sanjay":
        checkbox_var1 = IntVar()
        checkbox = Checkbutton(tab4, text="9:00", variable=checkbox_var1)
        checkbox.place(relx=0.40, rely=0.30, anchor="center")
        
 


        checkbox_var2 = IntVar()
        checkbox = Checkbutton(tab4, text="9:30", variable=checkbox_var2)
        checkbox.place(relx=0.55, rely=0.30, anchor="center")
        


        checkbox_var3 = IntVar()
        checkbox = Checkbutton(tab4, text="10:00", variable=checkbox_var3)
        checkbox.place(relx=0.40, rely=0.50, anchor="center")
        

        checkbox_var4 = IntVar()
        checkbox = Checkbutton(tab4, text="10:30", variable=checkbox_var4)
        checkbox.place(relx=0.55, rely=0.50, anchor="center")
        

        button2 = Button(tab4, text="Submit", font=custom_font1, bg="#9ee8f0", fg="#111212", command=new6, width=15, height=1)
        button2.place(relx=0.5, rely=0.80, anchor="center")

    #sundhar
    if name=="sundhar":
        checkbox_var1 = IntVar()
        checkbox = Checkbutton(tab4, text="11:00", variable=checkbox_var1)
        checkbox.place(relx=0.40, rely=0.30, anchor="center")
        
 


        checkbox_var2 = IntVar()
        checkbox = Checkbutton(tab4, text="11:30", variable=checkbox_var2)
        checkbox.place(relx=0.55, rely=0.30, anchor="center")
        


        checkbox_var3 = IntVar()
        checkbox = Checkbutton(tab4, text="12:00", variable=checkbox_var3)
        checkbox.place(relx=0.40, rely=0.50, anchor="center")
        

        checkbox_var4 = IntVar()
        checkbox = Checkbutton(tab4, text="12:30", variable=checkbox_var4)
        checkbox.place(relx=0.55, rely=0.50, anchor="center")
        

        button2 = Button(tab4, text="Submit", font=custom_font1, bg="#9ee8f0", fg="#111212", command=new6, width=15, height=1)
        button2.place(relx=0.5, rely=0.80, anchor="center")

    #madhu
    if name=="madhu":
        checkbox_var1 = IntVar()
        checkbox = Checkbutton(tab4, text="2:00", variable=checkbox_var1)
        checkbox.place(relx=0.40, rely=0.30, anchor="center")
        
 


        checkbox_var2 = IntVar()
        checkbox = Checkbutton(tab4, text="2:30", variable=checkbox_var2)
        checkbox.place(relx=0.55, rely=0.30, anchor="center")
        


        checkbox_var3 = IntVar()
        checkbox = Checkbutton(tab4, text="3:00", variable=checkbox_var3)
        checkbox.place(relx=0.40, rely=0.50, anchor="center")
        

        checkbox_var4 = IntVar()
        checkbox = Checkbutton(tab4, text="3:30", variable=checkbox_var4)
        checkbox.place(relx=0.55, rely=0.50, anchor="center")
        

        button2 = Button(tab4, text="Submit", font=custom_font1, bg="#9ee8f0", fg="#111212", command=new6, width=15, height=1)
        button2.place(relx=0.5, rely=0.80, anchor="center")

    #dharun
    if name=="dharun":
        checkbox_var1 = IntVar()
        checkbox = Checkbutton(tab4, text="4:00", variable=checkbox_var1)
        checkbox.place(relx=0.40, rely=0.30, anchor="center")
        
 


        checkbox_var2 = IntVar()
        checkbox = Checkbutton(tab4, text="4:30", variable=checkbox_var2)
        checkbox.place(relx=0.55, rely=0.30, anchor="center")
        


        checkbox_var3 = IntVar()
        checkbox = Checkbutton(tab4, text="5:00", variable=checkbox_var3)
        checkbox.place(relx=0.40, rely=0.50, anchor="center")
        

        checkbox_var4 = IntVar()
        checkbox = Checkbutton(tab4, text="5:30", variable=checkbox_var4)
        checkbox.place(relx=0.55, rely=0.50, anchor="center")
        

        button2 = Button(tab4, text="Submit", font=custom_font1, bg="#9ee8f0", fg="#111212", command=new6, width=15, height=1)
        button2.place(relx=0.5, rely=0.80, anchor="center")

    #rahul
    if name=="rahul":
        checkbox_var1 = IntVar()
        checkbox = Checkbutton(tab4, text="9:00", variable=checkbox_var1)
        checkbox.place(relx=0.40, rely=0.30, anchor="center")
        
 


        checkbox_var2 = IntVar()
        checkbox = Checkbutton(tab4, text="9:30", variable=checkbox_var2)
        checkbox.place(relx=0.55, rely=0.30, anchor="center")
        


        checkbox_var3 = IntVar()
        checkbox = Checkbutton(tab4, text="10:00", variable=checkbox_var3)
        checkbox.place(relx=0.40, rely=0.50, anchor="center")
        

        checkbox_var4 = IntVar()
        checkbox = Checkbutton(tab4, text="10:30", variable=checkbox_var4)
        checkbox.place(relx=0.55, rely=0.50, anchor="center")
        

        button2 = Button(tab4, text="Submit", font=custom_font1, bg="#9ee8f0", fg="#111212", command=new6, width=15, height=1)
        button2.place(relx=0.5, rely=0.80, anchor="center")

    #ram

    if name=="ram":
        checkbox_var1 = IntVar()
        checkbox = Checkbutton(tab4, text="11:00", variable=checkbox_var1)
        checkbox.place(relx=0.40, rely=0.30, anchor="center")
        
 


        checkbox_var2 = IntVar()
        checkbox = Checkbutton(tab4, text="11:30", variable=checkbox_var2)
        checkbox.place(relx=0.55, rely=0.30, anchor="center")
        


        checkbox_var3 = IntVar()
        checkbox = Checkbutton(tab4, text="12:00", variable=checkbox_var3)
        checkbox.place(relx=0.40, rely=0.50, anchor="center")
        

        checkbox_var4 = IntVar()
        checkbox = Checkbutton(tab4, text="12:30", variable=checkbox_var4)
        checkbox.place(relx=0.55, rely=0.50, anchor="center")
        

        button2 = Button(tab4, text="Submit", font=custom_font1, bg="#9ee8f0", fg="#111212", command=new6, width=15, height=1)
        button2.place(relx=0.5, rely=0.80, anchor="center")

    #sara
    if name=="sara":
        checkbox_var1 = IntVar()
        checkbox = Checkbutton(tab4, text="2:00", variable=checkbox_var1)
        checkbox.place(relx=0.40, rely=0.30, anchor="center")
        
 


        checkbox_var2 = IntVar()
        checkbox = Checkbutton(tab4, text="2:30", variable=checkbox_var2)
        checkbox.place(relx=0.55, rely=0.30, anchor="center")
        


        checkbox_var3 = IntVar()
        checkbox = Checkbutton(tab4, text="3:00", variable=checkbox_var3)
        checkbox.place(relx=0.40, rely=0.50, anchor="center")
        

        checkbox_var4 = IntVar()
        checkbox = Checkbutton(tab4, text="3:30", variable=checkbox_var4)
        checkbox.place(relx=0.55, rely=0.50, anchor="center")
        

        button2 = Button(tab4, text="Submit", font=custom_font1, bg="#9ee8f0", fg="#111212", command=new6, width=15, height=1)
        button2.place(relx=0.5, rely=0.80, anchor="center")

    #vasan
    if name=="vasan":
        checkbox_var1 = IntVar()
        checkbox = Checkbutton(tab4, text="4:00", variable=checkbox_var1)
        checkbox.place(relx=0.40, rely=0.30, anchor="center")
        
 


        checkbox_var2 = IntVar()
        checkbox = Checkbutton(tab4, text="4:30", variable=checkbox_var2)
        checkbox.place(relx=0.55, rely=0.30, anchor="center")
        


        checkbox_var3 = IntVar()
        checkbox = Checkbutton(tab4, text="5:00", variable=checkbox_var3)
        checkbox.place(relx=0.40, rely=0.50, anchor="center")
        

        checkbox_var4 = IntVar()
        checkbox = Checkbutton(tab4, text="5:30", variable=checkbox_var4)
        checkbox.place(relx=0.55, rely=0.50, anchor="center")
        

        button2 = Button(tab4, text="Submit", font=custom_font1, bg="#9ee8f0", fg="#111212", command=new6, width=15, height=1)
        button2.place(relx=0.5, rely=0.80, anchor="center")





def update():
    text = text_entry.get("1.0", "end-1c") 
    print(text)
    last_reading["Discription"] = text

    print(last_reading)
    # Write the updated data back to the JSON file
    with open(destination_path, 'w') as file:
        json.dump(data, file, indent=4)

    if os.path.exists(destination_path):
        # Step 1: Read the JSON file
        with open(destination_path, 'r') as file:
            # Read the JSON data
            json_data = file.read()

        # Step 2: Parse the JSON data
        data1 = json.loads(json_data)

        aws_access_key_id = 'AKIAZKHZJ4ZMCFFSCZDJ'
        aws_secret_access_key = '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'

        s3 = boto3.client('s3', region_name='Ohio')


        s3 = boto3.client('s3', 
                        aws_access_key_id=aws_access_key_id, 
                        aws_secret_access_key=aws_secret_access_key)

        # Specify the bucket name and the folder (prefix) you want to create
        bucket_name = 'medicaregk'




        # Convert the JSON data to string
        json_string = json.dumps(data1)

        # Specify the file name for the JSON file
        file_name = folder_name + ".json"

        # Upload the JSON file to S3
        s3.put_object(Bucket=bucket_name, Key=file_name, Body=json_string)
        print("done")
        root.quit()
    


    



def new7(patientid):
    print(patientid)
    global text_entry,last_reading,destination_path,data,folder_name
    tab9 = Toplevel()
    tab9.title("MediSense System")
    tab9.geometry(root.geometry())
    back1_label = Label(tab9, image=back1)
    back1_label.place(x=0, y=0, relwidth=1, relheight=1)
    os.environ['AWS_ACCESS_KEY_ID'] = 'AKIAZKHZJ4ZMCFFSCZDJ'
    os.environ['AWS_SECRET_ACCESS_KEY'] = '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'
    folder_name = str(patientid)


    def download_json_from_s3(bucket_name, file_key, destination_path):
        # Initialize the S3 client
        s3 = boto3.client('s3')
        
        try:
            # Download JSON file from S3
            s3.download_file(bucket_name, file_key, destination_path)
            print(f"Downloaded JSON file from S3 to {destination_path}")
        except Exception as e:
            pass

    if __name__ == "__main__":
        bucket_name = 'medicaregk'
        file_key = folder_name + ".json"
        
        # Set the local file path with the desired destination path
        destination_path = r"D:\mini\output\\" + folder_name + ".json"
        
        download_json_from_s3(bucket_name, file_key, destination_path)


        # Variable for the folder name
 
        

        # Check if the file exists
        if os.path.exists(destination_path):
            # Step 1: Read the JSON file
            with open(destination_path, 'r') as file:
                # Read the JSON data
                json_data = file.read()

            # Step 2: Parse the JSON data
            data = json.loads(json_data)

            # Step 3: Access the data
            # Example: Assuming the JSON structure is {"key": "value"}
            value = data['readings']
            print(value)
            last_reading = data["readings"][-1]
            print(last_reading)
            
        else:
            pass
    name1=last_reading["patient_name"]
    print(name1)
    phone1=last_reading["patient_phone_no"]
    age1=last_reading["patient_age"]
    date1=last_reading["date"]
    height1=last_reading["height"]
    formatted_height="{:.3f}".format(height1)  
    weight1=last_reading["weight"]
    formatted_weight="{:.3f}".format(weight1)  
    temperature1=last_reading["temperature"]
    formatted_temperature="{:.3f}".format(temperature1)  
    heartrate1=last_reading["heartrate"]
    formatted_heartrate="{:.3f}".format(heartrate1) 
    spo2=last_reading["spo2"]
    formatted_spo2="{:.3f}".format(spo2) 
    bmi1=last_reading["bmi"]
    formatted_bmi="{:.3f}".format(bmi1)
    bmi_classification=last_reading["bmi_classification"]

    name2 = f"Name: {name1}"
    phone2 = f"Phone No: {phone1}"
    age2 = f"Age: {age1}"
    date2 = f"Date: {date1}"
    height2 = f"Height: {formatted_height}"+"cm"
    weight2 = f"Weight: {formatted_weight}"+"kg"
    temperature2 = f"Temperature: {formatted_temperature}"+"c"
    heartrate2 = f"Heartrate: {formatted_heartrate}"+"bpm"
    spo22=f"Spo2: {formatted_spo2}"+"%"
    bmi2=f"Bmi: {formatted_bmi}"
    bmi_classification2=f"Bmi Classification: {bmi_classification}"

    label1=Label(tab9, text="Current Record",font=custom_font5,bg="#9ee8f0", fg="#111212",height=2,width=15)
    label1.place(relx=0.5, rely=0.1, anchor="center")
    label2=Label(tab9, text=name2,font=custom_font5,bg="#9ee8f0", fg="#111212",width=25)
    label2.place(relx=0.25, rely=0.25, anchor="center")
    label3=Label(tab9, text=phone2,font=custom_font5,bg="#9ee8f0", fg="#111212",width=25)
    label3.place(relx=0.75, rely=0.25, anchor="center")
    label4=Label(tab9, text=age2,font=custom_font5,bg="#9ee8f0", fg="#111212",width=25)
    label4.place(relx=0.25, rely=0.35, anchor="center")
    label5=Label(tab9, text=height2,font=custom_font5,bg="#9ee8f0", fg="#111212",width=25)
    label5.place(relx=0.75, rely=0.35, anchor="center")
    label6=Label(tab9, text=weight2,font=custom_font5,bg="#9ee8f0", fg="#111212",width=25)
    label6.place(relx=0.25, rely=0.45, anchor="center")
    label7=Label(tab9, text=temperature2,font=custom_font5,bg="#9ee8f0", fg="#111212",width=25)
    label7.place(relx=0.75, rely=0.45, anchor="center")
    label8=Label(tab9, text=heartrate2,font=custom_font5,bg="#9ee8f0", fg="#111212",width=25)
    label8.place(relx=0.25, rely=0.55, anchor="center")
    label9=Label(tab9, text=spo22,font=custom_font5,bg="#9ee8f0", fg="#111212",width=25)
    label9.place(relx=0.75, rely=0.55, anchor="center")
    label10=Label(tab9, text=bmi2,font=custom_font5,bg="#9ee8f0", fg="#111212",width=25)
    label10.place(relx=0.25, rely=0.65, anchor="center")
    label11=Label(tab9, text=bmi_classification2,font=custom_font5,bg="#9ee8f0", fg="#111212",width=25)
    label11.place(relx=0.75, rely=0.65, anchor="center")
    label12=Label(tab9, text="Description:",font=custom_font5,bg="#9ee8f0", fg="#111212",width=10)
    label12.place(relx=0.15, rely=0.75, anchor="center")
    text_entry = Text(tab9, wrap="word", height=4, width=50)  # Set wrap to "word" for word wrapping
    text_entry.place(relx=0.60, rely=0.79, anchor="center")
    text = text_entry.get("1.0", "end-1c") 
    button1 = Button(tab9, text="Submit", font=custom_font5, bg="#9ee8f0", fg="#111212", command=update)
    button1.place(relx=0.5, rely=0.95, anchor="center")

def new5():
    global tab5
    tab5 = Toplevel()
    tab5.title("MediSense System")
    tab5.geometry(root.geometry())
    back1_label = Label(tab5, image=back1)
    back1_label.place(x=0, y=0, relwidth=1, relheight=1)
    label1=Label(tab5, text="Patient Id:",font=custom_font5,bg="#9ee8f0", fg="#111212")
    label1.place(relx=0.25, rely=0.2, anchor="center")
    username_entry = Entry(tab5,width=30)
    username_entry.place(relx=0.7, rely=0.2, anchor="center")
    button1 = Button(tab5, text="Submit", font=custom_font5, bg="#9ee8f0", fg="#111212", command=lambda: new7(username_entry.get()))
    button1.place(relx=0.45, rely=0.3, anchor="center")

def new3():
    tab3 = Toplevel()
    tab3.title("MediSense System")
    tab3.geometry(root.geometry())
    back1_label = Label(tab3, image=back1)
    back1_label.place(x=0, y=0, relwidth=1, relheight=1)
    button1 = Button(tab3, text="Manage Availability", font=custom_font1, bg="#9ee8f0", fg="#111212", command=new4, width=15, height=1)
    button1.place(relx=0.25, rely=0.45, anchor="center")
    button2 = Button(tab3, text="Patient Records", font=custom_font1, bg="#9ee8f0", fg="#111212", command=new5, width=15, height=1)
    button2.place(relx=0.75, rely=0.45, anchor="center")

def signup(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Signup successful!")
    except sqlite3.IntegrityError:
        conn.close()
        messagebox.showerror("Error", "Username already exists. Please choose a different username.")

def login(username, password):
    global name
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone()
    conn.close()
    if user:
        messagebox.showinfo("Success", "Login successful!")
        name=user[1]
        print(name)
        new3()
    else:
        messagebox.showerror("Error", "Invalid username or password.")
    


def new1():
    tab1 = Toplevel()
    tab1.title("MediSense System")
    tab1.geometry(root.geometry())
    back1_label = Label(tab1, image=back1)
    back1_label.place(x=0, y=0, relwidth=1, relheight=1)
    label1=Label(tab1, text="Username:",font=custom_font5,bg="#9ee8f0", fg="#111212")
    label1.place(relx=0.30, rely=0.20, anchor="center")
    username_entry = Entry(tab1,width=30)
    username_entry.place(relx=0.67, rely=0.20, anchor="center")
    label2=Label(tab1, text="Password:",font=custom_font5,bg="#9ee8f0", fg="#111212")
    label2.place(relx=0.30, rely=0.30, anchor="center")
    password_entry = Entry(tab1,width=30, show="*")
    password_entry.place(relx=0.67, rely=0.30, anchor="center")
    button1=Button(tab1, text="Sign Up",font=custom_font5, command=lambda: signup(username_entry.get(), password_entry.get()))
    button1.place(relx=0.47, rely=0.45, anchor="center")

def new2():
    tab2 = Toplevel()
    tab2.title("MediSense System")
    tab2.geometry(root.geometry())
    back1_label = Label(tab2, image=back1)
    back1_label.place(x=0, y=0, relwidth=1, relheight=1)
    label1=Label(tab2, text="Username:",font=custom_font5,bg="#9ee8f0", fg="#111212")
    label1.place(relx=0.30, rely=0.20, anchor="center")
    username_entry = Entry(tab2,width=30)
    username_entry.place(relx=0.67, rely=0.20, anchor="center")
    label2=Label(tab2, text="Password:",font=custom_font5,bg="#9ee8f0", fg="#111212")
    label2.place(relx=0.30, rely=0.30, anchor="center")
    password_entry = Entry(tab2,width=30, show="*")
    password_entry.place(relx=0.67, rely=0.30, anchor="center")
    button1=Button(tab2, text="Sign Up",font=custom_font5, command=lambda: login(username_entry.get(), password_entry.get()))
    button1.place(relx=0.47, rely=0.45, anchor="center")


global back,back_label,custom_font5
root = Tk()
root.geometry("600x400")
root.title("MediSense System")
back = ImageTk.PhotoImage(Image.open(r"C:\pyy\project\main 3.jpg"))
back1 = ImageTk.PhotoImage(Image.open(r"C:\pyy\project\main4.jpg"))
back_label = Label(root, image=back)
back_label.place(x=0, y=0, relwidth=1, relheight=1)  # Use place() to cover the entire window
custom_font = Font(family="Arial", size=20, weight="bold")
custom_font1= Font(family="Arial", size=15, weight="bold")
custom_font5= Font(family="Arial", size=13, weight="bold")
label1 = Label(root, text="MediSense System", font=custom_font,bg="#fcfafa",fg="#111212",width=15, height=1)#f00a1d
label1.place(relx=0.25, rely=0.35, anchor="center")  # Center the label horizontally and vertically
button1 = Button(root, text="Sign Up", font=custom_font1, bg="#9ee8f0", fg="#111212", command=new1, width=8, height=1)
button1.place(relx=0.25, rely=0.55, anchor="center")
button2 = Button(root, text="Log in", font=custom_font1, bg="#9ee8f0", fg="#111212", command=new2, width=8, height=1)
button2.place(relx=0.25, rely=0.70, anchor="center")



root.mainloop()