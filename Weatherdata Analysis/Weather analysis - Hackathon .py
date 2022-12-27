#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
import matplotlib.pyplot as plt
import mplcursors as mpc

place=input("Enter place in this list (Heathrow,Leuchars) :")
year=int(input("Enter year in this list (1980 - 2000):"))
print(place,year)

excel=pd.read_excel('Dataset for weather analysis.xlsx',skiprows=1)
column1=[]
location1=[]
year1=[]
Month1=[]
tmax1=[]
tmin1=[]
rain1=[]
sun1=[]
af1=[]

for col in excel.columns:
    column1.append((col))

print('\n')
result=0
for index in excel.index:
    if(excel.at[index,'Location']==place and excel.at[index,'Year']==year ):
        location1.append((excel.at[index,'Location']))   
        year1.append((excel.at[index,'Year']))
        Month1.append((excel.at[index,'Month']))
        tmax1.append((excel.at[index,'tmax']))
        tmin1.append((excel.at[index,'tmin']))
        af1.append((excel.at[index,'af']))
        rain1.append((excel.at[index,'rain']))
        sun1.append((excel.at[index,'sun']))
        result=result+1
        
def addlabelbar(Month1,tmin1):
    for i in range(1,result+1):
        plt.text(i,tmin1[i-1]/2,tmin1[i-1], ha='center')
def addlabelline(x=[],y=[]):
    for x1,y1 in zip(x,y):
        label = "{:.2f}".format(y1)
        plt.annotate(label, # this is the text
                 (x1,y1), # these are the coordinates to position the label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

        
def chart():
    #chart1
    plt.subplots(1,1)
    plt.bar(Month1,tmin1)
    plt.plot(Month1,tmax1,color = 'green',linestyle = 'solid', marker = 'o',markerfacecolor = 'red', markersize = 12)
    plt.xlabel('Months')
    plt.ylabel('tmin & tmax')
    plt.title('Temperature Chart for: ' +str(year))
    plt.legend(['MaxTemp','MinTemp'])
    plt.grid()
    addlabelbar(Month1,tmin1)
    addlabelline(Month1,tmax1)
    #Chart2 
    plt.subplots(1,1)
    plt.scatter(Month1,rain1)
    plt.plot(Month1,rain1)
    plt.fill_between(Month1,rain1,color="lightblue")
    plt.xlabel('Months')
    plt.ylabel('af')
    plt.title('Rainfall chart for:' +str(year))
    plt.legend(['Precipitation'])
    plt.grid()
    addlabelline(Month1,rain1)
    #Chart3
    plt.subplots(1,1)
    plt.plot(Month1,sun1,color="orange")
    plt.scatter(Month1,sun1,marker ='^',color="orange")
    plt.fill_between(Month1,sun1,color="yellow")
    plt.xlabel('Months')
    plt.ylabel('Sunny')
    plt.title('Sunlight chart for:' +str(year))
    plt.legend(['Sunlight'])
    plt.grid()
    mpc.cursor(hover=True)
    addlabelline(Month1,sun1)
    plt.show()
    
if(result):
    print("Results are here...")
    chart()
else:
    print("Please check the parameter given!!!")

