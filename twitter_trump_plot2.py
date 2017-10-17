import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from datetime import datetime, timedelta
import matplotlib.dates as mdates
#import time

style.use("ggplot")

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    graph_data = open('twitter_trump_score2.txt','r').read()
    lines = graph_data.split('\n')
    xs = []
    ys = []
    timeStamp = []
    for line in lines[-5000:]:#for line in lines[-200:]:
        if len(line) > 1:
            x, y, timeStamp = line.split(',')
            timeStamp = timeStamp.split(' ')
            date = timeStamp[1] + " " + timeStamp[2] + " " + timeStamp[5] + " " + timeStamp[3]
            date_object = datetime.strptime(date, '%b %d %Y %H:%M:%S')
            date_object = date_object + timedelta(hours=-4)
            #print(date_object) 
            xs.append(date_object)
            ys.append(y)
    ax1.clear()
    ax1.plot(xs, ys)
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %d %Y %H:%M:%S'))
    plt.gcf().autofmt_xdate()
    fig.canvas.set_window_title('trump')
    ax1.set_xlabel('Time')
    ax1.set_ylabel('Total Score')
    ax1.set_title('"trump"')
    
ani = animation.FuncAnimation(fig, animate, interval=1000)
ax1.set_xlabel('Tweet #')
ax1.set_ylabel('Total Score')
#plt.xlabel('Tweet #')
#plt.ylabel('Total Score')
#plt.title('Obama')
plt.show()