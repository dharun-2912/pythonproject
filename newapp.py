
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
import pyttsx3
# Get current date and time
current_datetime = datetime.datetime.now()
global current_day,current_month,current_year,current_hour,current_minute,a00


# Extract date, month, year, hour, minute, and second
current_day = current_datetime.day
current_month = current_datetime.month
current_year = current_datetime.year
current_hour = current_datetime.hour
current_minute = current_datetime.minute
current_second = current_datetime.second

# Print the extracted values
print("Date:", current_day)
print("Month:", current_month)
print("Year:", current_year)
print("Hour:", current_hour)
print("Minute:", current_minute)
print("Second:", current_second)
global formatted_date
current_date = datetime.date.today()

# Format the current date as 'DD-MM-YYYY'
formatted_date = current_date.strftime("%d-%m-%Y")


conn = sqlite3.connect('time_tablebook.db')
c = conn.cursor()

# Execute a SELECT query to fetch the data
c.execute("SELECT * FROM time")

# Fetch the result
result = c.fetchone()

# Accessing the value '27' from the result
day_to_print = result[0]
month_to_print = result[1]
year_to_print = result[2]
print(day_to_print)
print(month_to_print)
print(year_to_print)  # Output: 27

# Close the connection

if current_day != day_to_print or current_month != month_to_print or current_year != year_to_print:
    new_values = (current_day, current_month, current_year, 
              1, 1, 1, 1, 
              1, 1, 1, 1, 
              1, 1, 1, 1,  
              1, 1, 1, 1,  
              1, 1, 1, 1,  
              1, 1, 1, 1,  
              1, 1, 1, 1,  
              1, 1, 1, 1,  
              1, 1, 1, 1,  
              1, 1, 1, 1,  
              1, 1, 1, 1,  
              1, 1, 1, 1,  
              1, 1, 1, 1, 
              1, 1, 1, 1,  
              1, 1, 1, 1,  
              1, 1, 1, 1,
              1, 1, 1, 1, 
              1, 1, 1, 1, 
              1, 1, 1, 1,  
              1, 1, 1, 1,  
              1, 1, 1, 1,  
              1, 1, 1, 1,  
              1, 1, 1, 1,  
              1, 1, 1, 1,  
              1, 1, 1, 1,  
              1, 1, 1, 1,  
              1, 1, 1, 1,  
              1, 1, 1, 1,  
              1, 1, 1, 1, 
              1, 1, 1, 1,  
              1, 1, 1, 1,  
              1, 1, 1, 1)

    c.execute("""
    UPDATE time
    SET date=?, day=?, year=?,
        a0=?, b0=?, c0=?, d0=?,
        A0_1=?,B0_1=?,C0_1=?,D0_1=?,
        a1=?, b1=?, c1=?, d1=?,
        A1_1=?,B1_1=?,C1_1=?,D1_1=?,
        a2=?, b2=?, c2=?, d2=?,
        A2_1=?,B2_1=?,C2_1=?,D2_1=?,
        a3=?, b3=?, c3=?, d3=?,
        A3_1=?,B3_1=?,C3_1=?,D3_1=?,
        e0=?, f0=?, g0=?, h0=?,
        E0_1=?,F0_1=?,G0_1=?,H0_1=?,
        e1=?, f1=?, g1=?, h1=?,
        E1_1=?,F1_1=?,G1_1=?,H1_1=?,
        e2=?, f2=?, g2=?, h2=?,
        E2_1=?,F2_1=?,G2_1=?,H2_1=?,
        e3=?, f3=?, g3=?, h3=?,
        E3_1=?,F3_1=?,G3_1=?,H3_1=?,
        i0=?, j0=?, k0=?, l0=?,
        I0_1=?,J0_1=?,K0_1=?,L0_1=?,
        i1=?, j1=?, k1=?, l1=?,
        I1_1=?,J1_1=?,K1_1=?,L1_1=?,
        i2=?, j2=?, k2=?, l2=?,
        I2_1=?,J2_1=?,K2_1=?,L2_1=?,
        i3=?, j3=?, k3=?, l3=?,
        I3_1=?,J3_1=?,K3_1=?,L3_1=?,
        m0=?, n0=?, o0=?, p0=?,
        M0_1=?,N0_1=?,O0_1=?,P0_1=?,
        m1=?, n1=?, o1=?, p1=?,
        M1_1=?,N1_1=?,O1_1=?,P1_1=?,
        m2=?, n2=?, o2=?, p2=?,
        M2_1=?,N2_1=?,O2_1=?,P2_1=?,
        m3=?, n3=?, o3=?, p3=?,
        M3_1=?,N3_1=?,O3_1=?,P3_1=?
    WHERE oid=1
    """, new_values)
    # Commit the transaction
conn.commit()

# Close the connection
conn.close()


conn = sqlite3.connect('time_tablebook.db')
c=conn.cursor()
c.execute("SELECT *,oid FROM time")
records=c.fetchall()
print(records)
# Commit the transaction
conn.commit()

# Close the connection
conn.close()

def a0():
    conn = sqlite3.connect('time_tablebook.db')  
    c = conn.cursor()
    new_values = (0,)

    c.execute("""
            UPDATE time
            SET A0_1=?
            WHERE oid=1
            """, new_values)

     # Commit the transaction
    
    conn.commit()
    conn.close
    engine1 = pyttsx3.init()
    voices = engine1.getProperty('voices')       #getting details of current voice
    #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
    engine1.setProperty('rate', 150) 
    engine1.say(" appointment is fixed ")
    engine1.runAndWait()
    response=messagebox.askyesno("Appointment","Your appointment is fixed with Dr. Arun at 9:00")
    if response:
         root.quit()
def b0():
    conn = sqlite3.connect('time_tablebook.db')  
    c = conn.cursor()
    new_values = (0,)

    c.execute("""
            UPDATE time
            SET B0_1=?
            WHERE oid=1
            """, new_values)

     # Commit the transaction
    
    conn.commit()
    conn.close
    engine1 = pyttsx3.init()
    voices = engine1.getProperty('voices')       #getting details of current voice
    #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
    engine1.setProperty('rate', 150) 
    engine1.say(" appointment is fixed ")
    engine1.runAndWait()
    response=messagebox.askyesno("Appointment","Your appointment is fixed with Dr. Arun at 9:30")
    if response:
         root.quit()
def c0():
    conn = sqlite3.connect('time_tablebook.db')  
    c = conn.cursor()
    new_values = (0,)

    c.execute("""
            UPDATE time
            SET C0_1=?
            WHERE oid=1
            """, new_values)

     # Commit the transaction
    
    conn.commit()
    conn.close
    engine1 = pyttsx3.init()
    voices = engine1.getProperty('voices')       #getting details of current voice
    #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
    engine1.setProperty('rate', 150) 
    engine1.say(" appointment is fixed ")
    engine1.runAndWait()
    response=messagebox.askyesno("Appointment","Your appointment is fixed with Dr. Arun at 10:00")
    if response:
         root.quit()
def d0():
    conn = sqlite3.connect('time_tablebook.db')  
    c = conn.cursor()
    new_values = (0,)

    c.execute("""
            UPDATE time
            SET D0_1=?
            WHERE oid=1
            """, new_values)

     # Commit the transaction
    
    conn.commit()
    conn.close
    engine1 = pyttsx3.init()
    voices = engine1.getProperty('voices')       #getting details of current voice
    #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
    engine1.setProperty('rate', 150) 
    engine1.say(" appointment is fixed ")
    engine1.runAndWait()
    response=messagebox.askyesno("Appointment","Your appointment is fixed with Dr. Arun at 10:30")
    if response:
         root.quit()
def a1():
    conn = sqlite3.connect('time_tablebook.db')  
    c = conn.cursor()
    new_values = (0,)

    c.execute("""
            UPDATE time
            SET A1_1=?
            WHERE oid=1
            """, new_values)

     # Commit the transaction
    
    conn.commit()
    conn.close
    engine1 = pyttsx3.init()
    voices = engine1.getProperty('voices')       #getting details of current voice
    #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
    engine1.setProperty('rate', 150) 
    engine1.say(" appointment is fixed ")
    engine1.runAndWait()
    response=messagebox.askyesno("Appointment","Your appointment is fixed with Dr. Paul at 11:00")
    if response:
         root.quit()
def b1():
    conn = sqlite3.connect('time_tablebook.db')  
    c = conn.cursor()
    new_values = (0,)

    c.execute("""
            UPDATE time
            SET B1_1=?
            WHERE oid=1
            """, new_values)

     # Commit the transaction
    
    conn.commit()
    conn.close
    engine1 = pyttsx3.init()
    voices = engine1.getProperty('voices')       #getting details of current voice
    #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
    engine1.setProperty('rate', 150) 
    engine1.say(" appointment is fixed ")
    engine1.runAndWait()
    response=messagebox.askyesno("Appointment","Your appointment is fixed with Dr. Paul at 11:30")
    if response:
         root.quit()
def c1():
    conn = sqlite3.connect('time_tablebook.db')  
    c = conn.cursor()
    new_values = (0,)

    c.execute("""
            UPDATE time
            SET C1_1=?
            WHERE oid=1
            """, new_values)

     # Commit the transaction
    
    conn.commit()
    conn.close
    engine1 = pyttsx3.init()
    voices = engine1.getProperty('voices')       #getting details of current voice
    #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
    engine1.setProperty('rate', 150) 
    engine1.say(" appointment is fixed ")
    engine1.runAndWait()
    response=messagebox.askyesno("Appointment","Your appointment is fixed with Dr. Paul at 12:00")
    if response:
         root.quit()
def d1():
    conn = sqlite3.connect('time_tablebook.db')  
    c = conn.cursor()
    new_values = (0,)

    c.execute("""
            UPDATE time
            SET D1_1=?
            WHERE oid=1
            """, new_values)

     # Commit the transaction
    
    conn.commit()
    conn.close
    engine1 = pyttsx3.init()
    voices = engine1.getProperty('voices')       #getting details of current voice
    #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
    engine1.setProperty('rate', 150) 
    engine1.say(" appointment is fixed ")
    engine1.runAndWait()
    response=messagebox.askyesno("Appointment","Your appointment is fixed with Dr. Paul at 12:30")
    if response:
         root.quit()
def a2():
    conn = sqlite3.connect('time_tablebook.db')  
    c = conn.cursor()
    new_values = (0,)

    c.execute("""
            UPDATE time
            SET A2_1=?
            WHERE oid=1
            """, new_values)

     # Commit the transaction
    
    conn.commit()
    conn.close
    engine1 = pyttsx3.init()
    voices = engine1.getProperty('voices')       #getting details of current voice
    #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
    engine1.setProperty('rate', 150) 
    engine1.say(" appointment is fixed ")
    engine1.runAndWait()
    response=messagebox.askyesno("Appointment","Your appointment is fixed with Dr. Karan at 2:00")
    if response:
         root.quit()
def b2():
    conn = sqlite3.connect('time_tablebook.db')  
    c = conn.cursor()
    new_values = (0,)

    c.execute("""
            UPDATE time
            SET B2_1=?
            WHERE oid=1
            """, new_values)

     # Commit the transaction
    
    conn.commit()
    conn.close
    engine1 = pyttsx3.init()
    voices = engine1.getProperty('voices')       #getting details of current voice
    #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
    engine1.setProperty('rate', 150) 
    engine1.say(" appointment is fixed ")
    engine1.runAndWait()
    response=messagebox.askyesno("Appointment","Your appointment is fixed with Dr. Karan at 2:30")
    if response:
         root.quit()
def c2():
    conn = sqlite3.connect('time_tablebook.db')  
    c = conn.cursor()
    new_values = (0,)

    c.execute("""
            UPDATE time
            SET C2_1=?
            WHERE oid=1
            """, new_values)

     # Commit the transaction
    
    conn.commit()
    conn.close
    engine1 = pyttsx3.init()
    voices = engine1.getProperty('voices')       #getting details of current voice
    #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
    engine1.setProperty('rate', 150) 
    engine1.say(" appointment is fixed ")
    engine1.runAndWait()
    response=messagebox.askyesno("Appointment","Your appointment is fixed with Dr. Karan at 3:00")
    if response:
         root.quit()
def d2():
    conn = sqlite3.connect('time_tablebook.db')  
    c = conn.cursor()
    new_values = (0,)

    c.execute("""
            UPDATE time
            SET D2_1=?
            WHERE oid=1
            """, new_values)

     # Commit the transaction
    
    conn.commit()
    conn.close
    engine1 = pyttsx3.init()
    voices = engine1.getProperty('voices')       #getting details of current voice
    #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
    engine1.setProperty('rate', 150) 
    engine1.say(" appointment is fixed ")
    engine1.runAndWait()
    response=messagebox.askyesno("Appointment","Your appointment is fixed with Dr. Karan at 3:30")
    if response:
         root.quit()
def a3():
    conn = sqlite3.connect('time_tablebook.db')  
    c = conn.cursor()
    new_values = (0,)

    c.execute("""
            UPDATE time
            SET A3_1=?
            WHERE oid=1
            """, new_values)

     # Commit the transaction
    
    conn.commit()
    conn.close
    engine1 = pyttsx3.init()
    voices = engine1.getProperty('voices')       #getting details of current voice
    #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
    engine1.setProperty('rate', 150) 
    engine1.say(" appointment is fixed ")
    engine1.runAndWait()
    response=messagebox.askyesno("Appointment","Your appointment is fixed with Dr. Kishore at 4:00")
    if response:
         root.quit()
def b3():
    conn = sqlite3.connect('time_tablebook.db')  
    c = conn.cursor()
    new_values = (0,)

    c.execute("""
            UPDATE time
            SET B3_1=?
            WHERE oid=1
            """, new_values)

     # Commit the transaction
    
    conn.commit()
    conn.close
    engine1 = pyttsx3.init()
    voices = engine1.getProperty('voices')       #getting details of current voice
    #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
    engine1.setProperty('rate', 150) 
    engine1.say(" appointment is fixed ")
    engine1.runAndWait()
    response=messagebox.askyesno("Appointment","Your appointment is fixed with Dr. Kishore at 4:30")
    if response:
         root.quit()
def c3():
    conn = sqlite3.connect('time_tablebook.db')  
    c = conn.cursor()
    new_values = (0,)

    c.execute("""
            UPDATE time
            SET C3_1=?
            WHERE oid=1
            """, new_values)

     # Commit the transaction
    
    conn.commit()
    conn.close
    engine1 = pyttsx3.init()
    voices = engine1.getProperty('voices')       #getting details of current voice
    #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
    engine1.setProperty('rate', 150) 
    engine1.say(" appointment is fixed ")
    engine1.runAndWait()
    response=messagebox.askyesno("Appointment","Your appointment is fixed with Dr. Kishore at 5:00")
    if response:
         root.quit()
def d3():
    conn = sqlite3.connect('time_tablebook.db')  
    c = conn.cursor()
    new_values = (0,)

    c.execute("""
            UPDATE time
            SET D3_1=?
            WHERE oid=1
            """, new_values)

     # Commit the transaction
    
    conn.commit()
    conn.close
    engine1 = pyttsx3.init()
    voices = engine1.getProperty('voices')       #getting details of current voice
    #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
    engine1.setProperty('rate', 150) 
    engine1.say(" appointment is fixed ")
    engine1.runAndWait()
    response=messagebox.askyesno("Appointment","Your appointment is fixed with Dr. Kishore at 5:30")
    if response:
         root.quit()

def e0():
    conn = sqlite3.connect('time_tablebook.db')  
    c = conn.cursor()
    new_values = (0,)

    c.execute("""
            UPDATE time
            SET E0_1=?
            WHERE oid=1
            """, new_values)

     # Commit the transaction
    
    conn.commit()
    conn.close
    engine1 = pyttsx3.init()
    voices = engine1.getProperty('voices')       #getting details of current voice
    #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
    engine1.setProperty('rate', 150) 
    engine1.say(" appointment is fixed ")
    engine1.runAndWait()
    response=messagebox.askyesno("Appointment","Your appointment is fixed with Dr. Raj at 9:00")
    if response:
         root.quit()
def f0():
    conn = sqlite3.connect('time_tablebook.db')  
    c = conn.cursor()
    new_values = (0,)

    c.execute("""
            UPDATE time
            SET F0_1=?
            WHERE oid=1
            """, new_values)

     # Commit the transaction
    
    conn.commit()
    conn.close
    engine1 = pyttsx3.init()
    voices = engine1.getProperty('voices')       #getting details of current voice
    #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
    engine1.setProperty('rate', 150) 
    engine1.say(" appointment is fixed ")
    engine1.runAndWait()
    response=messagebox.askyesno("Appointment","Your appointment is fixed with Dr. Raj at 9:30")
    if response:
         root.quit()
def g0():
    conn = sqlite3.connect('time_tablebook.db')  
    c = conn.cursor()
    new_values = (0,)

    c.execute("""
            UPDATE time
            SET G0_1=?
            WHERE oid=1
            """, new_values)

     # Commit the transaction
    
    conn.commit()
    conn.close
    engine1 = pyttsx3.init()
    voices = engine1.getProperty('voices')       #getting details of current voice
    #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
    engine1.setProperty('rate', 150) 
    engine1.say(" appointment is fixed ")
    engine1.runAndWait()
    response=messagebox.askyesno("Appointment","Your appointment is fixed with Dr. Raj at 10:00")
    if response:
         root.quit()
def h0():
    conn = sqlite3.connect('time_tablebook.db')  
    c = conn.cursor()
    new_values = (0,)

    c.execute("""
            UPDATE time
            SET H0_1=?
            WHERE oid=1
            """, new_values)

     # Commit the transaction
    
    conn.commit()
    conn.close
    engine1 = pyttsx3.init()
    voices = engine1.getProperty('voices')       #getting details of current voice
    #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
    engine1.setProperty('rate', 150) 
    engine1.say(" appointment is fixed ")
    engine1.runAndWait()
    response=messagebox.askyesno("Appointment","Your appointment is fixed with Dr. Raj at 10:30")
    if response:
         root.quit()
def e1():
    conn = sqlite3.connect('time_tablebook.db')  
    c = conn.cursor()
    new_values = (0,)

    c.execute("""
            UPDATE time
            SET E1_1=?
            WHERE oid=1
            """, new_values)

     # Commit the transaction
    
    conn.commit()
    conn.close
    engine1 = pyttsx3.init()
    voices = engine1.getProperty('voices')       #getting details of current voice
    #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
    engine1.setProperty('rate', 150) 
    engine1.say(" appointment is fixed ")
    engine1.runAndWait()
    response=messagebox.askyesno("Appointment","Your appointment is fixed with Dr. Kajal at 11:00")
    if response:
         root.quit()
def f1():
    conn = sqlite3.connect('time_tablebook.db')  
    c = conn.cursor()
    new_values = (0,)

    c.execute("""
            UPDATE time
            SET F1_1=?
            WHERE oid=1
            """, new_values)

     # Commit the transaction
    
    conn.commit()
    conn.close
    engine1 = pyttsx3.init()
    voices = engine1.getProperty('voices')       #getting details of current voice
    #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
    engine1.setProperty('rate', 150) 
    engine1.say(" appointment is fixed ")
    engine1.runAndWait()
    response=messagebox.askyesno("Appointment","Your appointment is fixed with Dr. Kajal at 11:30")
    if response:
         root.quit()
def g1():
    conn = sqlite3.connect('time_tablebook.db')  
    c = conn.cursor()
    new_values = (0,)

    c.execute("""
            UPDATE time
            SET G1_1=?
            WHERE oid=1
            """, new_values)

     # Commit the transaction
    
    conn.commit()
    conn.close
    engine1 = pyttsx3.init()
    voices = engine1.getProperty('voices')       #getting details of current voice
    #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
    engine1.setProperty('rate', 150) 
    engine1.say(" appointment is fixed ")
    engine1.runAndWait()
    response=messagebox.askyesno("Appointment","Your appointment is fixed with Dr. Kajal at 12:00")
    if response:
         root.quit()
def h1():
    conn = sqlite3.connect('time_tablebook.db')  
    c = conn.cursor()
    new_values = (0,)

    c.execute("""
            UPDATE time
            SET H1_1=?
            WHERE oid=1
            """, new_values)

     # Commit the transaction
    
    conn.commit()
    conn.close
    engine1 = pyttsx3.init()
    voices = engine1.getProperty('voices')       #getting details of current voice
    #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
    engine1.setProperty('rate', 150) 
    engine1.say(" appointment is fixed ")
    engine1.runAndWait()
    response=messagebox.askyesno("Appointment","Your appointment is fixed with Dr. Kajal at 12:30")
    if response:
         root.quit()
