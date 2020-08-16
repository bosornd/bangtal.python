from bangtal import *

setGameOption(GameOption.INVENTORY_BUTTON, False)
setGameOption(GameOption.MESSAGE_BOX_BUTTON, False)

scene = Scene("틀린그림찾기", "SpotDifference/problem.png")

problem = Object("SpotDifference/problem.png")
problem.locate(scene, 0, 0)
problem.show()

class Rect:
    def __init__(self, cx, cy, r):
        self.centerX = cx
        self.centerY = cy
        self.radius = r

    def checkIn(self, x, y):
        return self.centerX - self.radius < x < self.centerX + self.radius and self.centerY - self.radius < y < self.centerY + self.radius

class DifferencePoint:
    def __init__(self, left_cx, right_cx, cy, r):
        self.left = Rect(left_cx, cy, r)
        self.right = Rect(right_cx, cy, r)

        self.left_check = Object("SpotDifference/check.png")
        self.left_check.locate(scene, left_cx - 25, cy - 25);

        self.right_check = Object("SpotDifference/check.png")
        self.right_check.locate(scene, right_cx - 25, cy - 25);

        self.found = False

    def checkIn(self, x, y):
        return self.left.checkIn(x, y) or self.right.checkIn(x, y)

    def show(self):
        self.left_check.show()
        self.right_check.show()
        self.found = True

points = [
    DifferencePoint(568, 1186, 594, 54),
    DifferencePoint(99, 717, 551, 17),
    DifferencePoint(383, 1001, 482, 16),
    DifferencePoint(401, 1019, 158, 27),
    DifferencePoint(61, 679, 255, 36),
    DifferencePoint(592, 1210, 421, 35),
    DifferencePoint(320, 938, 117, 13),
]

count = 0
def problem_onMouseAction(x, y, action):
    wrong = True
    for p in points:
        if p.checkIn(x, y):
            wrong = False
            if p.found == False:
                global count
                count = count + 1
                p.show()

    if wrong:
        endGame()

    if count == 7:
        showMessage("성공, 다 찾았다!!!")

problem.onMouseAction = problem_onMouseAction

showMessage("좌우에 틀린 곳을 찾아보세요.")
startGame(scene)


