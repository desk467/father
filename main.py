from game import Game

from states.menu import Menu
from states.main_game import MainGame

game = Game(
    resolution=(800, 480),
    title='father',
    states=[
        Menu(),
        MainGame(),
    ]
)

game.run()