def e2():
    conn = sqlite3.connect('time_tablebook.db')  
    c = conn.cursor()
    new_values = (0,)

    c.execute("""
            UPDATE time
            SET E2_1=?
            WHERE oid=1
            """, new_values)

     # Commit the transaction
    
    conn.commit()
    conn.close
    engine1 = pyttsx3.init()
    voices = engine1.getProperty('voices')       #getting details of current voice
    #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
    engine1.setProperty('rate', 150) 
    engine1.say(" appointment is fixed ")
    engine1.runAndWait()
    response=messagebox.askyesno("Appointment","Your appointment is fixed with Dr. Kapoor at 2:00")
    if response:
         root.quit()
def f2():
    conn = sqlite3.connect('time_tablebook.db')  
    c = conn.cursor()
    new_values = (0,)

    c.execute("""
            UPDATE time
            SET F2_1=?
            WHERE oid=1
            """, new_values)

     # Commit the transaction
    
    conn.commit()
    conn.close
    engine1 = pyttsx3.init()
    voices = engine1.getProperty('voices')       #getting details of current voice
    #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
    engine1.setProperty('rate', 150) 
    engine1.say(" appointment is fixed ")
    engine1.runAndWait()
    response=messagebox.askyesno("Appointment","Your appointment is fixed with Dr. Kapoor at 2:30")
    if response:
         root.quit()
def g2():
    conn = sqlite3.connect('time_tablebook.db')  
    c = conn.cursor()
    new_values = (0,)

    c.execute("""
            UPDATE time
            SET G2_1=?
            WHERE oid=1
            """, new_values)

     # Commit the transaction
    
    conn.commit()
    conn.close
    engine1 = pyttsx3.init()
    voices = engine1.getProperty('voices')       #getting details of current voice
    #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
    engine1.setProperty('rate', 150) 
    engine1.say(" appointment is fixed ")
    engine1.runAndWait()
    response=messagebox.askyesno("Appointment","Your appointment is fixed with Dr. Kapoor at 3:00")
    if response:
         root.quit()
def h2():
    conn = sqlite3.connect('time_tablebook.db')  
    c = conn.cursor()
    new_values = (0,)

    c.execute("""
            UPDATE time
            SET H2_1=?
            WHERE oid=1
            """, new_values)

     # Commit the transaction
    
    conn.commit()
    conn.close
    engine1 = pyttsx3.init()
    voices = engine1.getProperty('voices')       #getting details of current voice
    #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
    engine1.setProperty('rate', 150) 
    engine1.say(" appointment is fixed ")
    engine1.runAndWait()
    response=messagebox.askyesno("Appointment","Your appointment is fixed with Dr. Kapoor at 3:30")
    if response:
         root.quit()
def e3():
    conn = sqlite3.connect('time_tablebook.db')  
    c = conn.cursor()
    new_values = (0,)

    c.execute("""
            UPDATE time
            SET E3_1=?
            WHERE oid=1
            """, new_values)

     # Commit the transaction
    
    conn.commit()
    conn.close
    engine1 = pyttsx3.init()
    voices = engine1.getProperty('voices')       #getting details of current voice
    #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
    engine1.setProperty('rate', 150) 
    engine1.say(" appointment is fixed ")
    engine1.runAndWait()
    response=messagebox.askyesno("Appointment","Your appointment is fixed with Dr. Hari at 4:00")
    if response:
         root.quit()
def f3():
    conn = sqlite3.connect('time_tablebook.db')  
    c = conn.cursor()
    new_values = (0,)

    c.execute("""
            UPDATE time
            SET F3_1=?
            WHERE oid=1
            """, new_values)

     # Commit the transaction
    
    conn.commit()
    conn.close
    engine1 = pyttsx3.init()
    voices = engine1.getProperty('voices')       #getting details of current voice
    #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
    engine1.setProperty('rate', 150) 
    engine1.say(" appointment is fixed ")
    engine1.runAndWait()
    response=messagebox.askyesno("Appointment","Your appointment is fixed with Dr. Hari at 4:30")
    if response:
         root.quit()
def g3():
    conn = sqlite3.connect('time_tablebook.db')  
    c = conn.cursor()
    new_values = (0,)

    c.execute("""
            UPDATE time
            SET G3_1=?
            WHERE oid=1
            """, new_values)

     # Commit the transaction
    
    conn.commit()
    conn.close
    engine1 = pyttsx3.init()
    voices = engine1.getProperty('voices')       #getting details of current voice
    #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
    engine1.setProperty('rate', 150) 
    engine1.say(" appointment is fixed ")
    engine1.runAndWait()
    response=messagebox.askyesno("Appointment","Your appointment is fixed with Dr. Hari at 5:00")
    if response:
         root.quit()
def h3():
    conn = sqlite3.connect('time_tablebook.db')  
    c = conn.cursor()
    new_values = (0,)

    c.execute("""
            UPDATE time
            SET H3_1=?
            WHERE oid=1
            """, new_values)

     # Commit the transaction
    
    conn.commit()
    conn.close
    engine1 = pyttsx3.init()
    voices = engine1.getProperty('voices')       #getting details of current voice
    #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
    engine1.setProperty('rate', 150) 
    engine1.say(" appointment is fixed ")
    engine1.runAndWait()
    response=messagebox.askyesno("Appointment","Your appointment is fixed with Dr. Hari at 5:30")
    if response:
         root.quit()

def i0():
    conn = sqlite3.connect('time_tablebook.db')  
    c = conn.cursor()
    new_values = (0,)

    c.execute("""
            UPDATE time
            SET I0_1=?
            WHERE oid=1
            """, new_values)

     # Commit the transaction
    
    conn.commit()
    conn.close
    engine1 = pyttsx3.init()
    voices = engine1.getProperty('voices')       #getting details of current voice
    #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
    engine1.setProperty('rate', 150) 
    engine1.say(" appointment is fixed ")
    engine1.runAndWait()
    response=messagebox.askyesno("Appointment","Your appointment is fixed with Dr. Sanjay at 9:00")
    if response:
         root.quit()
def j0():
    conn = sqlite3.connect('time_tablebook.db')  
    c = conn.cursor()
    new_values = (0,)

    c.execute("""
            UPDATE time
            SET J0_1=?
            WHERE oid=1
            """, new_values)

     # Commit the transaction
    
    conn.commit()
    conn.close
    engine1 = pyttsx3.init()
    voices = engine1.getProperty('voices')       #getting details of current voice
    #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
    engine1.setProperty('rate', 150) 
    engine1.say(" appointment is fixed ")
    engine1.runAndWait()
    response=messagebox.askyesno("Appointment","Your appointment is fixed with Dr. Sanjay at 9:30")
    if response:
         root.quit()
def k0():
    conn = sqlite3.connect('time_tablebook.db')  
    c = conn.cursor()
    new_values = (0,)

    c.execute("""
            UPDATE time
            SET K0_1=?
            WHERE oid=1
            """, new_values)

     # Commit the transaction
    
    conn.commit()
    conn.close
    engine1 = pyttsx3.init()
    voices = engine1.getProperty('voices')       #getting details of current voice
    #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
    engine1.setProperty('rate', 150) 
    engine1.say(" appointment is fixed ")
    engine1.runAndWait()
    response=messagebox.askyesno("Appointment","Your appointment is fixed with Dr. Sanjay at 10:00")
    if response:
         root.quit()
def l0():
    conn = sqlite3.connect('time_tablebook.db')  
    c = conn.cursor()
    new_values = (0,)

    c.execute("""
            UPDATE time
            SET L0_1=?
            WHERE oid=1
            """, new_values)

     # Commit the transaction
    
    conn.commit()
    conn.close
    engine1 = pyttsx3.init()
    voices = engine1.getProperty('voices')       #getting details of current voice
    #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
    engine1.setProperty('rate', 150) 
    engine1.say(" appointment is fixed ")
    engine1.runAndWait()
    response=messagebox.askyesno("Appointment","Your appointment is fixed with Dr. Sanjay at 10:30")
    if response:
         root.quit()
def i1():
    conn = sqlite3.connect('time_tablebook.db')  
    c = conn.cursor()
    new_values = (0,)

    c.execute("""
            UPDATE time
            SET I1_1=?
            WHERE oid=1
            """, new_values)

     # Commit the transaction
    
    conn.commit()
    conn.close
    engine1 = pyttsx3.init()
    voices = engine1.getProperty('voices')       #getting details of current voice
    #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
    engine1.setProperty('rate', 150) 
    engine1.say(" appointment is fixed ")
    engine1.runAndWait()
    response=messagebox.askyesno("Appointment","Your appointment is fixed with Dr. Sundhar at 11:00")
    if response:
         root.quit()
def j1():
    conn = sqlite3.connect('time_tablebook.db')  
    c = conn.cursor()
    new_values = (0,)

    c.execute("""
            UPDATE time
            SET J1_1=?
            WHERE oid=1
            """, new_values)

     # Commit the transaction
    
    conn.commit()
    conn.close
    engine1 = pyttsx3.init()
    voices = engine1.getProperty('voices')       #getting details of current voice
    #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
    engine1.setProperty('rate', 150) 
    engine1.say(" appointment is fixed ")
    engine1.runAndWait()
    response=messagebox.askyesno("Appointment","Your appointment is fixed with Dr. Sundhar at 11:30")
    if response:
         root.quit()
def k1():
    conn = sqlite3.connect('time_tablebook.db')  
    c = conn.cursor()
    new_values = (0,)

    c.execute("""
            UPDATE time
            SET K1_1=?
            WHERE oid=1
            """, new_values)

     # Commit the transaction
    
    conn.commit()
    conn.close
    engine1 = pyttsx3.init()
    voices = engine1.getProperty('voices')       #getting details of current voice
    #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
    engine1.setProperty('rate', 150) 
    engine1.say(" appointment is fixed ")
    engine1.runAndWait()
    response=messagebox.askyesno("Appointment","Your appointment is fixed with Dr. Sundhar at 12:00")
    if response:
         root.quit()
def l1():
    conn = sqlite3.connect('time_tablebook.db')  
    c = conn.cursor()
    new_values = (0,)

    c.execute("""
            UPDATE time
            SET L1_1=?
            WHERE oid=1
            """, new_values)

     # Commit the transaction
    
    conn.commit()
    conn.close
    engine1 = pyttsx3.init()
    voices = engine1.getProperty('voices')       #getting details of current voice
    #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
    engine1.setProperty('rate', 150) 
    engine1.say(" appointment is fixed ")
    engine1.runAndWait()
    response=messagebox.askyesno("Appointment","Your appointment is fixed with Dr. Sundhar at 12:30")
    if response:
         root.quit()
def i2():
    conn = sqlite3.connect('time_tablebook.db')  
    c = conn.cursor()
    new_values = (0,)

    c.execute("""
            UPDATE time
            SET I2_1=?
            WHERE oid=1
            """, new_values)

     # Commit the transaction
    
    conn.commit()
    conn.close
    engine1 = pyttsx3.init()
    voices = engine1.getProperty('voices')       #getting details of current voice
    #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
    engine1.setProperty('rate', 150) 
    engine1.say(" appointment is fixed ")
    engine1.runAndWait()
    response=messagebox.askyesno("Appointment","Your appointment is fixed with Dr. Madhu at 2:00")
    if response:
         root.quit()
def j2():
    conn = sqlite3.connect('time_tablebook.db')  
    c = conn.cursor()
    new_values = (0,)

    c.execute("""
            UPDATE time
            SET J2_1=?
            WHERE oid=1
            """, new_values)

     # Commit the transaction
    
    conn.commit()
    conn.close
    engine1 = pyttsx3.init()
    voices = engine1.getProperty('voices')       #getting details of current voice
    #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
    engine1.setProperty('rate', 150) 
    engine1.say(" appointment is fixed ")
    engine1.runAndWait()
    response=messagebox.askyesno("Appointment","Your appointment is fixed with Dr. Madhu at 2:30")
    if response:
         root.quit()
def k2():
    conn = sqlite3.connect('time_tablebook.db')  
    c = conn.cursor()
    new_values = (0,)

    c.execute("""
            UPDATE time
            SET K2_1=?
            WHERE oid=1
            """, new_values)

     # Commit the transaction
    
    conn.commit()
    conn.close
    engine1 = pyttsx3.init()
    voices = engine1.getProperty('voices')       #getting details of current voice
    #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
    engine1.setProperty('rate', 150) 
    engine1.say(" appointment is fixed ")
    engine1.runAndWait()
    response=messagebox.askyesno("Appointment","Your appointment is fixed with Dr. Madhu at 3:00")
    if response:
         root.quit()
def l2():
    conn = sqlite3.connect('time_tablebook.db')  
    c = conn.cursor()
    new_values = (0,)

    c.execute("""
            UPDATE time
            SET L2_1=?
            WHERE oid=1
            """, new_values)

     # Commit the transaction
    
    conn.commit()
    conn.close
    engine1 = pyttsx3.init()
    voices = engine1.getProperty('voices')       #getting details of current voice
    #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
    engine1.setProperty('rate', 150) 
    engine1.say(" appointment is fixed ")
    engine1.runAndWait()
    response=messagebox.askyesno("Appointment","Your appointment is fixed with Dr. Madhu at 3:30")
    if response:
         root.quit()
def i3():
    conn = sqlite3.connect('time_tablebook.db')  
    c = conn.cursor()
    new_values = (0,)

    c.execute("""
            UPDATE time
            SET I3_1=?
            WHERE oid=1
            """, new_values)

     # Commit the transaction
    
    conn.commit()
    conn.close
    engine1 = pyttsx3.init()
    voices = engine1.getProperty('voices')       #getting details of current voice
    #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
    engine1.setProperty('rate', 150) 
    engine1.say(" appointment is fixed ")
    engine1.runAndWait()
    response=messagebox.askyesno("Appointment","Your appointment is fixed with Dr. Dharun at 4:00")
    if response:
         root.quit()
def j3():
    conn = sqlite3.connect('time_tablebook.db')  
    c = conn.cursor()
    new_values = (0,)

    c.execute("""
            UPDATE time
            SET J3_1=?
            WHERE oid=1
            """, new_values)

     # Commit the transaction
    
    conn.commit()
    conn.close
    engine1 = pyttsx3.init()
    voices = engine1.getProperty('voices')       #getting details of current voice
    #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
    engine1.setProperty('rate', 150) 
    engine1.say(" appointment is fixed ")
    engine1.runAndWait()
    response=messagebox.askyesno("Appointment","Your appointment is fixed with Dr. Dharun at 4:30")
    if response:
         root.quit()
def k3():
    conn = sqlite3.connect('time_tablebook.db')  
    c = conn.cursor()
    new_values = (0,)

    c.execute("""
            UPDATE time
            SET K3_1=?
            WHERE oid=1
            """, new_values)

     # Commit the transaction
    
    conn.commit()
    conn.close
    engine1 = pyttsx3.init()
    voices = engine1.getProperty('voices')       #getting details of current voice
    #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
    engine1.setProperty('rate', 150) 
    engine1.say(" appointment is fixed ")
    engine1.runAndWait()
    response=messagebox.askyesno("Appointment","Your appointment is fixed with Dr. Dharun at 5:00")
    if response:
         root.quit()
def l3():
    conn = sqlite3.connect('time_tablebook.db')  
    c = conn.cursor()
    new_values = (0,)

    c.execute("""
            UPDATE time
            SET L3_1=?
            WHERE oid=1
            """, new_values)

     # Commit the transaction
    
    conn.commit()
    conn.close
    engine1 = pyttsx3.init()
    voices = engine1.getProperty('voices')       #getting details of current voice
    #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
    engine1.setProperty('rate', 150) 
    engine1.say(" appointment is fixed ")
    engine1.runAndWait()
    response=messagebox.askyesno("Appointment","Your appointment is fixed with Dr. Dharun at 5:30")
    if response:
         root.quit()

def m0():
    conn = sqlite3.connect('time_tablebook.db')  
    c = conn.cursor()
    new_values = (0,)

    c.execute("""
            UPDATE time
            SET M0_1=?
            WHERE oid=1
            """, new_values)

     # Commit the transaction
    
    conn.commit()
    conn.close
    engine1 = pyttsx3.init()
    voices = engine1.getProperty('voices')       #getting details of current voice
    #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
    engine1.setProperty('rate', 150) 
    engine1.say(" appointment is fixed ")
    engine1.runAndWait()
    response=messagebox.askyesno("Appointment","Your appointment is fixed with Dr. Rahul at 9:00")
    if response:
         root.quit()
def n0():
    conn = sqlite3.connect('time_tablebook.db')  
    c = conn.cursor()
    new_values = (0,)

    c.execute("""
            UPDATE time
            SET N0_1=?
            WHERE oid=1
            """, new_values)

     # Commit the transaction
    
    conn.commit()
    conn.close
    engine1 = pyttsx3.init()
    voices = engine1.getProperty('voices')       #getting details of current voice
    #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
    engine1.setProperty('rate', 150) 
    engine1.say(" appointment is fixed ")
    engine1.runAndWait()
    response=messagebox.askyesno("Appointment","Your appointment is fixed with Dr. Rahul at 9:30")
    if response:
         root.quit()
def o0():
    conn = sqlite3.connect('time_tablebook.db')  
    c = conn.cursor()
    new_values = (0,)

    c.execute("""
            UPDATE time
            SET O0_1=?
            WHERE oid=1
            """, new_values)

     # Commit the transaction
    
    conn.commit()
    conn.close
    engine1 = pyttsx3.init()
    voices = engine1.getProperty('voices')       #getting details of current voice
    #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
    engine1.setProperty('rate', 150) 
    engine1.say(" appointment is fixed ")
    engine1.runAndWait()
    response=messagebox.askyesno("Appointment","Your appointment is fixed with Dr. Rahul at 10:00")
    if response:
         root.quit()
def p0():
    conn = sqlite3.connect('time_tablebook.db')  
    c = conn.cursor()
    new_values = (0,)

    c.execute("""
            UPDATE time
            SET P0_1=?
            WHERE oid=1
            """, new_values)

     # Commit the transaction
    
    conn.commit()
    conn.close
    engine1 = pyttsx3.init()
    voices = engine1.getProperty('voices')       #getting details of current voice
    #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
    engine1.setProperty('rate', 150) 
    engine1.say(" appointment is fixed ")
    engine1.runAndWait()
    response=messagebox.askyesno("Appointment","Your appointment is fixed with Dr. Rahul at 9:30")
    if response:
         root.quit()
def m1():
    conn = sqlite3.connect('time_tablebook.db')  
    c = conn.cursor()
    new_values = (0,)

    c.execute("""
            UPDATE time
            SET M1_1=?
            WHERE oid=1
            """, new_values)

     # Commit the transaction
    
    conn.commit()
    conn.close
    engine1 = pyttsx3.init()
    voices = engine1.getProperty('voices')       #getting details of current voice
    #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
    engine1.setProperty('rate', 150) 
    engine1.say(" appointment is fixed ")
    engine1.runAndWait()
    response=messagebox.askyesno("Appointment","Your appointment is fixed with Dr. Ram at 11:00")
    if response:
         root.quit()
def n1():
    conn = sqlite3.connect('time_tablebook.db')  
    c = conn.cursor()
    new_values = (0,)

    c.execute("""
            UPDATE time
            SET N1_1=?
            WHERE oid=1
            """, new_values)

     # Commit the transaction
    
    conn.commit()
    conn.close
    engine1 = pyttsx3.init()
    voices = engine1.getProperty('voices')       #getting details of current voice
    #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
    engine1.setProperty('rate', 150) 
    engine1.say(" appointment is fixed ")
    engine1.runAndWait()
    response=messagebox.askyesno("Appointment","Your appointment is fixed with Dr. Ram at 11:30")
    if response:
         root.quit()
def o1():
    conn = sqlite3.connect('time_tablebook.db')  
    c = conn.cursor()
    new_values = (0,)

    c.execute("""
            UPDATE time
            SET O1_1=?
            WHERE oid=1
            """, new_values)

     # Commit the transaction
    
    conn.commit()
    conn.close
    engine1 = pyttsx3.init()
    voices = engine1.getProperty('voices')       #getting details of current voice
    #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
    engine1.setProperty('rate', 150) 
    engine1.say(" appointment is fixed ")
    engine1.runAndWait()
    response=messagebox.askyesno("Appointment","Your appointment is fixed with Dr. Ram at 12:00")
    if response:
         root.quit()
