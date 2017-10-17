import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from datetime import datetime, timedelta
import matplotlib.dates as mdates

style.use("ggplot")

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
#ax1 = fig.add_subplot(121)


def animate(i):
    graph_data = open('twitter_msft_score2.txt','r').read()
    lines = graph_data.split('\n')
    xs = []
    ys = []
    timeStamp = []
    color = []
    for line in lines[-5000:]:
        if len(line) > 1:
            x, y, timeStamp = line.split(',')
            #x, y = line.split(',')
            #print(timeStamp)
            #print(y)
            #print(x)
            timeStamp = timeStamp.split(' ')
            #month = timeStamp[1]
            #date = timeStamp[2]
            #time = timeStamp[3]
            #year = timeStamp[5]
            #print(timeStamp[1])
            #print(timeStamp[2])
            #print(timeStamp[3])
            #print(timeStamp[4])
            #print(timeStamp[5])
            date = timeStamp[1] + " " + timeStamp[2] + " " + timeStamp[5] + " " + timeStamp[3]
            #print(date)
            #date_object = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')
            date_object = datetime.strptime(date, '%b %d %Y %H:%M:%S')
            date_object = date_object + timedelta(hours=-4)
            #print(date_object) 
            xs.append(date_object)
            #xs.append(x)
            ys.append(y)
            '''
            if float(y) > 30:
                color.append('g')
            else:
                color.append('r')
                
            #print(float(y))
            print(color) 
            '''
    ax1.clear()
    ax1.plot(xs, ys)
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %d %Y %H:%M:%S'))
    plt.gcf().autofmt_xdate()
    fig.canvas.set_window_title('microsoft')
    ax1.set_xlabel('Time')
    ax1.set_ylabel('Total Score')
    ax1.set_title('"msft", "microsoft", "windows10"')
    
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()