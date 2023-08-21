import os
import matplotlib.pyplot as plt
import collections
from datetime import datetime

path = r"A:\Program Files (x86)"
path2 = r"C:\Program Files (x86)\Adobe"
#time = os.path.getctime(path)
#print(time)
#print(datetime.fromtimestamp(time))
ignore_path = [r"A:\Program Files (x86)\Favourites\202001-203000",
          r"A:\Program Files (x86)\NSFW\Haneru Himitsu Collection\Himitsu ひみつ gallary"]
ignore_date = ["2020-05-19"] #mass reddit save

def iterate(pathname,paths=[]):
    for file in os.listdir(pathname):
        path = pathname+"\\"+file
        #print(path)
        if os.path.isdir(path):
            iterate(path,paths)
        elif pathname not in ignore_path:
            paths.append(pathname+"\\"+file)
    return paths

def getcdates(files):
    dates = []
    for f in files:
        #print(f)
        date = str(datetime.fromtimestamp(os.path.getmtime(f)).date())
        if date not in ignore_date:
            dates.append(date)
        if date in ignore_date:
            print(f)
    return dates

def processActivity(data):
    activity = collections.defaultdict(int)
    for d in data:
        activity[d] += 1
    return activity

files = iterate(path)
dates = getcdates(files)
activity = processActivity(dates)
#print(activity)
activity = [list(activity.keys()), list(activity.values())]
X = activity[0]
Y = activity[1]
#print([x for _, x in sorted(zip(Y, X), key=lambda pair: pair[0])])
X = sorted(X)
#print(X)
Y = [x for _, x in sorted(zip(X, Y), key=lambda pair: pair[0])]
#print(Y)

plt.scatter(X,Y,s=0.5)
plt.title("Art Folder Activity")
plt.xlabel("Date")
plt.ylabel("No. of added files")
plt.show()