def p1():
    conn = sqlite3.connect('time_tablebook.db')  
    c = conn.cursor()
    new_values = (0,)

    c.execute("""
            UPDATE time
            SET P1_1=?
            WHERE oid=1
            """, new_values)

     # Commit the transaction
    
    conn.commit()
    conn.close
    engine1 = pyttsx3.init()
    voices = engine1.getProperty('voices')       #getting details of current voice
    #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
    engine1.setProperty('rate', 150) 
    engine1.say(" appointment is fixed ")
    engine1.runAndWait()
    response=messagebox.askyesno("Appointment","Your appointment is fixed with Dr. Ram at 12:30")
    if response:
         root.quit()
def m2():
    conn = sqlite3.connect('time_tablebook.db')  
    c = conn.cursor()
    new_values = (0,)

    c.execute("""
            UPDATE time
            SET M2_1=?
            WHERE oid=1
            """, new_values)

     # Commit the transaction
    
    conn.commit()
    conn.close
    engine1 = pyttsx3.init()
    voices = engine1.getProperty('voices')       #getting details of current voice
    #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
    engine1.setProperty('rate', 150) 
    engine1.say(" appointment is fixed ")
    engine1.runAndWait()
    response=messagebox.askyesno("Appointment","Your appointment is fixed with Dr. Sara at 2:00")
    if response:
         root.quit()
def n2():
    conn = sqlite3.connect('time_tablebook.db')  
    c = conn.cursor()
    new_values = (0,)

    c.execute("""
            UPDATE time
            SET N2_1=?
            WHERE oid=1
            """, new_values)

     # Commit the transaction
    
    conn.commit()
    conn.close
    engine1 = pyttsx3.init()
    voices = engine1.getProperty('voices')       #getting details of current voice
    #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
    engine1.setProperty('rate', 150) 
    engine1.say(" appointment is fixed ")
    engine1.runAndWait()
    response=messagebox.askyesno("Appointment","Your appointment is fixed with Dr. Sara at 2:30")
    if response:
         root.quit()
def o2():
    conn = sqlite3.connect('time_tablebook.db')  
    c = conn.cursor()
    new_values = (0,)

    c.execute("""
            UPDATE time
            SET O2_1=?
            WHERE oid=1
            """, new_values)

     # Commit the transaction
    
    conn.commit()
    conn.close
    engine1 = pyttsx3.init()
    voices = engine1.getProperty('voices')       #getting details of current voice
    #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
    engine1.setProperty('rate', 150) 
    engine1.say(" appointment is fixed ")
    engine1.runAndWait()
    response=messagebox.askyesno("Appointment","Your appointment is fixed with Dr. Sara at 3:00")
    if response:
         root.quit()
def p2():
    conn = sqlite3.connect('time_tablebook.db')  
    c = conn.cursor()
    new_values = (0,)

    c.execute("""
            UPDATE time
            SET P2_1=?
            WHERE oid=1
            """, new_values)

     # Commit the transaction
    
    conn.commit()
    conn.close
    engine1 = pyttsx3.init()
    voices = engine1.getProperty('voices')       #getting details of current voice
    #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
    engine1.setProperty('rate', 150) 
    engine1.say(" appointment is fixed ")
    engine1.runAndWait()
    response=messagebox.askyesno("Appointment","Your appointment is fixed with Dr. Sara at 3:30")
    if response:
         root.quit()
def m3():
    conn = sqlite3.connect('time_tablebook.db')  
    c = conn.cursor()
    new_values = (0,)

    c.execute("""
            UPDATE time
            SET M3_1=?
            WHERE oid=1
            """, new_values)

     # Commit the transaction
    
    conn.commit()
    conn.close
    engine1 = pyttsx3.init()
    voices = engine1.getProperty('voices')       #getting details of current voice
    #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
    engine1.setProperty('rate', 150) 
    engine1.say(" appointment is fixed ")
    engine1.runAndWait()
    response=messagebox.askyesno("Appointment","Your appointment is fixed with Dr. Vasan at 4:00")
    if response:
         root.quit()
def n3():
    conn = sqlite3.connect('time_tablebook.db')  
    c = conn.cursor()
    new_values = (0,)

    c.execute("""
            UPDATE time
            SET N3_1=?
            WHERE oid=1
            """, new_values)

     # Commit the transaction
    
    conn.commit()
    conn.close
    engine1 = pyttsx3.init()
    voices = engine1.getProperty('voices')       #getting details of current voice
    #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
    engine1.setProperty('rate', 150) 
    engine1.say(" appointment is fixed ")
    engine1.runAndWait()
    response=messagebox.askyesno("Appointment","Your appointment is fixed with Dr. Vasan at 4:30")
    if response:
         root.quit()
def o3():
    conn = sqlite3.connect('time_tablebook.db')  
    c = conn.cursor()
    new_values = (0,)

    c.execute("""
            UPDATE time
            SET O3_1=?
            WHERE oid=1
            """, new_values)

     # Commit the transaction
    
    conn.commit()
    conn.close
    engine1 = pyttsx3.init()
    voices = engine1.getProperty('voices')       #getting details of current voice
    #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
    engine1.setProperty('rate', 150) 
    engine1.say(" appointment is fixed ")
    engine1.runAndWait()
    response=messagebox.askyesno("Appointment","Your appointment is fixed with Dr. Vasan at 5:00")
    if response:
         root.quit()
def p3():
    conn = sqlite3.connect('time_tablebook.db')  
    c = conn.cursor()
    new_values = (0,)

    c.execute("""
            UPDATE time
            SET P3_1=?
            WHERE oid=1
            """, new_values)

     # Commit the transaction
    
    conn.commit()
    conn.close
    engine1 = pyttsx3.init()
    voices = engine1.getProperty('voices')       #getting details of current voice
    #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
    engine1.setProperty('rate', 150) 
    engine1.say(" appointment is fixed ")
    engine1.runAndWait()
    response=messagebox.askyesno("Appointment","Your appointment is fixed with Dr. Vasan at 5:30")
    if response:
         root.quit()



def arun():
    tab10 = Toplevel()  # Assign tab1 to the new Tkinter application
    tab10.title("MediSense System")
    tab10.geometry(root.geometry())
    back4_label = Label(tab10, image=back5)
    back4_label.place(x=0, y=0, relwidth=1, relheight=1)
    def welcome_message10():
        engine1 = pyttsx3.init()
        voices = engine1.getProperty('voices')       #getting details of current voice
        #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
        engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
        engine1.setProperty('rate', 150) 
        engine1.say("Choose the Appointment time ")
        engine1.runAndWait()
    tab10.after(1000, welcome_message10)
    custom_font6= Font(family="Arial", size=13, weight="bold")
    label9= Label(tab10, text="Choose the Appointment time", font=custom_font3,bg="#f00a1d",fg="#ebe4e4",width=25, height=2)
    label9.place(relx=0.50, rely=0.20, anchor="center")
    button10 = Button(tab10, text="9:00", font=custom_font6, bg="#9ee8f0", fg="#111212", command=a0, width=10, height=1)
    button10.place(relx=0.35, rely=0.35, anchor="center")
    button11= Button(tab10, text="9:30", font=custom_font6, bg="#9ee8f0", fg="#111212", command=b0, width=10, height=1)
    button11.place(relx=0.65, rely=0.35, anchor="center")
    button12= Button(tab10, text="10:00", font=custom_font6,bg="#9ee8f0", fg="#111212", command=c0, width=10, height=1)
    button12.place(relx=0.35, rely=0.45, anchor="center")
    button13 = Button(tab10, text="10:30", font=custom_font6, bg="#9ee8f0", fg="#111212", command=d0, width=10, height=1)
    button13.place(relx=0.65, rely=0.45, anchor="center")
    conn = sqlite3.connect('time_tablebook.db')
    c = conn.cursor()

    # Execute a SELECT query to fetch the data
    c.execute("SELECT * FROM time")

    # Fetch the result
    result = c.fetchone()

    # Accessing the value '27' from the result
    a0_0 = result[8]
    b0_0= result[9]
    c0_0= result[10]
    d0_0= result[11]
    a0_1=result[12]
    b0_1=result[13]
    c0_1=result[14]
    d0_1=result[15]
  # Output: 
    if (a0_0 and a0_1):
        pass
    else:
        button10.config(state=DISABLED)
    if b0_0 and b0_1:
        pass
    else:
        button11.config(state=DISABLED)
    if c0_0 and c0_1:
        pass
    else:
        button12.config(state=DISABLED)
    if d0_0 and d0_1:
        pass
    else:
        button13.config(state=DISABLED)

    # Close the connection
    conn.close()





def paul():
    tab11 = Toplevel()  # Assign tab1 to the new Tkinter application
    tab11.title("MediSense System")
    tab11.geometry(root.geometry())
    back4_label = Label(tab11, image=back5)
    back4_label.place(x=0, y=0, relwidth=1, relheight=1)
    def welcome_message10():
        engine1 = pyttsx3.init()
        voices = engine1.getProperty('voices')       #getting details of current voice
        #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
        engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
        engine1.setProperty('rate', 150) 
        engine1.say("Choose the Appointment time ")
        engine1.runAndWait()
    tab11.after(1000, welcome_message10)
    custom_font6= Font(family="Arial", size=13, weight="bold")
    label9= Label(tab11, text="Choose the Appointment time", font=custom_font3,bg="#f00a1d",fg="#ebe4e4",width=25, height=2)
    label9.place(relx=0.50, rely=0.20, anchor="center")
    button10 = Button(tab11, text="11:00", font=custom_font6, bg="#9ee8f0", fg="#111212", command=a1, width=10, height=1)
    button10.place(relx=0.35, rely=0.35, anchor="center")
    button11= Button(tab11, text="11:30", font=custom_font6, bg="#9ee8f0", fg="#111212", command=b1, width=10, height=1)
    button11.place(relx=0.65, rely=0.35, anchor="center")
    button12= Button(tab11, text="12:00", font=custom_font6,bg="#9ee8f0", fg="#111212", command=c1, width=10, height=1)
    button12.place(relx=0.35, rely=0.45, anchor="center")
    button13 = Button(tab11, text="12:30", font=custom_font6, bg="#9ee8f0", fg="#111212", command=d1, width=10, height=1)
    button13.place(relx=0.65, rely=0.45, anchor="center")

    conn = sqlite3.connect('time_tablebook.db')
    c = conn.cursor()

    # Execute a SELECT query to fetch the data
    c.execute("SELECT * FROM time")

    # Fetch the result
    result = c.fetchone()

    # Accessing the value '27' from the result
    a1_0 = result[16]
    b1_0= result[17]
    c1_0= result[18]
    d1_0= result[19]
    a1_1=result[20]
    b1_1=result[21]
    c1_1=result[22]
    d1_1=result[23]

    print(a1_0) 
    print(b1_0) 
    print(c1_0) 
    print(d1_0) 
    print(a1_1) 
    print(b1_1) 
    print(c1_1) 
    print(d1_1)  # Output: 
    if (a1_0 and a1_1):
        pass
    else:
        button10.config(state=DISABLED)
    if b1_0 and b1_1:
        pass
    else:
        button11.config(state=DISABLED)
    if c1_0 and c1_1:
        pass
    else:
        button12.config(state=DISABLED)
    if d1_0 and d1_1:
        pass
    else:
        button13.config(state=DISABLED)

    # Close the connection
    conn.close()


def karan():
    tab12 = Toplevel()  # Assign tab1 to the new Tkinter application
    tab12.title("MediSense System")
    tab12.geometry(root.geometry())
    back4_label = Label(tab12, image=back5)
    back4_label.place(x=0, y=0, relwidth=1, relheight=1)
    def welcome_message10():
        engine1 = pyttsx3.init()
        voices = engine1.getProperty('voices')       #getting details of current voice
        #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
        engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
        engine1.setProperty('rate', 150) 
        engine1.say("Choose the Appointment time ")
        engine1.runAndWait()
    tab12.after(1000, welcome_message10)
    custom_font6= Font(family="Arial", size=13, weight="bold")
    label9= Label(tab12, text="Choose the Appointment time", font=custom_font3,bg="#f00a1d",fg="#ebe4e4",width=25, height=2)
    label9.place(relx=0.50, rely=0.20, anchor="center")
    button10 = Button(tab12, text="2:00", font=custom_font6, bg="#9ee8f0", fg="#111212", command=a2, width=10, height=1)
    button10.place(relx=0.35, rely=0.35, anchor="center")
    button11= Button(tab12, text="2:30", font=custom_font6, bg="#9ee8f0", fg="#111212", command=b2, width=10, height=1)
    button11.place(relx=0.65, rely=0.35, anchor="center")
    button12= Button(tab12, text="3:00", font=custom_font6,bg="#9ee8f0", fg="#111212", command=c2, width=10, height=1)
    button12.place(relx=0.35, rely=0.45, anchor="center")
    button13 = Button(tab12, text="3:30", font=custom_font6, bg="#9ee8f0", fg="#111212", command=d2, width=10, height=1)
    button13.place(relx=0.65, rely=0.45, anchor="center")

    conn = sqlite3.connect('time_tablebook.db')
    c = conn.cursor()

    # Execute a SELECT query to fetch the data
    c.execute("SELECT * FROM time")

    # Fetch the result
    result = c.fetchone()

    # Accessing the value '27' from the result
    a2_0 = result[24]
    b2_0= result[25]
    c2_0= result[26]
    d2_0= result[27]
    a2_1=result[28]
    b2_1=result[29]
    c2_1=result[30]
    d2_1=result[31]

    print(a2_0) 
    print(b2_0) 
    print(c2_0) 
    print(d2_0) 
    print(a2_1) 
    print(b2_1) 
    print(c2_1) 
    print(d2_1)  # Output: 
    if (a2_0 and a2_1):
        pass
    else:
        button10.config(state=DISABLED)
    if b2_0 and b2_1:
        pass
    else:
        button11.config(state=DISABLED)
    if c2_0 and c2_1:
        pass
    else:
        button12.config(state=DISABLED)
    if d2_0 and d2_1:
        pass
    else:
        button13.config(state=DISABLED)

    # Close the connection
    conn.close()


def kishore():
    tab13 = Toplevel()  # Assign tab1 to the new Tkinter application
    tab13.title("MediSense System")
    tab13.geometry(root.geometry())
    back4_label = Label(tab13, image=back5)
    back4_label.place(x=0, y=0, relwidth=1, relheight=1)
    def welcome_message10():
        engine1 = pyttsx3.init()
        voices = engine1.getProperty('voices')       #getting details of current voice
        #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
        engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
        engine1.setProperty('rate', 150) 
        engine1.say("Choose the Appointment time ")
        engine1.runAndWait()
    tab13.after(1000, welcome_message10)
    custom_font6= Font(family="Arial", size=13, weight="bold")
    label9= Label(tab13, text="Choose the Appointment time", font=custom_font3,bg="#f00a1d",fg="#ebe4e4",width=25, height=2)
    label9.place(relx=0.50, rely=0.20, anchor="center")
    button10 = Button(tab13, text="4:00", font=custom_font6, bg="#9ee8f0", fg="#111212", command=a3, width=10, height=1)
    button10.place(relx=0.35, rely=0.35, anchor="center")
    button11= Button(tab13, text="4:30", font=custom_font6, bg="#9ee8f0", fg="#111212", command=b3, width=10, height=1)
    button11.place(relx=0.65, rely=0.35, anchor="center")
    button12= Button(tab13, text="5:00", font=custom_font6,bg="#9ee8f0", fg="#111212", command=c3, width=10, height=1)
    button12.place(relx=0.35, rely=0.45, anchor="center")
    button13 = Button(tab13, text="5:30", font=custom_font6, bg="#9ee8f0", fg="#111212", command=d3, width=10, height=1)
    button13.place(relx=0.65, rely=0.45, anchor="center")
    
    conn = sqlite3.connect('time_tablebook.db')
    c = conn.cursor()

    # Execute a SELECT query to fetch the data
    c.execute("SELECT * FROM time")

    # Fetch the result
    result = c.fetchone()

    # Accessing the value '27' from the result
    a3_0 = result[32]
    b3_0= result[33]
    c3_0= result[34]
    d3_0= result[35]
    a3_1=result[36]
    b3_1=result[37]
    c3_1=result[38]
    d3_1=result[39]

    print(a3_0) 
    print(b3_0) 
    print(c3_0) 
    print(d3_0) 
    print(a3_1) 
    print(b3_1) 
    print(c3_1) 
    print(d3_1)  # Output: 
    if (a3_0 and a3_1):
        pass
    else:
        button10.config(state=DISABLED)
    if b3_0 and b3_1:
        pass
    else:
        button11.config(state=DISABLED)
    if c3_0 and c3_1:
        pass
    else:
        button12.config(state=DISABLED)
    if d3_0 and d3_1:
        pass
    else:
        button13.config(state=DISABLED)

    # Close the connection
    conn.close()


def raj():
    tab14 = Toplevel()  # Assign tab1 to the new Tkinter application
    tab14.title("MediSense System")
    tab14.geometry(root.geometry())
    back4_label = Label(tab14, image=back5)
    back4_label.place(x=0, y=0, relwidth=1, relheight=1)
    def welcome_message10():
        engine1 = pyttsx3.init()
        voices = engine1.getProperty('voices')       #getting details of current voice
        #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
        engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
        engine1.setProperty('rate', 150) 
        engine1.say("Choose the Appointment time ")
        engine1.runAndWait()
    tab14.after(1000, welcome_message10)
    custom_font6= Font(family="Arial", size=13, weight="bold")
    label9= Label(tab14, text="Choose the Appointment time", font=custom_font3,bg="#f00a1d",fg="#ebe4e4",width=25, height=2)
    label9.place(relx=0.50, rely=0.20, anchor="center")
    button10 = Button(tab14, text="9:00", font=custom_font6, bg="#9ee8f0", fg="#111212", command=e0, width=10, height=1)
    button10.place(relx=0.35, rely=0.35, anchor="center")
    button11= Button(tab14, text="9:30", font=custom_font6, bg="#9ee8f0", fg="#111212", command=f0, width=10, height=1)
    button11.place(relx=0.65, rely=0.35, anchor="center")
    button12= Button(tab14, text="10:00", font=custom_font6,bg="#9ee8f0", fg="#111212", command=g0, width=10, height=1)
    button12.place(relx=0.35, rely=0.45, anchor="center")
    button13 = Button(tab14, text="10:30", font=custom_font6, bg="#9ee8f0", fg="#111212", command=h0, width=10, height=1)
    button13.place(relx=0.65, rely=0.45, anchor="center")

    conn = sqlite3.connect('time_tablebook.db')
    c = conn.cursor()

    # Execute a SELECT query to fetch the data
    c.execute("SELECT * FROM time")

    # Fetch the result
    result = c.fetchone()

    # Accessing the value '27' from the result
    e0_0 = result[40]
    f0_0= result[41]
    g0_0= result[42]
    h0_0= result[43]
    e0_1=result[44]
    f0_1=result[45]
    g0_1=result[46]
    h0_1=result[47]

    print(e0_0) 
    print(f0_0) 
    print(g0_0) 
    print(h0_0) 
    print(e0_1) 
    print(f0_1) 
    print(g0_1) 
    print(h0_1)  # Output: 
    if (e0_0 and e0_1):
        pass
    else:
        button10.config(state=DISABLED)
    if f0_0 and f0_1:
        pass
    else:
        button11.config(state=DISABLED)
    if g0_0 and g0_1:
        pass
    else:
        button12.config(state=DISABLED)
    if h0_0 and h0_1:
        pass
    else:
        button13.config(state=DISABLED)

    # Close the connection
    conn.close()

