class scoreboard:
    def __init__(self, canvas):
        self.canvas = canvas;
        self.width = canvas.winfo_width();
        self.height = canvas.winfo_height();
        self.multiplier = self.height / 400;

        #divide screen in 15 lines
        self.line = self.width / 15;
        self.scoreboard_title = self.canvas.create_text(self.width / 2, self.line * 3, text="Scoreboard", state='normal', font=("Arial", int(44 * self.multiplier)));

        self.load();

    def load(self, arg):
        pass
    def draw(self):
        pass
