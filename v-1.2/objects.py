import random
#wall
class wall:
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
        self.x = -5;

        #set variables for use later
        self.spacing = spacing;

    def create_wall(self, canvas_width, canvas_height, startx):
        #randomize the place of the gap (width is fixed)
        #it has to be in a range of 200 px,
        multiplier = self.canvas_height / 400;
        min_height = int(self.canvas_height / 2 - 100 * multiplier);
        max_height = int(self.canvas_height / 2 + 100 * multiplier);
        self.gapheight = random.randint(min_height, max_height);
        #create upper wall
        self.upper_y = self.canvas_height - self.gapheight;
        self.id_upper = self.canvas.create_rectangle(0, 0, 32, self.upper_y, fill='green');
        self.canvas.move(self.id_upper, startx, 0);
        #Create lower wall;
        self.lower_y = self.gapheight - 88;
        self.id_lower = self.canvas.create_rectangle(0, 0, 32, self.lower_y, fill='green');
        self.canvas.move(self.id_lower, startx, self.canvas_height - self.lower_y);

        #name gap area
        self.gap = [self.upper_y, self.lower_y];

    def draw(self):
        #move to new x
        self.canvas.move(self.id_upper, self.x, 0);
        self.canvas.move(self.id_lower, self.x, 0);

        #check for position, if last pixel is below x = 0, generate new wall and move to back
        self.pos = self.canvas.coords(self.id_upper);
        if self.pos[2] < 0:
            self.create_wall(self.canvas_width, self.canvas_height, self.startx);
            self.canvas.move(self.id_upper, self.spacing * 5 - 32, 0);
            self.canvas.move(self.id_lower, self.spacing * 5 - 32, 0);

    def remove(self):
        self.canvas.delete();
#player
class player:
    def __init__(self, canvas):
        self.canvas = canvas;
        #create the sprite and move to correct place
        self.id_player = canvas.create_rectangle(0, 0, 32, 32, fill='orange');
        self.canvas.move(self.id_player, 100, 100)

        self.y = 0;
        self.x = 0;
        self.canvas_width = self.canvas.winfo_width();
        self.canvas_height = self.canvas.winfo_height();
        #initiate the controls
        self.canvas.bind_all('<space>', self.move);
        self.canvas.bind_all('<Button-1>', self.move);

        #set control variables
        self.recordscore = True;
        self.collide = False;
        self.score = -1.7;

    def draw(self):
            #Very complicated physics engine

        if not self.collide and self.y < 7:
            self.y += abs(self.y) / 10 + .1;
        self.canvas.move(self.id_player, self.x, self.y)
        self.pos = self.canvas.coords(self.id_player);

        #check if player is in the playingfield
        if self.pos[1] < 0 or self.pos[3] > self.canvas_height:
            self.collide = True;
            self.recordscore = False;
            self.y = 0;
        #score
        if self.recordscore:
            self.score += 1 / 60;


    def move(self, info):
        #make sure to disable movement after game end
        if not self.collide:
            self.y = -7;

    def remove(self):
        self.canvas.delete();