def kajal():
    tab15 = Toplevel()  # Assign tab1 to the new Tkinter application
    tab15.title("MediSense System")
    tab15.geometry(root.geometry())
    back4_label = Label(tab15, image=back5)
    back4_label.place(x=0, y=0, relwidth=1, relheight=1)
    def welcome_message10():
        engine1 = pyttsx3.init()
        voices = engine1.getProperty('voices')       #getting details of current voice
        #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
        engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
        engine1.setProperty('rate', 150) 
        engine1.say("Choose the Appointment time ")
        engine1.runAndWait()
    tab15.after(1000, welcome_message10)
    custom_font6= Font(family="Arial", size=13, weight="bold")
    label9= Label(tab15, text="Choose the Appointment time", font=custom_font3,bg="#f00a1d",fg="#ebe4e4",width=25, height=2)
    label9.place(relx=0.50, rely=0.20, anchor="center")
    button10 = Button(tab15, text="11:00", font=custom_font6, bg="#9ee8f0", fg="#111212", command=e1, width=10, height=1)
    button10.place(relx=0.35, rely=0.35, anchor="center")
    button11= Button(tab15, text="11:30", font=custom_font6, bg="#9ee8f0", fg="#111212", command=f1, width=10, height=1)
    button11.place(relx=0.65, rely=0.35, anchor="center")
    button12= Button(tab15, text="12:00", font=custom_font6,bg="#9ee8f0", fg="#111212", command=g1, width=10, height=1)
    button12.place(relx=0.35, rely=0.45, anchor="center")
    button13 = Button(tab15, text="12:30", font=custom_font6, bg="#9ee8f0", fg="#111212", command=h1, width=10, height=1)
    button13.place(relx=0.65, rely=0.45, anchor="center")

    conn = sqlite3.connect('time_tablebook.db')
    c = conn.cursor()

    # Execute a SELECT query to fetch the data
    c.execute("SELECT * FROM time")

    # Fetch the result
    result = c.fetchone()

    # Accessing the value '27' from the result
    e1_0 = result[48]
    f1_0= result[49]
    g1_0= result[50]
    h1_0= result[51]
    e1_1=result[52]
    f1_1=result[53]
    g1_1=result[54]
    h1_1=result[55]

    print(e1_0) 
    print(f1_0) 
    print(g1_0) 
    print(h1_0) 
    print(e1_1) 
    print(f1_1) 
    print(g1_1) 
    print(h1_1)  # Output: 
    if (e1_0 and e1_1):
        pass
    else:
        button10.config(state=DISABLED)
    if f1_0 and f1_1:
        pass
    else:
        button11.config(state=DISABLED)
    if g1_0 and g1_1:
        pass
    else:
        button12.config(state=DISABLED)
    if h1_0 and h1_1:
        pass
    else:
        button13.config(state=DISABLED)

    # Close the connection
    conn.close()

def kapoor():
    tab16 = Toplevel()  # Assign tab1 to the new Tkinter application
    tab16.title("MediSense System")
    tab16.geometry(root.geometry())
    back4_label = Label(tab16, image=back5)
    back4_label.place(x=0, y=0, relwidth=1, relheight=1)
    def welcome_message10():
        engine1 = pyttsx3.init()
        voices = engine1.getProperty('voices')       #getting details of current voice
        #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
        engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
        engine1.setProperty('rate', 150) 
        engine1.say("Choose the Appointment time ")
        engine1.runAndWait()
    tab16.after(1000, welcome_message10)
    custom_font6= Font(family="Arial", size=13, weight="bold")
    label9= Label(tab16, text="Choose the Appointment time", font=custom_font3,bg="#f00a1d",fg="#ebe4e4",width=25, height=2)
    label9.place(relx=0.50, rely=0.20, anchor="center")
    button10 = Button(tab16, text="2:00", font=custom_font6, bg="#9ee8f0", fg="#111212", command=e2, width=10, height=1)
    button10.place(relx=0.35, rely=0.35, anchor="center")
    button11= Button(tab16, text="2:30", font=custom_font6, bg="#9ee8f0", fg="#111212", command=f2, width=10, height=1)
    button11.place(relx=0.65, rely=0.35, anchor="center")
    button12= Button(tab16, text="3:00", font=custom_font6,bg="#9ee8f0", fg="#111212", command=g2, width=10, height=1)
    button12.place(relx=0.35, rely=0.45, anchor="center")
    button13 = Button(tab16, text="3:30", font=custom_font6, bg="#9ee8f0", fg="#111212", command=h2, width=10, height=1)
    button13.place(relx=0.65, rely=0.45, anchor="center")

    conn = sqlite3.connect('time_tablebook.db')
    c = conn.cursor()

    # Execute a SELECT query to fetch the data
    c.execute("SELECT * FROM time")

    # Fetch the result
    result = c.fetchone()

    # Accessing the value '27' from the result
    e2_0 = result[56]
    f2_0= result[57]
    g2_0= result[58]
    h2_0= result[59]
    e2_1=result[60]
    f2_1=result[61]
    g2_1=result[62]
    h2_1=result[63]

    print(e2_0) 
    print(f2_0) 
    print(g2_0) 
    print(h2_0) 
    print(e2_1) 
    print(f2_1) 
    print(g2_1) 
    print(h2_1)  # Output: 
    if (e2_0 and e2_1):
        pass
    else:
        button10.config(state=DISABLED)
    if f2_0 and f2_1:
        pass
    else:
        button11.config(state=DISABLED)
    if g2_0 and g2_1:
        pass
    else:
        button12.config(state=DISABLED)
    if h2_0 and h2_1:
        pass
    else:
        button13.config(state=DISABLED)

    # Close the connection
    conn.close()

def hari():
    tab17 = Toplevel()  # Assign tab1 to the new Tkinter application
    tab17.title("MediSense System")
    tab17.geometry(root.geometry())
    back4_label = Label(tab17, image=back5)
    back4_label.place(x=0, y=0, relwidth=1, relheight=1)
    def welcome_message10():
        engine1 = pyttsx3.init()
        voices = engine1.getProperty('voices')       #getting details of current voice
        #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
        engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
        engine1.setProperty('rate', 150) 
        engine1.say("Choose the Appointment time ")
        engine1.runAndWait()
    tab17.after(1000, welcome_message10)
    custom_font6= Font(family="Arial", size=13, weight="bold")
    label9= Label(tab17, text="Choose the Appointment time", font=custom_font3,bg="#f00a1d",fg="#ebe4e4",width=25, height=2)
    label9.place(relx=0.50, rely=0.20, anchor="center")
    button10 = Button(tab17, text="4:00", font=custom_font6, bg="#9ee8f0", fg="#111212", command=e3, width=10, height=1)
    button10.place(relx=0.35, rely=0.35, anchor="center")
    button11= Button(tab17, text="4:30", font=custom_font6, bg="#9ee8f0", fg="#111212", command=f3, width=10, height=1)
    button11.place(relx=0.65, rely=0.35, anchor="center")
    button12= Button(tab17, text="5:00", font=custom_font6,bg="#9ee8f0", fg="#111212", command=g3, width=10, height=1)
    button12.place(relx=0.35, rely=0.45, anchor="center")
    button13 = Button(tab17, text="5:30", font=custom_font6, bg="#9ee8f0", fg="#111212", command=h3, width=10, height=1)
    button13.place(relx=0.65, rely=0.45, anchor="center")

    conn = sqlite3.connect('time_tablebook.db')
    c = conn.cursor()

    # Execute a SELECT query to fetch the data
    c.execute("SELECT * FROM time")

    # Fetch the result
    result = c.fetchone()

    # Accessing the value '27' from the result
    e3_0 = result[64]
    f3_0= result[65]
    g3_0= result[66]
    h3_0= result[67]
    e3_1=result[68]
    f3_1=result[69]
    g3_1=result[70]
    h3_1=result[71]

    print(e3_0) 
    print(f3_0) 
    print(g3_0) 
    print(h3_0) 
    print(e3_1) 
    print(f3_1) 
    print(g3_1) 
    print(h3_1)  # Output: 
    if (e3_0 and e3_1):
        pass
    else:
        button10.config(state=DISABLED)
    if f3_0 and f3_1:
        pass
    else:
        button11.config(state=DISABLED)
    if g3_0 and g3_1:
        pass
    else:
        button12.config(state=DISABLED)
    if h3_0 and h3_1:
        pass
    else:
        button13.config(state=DISABLED)

    # Close the connection
    conn.close()


def sanjay():
    tab18 = Toplevel()  # Assign tab1 to the new Tkinter application
    tab18.title("MediSense System")
    tab18.geometry(root.geometry())
    back4_label = Label(tab18, image=back5)
    back4_label.place(x=0, y=0, relwidth=1, relheight=1)
    def welcome_message10():
        engine1 = pyttsx3.init()
        voices = engine1.getProperty('voices')       #getting details of current voice
        #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
        engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
        engine1.setProperty('rate', 150) 
        engine1.say("Choose the Appointment time ")
        engine1.runAndWait()
    tab18.after(1000, welcome_message10)
    custom_font6= Font(family="Arial", size=13, weight="bold")
    label9= Label(tab18, text="Choose the Appointment time", font=custom_font3,bg="#f00a1d",fg="#ebe4e4",width=25, height=2)
    label9.place(relx=0.50, rely=0.20, anchor="center")
    button10 = Button(tab18, text="9:00", font=custom_font6, bg="#9ee8f0", fg="#111212", command=i0, width=10, height=1)
    button10.place(relx=0.35, rely=0.35, anchor="center")
    button11= Button(tab18, text="9:30", font=custom_font6, bg="#9ee8f0", fg="#111212", command=j0, width=10, height=1)
    button11.place(relx=0.65, rely=0.35, anchor="center")
    button12= Button(tab18, text="10:00", font=custom_font6,bg="#9ee8f0", fg="#111212", command=k0, width=10, height=1)
    button12.place(relx=0.35, rely=0.45, anchor="center")
    button13 = Button(tab18, text="10:30", font=custom_font6, bg="#9ee8f0", fg="#111212", command=l0, width=10, height=1)
    button13.place(relx=0.65, rely=0.45, anchor="center")

    conn = sqlite3.connect('time_tablebook.db')
    c = conn.cursor()

    # Execute a SELECT query to fetch the data
    c.execute("SELECT * FROM time")

    # Fetch the result
    result = c.fetchone()

    # Accessing the value '27' from the result
    i0_0 = result[72]
    j0_0= result[73]
    k0_0= result[74]
    l0_0= result[75]
    i0_1=result[76]
    j0_1=result[77]
    k0_1=result[78]
    l0_1=result[79]

    print(i0_0) 
    print(j0_0) 
    print(k0_0) 
    print(l0_0) 
    print(i0_1) 
    print(j0_1) 
    print(k0_1) 
    print(l0_1)  # Output: 
    if (i0_0 and i0_1):
        pass
    else:
        button10.config(state=DISABLED)
    if j0_0 and j0_1:
        pass
    else:
        button11.config(state=DISABLED)
    if k0_0 and k0_1:
        pass
    else:
        button12.config(state=DISABLED)
    if l0_0 and l0_1:
        pass
    else:
        button13.config(state=DISABLED)

    # Close the connection
    conn.close()
def sundhar():
    tab19 = Toplevel()  # Assign tab1 to the new Tkinter application
    tab19.title("MediSense System")
    tab19.geometry(root.geometry())
    back4_label = Label(tab19, image=back5)
    back4_label.place(x=0, y=0, relwidth=1, relheight=1)
    def welcome_message10():
        engine1 = pyttsx3.init()
        voices = engine1.getProperty('voices')       #getting details of current voice
        #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
        engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
        engine1.setProperty('rate', 150) 
        engine1.say("Choose the Appointment time ")
        engine1.runAndWait()
    tab19.after(1000, welcome_message10)
    custom_font6= Font(family="Arial", size=13, weight="bold")
    label9= Label(tab19, text="Choose the Appointment time", font=custom_font3,bg="#f00a1d",fg="#ebe4e4",width=25, height=2)
    label9.place(relx=0.50, rely=0.20, anchor="center")
    button10 = Button(tab19, text="11:00", font=custom_font6, bg="#9ee8f0", fg="#111212", command=i1, width=10, height=1)
    button10.place(relx=0.35, rely=0.35, anchor="center")
    button11= Button(tab19, text="11:30", font=custom_font6, bg="#9ee8f0", fg="#111212", command=j1, width=10, height=1)
    button11.place(relx=0.65, rely=0.35, anchor="center")
    button12= Button(tab19, text="12:00", font=custom_font6,bg="#9ee8f0", fg="#111212", command=k1, width=10, height=1)
    button12.place(relx=0.35, rely=0.45, anchor="center")
    button13 = Button(tab19, text="12:30", font=custom_font6, bg="#9ee8f0", fg="#111212", command=l1, width=10, height=1)
    button13.place(relx=0.65, rely=0.45, anchor="center")

    conn = sqlite3.connect('time_tablebook.db')
    c = conn.cursor()

    # Execute a SELECT query to fetch the data
    c.execute("SELECT * FROM time")

    # Fetch the result
    result = c.fetchone()

    # Accessing the value '27' from the result
    i1_0 = result[80]
    j1_0= result[81]
    k1_0= result[82]
    l1_0= result[83]
    i1_1=result[84]
    j1_1=result[85]
    k1_1=result[86]
    l1_1=result[87]

    print(i1_0) 
    print(j1_0) 
    print(k1_0) 
    print(l1_0) 
    print(i1_1) 
    print(j1_1) 
    print(k1_1) 
    print(l1_1)  # Output: 
    if (i1_0 and i1_1):
        pass
    else:
        button10.config(state=DISABLED)
    if j1_0 and j1_1:
        pass
    else:
        button11.config(state=DISABLED)
    if k1_0 and k1_1:
        pass
    else:
        button12.config(state=DISABLED)
    if l1_0 and l1_1:
        pass
    else:
        button13.config(state=DISABLED)

    # Close the connection
    conn.close()
def madhu():
    tab20 = Toplevel()  # Assign tab1 to the new Tkinter application
    tab20.title("MediSense System")
    tab20.geometry(root.geometry())
    back4_label = Label(tab20, image=back5)
    back4_label.place(x=0, y=0, relwidth=1, relheight=1)
    def welcome_message10():
        engine1 = pyttsx3.init()
        voices = engine1.getProperty('voices')       #getting details of current voice
        #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
        engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
        engine1.setProperty('rate', 150) 
        engine1.say("Choose the Appointment time ")
        engine1.runAndWait()
    tab20.after(1000, welcome_message10)
    custom_font6= Font(family="Arial", size=13, weight="bold")
    label9= Label(tab20, text="Choose the Appointment time", font=custom_font3,bg="#f00a1d",fg="#ebe4e4",width=25, height=2)
    label9.place(relx=0.50, rely=0.20, anchor="center")
    button10 = Button(tab20, text="2:00", font=custom_font6, bg="#9ee8f0", fg="#111212", command=i2, width=10, height=1)
    button10.place(relx=0.35, rely=0.35, anchor="center")
    button11= Button(tab20, text="2:30", font=custom_font6, bg="#9ee8f0", fg="#111212", command=j2, width=10, height=1)
    button11.place(relx=0.65, rely=0.35, anchor="center")
    button12= Button(tab20, text="3:00", font=custom_font6,bg="#9ee8f0", fg="#111212", command=k2, width=10, height=1)
    button12.place(relx=0.35, rely=0.45, anchor="center")
    button13 = Button(tab20, text="3:30", font=custom_font6, bg="#9ee8f0", fg="#111212", command=l2, width=10, height=1)
    button13.place(relx=0.65, rely=0.45, anchor="center")

    conn = sqlite3.connect('time_tablebook.db')
    c = conn.cursor()

    # Execute a SELECT query to fetch the data
    c.execute("SELECT * FROM time")

    # Fetch the result
    result = c.fetchone()

    # Accessing the value '27' from the result
    i2_0 = result[88]
    j2_0= result[89]
    k2_0= result[90]
    l2_0= result[91]
    i2_1=result[92]
    j2_1=result[93]
    k2_1=result[94]
    l2_1=result[95]

    print(i2_0) 
    print(j2_0) 
    print(k2_0) 
    print(l2_0) 
    print(i2_1) 
    print(j2_1) 
    print(k2_1) 
    print(l2_1)  # Output: 
    if (i2_0 and i2_1):
        pass
    else:
        button10.config(state=DISABLED)
    if j2_0 and j2_1:
        pass
    else:
        button11.config(state=DISABLED)
    if k2_0 and k2_1:
        pass
    else:
        button12.config(state=DISABLED)
    if l2_0 and l2_1:
        pass
    else:
        button13.config(state=DISABLED)

    # Close the connection
    conn.close()
def dharun():
    tab21 = Toplevel()  # Assign tab1 to the new Tkinter application
    tab21.title("MediSense System")
    tab21.geometry(root.geometry())
    back4_label = Label(tab21, image=back5)
    back4_label.place(x=0, y=0, relwidth=1, relheight=1)
    def welcome_message10():
        engine1 = pyttsx3.init()
        voices = engine1.getProperty('voices')       #getting details of current voice
        #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
        engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
        engine1.setProperty('rate', 150) 
        engine1.say("Choose the Appointment time ")
        engine1.runAndWait()
    tab21.after(1000, welcome_message10)
    custom_font6= Font(family="Arial", size=13, weight="bold")
    label9= Label(tab21, text="Choose the Appointment time", font=custom_font3,bg="#f00a1d",fg="#ebe4e4",width=25, height=2)
    label9.place(relx=0.50, rely=0.20, anchor="center")
    button10 = Button(tab21, text="4:00", font=custom_font6, bg="#9ee8f0", fg="#111212", command=i3, width=10, height=1)
    button10.place(relx=0.35, rely=0.35, anchor="center")
    button11= Button(tab21, text="4:30", font=custom_font6, bg="#9ee8f0", fg="#111212", command=j3, width=10, height=1)
    button11.place(relx=0.65, rely=0.35, anchor="center")
    button12= Button(tab21, text="5:00", font=custom_font6,bg="#9ee8f0", fg="#111212", command=k3, width=10, height=1)
    button12.place(relx=0.35, rely=0.45, anchor="center")
    button13 = Button(tab21, text="5:30", font=custom_font6, bg="#9ee8f0", fg="#111212", command=l3, width=10, height=1)
    button13.place(relx=0.65, rely=0.45, anchor="center")

    conn = sqlite3.connect('time_tablebook.db')
    c = conn.cursor()

    # Execute a SELECT query to fetch the data
    c.execute("SELECT * FROM time")

    # Fetch the result
    result = c.fetchone()

    # Accessing the value '27' from the result
    i3_0 = result[96]
    j3_0= result[97]
    k3_0= result[98]
    l3_0= result[99]
    i3_1=result[100]
    j3_1=result[101]
    k3_1=result[102]
    l3_1=result[103]

    print(i3_0) 
    print(j3_0) 
    print(k3_0) 
    print(l3_0) 
    print(i3_1) 
    print(j3_1) 
    print(k3_1) 
    print(l3_1)  # Output: 
    if (i3_0 and i3_1):
        pass
    else:
        button10.config(state=DISABLED)
    if j3_0 and j3_1:
        pass
    else:
        button11.config(state=DISABLED)
    if k3_0 and k3_1:
        pass
    else:
        button12.config(state=DISABLED)
    if l3_0 and l3_1:
        pass
    else:
        button13.config(state=DISABLED)

    # Close the connection
    conn.close()   
def rahul():
    tab22 = Toplevel()  # Assign tab1 to the new Tkinter application
    tab22.title("MediSense System")
    tab22.geometry(root.geometry())
    back4_label = Label(tab22, image=back5)
    back4_label.place(x=0, y=0, relwidth=1, relheight=1)
    def welcome_message10():
        engine1 = pyttsx3.init()
        voices = engine1.getProperty('voices')       #getting details of current voice
        #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
        engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
        engine1.setProperty('rate', 150) 
        engine1.say("Choose the Appointment time ")
        engine1.runAndWait()
    tab22.after(1000, welcome_message10)
    custom_font6= Font(family="Arial", size=13, weight="bold")
    label9= Label(tab22, text="Choose the Appointment time", font=custom_font3,bg="#f00a1d",fg="#ebe4e4",width=25, height=2)
    label9.place(relx=0.50, rely=0.20, anchor="center")
    button10 = Button(tab22, text="9:00", font=custom_font6, bg="#9ee8f0", fg="#111212", command=m0, width=10, height=1)
    button10.place(relx=0.35, rely=0.35, anchor="center")
    button11= Button(tab22, text="9:30", font=custom_font6, bg="#9ee8f0", fg="#111212", command=n0, width=10, height=1)
    button11.place(relx=0.65, rely=0.35, anchor="center")
    button12= Button(tab22, text="10:00", font=custom_font6,bg="#9ee8f0", fg="#111212", command=o0, width=10, height=1)
    button12.place(relx=0.35, rely=0.45, anchor="center")
    button13 = Button(tab22, text="10:30", font=custom_font6, bg="#9ee8f0", fg="#111212", command=p0, width=10, height=1)
    button13.place(relx=0.65, rely=0.45, anchor="center")

    conn = sqlite3.connect('time_tablebook.db')
    c = conn.cursor()

    # Execute a SELECT query to fetch the data
    c.execute("SELECT * FROM time")

    # Fetch the result
    result = c.fetchone()

    # Accessing the value '27' from the result
    m0_0 = result[104]
    n0_0= result[105]
    o0_0= result[106]
    p0_0= result[107]
    m0_1=result[108]
    n0_1=result[109]
    o0_1=result[110]
    p0_1=result[111]

    print(m0_0) 
    print(n0_0) 
    print(o0_0) 
    print(p0_0) 
    print(m0_1) 
    print(n0_1) 
    print(o0_1) 
    print(p0_1)  # Output: 
    if (m0_0 and m0_1):
        pass
    else:
        button10.config(state=DISABLED)
    if n0_0 and n0_1:
        pass
    else:
        button11.config(state=DISABLED)
    if o0_0 and o0_1:
        pass
    else:
        button12.config(state=DISABLED)
    if p0_0 and p0_1:
        pass
    else:
        button13.config(state=DISABLED)

    # Close the connection
    conn.close()   

