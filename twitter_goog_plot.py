import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
#import time

style.use("ggplot")

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    graph_data = open('twitter_goog_score.txt','r').read()
    lines = graph_data.split('\n')
    xs = []
    ys = []
    for line in lines[-5000:]:
        if len(line) > 1:
            x, y = line.split(',')
            xs.append(x)
            ys.append(y)
    ax1.clear()
    ax1.plot(xs, ys)
    ax1.set_xlabel('Tweet #')
    ax1.set_ylabel('Total Score')
    ax1.set_title('"googl", "google", "goog"')
    
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()