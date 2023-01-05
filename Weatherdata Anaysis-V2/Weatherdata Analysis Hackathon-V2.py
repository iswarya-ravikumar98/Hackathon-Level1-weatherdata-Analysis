import pandas as pd
import matplotlib.pyplot as plt
#assign excel value to dataframe
df=pd.read_excel("C:\\Users\\admin\\Desktop\\Sample Jupyter\\Dataset_new.xlsx")
#preprocessing
df=df.replace('\*','',regex=True)
df=df.replace('\#','',regex=True)
df=df.replace('\---','0',regex=True)
#Getting User Input for Location
inputlocation=str(input("Enter location from list(Hurn,Heathrow,Valley):"))
#introducing list to have average values of each column(sun,rainfall,Air Frost, Min and Max Temperature)
Month1=[1,2,3,4,5,6,7,8,9,10,11,12]
sun_chart=[]
tmax_chart=[]
tmin_chart=[]
rain_chart=[]
af_chart=[]
#Methods for adding datalabels to the chart
def addlabelline(x=[],y=[]):
    for x1,y1 in zip(x,y):
        label = "{:.2f}".format(y1)
        plt.annotate(label, # this is the text
                 (x1,y1), # these are the coordinates to position the label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

#Finding Avg value and creating chart of diferent styles
def sunchart():
    for i in range(12):
        df_temp=df.loc[((df['Location']==inputlocation) & (df['mm']==i+1))]
        df_temp=pd.to_numeric(df_temp['sun'], downcast="float")
        sun_chart.append(df_temp.mean())
    print("Sun chart Average Value:\n",sun_chart)
    plt.subplots(1,1)
    plt.plot(Month1,sun_chart,color="green",marker='*')
    plt.fill_between(Month1,sun_chart,color="yellow")
    plt.title('Chart for Sunlight -'+str(inputlocation))
    plt.legend(['Sunlight'])
    plt.xlabel('Months')
    plt.ylabel('Monthly avarage value for Sunlight')
    addlabelline(Month1,sun_chart)
    plt.grid()
    
    
def rainchart():
    for i in range(12):
        df_temp=df.loc[((df['Location']==inputlocation) & (df['mm']==i+1))]
        df_temp=pd.to_numeric(df_temp['rain'], downcast="float")
        rain_chart.append(df_temp.mean())
    print("Rain chart Average Value:\n",rain_chart)
    plt.subplots(1,1)
    plt.plot(Month1,rain_chart,color="green")
    plt.fill_between(Month1,rain_chart,color="blue")
    plt.title('Chart for Rainfall  -'+str(inputlocation))
    plt.legend(['Precipitation'])
    plt.xlabel('Months')
    plt.ylabel('Monthly avarage value for Precipitation')
    addlabelline(Month1,rain_chart)
    plt.grid()
    
def tminchart():
    for i in range(12):
        df_temp=df.loc[((df['Location']==inputlocation) & (df['mm']==i+1))]
        df_temp=pd.to_numeric(df_temp['tmin'], downcast="float")
        tmin_chart.append(df_temp.mean())
    print("tmin chart Average Value:\n",tmin_chart)

def tmaxchart():
    for i in range(12):
        df_temp=df.loc[((df['Location']==inputlocation) & (df['mm']==i+1))]
        df_temp=pd.to_numeric(df_temp['tmax'], downcast="float")
        tmax_chart.append(df_temp.mean())
    print("tmax chart Average Value:\n",tmax_chart)
    plt.subplots(1,1)
    plt.scatter(Month1,tmin_chart,color="red")
    plt.plot(Month1,tmax_chart,color = 'blue',linestyle = 'solid', marker = 'o',markerfacecolor = 'green', markersize = 12)
    plt.legend(['MinTemp','MaxTemp'])
    plt.xlabel('Months')
    plt.ylabel('Monthly avarage value for Min and Max Temperature')
    plt.title('Chart for Min and Max Temperature-'+str(inputlocation))
    addlabelline(Month1,tmin_chart)
    addlabelline(Month1,tmax_chart)
    plt.grid()

def afchart():
    for i in range(12):
        df_temp=df.loc[((df['Location']==inputlocation) & (df['mm']==i+1))]
        df_temp=pd.to_numeric(df_temp['af'], downcast="float")
        af_chart.append(df_temp.mean())
    print("af chart Average Value:\n",af_chart)
    plt.subplots(1,1)
    plt.plot(Month1,af_chart,marker ='*',color="brown")
    plt.fill_between(Month1,af_chart,color="pink")
    plt.title('Chart for Air Frost -'+str(inputlocation))
    plt.legend(['af'])
    plt.xlabel('Months')
    plt.ylabel('Monthly avarage value for Air Frost')
    addlabelline(Month1,af_chart)
    plt.grid()

# Function Calling to create chart    
sunchart()
rainchart()
tminchart()
tmaxchart()
afchart()
plt.show()
    