def ram():
    tab23 = Toplevel()  # Assign tab1 to the new Tkinter application
    tab23.title("MediSense System")
    tab23.geometry(root.geometry())
    back4_label = Label(tab23, image=back5)
    back4_label.place(x=0, y=0, relwidth=1, relheight=1)
    def welcome_message10():
        engine1 = pyttsx3.init()
        voices = engine1.getProperty('voices')       #getting details of current voice
        #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
        engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
        engine1.setProperty('rate', 150) 
        engine1.say("Choose the Appointment time ")
        engine1.runAndWait()
    tab23.after(1000, welcome_message10)
    custom_font6= Font(family="Arial", size=13, weight="bold")
    label9= Label(tab23, text="Choose the Appointment time", font=custom_font3,bg="#f00a1d",fg="#ebe4e4",width=25, height=2)
    label9.place(relx=0.50, rely=0.20, anchor="center")
    button10 = Button(tab23, text="11:00", font=custom_font6, bg="#9ee8f0", fg="#111212", command=m1, width=10, height=1)
    button10.place(relx=0.35, rely=0.35, anchor="center")
    button11= Button(tab23, text="11:30", font=custom_font6, bg="#9ee8f0", fg="#111212", command=n1, width=10, height=1)
    button11.place(relx=0.65, rely=0.35, anchor="center")
    button12= Button(tab23, text="12:00", font=custom_font6,bg="#9ee8f0", fg="#111212", command=o1, width=10, height=1)
    button12.place(relx=0.35, rely=0.45, anchor="center")
    button13 = Button(tab23, text="12:30", font=custom_font6, bg="#9ee8f0", fg="#111212", command=p1, width=10, height=1)
    button13.place(relx=0.65, rely=0.45, anchor="center")

    conn = sqlite3.connect('time_tablebook.db')
    c = conn.cursor()

    # Execute a SELECT query to fetch the data
    c.execute("SELECT * FROM time")

    # Fetch the result
    result = c.fetchone()

    # Accessing the value '27' from the result
    m1_0 = result[112]
    n1_0= result[113]
    o1_0= result[114]
    p1_0= result[115]
    m1_1=result[116]
    n1_1=result[117]
    o1_1=result[118]
    p1_1=result[119]

    print(m1_0) 
    print(n1_0) 
    print(o1_0) 
    print(p1_0) 
    print(m1_1) 
    print(n1_1) 
    print(o1_1) 
    print(p1_1)  # Output: 
    if (m1_0 and m1_1):
        pass
    else:
        button10.config(state=DISABLED)
    if n1_0 and n1_1:
        pass
    else:
        button11.config(state=DISABLED)
    if o1_0 and o1_1:
        pass
    else:
        button12.config(state=DISABLED)
    if p1_0 and p1_1:
        pass
    else:
        button13.config(state=DISABLED)

    # Close the connection
    conn.close()   
def sara():
    tab24 = Toplevel()  # Assign tab1 to the new Tkinter application
    tab24.title("MediSense System")
    tab24.geometry(root.geometry())
    back4_label = Label(tab24, image=back5)
    back4_label.place(x=0, y=0, relwidth=1, relheight=1)
    def welcome_message10():
        engine1 = pyttsx3.init()
        voices = engine1.getProperty('voices')       #getting details of current voice
        #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
        engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
        engine1.setProperty('rate', 150) 
        engine1.say("Choose the Appointment time ")
        engine1.runAndWait()
    tab24.after(1000, welcome_message10)
    custom_font6= Font(family="Arial", size=13, weight="bold")
    label9= Label(tab24, text="Choose the Appointment time", font=custom_font3,bg="#f00a1d",fg="#ebe4e4",width=25, height=2)
    label9.place(relx=0.50, rely=0.20, anchor="center")
    button10 = Button(tab24, text="2:00", font=custom_font6, bg="#9ee8f0", fg="#111212", command=m2, width=10, height=1)
    button10.place(relx=0.35, rely=0.35, anchor="center")
    button11= Button(tab24, text="2:30", font=custom_font6, bg="#9ee8f0", fg="#111212", command=n2, width=10, height=1)
    button11.place(relx=0.65, rely=0.35, anchor="center")
    button12= Button(tab24, text="3:00", font=custom_font6,bg="#9ee8f0", fg="#111212", command=o2, width=10, height=1)
    button12.place(relx=0.35, rely=0.45, anchor="center")
    button13 = Button(tab24, text="3:30", font=custom_font6, bg="#9ee8f0", fg="#111212", command=p2, width=10, height=1)
    button13.place(relx=0.65, rely=0.45, anchor="center")

    conn = sqlite3.connect('time_tablebook.db')
    c = conn.cursor()

    # Execute a SELECT query to fetch the data
    c.execute("SELECT * FROM time")

    # Fetch the result
    result = c.fetchone()

    # Accessing the value '27' from the result
    m2_0 = result[120]
    n2_0= result[121]
    o2_0= result[122]
    p2_0= result[123]
    m2_1=result[124]
    n2_1=result[125]
    o2_1=result[126]
    p2_1=result[127]

    print(m2_0) 
    print(n2_0) 
    print(o2_0) 
    print(p2_0) 
    print(m2_1) 
    print(n2_1) 
    print(o2_1) 
    print(p2_1)  # Output: 
    if (m2_0 and m2_1):
        pass
    else:
        button10.config(state=DISABLED)
    if n2_0 and n2_1:
        pass
    else:
        button11.config(state=DISABLED)
    if o2_0 and o2_1:
        pass
    else:
        button12.config(state=DISABLED)
    if p2_0 and p2_1:
        pass
    else:
        button13.config(state=DISABLED)

    # Close the connection
    conn.close()   
def vasan():
    tab25 = Toplevel()  # Assign tab1 to the new Tkinter application
    tab25.title("MediSense System")
    tab25.geometry(root.geometry())
    back4_label = Label(tab25, image=back5)
    back4_label.place(x=0, y=0, relwidth=1, relheight=1)
    def welcome_message10():
        engine1 = pyttsx3.init()
        voices = engine1.getProperty('voices')       #getting details of current voice
        #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
        engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
        engine1.setProperty('rate', 150) 
        engine1.say("Choose the Appointment time ")
        engine1.runAndWait()
    tab25.after(1000, welcome_message10)
    custom_font6= Font(family="Arial", size=13, weight="bold")
    label9= Label(tab25, text="Choose the Appointment time", font=custom_font3,bg="#f00a1d",fg="#ebe4e4",width=25, height=2)
    label9.place(relx=0.50, rely=0.20, anchor="center")
    button10 = Button(tab25, text="4:00", font=custom_font6, bg="#9ee8f0", fg="#111212", command=m3, width=10, height=1)
    button10.place(relx=0.35, rely=0.35, anchor="center")
    button11= Button(tab25, text="4:30", font=custom_font6, bg="#9ee8f0", fg="#111212", command=n3, width=10, height=1)
    button11.place(relx=0.65, rely=0.35, anchor="center")
    button12= Button(tab25, text="5:00", font=custom_font6,bg="#9ee8f0", fg="#111212", command=o3, width=10, height=1)
    button12.place(relx=0.35, rely=0.45, anchor="center")
    button13 = Button(tab25, text="5:30", font=custom_font6, bg="#9ee8f0", fg="#111212", command=p3, width=10, height=1)
    button13.place(relx=0.65, rely=0.45, anchor="center")

    conn = sqlite3.connect('time_tablebook.db')
    c = conn.cursor()

    # Execute a SELECT query to fetch the data
    c.execute("SELECT * FROM time")

    # Fetch the result
    result = c.fetchone()

    # Accessing the value '27' from the result
    m3_0 = result[128]
    n3_0= result[129]
    o3_0= result[130]
    p3_0= result[131]
    m3_1=result[132]
    n3_1=result[133]
    o3_1=result[134]
    p3_1=result[135]

    print(m3_0) 
    print(n3_0) 
    print(o3_0) 
    print(p3_0) 
    print(m3_1) 
    print(n3_1) 
    print(o3_1) 
    print(p3_1)  # Output: 
    if (m3_0 and m3_1):
        pass
    else:
        button10.config(state=DISABLED)
    if n3_0 and n3_1:
        pass
    else:
        button11.config(state=DISABLED)
    if o3_0 and o3_1:
        pass
    else:
        button12.config(state=DISABLED)
    if p3_0 and p3_1:
        pass
    else:
        button13.config(state=DISABLED)

    # Close the connection
    conn.close()   



def gen():
    tab6 = Toplevel()  # Assign tab1 to the new Tkinter application
    tab6.title("MediSense System")
    tab6.geometry(root.geometry())
    back4_label = Label(tab6, image=back5)
    back4_label.place(x=0, y=0, relwidth=1, relheight=1)
    def welcome_message10():
        engine1 = pyttsx3.init()
        voices = engine1.getProperty('voices')       #getting details of current voice
        #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
        engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
        engine1.setProperty('rate', 150) 
        engine1.say("Choose the Doctor ")
        engine1.runAndWait()
    tab6.after(1000, welcome_message10)
    custom_font6= Font(family="Arial", size=13, weight="bold")
    label9= Label(tab6, text="Choose the Doctor", font=custom_font3,bg="#f00a1d",fg="#ebe4e4",width=25, height=2)
    label9.place(relx=0.50, rely=0.20, anchor="center")
    button10 = Button(tab6, text="Dr Arun", font=custom_font6, bg="#9ee8f0", fg="#111212", command=arun, width=10, height=1)
    button10.place(relx=0.35, rely=0.35, anchor="center")
    button11= Button(tab6, text="Dr Paul", font=custom_font6, bg="#9ee8f0", fg="#111212", command=paul, width=10, height=1)
    button11.place(relx=0.65, rely=0.35, anchor="center")
    button12= Button(tab6, text="Dr Karan", font=custom_font6,bg="#9ee8f0", fg="#111212", command=karan, width=10, height=1)
    button12.place(relx=0.35, rely=0.45, anchor="center")
    button13 = Button(tab6, text="Dr Kishore", font=custom_font6, bg="#9ee8f0", fg="#111212", command=kishore, width=10, height=1)
    button13.place(relx=0.65, rely=0.45, anchor="center")
def ent():
    tab7 = Toplevel()  # Assign tab1 to the new Tkinter application
    tab7.title("MediSense System")
    tab7.geometry(root.geometry())
    back4_label = Label(tab7, image=back5)
    back4_label.place(x=0, y=0, relwidth=1, relheight=1)
    def welcome_message10():
        engine1 = pyttsx3.init()
        voices = engine1.getProperty('voices')       #getting details of current voice
        #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
        engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
        engine1.setProperty('rate', 150) 
        engine1.say("Choose the Doctor ")
        engine1.runAndWait()
    tab7.after(1000, welcome_message10)
    custom_font6= Font(family="Arial", size=13, weight="bold")
    label9= Label(tab7, text="Choose the Doctor", font=custom_font3,bg="#f00a1d",fg="#ebe4e4",width=25, height=2)
    label9.place(relx=0.50, rely=0.20, anchor="center")
    button10 = Button(tab7, text="Dr Raj", font=custom_font6, bg="#9ee8f0", fg="#111212", command=raj, width=10, height=1)
    button10.place(relx=0.35, rely=0.35, anchor="center")
    button11= Button(tab7, text="Dr Kajal", font=custom_font6, bg="#9ee8f0", fg="#111212", command=kajal, width=10, height=1)
    button11.place(relx=0.65, rely=0.35, anchor="center")
    button12= Button(tab7, text="Dr Kapoor", font=custom_font6,bg="#9ee8f0", fg="#111212", command=kapoor, width=10, height=1)
    button12.place(relx=0.35, rely=0.45, anchor="center")
    button13 = Button(tab7, text="Dr Hari", font=custom_font6, bg="#9ee8f0", fg="#111212", command=hari, width=10, height=1)
    button13.place(relx=0.65, rely=0.45, anchor="center")
def ortho():
    tab8 = Toplevel()  # Assign tab1 to the new Tkinter application
    tab8.title("MediSense System")
    tab8.geometry(root.geometry())
    back4_label = Label(tab8, image=back5)
    back4_label.place(x=0, y=0, relwidth=1, relheight=1)
    def welcome_message10():
        engine1 = pyttsx3.init()
        voices = engine1.getProperty('voices')       #getting details of current voice
        #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
        engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
        engine1.setProperty('rate', 150) 
        engine1.say("Choose the Doctor ")
        engine1.runAndWait()
    tab8.after(1000, welcome_message10)
    custom_font6= Font(family="Arial", size=13, weight="bold")
    label9= Label(tab8, text="Choose the Doctor", font=custom_font3,bg="#f00a1d",fg="#ebe4e4",width=25, height=2)
    label9.place(relx=0.50, rely=0.20, anchor="center")
    button10 = Button(tab8, text="Dr Sanjay", font=custom_font6, bg="#9ee8f0", fg="#111212", command=sanjay, width=10, height=1)
    button10.place(relx=0.35, rely=0.35, anchor="center")
    button11= Button(tab8, text="Dr Sundhar", font=custom_font6, bg="#9ee8f0", fg="#111212", command=sundhar, width=10, height=1)
    button11.place(relx=0.65, rely=0.35, anchor="center")
    button12= Button(tab8, text="Dr Madhu", font=custom_font6,bg="#9ee8f0", fg="#111212", command=madhu, width=10, height=1)
    button12.place(relx=0.35, rely=0.45, anchor="center")
    button13 = Button(tab8, text="Dr Dharun", font=custom_font6, bg="#9ee8f0", fg="#111212", command=dharun, width=10, height=1)
    button13.place(relx=0.65, rely=0.45, anchor="center")

def dent():
    tab9 = Toplevel()  # Assign tab1 to the new Tkinter application
    tab9.title("MediSense System")
    tab9.geometry(root.geometry())
    back4_label = Label(tab9, image=back5)
    back4_label.place(x=0, y=0, relwidth=1, relheight=1)
    def welcome_message10():
        engine1 = pyttsx3.init()
        voices = engine1.getProperty('voices')       #getting details of current voice
        #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
        engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
        engine1.setProperty('rate', 150) 
        engine1.say("Choose the Doctor ")
        engine1.runAndWait()
    tab9.after(1000, welcome_message10)
    custom_font6= Font(family="Arial", size=13, weight="bold")
    label9= Label(tab9, text="Choose the Doctor", font=custom_font3,bg="#f00a1d",fg="#ebe4e4",width=25, height=2)
    label9.place(relx=0.50, rely=0.20, anchor="center")
    button10 = Button(tab9, text="Dr Rahul", font=custom_font6, bg="#9ee8f0", fg="#111212", command=rahul, width=10, height=1)
    button10.place(relx=0.35, rely=0.35, anchor="center")
    button11= Button(tab9, text="Dr Ram", font=custom_font6, bg="#9ee8f0", fg="#111212", command=ram, width=10, height=1)
    button11.place(relx=0.65, rely=0.35, anchor="center")
    button12= Button(tab9, text="Dr Sara", font=custom_font6,bg="#9ee8f0", fg="#111212", command=sara, width=10, height=1)
    button12.place(relx=0.35, rely=0.45, anchor="center")
    button13 = Button(tab9, text="Dr Vasan", font=custom_font6, bg="#9ee8f0", fg="#111212", command=vasan, width=10, height=1)
    button13.place(relx=0.65, rely=0.45, anchor="center")



def new4():

    global tab3,tab4,back5,custom_font6,custom_font3
    custom_font3= Font(family="Arial", size=18, weight="bold")
    
    tab5 = Toplevel()  # Assign tab1 to the new Tkinter application
    tab5.title("MediSense System")
    tab5.geometry(root.geometry())
    back5 = ImageTk.PhotoImage(Image.open(r"C:\pyy\project\new2.jpg"))
    back3_label = Label(tab5, image=back5)
    back3_label.place(x=0, y=0, relwidth=1, relheight=1)
    def welcome_message9():
        engine1 = pyttsx3.init()
        voices = engine1.getProperty('voices')       #getting details of current voice
        #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
        engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
        engine1.setProperty('rate', 150) 
        engine1.say("Choose the Specialization ")
        engine1.runAndWait()
    tab5.after(1000, welcome_message9)
    custom_font6= Font(family="Arial", size=13, weight="bold")
    label5= Label(tab5, text="Choose the Specialization", font=custom_font3,bg="#f00a1d",fg="#ebe4e4",width=25, height=2)
    label5.place(relx=0.50, rely=0.20, anchor="center")
    button5 = Button(tab5, text="General", font=custom_font6, bg="#9ee8f0", fg="#111212", command=gen, width=10, height=1)
    button5.place(relx=0.35, rely=0.35, anchor="center")
    button6 = Button(tab5, text="ENT", font=custom_font6, bg="#9ee8f0", fg="#111212", command=ent, width=10, height=1)
    button6.place(relx=0.65, rely=0.35, anchor="center")
    button7 = Button(tab5, text="Ortho", font=custom_font6,bg="#9ee8f0", fg="#111212", command=ortho, width=10, height=1)
    button7.place(relx=0.35, rely=0.45, anchor="center")
    button8 = Button(tab5, text="Dentist", font=custom_font6, bg="#9ee8f0", fg="#111212", command=dent, width=10, height=1)
    button8.place(relx=0.65, rely=0.45, anchor="center")
    buttons = [button5, button6, button7, button8]
    for button in buttons:
        button.config(state=DISABLED)

    root.after(2000, lambda: [button.config(state=NORMAL) for button in buttons])
    if current_hour > 9 or (current_hour == 9 and current_minute > 0):
            # Update specific values
                conn = sqlite3.connect('time_tablebook.db')  
                c = conn.cursor()
                new_values = (0,0,0,0)

                c.execute("""
                        UPDATE time
                        SET A0_1=?, E0_1=?, I0_1=?, M0_1=?
                        WHERE oid=1
                        """, new_values)

                    # Commit the transaction
                conn.commit()
                conn.close()
    if current_hour > 9 or (current_hour == 9 and current_minute > 30):
            # Update specific values
            conn = sqlite3.connect('time_tablebook.db')  
            c = conn.cursor()
            new_values = (0,0,0,0)

            c.execute("""
                        UPDATE time
                        SET B0_1=?, F0_1=?, J0_1=?, N0_1=?
                        WHERE oid=1
                        """, new_values)

                    # Commit the transaction
            conn.commit()
            conn.close()
    if current_hour > 10 or (current_hour == 10 and current_minute > 0):
            # Update specific values
            conn = sqlite3.connect('time_tablebook.db')  
            c = conn.cursor()
            new_values = (0,0,0,0)

            c.execute("""
                        UPDATE time
                        SET C0_1=?, G0_1=?, K0_1=?, O0_1=?
                        WHERE oid=1
                        """, new_values)

                    # Commit the transaction
            conn.commit()
            conn.close()
    if current_hour > 10 or (current_hour == 10 and current_minute > 30):
            # Update specific values
            conn = sqlite3.connect('time_tablebook.db')  
            c = conn.cursor()
            new_values = (0,0,0,0)

            c.execute("""
                        UPDATE time
                        SET D0_1=?, H0_1=?, L0_1=?, P0_1=?
                        WHERE oid=1 
                        """, new_values)

                    # Commit the transaction
            conn.commit()
            conn.close()    
    if current_hour > 11 or (current_hour == 11 and current_minute > 0):
            # Update specific values
            conn = sqlite3.connect('time_tablebook.db')  
            c = conn.cursor()
            new_values = (0,0,0,0)

            c.execute("""
                        UPDATE time
                        SET A1_1=?, E1_1=?, I1_1=?, M1_1=?
                        WHERE oid=1 
                        """, new_values)

                    # Commit the transaction
            conn.commit()
            conn.close() 
    if current_hour > 11 or (current_hour == 11 and current_minute > 30):
            # Update specific values
            conn = sqlite3.connect('time_tablebook.db')  
            c = conn.cursor()
            new_values = (0,0,0,0)

            c.execute("""
                        UPDATE time
                        SET B1_1=?, F1_1=?, J1_1=?, N1_1=?
                        WHERE oid=1 
                        """, new_values)

                    # Commit the transaction
            conn.commit()
            conn.close() 
    if current_hour > 12 or (current_hour == 12 and current_minute > 0):
            # Update specific values
            conn = sqlite3.connect('time_tablebook.db')  
            c = conn.cursor()
            new_values = (0,0,0,0)

            c.execute("""
                        UPDATE time
                        SET C1_1=?, G1_1=?, K1_1=?, O1_1=?
                        WHERE oid=1 
                        """, new_values)

                    # Commit the transaction
            conn.commit()
            conn.close()
    if current_hour > 12 or (current_hour == 12 and current_minute > 30):
            # Update specific values
            conn = sqlite3.connect('time_tablebook.db')  
            c = conn.cursor()
            new_values = (0,0,0,0)

            c.execute("""
                        UPDATE time
                        SET D1_1=?, H1_1=?, L1_1=?, P1_1=?
                        WHERE oid=1 
                        """, new_values)

                    # Commit the transaction
            conn.commit()
            conn.close()
    if current_hour > 14 or (current_hour == 14 and current_minute > 0):
            # Update specific values
            conn = sqlite3.connect('time_tablebook.db')  
            c = conn.cursor()
            new_values = (0,0,0,0)

            c.execute("""
                        UPDATE time
                        SET A2_1=?, E2_1=?, I2_1=?, M2_1=?
                        WHERE oid=1 
                        """, new_values)

                    # Commit the transaction
            conn.commit()
            conn.close()
    if current_hour > 14 or (current_hour == 14 and current_minute > 30):
            # Update specific values
            conn = sqlite3.connect('time_tablebook.db')  
            c = conn.cursor()
            new_values = (0,0,0,0)

            c.execute("""
                        UPDATE time
                        SET B2_1=?, F2_1=?, J2_1=?, N2_1=?
                        WHERE oid=1 
                        """, new_values)

                    # Commit the transaction
            conn.commit()
            conn.close()
    if current_hour > 15 or (current_hour == 15 and current_minute > 0):
            # Update specific values
            conn = sqlite3.connect('time_tablebook.db')  
            c = conn.cursor()
            new_values = (0,0,0,0)

            c.execute("""
                        UPDATE time
                        SET C2_1=?, G2_1=?, K2_1=?, O2_1=?
                        WHERE oid=1 
                        """, new_values)

                    # Commit the transaction
            conn.commit()
            conn.close()
    if current_hour > 15 or (current_hour == 15 and current_minute > 30):
            # Update specific values
            conn = sqlite3.connect('time_tablebook.db')  
            c = conn.cursor()
            new_values = (0,0,0,0)

            c.execute("""
                        UPDATE time
                        SET D2_1=?, H2_1=?, L2_1=?, P2_1=?
                        WHERE oid=1 
                        """, new_values)

                    # Commit the transaction
            conn.commit()
            conn.close()
    if current_hour > 16 or (current_hour == 16 and current_minute > 0):
            # Update specific values
            conn = sqlite3.connect('time_tablebook.db')  
            c = conn.cursor()
            new_values = (0,0,0,0)

            c.execute("""
                        UPDATE time
                        SET A3_1=?, E3_1=?, I3_1=?, M3_1=?
                        WHERE oid=1 
                        """, new_values)

                    # Commit the transaction
            conn.commit()
            conn.close()
    if current_hour > 16 or (current_hour == 16 and current_minute > 30):
            # Update specific values
            conn = sqlite3.connect('time_tablebook.db')  
            c = conn.cursor()
            new_values = (0,0,0,0)

            c.execute("""
                        UPDATE time
                        SET B3_1=?, F3_1=?, J3_1=?, N3_1=?
                        WHERE oid=1 
                        """, new_values)

                    # Commit the transaction
            conn.commit()
            conn.close()
    if current_hour > 17 or (current_hour == 17 and current_minute > 0):
            # Update specific values
            conn = sqlite3.connect('time_tablebook.db')  
            c = conn.cursor()
            new_values = (0,0,0,0)

            c.execute("""
                        UPDATE time
                        SET C3_1=?, G3_1=?, K3_1=?, O3_1=?
                        WHERE oid=1 
                        """, new_values)

                    # Commit the transaction
            conn.commit()
            conn.close()
    if current_hour > 17 or (current_hour == 17 and current_minute > 30):
            # Update specific values
            conn = sqlite3.connect('time_tablebook.db')  
            c = conn.cursor()
            new_values = (0,0,0,0)

            c.execute("""
                        UPDATE time
                        SET D3_1=?, H3_1=?, L3_1=?, P3_1=?
                        WHERE oid=1 
                        """, new_values)

                    # Commit the transaction
            conn.commit()
            conn.close() 
    conn = sqlite3.connect('time_tablebook.db')
    c=conn.cursor()
    c.execute("SELECT *,oid FROM time")
    records=c.fetchall()
    print(records)
    # Commit the transaction
    conn.commit()

    # Close the connection
    conn.close()
   
    




