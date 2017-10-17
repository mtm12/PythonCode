import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from datetime import datetime, timedelta
import matplotlib.dates as mdates
import numpy as np
import itertools

style.use("ggplot")

fig = plt.figure()
#fig2 = plt.figure()
ax1 = fig.add_subplot(511)
ax2 = fig.add_subplot(513)
ax3 = fig.add_subplot(515)

def animate(i):
    graph_data = open('twitter_msft_score3.txt','r').read()
    lines = graph_data.split('\n')
    xs = []
    ys = []
    timeStamp = []
    ss = []
    for line in lines[-5000:]:
        if len(line) > 1:
            x, y, sumation, timeStamp = line.split(',')
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
            ss.append(sumation)

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
    ax1.set_xlabel('Time')
    ax1.set_ylabel('Total Score')
    ax1.set_title('"msft", "microsoft", "windows10"')
    #ax1.xaxis.set_visible(False)
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%b %d %Y %H:%M'))
    #ax1.autofmt_xdate()
    #ax1.xticks(rotation=45)
    #ax1.xaxis.set_rotation(45)
    for tick in ax1.get_xticklabels():
        tick.set_rotation(45)
        tick.set_horizontalalignment('right')
        
    ax2.clear()
    ax2.plot(xs, ss)
    ax2.set_xlabel('Time')
    ax2.set_ylabel('Score')
    #plt.pyplot.sca(1)
    #plt.xticks(rotation=45)
    #ax2.xaxis.set_major_formatter(mdates.DateFormatter('%b %d %Y %H:%M:%S'))
    ax2.xaxis.set_major_formatter(mdates.DateFormatter('%b %d %Y %H:%M'))
    #ax2.xticks.set_rotation(45)
    #ax2.autofmt_xdate()
    #plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %d %Y %H:%M:%S'))
    #plt.gcf().autofmt_xdate()
    #plt.xticks(rotation=45)
    for tick in ax2.get_xticklabels():
        tick.set_rotation(45)
        tick.set_horizontalalignment('right')
        
        

    ax3.clear()
    x = np.array(ss)
    x = x.astype(np.float)
    ax3.hist(x, 100, color='g', alpha=0.75)
    ax3.set_ylim(0,100)
    ax3.set_xlim(-1,1)
    ax3.set_xlabel('Score Distribution')
    ax3.set_ylabel('# of Tweets')
    



    
fig.canvas.set_window_title('microsoft')
ani = animation.FuncAnimation(fig, animate, interval=1000)
#plt.show()