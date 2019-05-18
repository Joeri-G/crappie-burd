try:
    from tkinter import *
    import time, objects
    tk = Tk()
    tk.title("Flappie Burd")
    tk.resizable(0, 0)
    tk.wm_attributes("-topmost", 1)
    canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
    canvas.pack()
    tk.update()

    spacing = 240;
    start = False;

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

    def start_game(arg):
        global start;
        start = True;

    #main start screen
    start_button = canvas.create_text(250, 200, text="Start", state='hidden', font=("Courier", 44));
    canvas.itemconfig(start_button, state='normal');
    while not start:

        canvas.tag_bind(start_button, "<Button-1>", start_game)

        #update and wait 1 / 60th of a second (1 fps)
        tk.update_idletasks();
        tk.update();
        time.sleep(1 / 60);

    #hide text
    canvas.itemconfig(start_button, state='hidden');

    #init player and walls
    player = objects.player(canvas);

    #generate 5 walls
    walls = [];
    for x in range(5):
        walls.append(objects.wall(canvas, x * spacing, spacing));

    game_over_text = canvas.create_text(250, 150, text='GAME OVER', state='hidden', font=("Courier", 32));


    while True:
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
    score_text = canvas.create_text(250, 250, text='Your score is %s' % int(player.score), font=("Courier", 24));


    while True:
        #keep on generating and updating terrain.
        player.move = False;
        player.draw();
        for x in walls:
            x.x = 0;
        tk.update_idletasks();
        tk.update();
        time.sleep(1 / 60);


except Exception as e:
    try:
        print("Your score is %s" % int(player.score));
    except Exception as e:
        print('No score available');
    print("Exiting porgram...");
    exit();