def aws():



    current_date1 = datetime.date.today()
    formatted_date = current_date1.strftime("%d-%m-%Y")
# Print the formatted date
    print( formatted_date)
    conn = sqlite3.connect('time_tablebook.db')
    c = conn.cursor()

    # Execute a SELECT query to fetch the data
    c.execute("SELECT * FROM time")

    # Fetch the result
    result = c.fetchone()

    # Accessing the value '27' from the result
    height2= result[3]
    temperature2=result[4]
    weight2=result[5]
    heartrate2=result[6]
    oxygenlevel2=result[7]
    height3=height2/100
    bmi = weight2 / (height3 ** 2)
    if bmi < 18.5:
        bmiclass="Underweight"
    elif 18.5 <= bmi < 25:
        bmiclass= "Normal weight"
    elif 25 <= bmi < 30:
        bmiclass= "Overweight"
    else:
        bmiclass= "Obese"
    print(bmiclass)
    patientiddd=realpatient
    print(realpatient)
    
    # Close the connection
    conn.close()
    conn = sqlite3.connect('patient_book.db')
    c = conn.cursor()
    c.execute("SELECT * FROM patient WHERE oid="+ str(patientid2))
    patient_data = c.fetchone()
    print(patient_data)
    name11=patient_data[0]
    age11=patient_data[1]
    phone11=patient_data[2]
    print(age11)



    conn.commit()
    conn.close()

    









    # Initialize the S3 client

    # Define your AWS credentials and region
    aws_access_key_id = 'AKIAZKHZJ4ZMCFFSCZDJ'
    aws_secret_access_key = 'KpEu2hZOKXGUoDe5EO+U717siLmXdIRq5AOsT5Iu'

    s3 = boto3.client('s3', region_name='Ohio')


    s3 = boto3.client('s3', 
                    aws_access_key_id=aws_access_key_id, 
                    aws_secret_access_key=aws_secret_access_key)

    # Specify the bucket name and the folder (prefix) you want to create
    bucket_name = 'trial-new'
    folder_name = str(patientiddd)
    helo=str(formatted_date)


    # Create a sample JSON data
    json_data = {"readings":
                [
                {
                "patient_identifer": patientiddd ,
                "patient_name":   name11 ,
                "patient_phone_no":  phone11,
                "patient_age":  age11,
                "date": formatted_date,
                "height": height1,
                "weight": weight2,
                "temperature": temperature2,
                "heartrate": heartrate2,
                "spo2":oxygenlevel2,
                "bmi":bmi,
                "bmi_classification":bmiclass
                }
                ]
    
    }

    # Convert the JSON data to string
    json_string = json.dumps(json_data)

    # Specify the file name for the JSON file
    file_name = folder_name + "/" + helo+".json"

    # Upload the JSON file to S3
    s3.put_object(Bucket=bucket_name, Key=file_name, Body=json_string)

    #who



    Name=arun
    os.environ['AWS_ACCESS_KEY_ID'] = 'AKIAZKHZJ4ZMCFFSCZDJ'
    os.environ['AWS_SECRET_ACCESS_KEY'] = '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'


    folder_name = "who"+ str(formatted_date)


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
        bucket_name = 'trial14567543'
        file_key = folder_name + ".json"
        
        # Set the local file path with the desired destination path
        destination_path = r"D:\mini\doctoravail\\" + folder_name + ".json"
        
        download_json_from_s3(bucket_name, file_key, destination_path)
    
    #from pc
   
    
    # Construct the file path
    file_path = r"D:\mini\doctoravail\\" + folder_name + ".json"

    # Check if the file exists
    if os.path.exists(file_path):
        # Step 1: Read the JSON file
        with open(file_path, 'r') as file:
            # Read the JSON data
            json_data = file.read()

        # Step 2: Parse the JSON data
        data = json.loads(json_data)
        Name=data['name']
        print(Name)






    if Name=="arun":

        #arun



        os.environ['AWS_ACCESS_KEY_ID'] = 'AKIAZKHZJ4ZMCFFSCZDJ'
        os.environ['AWS_SECRET_ACCESS_KEY'] = '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'


        folder_name = "arun"+ str(formatted_date)


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
            bucket_name = 'trial14567543'
            file_key = folder_name + ".json"
            
            # Set the local file path with the desired destination path
            destination_path = r"D:\mini\doctoravail\\" + folder_name + ".json"
            
            download_json_from_s3(bucket_name, file_key, destination_path)
        
        #from pc
    

        # Construct the file path
        file_path = r"D:\mini\doctoravail\\" + folder_name + ".json"

        # Check if the file exists
        if os.path.exists(file_path):
            # Step 1: Read the JSON file
            with open(file_path, 'r') as file:
                # Read the JSON data
                json_data = file.read()

            # Step 2: Parse the JSON data
            data = json.loads(json_data)
            conn = sqlite3.connect('time_tablebook.db')
            c = conn.cursor()

            # Execute a SELECT query to fetch the data
            c.execute("SELECT * FROM time")

            # Fetch the result
            result = c.fetchone()

            # Accessing the value '27' from the result

            a0_1=result[12]
            b0_1=result[13]
            c0_1=result[14]
            d0_1=result[15]

            # Step 3: Access the data
            # Example: Assuming the JSON structure is {"key": "value"}
            if a0_1==1:
                A0_1= data['a0']
            else:
                A0_1=0
            if b0_1==1:
                B0_1= data['b0']
            else:
                B0_1=0
            if c0_1==1:
                C0_1= data['c0']
            else:
                C0_1=0
            if d0_1==1:
                D0_1= data['d0']
            else:
                D0_1=0
            conn = sqlite3.connect('time_tablebook.db')
            c = conn.cursor()

            # Update specific values
            new_values = (A0_1, B0_1, C0_1,D0_1 )

            c.execute("""
                UPDATE time
                SET A0_1=?, B0_1=?, C0_1=?,D0_1=?

                WHERE oid=1
                """, new_values)

            # Commit the transaction
            conn.commit()

            # Close the connection
            conn.close()


        else:
            pass

    if Name=="paul":
        #paul

        folder_name = "paul"+ str(formatted_date)

        os.environ['AWS_ACCESS_KEY_ID'] = 'AKIAZKHZJ4ZMCFFSCZDJ'
        os.environ['AWS_SECRET_ACCESS_KEY'] = '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'





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
            bucket_name = 'trial14567543'
            file_key = folder_name + ".json"
            
            # Set the local file path with the desired destination path
            destination_path = r"D:\mini\doctoravail\\" + folder_name + ".json"
            
            download_json_from_s3(bucket_name, file_key, destination_path)
        
        #from pc
    

        # Construct the file path
        file_path = r"D:\mini\doctoravail\\" + folder_name + ".json"

        # Check if the file exists
        if os.path.exists(file_path):
            # Step 1: Read the JSON file
            with open(file_path, 'r') as file:
                # Read the JSON data
                json_data = file.read()

            # Step 2: Parse the JSON data
            data = json.loads(json_data)
            conn = sqlite3.connect('time_tablebook.db')
            c = conn.cursor()

            # Execute a SELECT query to fetch the data
            c.execute("SELECT * FROM time")

            # Fetch the result
            result = c.fetchone()

            # Accessing the value '27' from the result

            a1_1=result[20]
            b1_1=result[21]
            c1_1=result[22]
            d1_1=result[23]

            # Step 3: Access the data
            # Example: Assuming the JSON structure is {"key": "value"}
            if a1_1==1:
                A1_1 = data['a1']
            else:
                A1_1=0
            if b1_1==1:
                B1_1= data['b1']
            else:
                B1_1=0
            if c1_1==1:
                C1_1= data['c1']
            else:
                C1_1=0
            if d1_1==1:
                D1_1= data['d1']
            else:
                D1_1=0
            conn = sqlite3.connect('time_tablebook.db')
            c = conn.cursor()

            # Update specific values
            new_values = (A1_1, B1_1, C1_1,D1_1 )

            c.execute("""
                UPDATE time
                SET A1_1=?, B1_1=?, C1_1=?,D1_1=?

                WHERE oid=1
                """, new_values)

            # Commit the transaction
            conn.commit()

            # Close the connection
            conn.close()


        else:
            pass
    if Name=="karan":
        #karan
        folder_name = "karan"+ str(formatted_date)

        os.environ['AWS_ACCESS_KEY_ID'] = 'AKIAZKHZJ4ZMCFFSCZDJ'
        os.environ['AWS_SECRET_ACCESS_KEY'] = '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'





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
            bucket_name = 'trial14567543'
            file_key = folder_name + ".json"
            
            # Set the local file path with the desired destination path
            destination_path = r"D:\mini\doctoravail\\" + folder_name + ".json"
            
            download_json_from_s3(bucket_name, file_key, destination_path)
        
        #from pc
    

        # Construct the file path
        file_path = r"D:\mini\doctoravail\\" + folder_name + ".json"

        # Check if the file exists
        if os.path.exists(file_path):
            # Step 1: Read the JSON file
            with open(file_path, 'r') as file:
                # Read the JSON data
                json_data = file.read()

            # Step 2: Parse the JSON data
            data = json.loads(json_data)

            # Step 3: Access the data
            # Example: Assuming the JSON structure is {"key": "value"}
            conn = sqlite3.connect('time_tablebook.db')
            c = conn.cursor()

            # Execute a SELECT query to fetch the data
            c.execute("SELECT * FROM time")

            # Fetch the result
            result = c.fetchone()

            # Accessing the value '27' from the result

            a2_1=result[28]
            b2_1=result[29]
            c2_1=result[30]
            d2_1=result[31]

            if a2_1==1:
                A2_1 = data['a2']
            else:
                A2_1=0
            if b2_1==1:
                B2_1= data['b2']
            else:
                B2_1=0
            if c2_1==1:
                C2_1= data['c2']
            else:
                C2_1=0
            if d2_1==1:
                D2_1= data['d2']
            else:
                D2_1=0
            conn = sqlite3.connect('time_tablebook.db')
            c = conn.cursor()

            # Update specific values
            new_values = (A2_1, B2_1, C2_1,D2_1 )

            c.execute("""
                UPDATE time
                SET A2_1=?, B2_1=?, C2_1=?,D2_1=?

                WHERE oid=1
                """, new_values)

            # Commit the transaction
            conn.commit()

            # Close the connection
            conn.close()


        else:
            pass


    if Name=="kishore":
            #kishore
            folder_name = "kishore"+ str(formatted_date)

            os.environ['AWS_ACCESS_KEY_ID'] = 'AKIAZKHZJ4ZMCFFSCZDJ'
            os.environ['AWS_SECRET_ACCESS_KEY'] = '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'





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
                bucket_name = 'trial14567543'
                file_key = folder_name + ".json"
                
                # Set the local file path with the desired destination path
                destination_path = r"D:\mini\doctoravail\\" + folder_name + ".json"
                
                download_json_from_s3(bucket_name, file_key, destination_path)
            
            #from pc
        

            # Construct the file path
            file_path = r"D:\mini\doctoravail\\" + folder_name + ".json"

            # Check if the file exists
            if os.path.exists(file_path):
                # Step 1: Read the JSON file
                with open(file_path, 'r') as file:
                    # Read the JSON data
                    json_data = file.read()

                # Step 2: Parse the JSON data
                data = json.loads(json_data)
                conn = sqlite3.connect('time_tablebook.db')
                c = conn.cursor()

                # Execute a SELECT query to fetch the data
                c.execute("SELECT * FROM time")

                # Fetch the result
                result = c.fetchone()

                # Accessing the value '27' from the result

                a3_1=result[36]
                b3_1=result[37]
                c3_1=result[38]
                d3_1=result[39]

                # Step 3: Access the data
                # Example: Assuming the JSON structure is {"key": "value"}
                if a3_1==1:
                    A3_1 = data['a3']
                else:
                    A3_1=0
                if b3_1==1:
                    B3_1= data['b3']
                else:
                    B3_1=0
                if c3_1==1:
                    C3_1= data['c3']
                else:
                    C3_1=0
                if d3_1==1:
                    D3_1= data['d3']
                else:
                    D3_1=0





                
                
                
                
                conn = sqlite3.connect('time_tablebook.db')
                c = conn.cursor()

                # Update specific values
                new_values = (A3_1, B3_1, C3_1,D3_1 )

                c.execute("""
                    UPDATE time
                    SET A3_1=?, B3_1=?, C3_1=?,D3_1=?

                    WHERE oid=1
                    """, new_values)

                # Commit the transaction
                conn.commit()

                # Close the connection
                conn.close()


            else:
                pass
    if Name=="raj":
        # raj
        folder_name = "raj"+ str(formatted_date)

        os.environ['AWS_ACCESS_KEY_ID'] = 'AKIAZKHZJ4ZMCFFSCZDJ'
        os.environ['AWS_SECRET_ACCESS_KEY'] = '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'





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
            bucket_name = 'trial14567543'
            file_key = folder_name + ".json"
            
            # Set the local file path with the desired destination path
            destination_path = r"D:\mini\doctoravail\\" + folder_name + ".json"
            
            download_json_from_s3(bucket_name, file_key, destination_path)
        
        #from pc
    

        # Construct the file path
        file_path = r"D:\mini\doctoravail\\" + folder_name + ".json"

        # Check if the file exists
        if os.path.exists(file_path):
            # Step 1: Read the JSON file
            with open(file_path, 'r') as file:
                # Read the JSON data
                json_data = file.read()

            # Step 2: Parse the JSON data
            data = json.loads(json_data)

            # Step 3: Access the data
            # Example: Assuming the JSON structure is {"key": "value"}
            conn = sqlite3.connect('time_tablebook.db')
            c = conn.cursor()

            # Execute a SELECT query to fetch the data
            c.execute("SELECT * FROM time")

            # Fetch the result
            result = c.fetchone()

            # Accessing the value '27' from the result

            e0_1=result[44]
            f0_1=result[45]
            g0_1=result[46]
            h0_1=result[47]

            if e0_1==1:
                E0_1 = data['e0']
            else:
                E0_1=0
            if f0_1==1:
                F0_1= data['f0']
            else:
                F0_1=0
            if g0_1==1:
                G0_1= data['g0']
            else:
                G0_1=0
            if h0_1==1:
                H0_1= data['h0']
            else:
                H0_1=0
            conn = sqlite3.connect('time_tablebook.db')
            c = conn.cursor()

            # Update specific values
            new_values = (E0_1, F0_1, G0_1,H0_1 )

            c.execute("""
                UPDATE time
                SET E0_1=?, F0_1=?, G0_1=?,H0_1=?

                WHERE oid=1
                """, new_values)

            # Commit the transaction
            conn.commit()

            # Close the connection
            conn.close()


        else:
            pass

    if Name=="kajal":
        #kajal
        
        folder_name = "kajal"+ str(formatted_date)

        os.environ['AWS_ACCESS_KEY_ID'] = 'AKIAZKHZJ4ZMCFFSCZDJ'
        os.environ['AWS_SECRET_ACCESS_KEY'] = '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'





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
            bucket_name = 'trial14567543'
            file_key = folder_name + ".json"
            
            # Set the local file path with the desired destination path
            destination_path = r"D:\mini\doctoravail\\" + folder_name + ".json"
            
            download_json_from_s3(bucket_name, file_key, destination_path)
        
        #from pc
    

        # Construct the file path
        file_path = r"D:\mini\doctoravail\\" + folder_name + ".json"

        # Check if the file exists
        if os.path.exists(file_path):
            # Step 1: Read the JSON file
            with open(file_path, 'r') as file:
                # Read the JSON data
                json_data = file.read()

            # Step 2: Parse the JSON data
            data = json.loads(json_data)

            # Step 3: Access the data
            # Example: Assuming the JSON structure is {"key": "value"}
            conn = sqlite3.connect('time_tablebook.db')
            c = conn.cursor()

            # Execute a SELECT query to fetch the data
            c.execute("SELECT * FROM time")

            # Fetch the result
            result = c.fetchone()

            # Accessing the value '27' from the result

            e1_1=result[52]
            f1_1=result[53]
            g1_1=result[54]
            h1_1=result[55]

            if e1_1==1:
                E1_1 = data['e1']
            else:
                E1_1=0
            if f1_1==1:
                F1_1= data['f1']
            else:
                F1_1=0
            if g1_1==1:
                G1_1= data['g1']
            else:
                G1_1=0
            if h1_1==1:
                H1_1= data['h1']
            else:
                H1_1=0
            conn = sqlite3.connect('time_tablebook.db')
            c = conn.cursor()

            # Update specific values
            new_values = (E1_1, F1_1, G1_1,H1_1 )

            c.execute("""
                UPDATE time
                SET E1_1=?, F1_1=?, G1_1=?,H1_1=?

                WHERE oid=1
                """, new_values)

            # Commit the transaction
            conn.commit()

            # Close the connection
            conn.close()


        else:
            pass


    if Name=="kapoor":
        #kapoor

        folder_name = "kapoor"+ str(formatted_date)

        os.environ['AWS_ACCESS_KEY_ID'] = 'AKIAZKHZJ4ZMCFFSCZDJ'
        os.environ['AWS_SECRET_ACCESS_KEY'] = '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'





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
            bucket_name = 'trial14567543'
            file_key = folder_name + ".json"
            
            # Set the local file path with the desired destination path
            destination_path = r"D:\mini\doctoravail\\" + folder_name + ".json"
            
            download_json_from_s3(bucket_name, file_key, destination_path)
        
        #from pc
    

        # Construct the file path
        file_path = r"D:\mini\doctoravail\\" + folder_name + ".json"

        # Check if the file exists
        if os.path.exists(file_path):
            # Step 1: Read the JSON file
            with open(file_path, 'r') as file:
                # Read the JSON data
                json_data = file.read()

            # Step 2: Parse the JSON data
            data = json.loads(json_data)

            # Step 3: Access the data
            # Example: Assuming the JSON structure is {"key": "value"}
            conn = sqlite3.connect('time_tablebook.db')
            c = conn.cursor()

            # Execute a SELECT query to fetch the data
            c.execute("SELECT * FROM time")

            # Fetch the result
            result = c.fetchone()

            # Accessing the value '27' from the result

            e2_1=result[60]
            f2_1=result[61]
            g2_1=result[62]
            h2_1=result[63]
            if e2_1==1:
                E2_1 = data['e2']
            else:
                E2_1=0
            if f2_1==1:
                F2_1= data['f2']
            else:
                F2_1=0
            if g2_1==1:
                G2_1= data['g2']
            else:
                G2_1=0
            if h2_1==1:
                H2_1= data['h2']
            else:
                H2_1=0
            conn = sqlite3.connect('time_tablebook.db')
            c = conn.cursor()

            # Update specific values
            new_values = (E2_1, F2_1, G2_1,H2_1 )

            c.execute("""
                UPDATE time
                SET E2_1=?, F2_1=?, G2_1=?,H2_1=?

                WHERE oid=1
                """, new_values)

            # Commit the transaction
            conn.commit()

            # Close the connection
            conn.close()


        else:
            pass


    if Name=="hari":
        #hari
        folder_name = "hari"+ str(formatted_date)

        os.environ['AWS_ACCESS_KEY_ID'] = 'AKIAZKHZJ4ZMCFFSCZDJ'
        os.environ['AWS_SECRET_ACCESS_KEY'] = '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'





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
            bucket_name = 'trial14567543'
            file_key = folder_name + ".json"
            
            # Set the local file path with the desired destination path
            destination_path = r"D:\mini\doctoravail\\" + folder_name + ".json"
            
            download_json_from_s3(bucket_name, file_key, destination_path)
        
        #from pc
    

        # Construct the file path
        file_path = r"D:\mini\doctoravail\\" + folder_name + ".json"

        # Check if the file exists
        if os.path.exists(file_path):
            # Step 1: Read the JSON file
            with open(file_path, 'r') as file:
                # Read the JSON data
                json_data = file.read()

            # Step 2: Parse the JSON data
            data = json.loads(json_data)

            # Step 3: Access the data
            # Example: Assuming the JSON structure is {"key": "value"}
            conn = sqlite3.connect('time_tablebook.db')
            c = conn.cursor()

            # Execute a SELECT query to fetch the data
            c.execute("SELECT * FROM time")

            # Fetch the result
            result = c.fetchone()

            # Accessing the value '27' from the result
            e3_1=result[68]
            f3_1=result[69]
            g3_1=result[70]
            h3_1=result[71]

            if e3_1==1:
                E3_1 = data['e3']
            else:
                E3_1=0
            if f3_1==1:
                F3_1= data['f3']
            else:
                F3_1=0
            if g3_1==1:
                G3_1= data['g3']
            else:
                G3_1=0
            if h3_1==1:
                H3_1= data['h3']
            else:
                H3_1=0
            conn = sqlite3.connect('time_tablebook.db')
            c = conn.cursor()

            # Update specific values
            new_values = (E3_1, F3_1, G3_1,H3_1 )

            c.execute("""
                UPDATE time
                SET E3_1=?, F3_1=?, G3_1=?,H3_1=?

                WHERE oid=1
                """, new_values)

            # Commit the transaction
            conn.commit()

            # Close the connection
            conn.close()


        else:
            pass

    if Name=="sanjay":
        #sanjay

        folder_name = "sanjay"+ str(formatted_date)

        os.environ['AWS_ACCESS_KEY_ID'] = 'AKIAZKHZJ4ZMCFFSCZDJ'
        os.environ['AWS_SECRET_ACCESS_KEY'] = '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'





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
            bucket_name = 'trial14567543'
            file_key = folder_name + ".json"
            
            # Set the local file path with the desired destination path
            destination_path = r"D:\mini\doctoravail\\" + folder_name + ".json"
            
            download_json_from_s3(bucket_name, file_key, destination_path)
        
        #from pc
    

        # Construct the file path
        file_path = r"D:\mini\doctoravail\\" + folder_name + ".json"

        # Check if the file exists
        if os.path.exists(file_path):
            # Step 1: Read the JSON file
            with open(file_path, 'r') as file:
                # Read the JSON data
                json_data = file.read()

            # Step 2: Parse the JSON data
            data = json.loads(json_data)

            # Step 3: Access the data
            # Example: Assuming the JSON structure is {"key": "value"}
            conn = sqlite3.connect('time_tablebook.db')
            c = conn.cursor()

            # Execute a SELECT query to fetch the data
            c.execute("SELECT * FROM time")

            # Fetch the result
            result = c.fetchone()

            # Accessing the value '27' from the result

            i0_1=result[76]
            j0_1=result[77]
            k0_1=result[78]
            l0_1=result[79]

            if i0_1==1:
                I0_1 = data['i0']
            else:
                I0_1=0
            if j0_1==1:
                J0_1= data['j0']
            else:
                J0_1=0
            if k0_1==1:
                K0_1= data['k0']
            else:
                K0_1=0
            if l0_1==1:
                L0_1= data['l0']
            else:
                L0_1=0
            conn = sqlite3.connect('time_tablebook.db')
            c = conn.cursor()

            # Update specific values
            new_values = (I0_1, J0_1, K0_1,L0_1 )

            c.execute("""
                UPDATE time
                SET I0_1=?, J0_1=?, K0_1=?,L0_1=?

                WHERE oid=1
                """, new_values)

            # Commit the transaction
            conn.commit()

            # Close the connection
            conn.close()


        else:
            pass

    if Name=="sundhar":
        #sundhar

        folder_name = "sundhar"+ str(formatted_date)

        os.environ['AWS_ACCESS_KEY_ID'] = 'AKIAZKHZJ4ZMCFFSCZDJ'
        os.environ['AWS_SECRET_ACCESS_KEY'] = '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'





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
            bucket_name = 'trial14567543'
            file_key = folder_name + ".json"
            
            # Set the local file path with the desired destination path
            destination_path = r"D:\mini\doctoravail\\" + folder_name + ".json"
            
            download_json_from_s3(bucket_name, file_key, destination_path)
        
        #from pc
    

        # Construct the file path
        file_path = r"D:\mini\doctoravail\\" + folder_name + ".json"

        # Check if the file exists
        if os.path.exists(file_path):
            # Step 1: Read the JSON file
            with open(file_path, 'r') as file:
                # Read the JSON data
                json_data = file.read()

            # Step 2: Parse the JSON data
            data = json.loads(json_data)

            # Step 3: Access the data
            # Example: Assuming the JSON structure is {"key": "value"}
            conn = sqlite3.connect('time_tablebook.db')
            c = conn.cursor()

            # Execute a SELECT query to fetch the data
            c.execute("SELECT * FROM time")

            # Fetch the result
            result = c.fetchone()

            # Accessing the value '27' from the result
 
            i1_1=result[84]
            j1_1=result[85]
            k1_1=result[86]
            l1_1=result[87]

            if i1_1==1:
                I1_1 = data['i1']
            else:
                I1_1 = 0

            if j1_1==1:
                J1_1= data['j1']
            else:
                J1_1= 0

            if k1_1==1:
                K1_1= data['k1']
            else:
                K1_1= 0

            if l1_1==1:
                L1_1= data['l1']
            else:
                L1_1= 0

            conn = sqlite3.connect('time_tablebook.db')
            c = conn.cursor()

            # Update specific values
            new_values = (I1_1, J1_1, K1_1,L1_1 )

            c.execute("""
                UPDATE time
                SET I1_1=?, J1_1=?, K1_1=?,L1_1=?

                WHERE oid=1
                """, new_values)

            # Commit the transaction
            conn.commit()

            # Close the connection
            conn.close()


        else:
            pass


    if Name=="madhu":
        #madhu

        folder_name = "madhu"+ str(formatted_date)

        os.environ['AWS_ACCESS_KEY_ID'] = 'AKIAZKHZJ4ZMCFFSCZDJ'
        os.environ['AWS_SECRET_ACCESS_KEY'] = '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'





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
            bucket_name = 'trial14567543'
            file_key = folder_name + ".json"
            
            # Set the local file path with the desired destination path
            destination_path = r"D:\mini\doctoravail\\" + folder_name + ".json"
            
            download_json_from_s3(bucket_name, file_key, destination_path)
        
        #from pc
    

        # Construct the file path
        file_path = r"D:\mini\doctoravail\\" + folder_name + ".json"

        # Check if the file exists
        if os.path.exists(file_path):
            # Step 1: Read the JSON file
            with open(file_path, 'r') as file:
                # Read the JSON data
                json_data = file.read()

            # Step 2: Parse the JSON data
            data = json.loads(json_data)

            # Step 3: Access the data
            # Example: Assuming the JSON structure is {"key": "value"}
            conn = sqlite3.connect('time_tablebook.db')
            c = conn.cursor()

            # Execute a SELECT query to fetch the data
            c.execute("SELECT * FROM time")

            # Fetch the result
            result = c.fetchone()

            # Accessing the value '27' from the result
           
            i2_1=result[92]
            j2_1=result[93]
            k2_1=result[94]
            l2_1=result[95]

            if i2_1==1:
                I2_1 = data['i2']
            else:
                I2_1=0
            if j2_1==1:
                J2_1= data['j2']
            else:
                J2_1=0
            
            if k2_1==1:
                K2_1= data['k2']
            else:
                K2_1=0
            if l2_1==1:
                L2_1= data['l2']
            else:
                L2_1=0
            conn = sqlite3.connect('time_tablebook.db')
            c = conn.cursor()

            # Update specific values
            new_values = (I2_1, J2_1, K2_1,L2_1 )

            c.execute("""
                UPDATE time
                SET I2_1=?, J2_1=?, K2_1=?,L2_1=?

                WHERE oid=1
                """, new_values)

            # Commit the transaction
            conn.commit()

            # Close the connection
            conn.close()


        else:
            pass

    if Name=="dharun":
        #dharun

        folder_name = "dharun"+ str(formatted_date)

        os.environ['AWS_ACCESS_KEY_ID'] = 'AKIAZKHZJ4ZMCFFSCZDJ'
        os.environ['AWS_SECRET_ACCESS_KEY'] = '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'





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
            bucket_name = 'trial14567543'
            file_key = folder_name + ".json"
            
            # Set the local file path with the desired destination path
            destination_path = r"D:\mini\doctoravail\\" + folder_name + ".json"
            
            download_json_from_s3(bucket_name, file_key, destination_path)
        
        #from pc
    

        # Construct the file path
        file_path = r"D:\mini\doctoravail\\" + folder_name + ".json"

        # Check if the file exists
        if os.path.exists(file_path):
            # Step 1: Read the JSON file
            with open(file_path, 'r') as file:
                # Read the JSON data
                json_data = file.read()

            # Step 2: Parse the JSON data
            data = json.loads(json_data)

            # Step 3: Access the data
            # Example: Assuming the JSON structure is {"key": "value"}
            conn = sqlite3.connect('time_tablebook.db')
            c = conn.cursor()

            # Execute a SELECT query to fetch the data
            c.execute("SELECT * FROM time")

            # Fetch the result
            result = c.fetchone()

            # Accessing the value '27' from the result

            i3_1=result[100]
            j3_1=result[101]
            k3_1=result[102]
            l3_1=result[103]

            if i3_1==1:
                I3_1 = data['i3']
            else :
                I3_1=0
            if j3_1==1:
                J3_1= data['j3']
            else:
                J3_1=0
            if k3_1==1:
                K3_1= data['k3']
            else:
                K3_1=0
            if l3_1==1:
                L3_1= data['l3']
            else:
                L3_1=0
            conn = sqlite3.connect('time_tablebook.db')
            c = conn.cursor()

            # Update specific values
            new_values = (I3_1, J3_1, K3_1,L3_1 )

            c.execute("""
                UPDATE time
                SET I3_1=?, J3_1=?, K3_1=?,L3_1=?

                WHERE oid=1
                """, new_values)

            # Commit the transaction
            conn.commit()

            # Close the connection
            conn.close()


        else:
            pass 
    if Name=="rahul":
        #rahul
        folder_name = "rahul"+ str(formatted_date)

        os.environ['AWS_ACCESS_KEY_ID'] = 'AKIAZKHZJ4ZMCFFSCZDJ'
        os.environ['AWS_SECRET_ACCESS_KEY'] = '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'





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
            bucket_name = 'trial14567543'
            file_key = folder_name + ".json"
            
            # Set the local file path with the desired destination path
            destination_path = r"D:\mini\doctoravail\\" + folder_name + ".json"
            
            download_json_from_s3(bucket_name, file_key, destination_path)
        
        #from pc
    

        # Construct the file path
        file_path = r"D:\mini\doctoravail\\" + folder_name + ".json"

        # Check if the file exists
        if os.path.exists(file_path):
            # Step 1: Read the JSON file
            with open(file_path, 'r') as file:
                # Read the JSON data
                json_data = file.read()

            # Step 2: Parse the JSON data
            data = json.loads(json_data)

            # Step 3: Access the data
            # Example: Assuming the JSON structure is {"key": "value"}
            conn = sqlite3.connect('time_tablebook.db')
            c = conn.cursor()

            # Execute a SELECT query to fetch the data
            c.execute("SELECT * FROM time")

            # Fetch the result
            result = c.fetchone()

            # Accessing the value '27' from the result
        
            m0_1=result[108]
            n0_1=result[109]
            o0_1=result[110]
            p0_1=result[111]

            if m0_1==1:
                M0_1 = data['m0']
            else:
                M0_1=0
            if n0_1==1:
                N0_1= data['n0']
            else:
                N0_1=0
            if o0_1==1:
                O0_1= data['o0']
            else:
                O0_1=0
            if p0_1==1:
                P0_1= data['p0']
            else:
                P0_1=0
            conn = sqlite3.connect('time_tablebook.db')
            c = conn.cursor()

            # Update specific values
            new_values = (M0_1, N0_1, O0_1,P0_1 )

            c.execute("""
                UPDATE time
                SET M0_1=?, N0_1=?, O0_1=?,P0_1=?

                WHERE oid=1
                """, new_values)

            # Commit the transaction
            conn.commit()

            # Close the connection
            conn.close()


        else:
            pass


    if Name=="ram":
        #ram

        folder_name = "ram"+ str(formatted_date)

        os.environ['AWS_ACCESS_KEY_ID'] = 'AKIAZKHZJ4ZMCFFSCZDJ'
        os.environ['AWS_SECRET_ACCESS_KEY'] = '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'





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
            bucket_name = 'trial14567543'
            file_key = folder_name + ".json"
            
            # Set the local file path with the desired destination path
            destination_path = r"D:\mini\doctoravail\\" + folder_name + ".json"
            
            download_json_from_s3(bucket_name, file_key, destination_path)
        
        #from pc
    

        # Construct the file path
        file_path = r"D:\mini\doctoravail\\" + folder_name + ".json"

        # Check if the file exists
        if os.path.exists(file_path):
            # Step 1: Read the JSON file
            with open(file_path, 'r') as file:
                # Read the JSON data
                json_data = file.read()

            # Step 2: Parse the JSON data
            data = json.loads(json_data)

            # Step 3: Access the data
            # Example: Assuming the JSON structure is {"key": "value"}
            conn = sqlite3.connect('time_tablebook.db')
            c = conn.cursor()

            # Execute a SELECT query to fetch the data
            c.execute("SELECT * FROM time")

            # Fetch the result
            result = c.fetchone()

            # Accessing the value '27' from the result
            
            m1_1=result[116]
            n1_1=result[117]
            o1_1=result[118]
            p1_1=result[119]

            if m1_1==1:
                M1_1 = data['m1']
            else:
                M1_1=0
            if n1_1==1:
                N1_1= data['n1']
            else:
                N1_1=0
            if o1_1==1:
                O1_1= data['o1']
            else:
                O1_1=0
            if p1_1==1:
                P1_1= data['p1']
            else:
                P1_1=0
            conn = sqlite3.connect('time_tablebook.db')
            c = conn.cursor()

            # Update specific values
            new_values = (M1_1, N1_1, O1_1,P1_1 )

            c.execute("""
                UPDATE time
                SET M1_1=?, N1_1=?, O1_1=?,P1_1=?

                WHERE oid=1
                """, new_values)

            # Commit the transaction
            conn.commit()

            # Close the connection
            conn.close()


        else:
            pass

    if Name=="sara":
        #sara

        folder_name = "sara"+ str(formatted_date)

        os.environ['AWS_ACCESS_KEY_ID'] = 'AKIAZKHZJ4ZMCFFSCZDJ'
        os.environ['AWS_SECRET_ACCESS_KEY'] = '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'





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
            bucket_name = 'trial14567543'
            file_key = folder_name + ".json"
            
            # Set the local file path with the desired destination path
            destination_path = r"D:\mini\doctoravail\\" + folder_name + ".json"
            
            download_json_from_s3(bucket_name, file_key, destination_path)
        
        #from pc
    

        # Construct the file path
        file_path = r"D:\mini\doctoravail\\" + folder_name + ".json"

        # Check if the file exists
        if os.path.exists(file_path):
            # Step 1: Read the JSON file
            with open(file_path, 'r') as file:
                # Read the JSON data
                json_data = file.read()

            # Step 2: Parse the JSON data
            data = json.loads(json_data)

            # Step 3: Access the data
            # Example: Assuming the JSON structure is {"key": "value"}
            conn = sqlite3.connect('time_tablebook.db')
            c = conn.cursor()

            # Execute a SELECT query to fetch the data
            c.execute("SELECT * FROM time")

            # Fetch the result
            result = c.fetchone()

            # Accessing the value '27' from the result
            
            m2_1=result[124]
            n2_1=result[125]
            o2_1=result[126]
            p2_1=result[127]

            if m2_1==1:
                M2_1 = data['m2']
            else:
                M2_1=0
            if n2_1==1:
                N2_1= data['n2']
            else:
                N2_1=0
            if o2_1==1:
                O2_1= data['o2']
            else:
                O2_1=0
            if p2_1==1:
                P2_1= data['p2']
            else:
                P2_1=0
            conn = sqlite3.connect('time_tablebook.db')
            c = conn.cursor()

            # Update specific values
            new_values = (M2_1, N2_1, O2_1,P2_1 )

            c.execute("""
                UPDATE time
                SET M2_1=?, N2_1=?, O2_1=?,P2_1=?

                WHERE oid=1
                """, new_values)

            # Commit the transaction
            conn.commit()

            # Close the connection
            conn.close()


        else:
            pass

    if Name=="vasan":

        #vasan

        folder_name = "vasan"+ str(formatted_date)

        os.environ['AWS_ACCESS_KEY_ID'] = 'AKIAZKHZJ4ZMCFFSCZDJ'
        os.environ['AWS_SECRET_ACCESS_KEY'] = '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'





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
            bucket_name = 'trial14567543'
            file_key = folder_name + ".json"
            
            # Set the local file path with the desired destination path
            destination_path = r"D:\mini\doctoravail\\" + folder_name + ".json"
            
            download_json_from_s3(bucket_name, file_key, destination_path)
        
        #from pc
    

        # Construct the file path
        file_path = r"D:\mini\doctoravail\\" + folder_name + ".json"

        # Check if the file exists
        if os.path.exists(file_path):
            # Step 1: Read the JSON file
            with open(file_path, 'r') as file:
                # Read the JSON data
                json_data = file.read()

            # Step 2: Parse the JSON data
            data = json.loads(json_data)

            # Step 3: Access the data
            # Example: Assuming the JSON structure is {"key": "value"}
            conn = sqlite3.connect('time_tablebook.db')
            c = conn.cursor()

            # Execute a SELECT query to fetch the data
            c.execute("SELECT * FROM time")

            # Fetch the result
            result = c.fetchone()

            # Accessing the value '27' from the result
            
            m3_1=result[132]
            n3_1=result[133]
            o3_1=result[134]
            p3_1=result[135]

            if m3_1==1:
                M3_1 = data['m3']
            else:
                M3_1=0
            if n3_1==1:
                N3_1= data['n3']
            else:
                N3_1=0
            if o3_1==1:
                O3_1= data['o3']
            else:
                O3_1=0
            if p3_1==1:
                P3_1= data['p3']
            else:
                P3_1=0
            conn = sqlite3.connect('time_tablebook.db')
            c = conn.cursor()

            # Update specific values
            new_values = (M3_1, N3_1, O3_1,P3_1 )

            c.execute("""
                UPDATE time
                SET M3_1=?, N3_1=?, O3_1=?,P3_1=?

                WHERE oid=1
                """, new_values)

            # Commit the transaction
            conn.commit()

            # Close the connection
            conn.close()




            conn = sqlite3.connect('time_tablebook.db')
            c=conn.cursor()
            c.execute("SELECT *,oid FROM time")
            records=c.fetchall()
            print(records)
            # Commit the transaction
            conn.commit()

            # Close the connection
            conn.close()


        else:
            pass      
    new4()

    








    

