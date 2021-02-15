# template for "Stopwatch: The Game"

# define global variables
import simplegui

running = False 
message = "0:00.0"
t = 0
x = 0  #the number of successful stops
y = 0  #the number of total stops

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D

def format(t):
    global message
    
    if t >= 600:
        a = t // 600
        b = t % 600 // 100
        
    else:
        a = 0
        b = t // 100
        
    c = (t - a * 600 - b * 100) // 10
    d = t % 10
    
    return str(a) + ':' + str(b) + str(c)+ '.' + str(d)
        
    
    
# define event handlers for buttons; "Start", "Stop", "Reset"   
    
def stop():
    timer.stop()
    global x
    global y
    global running
    
    if running == True:
        y += 1
        if t % 10 == 0:
            x += 1
            running = False
            
def start():
    timer.start()
    global running
    running = True          
     
            
def reset():
    timer.stop()
    global t
    global message
    global x
    global y
    
    t = 0
    x = 0 #the number of successful stops
    y = 0 #the number of total stops
    message = "0:00.0"
    


# define event handler for timer with 0.1 sec interval
def timer_handler():
    global t
    t += 1
    return t


# define draw handler
def draw(canvas):
    canvas.draw_text(format(t), [70,220], 100, "crimson")
    canvas.draw_text(str(x)+'/'+str(y), [300,40], 38, "turquoise")
    
# create frame
frame = simplegui.create_frame('Stopwatch: The Game', 400, 400)

# register event handlers
timer = simplegui.create_timer(100, timer_handler)
frame.set_draw_handler(draw)
start = frame.add_button('Start', start, 100)
stop = frame.add_button('Stop', stop, 100)
reset = frame.add_button('Reset', reset, 100)

# start frame
frame.start()


# Please remember to review the grading rubric
