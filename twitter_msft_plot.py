import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from datetime import datetime

style.use("ggplot")

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
#ax1 = fig.add_subplot(121)


def animate(i):
    graph_data = open('twitter_msft_score.txt','r').read()
    lines = graph_data.split('\n')
    xs = []
    ys = []
    timeStamp = []
    for line in lines[-50:]:
        if len(line) > 1:
            #x, y, timeStamp = line.split(',')
            x, y = line.split(',')
            #print(timeStamp)
            #print(y)
            #print(x)
            #timeStamp = timeStamp.split(' ')
            #month = timeStamp[1]
            #date = timeStamp[2]
            #time = timeStamp[3]
            #year = timeStamp[5]
            #print(timeStamp[1])
            #print(timeStamp[2])
            #print(timeStamp[3])
            #print(timeStamp[4])
            #print(timeStamp[5])
            #date = timeStamp[1] + " " + timeStamp[2] + " " + timeStamp[5] + " " + timeStamp[3]
            #print(date)
            #date_object = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')
            #date_object = datetime.strptime(date, '%b %d %Y %H:%M:%S')
            #print(date_object) 
            #xs.append(date_object)
            xs.append(x)
            ys.append(y)
    ax1.clear()
    ax1.plot(xs, ys)
    ax1.set_xlabel('Tweet #')
    ax1.set_ylabel('Total Score')
    ax1.set_title('"msft", "microsoft", "windows"')
    
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()