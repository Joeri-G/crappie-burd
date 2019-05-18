import time
from tkinter import *
import random
#importeren etc

#canvas maken
tk = Tk()
tk.title("Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=800, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()


def hitting(co1, co2):
    if co1[2] >= co2[0] and co1[0] <= co2[2]:
        if co1[1] <= co2[3] and co1[3] >= co2[1]:
            return True
        return False

class Bird:
    def __init__(self, canvas, p1, p2, p3, p4, p5):
        self.canvas = canvas
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
        self.p5 = p5
        self.id = canvas.create_oval(10, 10, 25, 25, fill='red')
        self.canvas.move(self.id, 10, 260)
        self.y = 0
        self.p = 150
        self.canvas.bind_all('<space>', self.jumping)
        self.stop = False
    
    def hit(self, pos):
        co1 = pos
        co2 = self.canvas.coords(self.p1.id)
        if hitting(co1, co2):
            return True
        co2 = self.canvas.coords(self.p1.id2)
        if hitting(co1, co2):
            return True
        
        co2 = self.canvas.coords(self.p2.id)
        if hitting(co1, co2):
            return True
        co2 = self.canvas.coords(self.p2.id2)
        if hitting(co1, co2):
            return True
        
        co2 = self.canvas.coords(self.p3.id)
        if hitting(co1, co2):
            return True
        co2 = self.canvas.coords(self.p3.id2)
        if hitting(co1, co2):
            return True
        
        co2 = self.canvas.coords(self.p4.id)
        if hitting(co1, co2):
            return True
        co2 = self.canvas.coords(self.p4.id2)
        if hitting(co1, co2):
            return True
        
        co2 = self.canvas.coords(self.p5.id)
        if hitting(co1, co2):
            return True
        co2 = self.canvas.coords(self.p5.id2)
        if hitting(co1, co2):
            return True
    
    def jumping(self, evt):
        self.y = -5
        pos = self.canvas.coords(self.id)
        self.p = pos[1] - 50
        
    def jump(self):
        self.canvas.move(self.id, 0, self.y)
        pos = self.canvas.coords(self.id)
        #print(pos[1])
        #tk.update()        
        if pos[1] <= self.p:
            self.y = 5
        elif pos[1] >= 381:
            self.stop = True
            print("game over")
        elif pos[1] <= 0:
            self.stop = True
            print("game over")
        
        if self.hit(pos) == True:
            self.stop = True
            print("game over")

class Pipe:
    def __init__(self, canvas):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 15, 300, fill='black')
        self.id2 = canvas.create_rectangle(0, 0, 15, 300, fill='black')
        self.x = 0
        self.y = -175
        self.canvas.move(self.id, self.x, self.y)
        self.canvas.move(self.id2, self.x, self.y)
        self.x = 500
        self.y = 25
        self.canvas.move(self.id, self.x, self.y)
        self.canvas.move(self.id2, self.x, self.y + 400)
        
    
    def moving(self):
        self.x = -5
        self.y = 0
        self.canvas.move(self.id, self.x, self.y)
        self.canvas.move(self.id2, self.x, self.y)

p1 = Pipe(canvas)
p2 = Pipe(canvas)
p3 = Pipe(canvas)
p4 = Pipe(canvas)
p5 = Pipe(canvas)
p_end = Pipe(canvas)
bird = Bird(canvas, p1, p2, p3, p4, p5)

starts = list(range(0, 1400, 200))
random.shuffle(starts)
starts2 = list(range(-125, 125))
random.shuffle(starts2)
canvas.move(p1.id, starts[0], starts2[0])
canvas.move(p1.id2, starts[0], starts2[0])
canvas.move(p2.id, starts[1], starts2[1])
canvas.move(p2.id2, starts[1], starts2[1])
canvas.move(p3.id, starts[2], starts2[2])
canvas.move(p3.id2, starts[2], starts2[2])
canvas.move(p4.id, starts[3], starts2[3])
canvas.move(p4.id2, starts[3], starts2[3])
canvas.move(p5.id, starts[4], starts2[4])
canvas.move(p5.id2, starts[4], starts2[4])

canvas.move(p_end.id, 1600, 200)
canvas.move(p_end.id2, 1600, 500)
canvas.itemconfig(p_end.id, fill='white')
canvas.itemconfig(p_end.id2, fill='white')



while True:
    if bird.stop == False:
        bird.jump()
        p1.moving()
        p2.moving()
        p3.moving() 
        p4.moving()
        p5.moving()
        p_end.moving()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.02)
    
    pipe_pos = canvas.coords(p_end.id)
    #print(pipe_pos[0])
    if pipe_pos[0] < 40:
        bird.stop = True
        print("FINISH")
        break
        