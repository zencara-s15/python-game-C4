import tkinter as tk
from tkinter import *
import winsound



# ---------------------------------------------------------------------------
# #=> CONSTANT
# ---------------------------------------------------------------------------
SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 700
window = tk.Tk()
window.geometry(str(SCREEN_WIDTH)+"x"+str(SCREEN_HEIGHT))
window.title('Group C5 - Juggle Game')
canvas = tk.Canvas(window)

# Varaible

game_start = tk.PhotoImage(file="img/bg_game.png")
game_help = tk.PhotoImage(file="img/Group 5.png")
game_level = tk.PhotoImage(file="img/back_level.png")

btn_start_game = tk.PhotoImage(file="img/start.png")
btn_exit_game = tk.PhotoImage(file="img/exit.png")
btn_help_game = tk.PhotoImage(file="img/help.png")
btn_back_game = tk.PhotoImage(file="img/back.png")

level1 = tk.PhotoImage(file="img/level1.png")
level2 = tk.PhotoImage(file="img/level2.png")
level3 = tk.PhotoImage(file="img/level3.png")

# Show start game
def gameShow(event):
    canvas.delete("all")
    canvas.create_image(680, 372, image=game_start)
    canvas.create_image(680,280, image=btn_start_game, tags="startgame")
    canvas.create_image(680,540,image=btn_help_game, tags="help")
    canvas.create_image(680,410,image=btn_exit_game, tags="exit")

# show level game

def levelGame(event):
    canvas.delete(all)
    canvas.create_image(680,372, image=game_level)
    canvas.create_image(330,372, image=level1)
    canvas.create_image(630,372, image=level2)
    canvas.create_image(930,372, image=level3)
    canvas.create_image(140, 100, image=btn_back_game, tags="back")

# show for how to play

def gameHelp(event):
    canvas.delete("all")
    canvas.create_image(680, 372, image=game_help)
    canvas.create_image(140, 200, image=btn_back_game, tags="back")

# close game
def gameExit(event):
    window.destroy()


canvas.create_image(680, 372, image=game_start)
canvas.create_image(630,280, image=btn_start_game, tags="startgame")
canvas.create_image(630,540,image=btn_help_game, tags="help")
canvas.create_image(630,410,image=btn_exit_game, tags="exit")
winsound.PlaySound("sounds/open.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)


# Bind the button clicks to the corresponding functions

canvas.tag_bind("startgame", "<Button-1>",levelGame )
canvas.tag_bind("help", "<Button-1>", gameHelp)
canvas.tag_bind("exit", "<Button-1>", gameExit)
canvas.tag_bind("back", "<Button-1>", gameShow)


canvas.pack(expand=True, fill='both')
window.mainloop()