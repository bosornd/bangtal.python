from bangtal import *

scene1 = Scene("룸1", "RoomEscape/배경-1.png")

door1 = Object("RoomEscape/문-오른쪽-닫힘.png")
door1.locate(scene1, 800, 270)
door1.show()

key = Object("RoomEscape/열쇠.png")
key.setScale(0.2)
key.locate(scene1, 600, 150)
key.show()

flowerpot = Object("RoomEscape/화분.png")
flowerpot.locate(scene1, 550, 150)
flowerpot.show()

scene2 = Scene("룸2", "RoomEscape/배경-2.png")

door2 = Object("RoomEscape/문-왼쪽-열림.png")
door2.locate(scene2, 320, 270)
door2.show()

door3 = Object("RoomEscape/문-오른쪽-닫힘.png")
door3.locate(scene2, 910, 270)
door3.show()

keypad = Object("RoomEscape/키패드.png")
keypad.locate(scene2, 885, 420)
keypad.show()

switch = Object("RoomEscape/스위치.png")
switch.locate(scene2, 880, 440)
switch.show()

password = Object("RoomEscape/암호.png")
password.locate(scene2, 400, 100)


door1.closed = True
def onMouseAction_door1(x, y, action):
    global door1, key, scene2
    if door1.closed == True:
        if key.inHand():
            door1.setImage("RoomEscape/문-오른쪽-열림.png")
            door1.closed = False
        else:
            showMessage("열쇠가 필요해~~~")
    else:
        scene2.enter()
door1.onMouseAction = onMouseAction_door1

def onMouseAction_key(x, y, action):
    global key
    key.pick()
key.onMouseAction = onMouseAction_key

flowerpot.moved = False
def onMouseAction_flowerpot(x, y, action):
    global flowerpot
    if flowerpot.moved == False:
        if action == MouseAction.DRAG_LEFT:
            flowerpot.locate(scene1, 450, 150)
            flowerpot.moved = True
        elif action == MouseAction.DRAG_RIGHT:
            flowerpot.locate(scene1, 650, 150)
            flowerpot.moved = True
flowerpot.onMouseAction = onMouseAction_flowerpot

def onMouseAction_door2(x, y, action):
    global scene1
    scene1.enter()
door2.onMouseAction = onMouseAction_door2

door3.closed = True
door3.unlocked = False
def onMouseAction_door3(x, y, action):
    global door3
    if door3.unlocked == False:
        showMessage("문이 잠겨있다.")
    elif door3.closed == True:
        door3.setImage("RoomEscape/문-오른쪽-열림.png")
        door3.closed = False
    else:
        endGame()
door3.onMouseAction = onMouseAction_door3

def onKeypad_door3():
    global door3
    showMessage("철커덕")
    door3.unlocked = True
door3.onKeypad = onKeypad_door3

def onMouseAction_keypad(x, y, action):
    showKeypad("BANGTAL", door3)
keypad.onMouseAction = onMouseAction_keypad

switch.lighted = True
def onMouseAction_switch(x, y, action):
    global switch, password, scene2
    switch.lighted = not switch.lighted
    if switch.lighted == True:
        scene2.setLight(1.)
        password.hide()
    else:
        scene2.setLight(.2)
        password.show()
switch.onMouseAction = onMouseAction_switch

startGame(scene1)
