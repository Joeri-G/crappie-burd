try:
    from tkinter import *
    import time, objects

    ####FUNCTIONS####

    def collisioncheck(pos, gap, player_pos, canvas_height):
        #check if the wall is near the player, who's position is fixed
        if pos[0] in range(68, 132):
            #if the y of the player is outside of the safe-space (the gap), return True
            if player_pos[1] < pos[3] or player_pos[3] > pos[3] + 88:
                return True;
        #check for out of bounds (touching the edges of the map)
        if player_pos[1] < 0 or player_pos[3] > canvas_height:
            return True;

    def get_nearest_object(walls):
        #empty pos array
        walls_pos = [];
        wall_nearest = [];
        #identifier
        nmr = 0;
        #loop through list
        for x in walls:
            walls_pos.append([x.pos, int(nmr)]);
            nmr += int(1);
        for x in walls_pos:
            if x[0][0] > 64:
                #closest X + identifier
                wall_nearest.append([x[0][0], x[1]]);
        #Get closest wall to player from array
        wall_nearest = min(wall_nearest);
        return wall_nearest;

    def start_game(self):
        global start;
        start = True;

    def restart_game(arg):
        global restart;
        restart = True;

    def quit_game(arg):
        global quit, restart;
        quit = restart = True;


    ###MAIN CODE####
    tk = Tk()
    tk.title("Crappie Burd | Alpha-1.1")
    tk.resizable(0, 0)
    tk.wm_attributes("-topmost", 1)
    #canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0, cursor='dot')
    canvas = Canvas(tk, width=800, height=640, bd=0, highlightthickness=0, cursor='dot')
    canvas.pack()
    tk.update()

    spacing = 260;
    start = False;

    #main start screen in the center of the screen
    start_button = canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2, text="Start", state='hidden', font=("Arial", 44));
    canvas.itemconfig(start_button, state='normal');
    canvas.tag_bind(start_button, "<Button-1>", start_game);
    while not start:
        #update and wait 1 / 60th of a second (1 fps)
        tk.update_idletasks();
        tk.update();
        time.sleep(1 / 60);

    #hide text
    canvas.itemconfig(start_button, state='hidden');

    quit = False;

    while not quit:
        #init player and walls
        player = objects.player(canvas);

        #generate 5 walls
        walls = [];
        for x in range(5):
            walls.append(objects.wall(canvas, x * spacing, spacing));

        while True:
            #set restart to false
            restart = False;
            restart_text = canvas.create_text(80, canvas.winfo_height()-32, text="Restart", state='hidden', font=("Arial", 22));
            quit_text = canvas.create_text(canvas.winfo_width()-80, canvas.winfo_height()-32, text='Quit', state='hidden', font=("Courier", 22));

            game_over_text = canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 3, text='GAME OVER', state='hidden', font=("Courier", 32));

            player.draw();
            #loop through walls
            for x in walls:
                x.draw();

            #get the nearest wall
            nearest = get_nearest_object(walls);
            #check for collisions at nearest wall
            if collisioncheck(walls[nearest[1]].pos, walls[nearest[1]].gap, player.pos, player.canvas_height):
                player.recordscore = False;
                canvas.itemconfig(game_over_text, state='normal');
                break;
            #update and wait 1 / 60th of a second (1 fps)
            tk.update_idletasks();
            tk.update();
            time.sleep(1 / 60);

        #after game text
        score_text = canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 3 * 2, text='You scored %s!' % int(player.score), font=("Courier", 28));

        canvas.tag_bind(restart_text, "<Button-1>", restart_game);
        canvas.itemconfig(restart_text, state='normal');

        canvas.tag_bind(quit_text, "<Button-1>", quit_game);
        canvas.itemconfig(quit_text, state='normal');

        while not restart:
            #keep on generating and updating terrain.
            player.move = False;
            player.draw();
            for x in walls:
                x.x = 0;
            tk.update_idletasks();
            tk.update();
            time.sleep(1 / 60);

        for x in walls:
            canvas.delete(x);
        canvas.delete(player);
        canvas.delete("all")


except Exception as e:
    exit();
