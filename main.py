import core
from Planete import Planete
from Soleil import Soleil


def setup():
    print("Setup START---------")
    core.fps = 60
    core.WINDOW_SIZE = [500, 500]
    core.memory("TabDePlanete", [])

    core.memory("Soleil", Soleil())

    for i in range(8):
        core.memory("TabDePlanete").append(Planete())



    print("Setup END-----------")


def run():
    core.cleanScreen()
# VUE DE FACE EN 2D
    for i in core.memory("TabDePlanete"):
        i.mouvement(core.memory("Soleil").masse, core.memory("Soleil").position)
    core.memory("Soleil").draw(core.screen)
    for i in core.memory("TabDePlanete"):
        i.draw(core.screen)


core.main(setup, run)