def welcome_message100():
    engine1 = pyttsx3.init()
    voices = engine1.getProperty('voices')       #getting details of current voice
    #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
    engine1.setProperty('rate', 150) 
    engine1.say("Click On admission")
    engine1.runAndWait()


def admi():
    global root, back1,label2,custom_font3,custom_font4,tab1
    tab108 = Toplevel()
    tab108.title("MediSense System")
    tab108.geometry(root.geometry())
    # Load the image if it's not already loaded
    back1_label = Label(tab108, image=back1)
    back1_label.place(x=0, y=0, relwidth=1, relheight=1)
    custom_font3= Font(family="Arial", size=20, weight="bold")
    custom_font4= Font(family="Arial", size=15, weight="bold")
    button2 = Button(tab108, text="Admission", font=custom_font1, bg="#f00a1d", fg="#ebe4e4", command=aws, width=20, height=1)
    button2.place(relx=0.50, rely=0.35, anchor="center")
    tab108.after(100, welcome_message100)


def sensor4delay():
    tab107 = Toplevel()  # Assign tab1 to the new Tkinter application
    tab107.title("MediSense System")
    tab107.geometry(root.geometry())
    back20_label = Label(tab107, image=back22)
    back20_label.place(x=0, y=0, relwidth=1, relheight=1)
    global heartrate1,oxygenlevel1
    heartrate1=25.5
    oxygenlevel1=30.0
    conn = sqlite3.connect('time_tablebook.db')
    c = conn.cursor()

    # Execute a SELECT query to fetch the data
    c.execute("SELECT * FROM time")

    # Fetch the result
    result = c.fetchone()
     # Close the connection
    conn.close()

    # Accessing the value '27' from the result
    value_to_print = result[6]
    print(value_to_print)  # Output: 27
    # Close the connection
    conn.close()
    if heartrate1 != value_to_print:

        conn = sqlite3.connect('time_tablebook.db')  
        c = conn.cursor()
        print(heartrate1)
        new_values = (heartrate1,)

        c.execute("""
                UPDATE time
                SET heartrate=?
                WHERE oid=1
                """, new_values)

        # Commit the transaction
        
        conn.commit()
        conn.close
    conn = sqlite3.connect('time_tablebook.db')
    c = conn.cursor()

    # Execute a SELECT query to fetch the data
    c.execute("SELECT * FROM time")

    # Fetch the result
    result = c.fetchone()
     # Close the connection
    conn.close()

    # Accessing the value '27' from the result
    value_to_print = result[7]
    print(value_to_print)  # Output: 27
    # Close the connection
    conn.close()
    if oxygenlevel1 != value_to_print:

        conn = sqlite3.connect('time_tablebook.db')  
        c = conn.cursor()
        print(oxygenlevel1)
        new_values = (oxygenlevel1,)

        c.execute("""
                UPDATE time
                SET oxygenlevel=?
                WHERE oid=1
                """, new_values)

        # Commit the transaction
        
        conn.commit()
        conn.close
    tab107.withdraw() 
    admi() 
    
    

    



