import random
class object:
    def __init__(self, canvas, xoffset, spacing):
        #create the sprite
        self.canvas = canvas;
        self.canvas_width = self.canvas.winfo_width()
        self.canvas_height = self.canvas.winfo_height();

        self.startx = self.canvas_width + xoffset;

        #create wall
        self.create_wall(self.canvas_width, self.canvas_height, self.startx);
        #set speed and start for new blocks
        self.startx = 0;
        self.x = -4;

        self.spacing = spacing;

    def create_wall(self, canvas_width, canvas_height, startx):
        gapheight= random.randint(150, 350)
        #create upper wall
        self.upper_y = self.canvas_height - gapheight;
        self.id_upper = self.canvas.create_rectangle(0, 0, 32, self.upper_y, fill='green');
        self.canvas.move(self.id_upper, startx, 0);
        #Create lower wall;
        self.lower_y = gapheight - 64;
        self.id_lower = self.canvas.create_rectangle(0, 0, 32, self.lower_y, fill='green');
        self.canvas.move(self.id_lower, startx, 400 - self.lower_y);

    def draw(self):
        #move to new x
        self.canvas.move(self.id_upper, self.x, 0);
        self.canvas.move(self.id_lower, self.x, 0);

        #check for position, if last pixel is below 0, generate new wall and move to back
        pos = self.canvas.coords(self.id_upper);
        if pos[2] < 0:
            self.create_wall(self.canvas_width, self.canvas_height, self.startx);
            self.canvas.move(self.id_upper, self.spacing * 5 - 32, 0);
            self.canvas.move(self.id_lower, self.spacing * 5 - 32, 0);
