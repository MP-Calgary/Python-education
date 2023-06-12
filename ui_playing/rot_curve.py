
# importing required modules
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
  
# create a figure, axis and plot element
fig = plt.figure()
ax = plt.axes(xlim=(-25, 25), ylim=(-25, 25))
line, = ax.plot([], [], lw=2)
  
# initialization function
def init():
    # creating an empty plot/frame
    line.set_data([], [])
    return line,
  
# set of points for a star (could be any curve)
p = np.arange(0, 4*np.pi, 0.1)
x = 12*np.cos(p) + 8*np.cos(1.5*p)
y = 12*np.sin(p) - 8*np.sin(1.5*p)
  
# animation function
def animate(i):
    # t is a parameter
    t = 0.1*i
      
    # x, y values to be plotted
    X = x*np.cos(t) - y*np.sin(t)
    Y = y*np.cos(t) + x*np.sin(t)
      
    # set/update the x and y axes data
    line.set_data(X, Y)
      
    # return line object
    return line,
      
# setting a title for the plot
plt.title('A rotating star!')
# hiding the axis details
plt.axis('off')
  
# call the animator    
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=100, interval=100, blit=True)
  
# save the animation as mp4 video file
# Needed to install ffmpeg, by using brew
# anim.save('basic_animation.mp4', writer = 'ffmpeg', fps = 10)
  
# show the plot
plt.show()