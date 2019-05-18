class object:
    def __init__(self, canvas):
        self.canvas = canvas;
        #create the sprite
        self.canvas = canvas;
        self.id_player = canvas.create_rectangle(0, 0, 32, 32, fill='orange');
        self.canvas.move(self.id_player, 100, 100)
        self.x = 0;
        self.y = 1;
        self.canvas_width = self.canvas.winfo_width()
        self.canvas_height = self.canvas.winfo_height();

        #bind space to jump
        self.canvas.bind_all('<KeyPress-Left>', self.move);

    def draw(self):
        self.canvas.move(self.id_player, 0, self.y)
        pos = self.canvas.coords(self.id_player)

    def move(self):
        pass