def sensor4():
    tab106 = Toplevel()  # Assign tab1 to the new Tkinter application
    tab106.title("MediSense System")
    tab106.geometry(root.geometry())
    back20_label = Label(tab106, image=back22)
    back20_label.place(x=0, y=0, relwidth=1, relheight=1)

  
    root.after(1000, sensor4delay)



def sensor3delay():
    tab105 = Toplevel()  # Assign tab1 to the new Tkinter application
    tab105.title("MediSense System")
    tab105.geometry(root.geometry())
    back20_label = Label(tab105, image=back21)
    back20_label.place(x=0, y=0, relwidth=1, relheight=1)
    global weight1
    weight1=130
    conn = sqlite3.connect('time_tablebook.db')
    c = conn.cursor()

    # Execute a SELECT query to fetch the data
    c.execute("SELECT * FROM time")

    # Fetch the result
    result = c.fetchone()
     # Close the connection
    conn.close()

    # Accessing the value '27' from the result
    value_to_print = result[5]
    print(value_to_print)  # Output: 27
    # Close the connection
    conn.close()
    if weight1 != value_to_print:

        conn = sqlite3.connect('time_tablebook.db')  
        c = conn.cursor()
        print(weight1)
        new_values = (weight1,)

        c.execute("""
                UPDATE time
                SET weight=?
                WHERE oid=1
                """, new_values)

        # Commit the transaction
        
        conn.commit()
        conn.close
        tab105.withdraw() 
        sensor4()
    else:
        tab105.withdraw() 
        sensor4()    # no need




def sensor3():
    tab104 = Toplevel()  # Assign tab1 to the new Tkinter application
    tab104.title("MediSense System")
    tab104.geometry(root.geometry())
    back20_label = Label(tab104, image=back21)
    back20_label.place(x=0, y=0, relwidth=1, relheight=1)

    root.after(1000, sensor3delay)



def sensor2delay():
    tab103 = Toplevel()  # Assign tab1 to the new Tkinter application
    tab103.title("MediSense System")
    tab103.geometry(root.geometry())

    back20_label = Label(tab103, image=back20)
    back20_label.place(x=0, y=0, relwidth=1, relheight=1)

    global temperature1
    temperature1=130
    conn = sqlite3.connect('time_tablebook.db')
    c = conn.cursor()

    # Execute a SELECT query to fetch the data
    c.execute("SELECT * FROM time")

    # Fetch the result
    result = c.fetchone()
     # Close the connection
    conn.close()

    # Accessing the value '27' from the result
    value_to_print = result[4]
    print(value_to_print)  # Output: 27
    # Close the connection
    conn.close()
    if temperature1 != value_to_print:

        conn = sqlite3.connect('time_tablebook.db')  
        c = conn.cursor()
        print(temperature1)
        new_values = (temperature1,)

        c.execute("""
                UPDATE time
                SET temperature=?
                WHERE oid=1
                """, new_values)

        # Commit the transaction
        
        conn.commit()
        conn.close
        tab103.withdraw() 
        sensor3()
    else:
        tab103.withdraw() 
        sensor3()    # no need



def sensor2():
    tab101 = Toplevel()  # Assign tab1 to the new Tkinter application
    tab101.title("MediSense System")
    tab101.geometry(root.geometry())
    back20_label = Label(tab101, image=back20)
    back20_label.place(x=0, y=0, relwidth=1, relheight=1)



    root.after(1000, sensor2delay)




def sensor1delay():
    tab102 = Toplevel()  # Assign tab1 to the new Tkinter application
    tab102.title("MediSense System")
    tab102.geometry(root.geometry())
    back20_label = Label(tab102, image=back23)
    back20_label.place(x=0, y=0, relwidth=1, relheight=1)
    global height1
    height1=150
    conn = sqlite3.connect('time_tablebook.db')
    c = conn.cursor()

    # Execute a SELECT query to fetch the data
    c.execute("SELECT * FROM time")

    # Fetch the result
    result = c.fetchone()
     # Close the connection
    conn.close()

    # Accessing the value '27' from the result
    value_to_print = result[3]
    print(value_to_print)  # Output: 27
    # Close the connection
    conn.close()
    if height1 != value_to_print:

        conn = sqlite3.connect('time_tablebook.db')  
        c = conn.cursor()
        print(height1)
        new_values = (height1,)

        c.execute("""
                UPDATE time
                SET height=?
                WHERE oid=1
                """, new_values)

        # Commit the transaction
        
        conn.commit()
        conn.close
        tab102.withdraw() 
        sensor2()
    else:
        tab102.withdraw() 
        sensor2()
    


    


def sensor1():
    tab100 = Toplevel()  # Assign tab1 to the new Tkinter application
    tab100.title("MediSense System")
    tab100.geometry(root.geometry())
    back20_label = Label(tab100, image=back23)
    back20_label.place(x=0, y=0, relwidth=1, relheight=1)


    root.after(1000, sensor1delay)

    


    


def submit3(patid_value,patid2_value):
    global patientid2, patient_data,patient3,realpatient
    realpatient=int(patid_value)
    patientid2 = int(patid_value) - 910000
    patient3=int(patid2_value)

    # Now you can use the converted integer value as needed
    conn = sqlite3.connect('patient_book.db')
    c = conn.cursor()
    c.execute("SELECT * FROM patient WHERE oid="+ str(patientid2))
    patient_data = c.fetchone()
    print(patient_data)
    print(patient3)
    if(patient_data[2]==patient3):
        response2=messagebox.askyesno("Admission","Hello "+patient_data[0]+"   Do you want to continue the Sensing process?")

        if response2:
            sensor1()
        else:
            root.quit()
    else:
        messagebox.askyesno("Admission","Incorrect Patient Id")
        root.quit()
    
    conn.commit()
    conn.close()



#yes
def new2():
    global tab1,tab2,back2
    tab2 = Toplevel()  # Assign tab1 to the new Tkinter application
    tab2.title("MediSense System")
    tab2.geometry(root.geometry())
    back2 = ImageTk.PhotoImage(Image.open(r"C:\pyy\project\new2.jpg"))
    back2_label = Label(tab2, image=back2)
    back2_label.place(x=0, y=0, relwidth=1, relheight=1)
    def welcome_message6():
        engine1 = pyttsx3.init()
        voices = engine1.getProperty('voices')       #getting details of current voice
        #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
        engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
        engine1.setProperty('rate', 150) 
        engine1.say("Enter Your Id and Phone number  ")
        engine1.runAndWait()
    tab2.after(1000, welcome_message6)
    custom_font5= Font(family="Arial", size=13, weight="bold")
    patid=Entry(tab2,width=30)
    patid.place(relx=0.67, rely=0.20, anchor="center")
    patid_label= Label(tab2, text="Patient Id", font=custom_font5,bg="#9ee8f0", fg="#111212",width=12, height=1)
    patid_label.place(relx=0.30, rely=0.20, anchor="center")
    patid2=Entry(tab2,width=30)
    patid2.place(relx=0.67, rely=0.30, anchor="center")
    patid2_label= Label(tab2, text="Phone Number", font=custom_font5,bg="#9ee8f0", fg="#111212",width=12, height=1)
    patid2_label.place(relx=0.30, rely=0.30, anchor="center")

    submit2_btn=Button(tab2,text="Submit",font=custom_font5,command=lambda:submit3(patid.get(),patid2.get()),width=12, height=1,bg="#f00a1d",fg="#ebe4e4")
    submit2_btn.place(relx=0.47, rely=0.45, anchor="center")






def welcome_message3():
    engine1 = pyttsx3.init()
    voices = engine1.getProperty('voices')       #getting details of current voice
    #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
    engine1.setProperty('rate', 150) 
    engine1.say("Enter Your Name , Age , Phone number and Date of Birth")
    engine1.runAndWait()
def welcome_message4():
    engine1 = pyttsx3.init()
    voices = engine1.getProperty('voices')       #getting details of current voice
    #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
    engine1.setProperty('rate', 150) 
    engine1.say("After  entering  the  Details  , click  patient  id  to  get  your  id")
    engine1.runAndWait()
#no
def new3():
    global tab1,tab3
    custom_font5= Font(family="Arial", size=13, weight="bold")
    tab3 = Toplevel()  # Assign tab1 to the new Tkinter application
    tab3.title("MediSense System")
    tab3.geometry(root.geometry())
    back3_label = Label(tab3, image=back1)
    back3_label.place(x=0, y=0, relwidth=1, relheight=1)
    tab3.after(500, welcome_message3)
    tab3.after(1500, welcome_message4)
    def submit():
        conn=sqlite3.connect('patient_book.db')
        c=conn.cursor()
        c.execute("INSERT INTO patient VALUES(:name1,:age1,:phn1,:dob1)",
                  {
                      'name1':name.get(),
                      'age1':age.get(),
                      'phn1':phone_no.get(),
                      'dob1':d_o_b.get(),
                      
                  })
        conn.commit()
        conn.close()
        name.delete(0,END)
        age.delete(0,END)
        phone_no.delete(0,END)
        d_o_b.delete(0,END)
    def query():
        global response
        conn=sqlite3.connect('patient_book.db')
        c=conn.cursor()
        c.execute("SELECT *,oid FROM patient")
        records=c.fetchall()
        print(records)
        def get_latest_oid():
            conn = sqlite3.connect('patient_book.db')
            c = conn.cursor()
            c.execute("SELECT MAX(oid) FROM patient")
            latest_oid = c.fetchone()[0]
            conn.close()
            return latest_oid
        latest_oid = get_latest_oid()
        print("Latest OID:", latest_oid)
        patient_id=910000+int(latest_oid)
        print(patient_id)
        def welcome_message5():
            engine1 = pyttsx3.init()
            voices = engine1.getProperty('voices')       #getting details of current voice
            #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
            engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
            engine1.setProperty('rate', 150) 
            engine1.say("Your Id   "+ " eeezzz"+ str(patient_id))
            engine1.runAndWait()
        tab3.after(1200, welcome_message5)
        def welcome_message7():
            engine2 = pyttsx3.init()
            voices = engine2.getProperty('voices')       #getting details of current voice
            #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
            engine2.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
            engine2.setProperty('rate', 150) 
            engine2.say("Do you want to go to the Admission page")
            engine2.runAndWait()
        tab3.after(1500, welcome_message7)

        

        response1=messagebox.askyesno("Admission","Your Id" +" is  "+ str(patient_id)+"  ==>  Do you want to go to the Admission page")
        

        if response1:
            new2()  # Call new3() function if "Yes" is clicked
        else:
            root.quit()  # Exit the application if "No" is clicked

    #entries
    name=Entry(tab3,width=30)
    name.place(relx=0.67, rely=0.20, anchor="center")
    age=Entry(tab3,width=30)
    age.place(relx=0.67, rely=0.30, anchor="center")
    phone_no=Entry(tab3,width=30)
    phone_no.place(relx=0.67, rely=0.40, anchor="center")
    d_o_b=Entry(tab3,width=30)
    d_o_b.place(relx=0.67, rely=0.50, anchor="center")


    #label
    name_label= Label(tab3, text="Name", font=custom_font5,bg="#9ee8f0", fg="#111212",width=12, height=1)
    name_label.place(relx=0.30, rely=0.20, anchor="center")
    age_label= Label(tab3, text="Age", font=custom_font5,bg="#9ee8f0", fg="#111212",width=12, height=1)
    age_label.place(relx=0.30, rely=0.30, anchor="center")
    phone_no_label= Label(tab3, text="Phone number", font=custom_font5,bg="#9ee8f0", fg="#111212",width=12, height=1)
    phone_no_label.place(relx=0.30, rely=0.40, anchor="center")
    d_o_b_label= Label(tab3, text="Date of birth", font=custom_font5,bg="#9ee8f0", fg="#111212",width=12, height=1)
    d_o_b_label.place(relx=0.30, rely=0.50, anchor="center")

    #submit
    submit_btn=Button(tab3,text="Submit",font=custom_font5,command=submit,width=12, height=1,bg="#f00a1d",fg="#ebe4e4")
    submit_btn.place(relx=0.47, rely=0.65, anchor="center")

    #query
    query_btn=Button(tab3,text="Patient Id",font=custom_font5,command=query,width=12, height=1,bg="#f00a1d",fg="#ebe4e4")
    query_btn.place(relx=0.47, rely=0.75, anchor="center")


def welcome_message1():
    engine1 = pyttsx3.init()
    voices = engine1.getProperty('voices')       #getting details of current voice
    #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine1.setProperty('voice', voices[1].id)   # getting details of current speaking rate                      #printing current voice rate
    engine1.setProperty('rate', 150) 
    engine1.say("Have You Consulted Here Before ?")
    engine1.runAndWait()



def new1():
    global root, back1,label2,custom_font3,custom_font4,tab1
    tab1 = Toplevel()
    tab1.title("MediSense System")
    tab1.geometry(root.geometry())
    # Load the image if it's not already loaded
    back1_label = Label(tab1, image=back1)
    back1_label.place(x=0, y=0, relwidth=1, relheight=1)
    custom_font3= Font(family="Arial", size=20, weight="bold")
    custom_font4= Font(family="Arial", size=15, weight="bold")
    label2 = Label(tab1, text="Have You Consulted Here Before ? ", font=custom_font3,bg="#f00a1d",fg="#ebe4e4",width=30, height=1)
    label2.place(relx=0.50, rely=0.35, anchor="center")
    button2 = Button(tab1, text="Yes", font=custom_font1, bg="#9ee8f0", fg="#111212", command=new2, width=10, height=1)
    button2.place(relx=0.35, rely=0.55, anchor="center")
    button3 = Button(tab1, text="No", font=custom_font1, bg="#9ee8f0", fg="#111212", command=new3, width=10, height=1)
    button3.place(relx=0.65, rely=0.55, anchor="center")
    tab1.after(500, welcome_message1)

def welcome_message():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')       #getting details of current voice
    #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine.setProperty('voice', voices[1].id)
   # getting details of current speaking rate                       #printing current voice rate
    engine.setProperty('rate', 150) 
    engine.say("Welcome To MediSense System")
    engine.runAndWait()

#main
global back,back_label,back20
root = Tk()
root.geometry("600x400")
root.title("MediSense System")
back = ImageTk.PhotoImage(Image.open(r"C:\pyy\project\new1.jpg"))
back1 = ImageTk.PhotoImage(Image.open(r"C:\pyy\project\new2.jpg"))
back20 = ImageTk.PhotoImage(Image.open(r"C:\pyy\project\temp.jpeg"))
back21 = ImageTk.PhotoImage(Image.open(r"C:\pyy\project\weight.jpeg"))
back22 = ImageTk.PhotoImage(Image.open(r"C:\pyy\project\max.jpeg"))
back23 = ImageTk.PhotoImage(Image.open(r"C:\pyy\project\height.jpg"))
back_label = Label(root, image=back)
back_label.place(x=0, y=0, relwidth=1, relheight=1)  # Use place() to cover the entire window
custom_font = Font(family="Arial", size=20, weight="bold")
custom_font1= Font(family="Arial", size=15, weight="bold")
label1 = Label(root, text="MediSense System", font=custom_font,bg="#f00a1d",fg="#ebe4e4",width=15, height=1)#f00a1d
label1.place(relx=0.25, rely=0.35, anchor="center")  # Center the label horizontally and vertically
button1 = Button(root, text="Get Started", font=custom_font1, bg="#9ee8f0", fg="#111212", command=new1, width=10, height=1)
button1.place(relx=0.25, rely=0.55, anchor="center")
root.after(500, welcome_message)

root.mainloop()