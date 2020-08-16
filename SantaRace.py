from bangtal import *

setGameOption(GameOption.INVENTORY_BUTTON, False)
setGameOption(GameOption.MESSAGE_BOX_BUTTON, False)

scene = Scene("산타 레이스", "SantaRace/background.png")

santa = Object("SantaRace/santa.png")
santa.x = 0
santa.y = 500
santa.locate(scene, santa.x, santa.y)
santa.show()

playButton = Object("SantaRace/play.png")
playButton.locate(scene, 610, 30)

startButton = Object("SantaRace/start.png")
startButton.locate(scene, 590, 70)
startButton.show()

endButton = Object("SantaRace/end.png")
endButton.locate(scene, 590, 20)
endButton.show()

timer = Timer(10)
showTimer(timer)

def startButton_onMouseAction(x, y, action):
    global santa, scene, startButton, endButton, playButton
    startButton.hide()
    endButton.hide()
    playButton.show()

    santa.x = 0
    santa.locate(scene, santa.x, santa.y)

    timer.set(10)
    timer.start()
startButton.onMouseAction = startButton_onMouseAction

def endButton_onMouseAction(x, y, action):
    endGame()
endButton.onMouseAction = endButton_onMouseAction

def playButton_onMouseAction(x, y, action):
    global santa, scene
    santa.x = santa.x + 30
    santa.locate(scene, santa.x, santa.y)

    if santa.x > 1280:
        playButton.hide()
        startButton.setImage("SantaRace/restart.png")
        startButton.show()
        endButton.show()

        timer.stop()
        showMessage("선물 배달 성공~~~")
playButton.onMouseAction = playButton_onMouseAction

def timer_onTimeout():
    playButton.hide()
    startButton.setImage("SantaRace/restart.png")
    startButton.show()
    endButton.show()

    showMessage("헉, 선물 배달 실패!!!")
timer.onTimeout = timer_onTimeout

startGame(scene)



