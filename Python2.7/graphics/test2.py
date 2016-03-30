from graphics import *
win = GraphWin("Draw a polygan",300,300)
win.setCoords(0.0,0.0,300.0,300.0)
message = Text(Point(150,20),"Click on five points")
message.draw(win)

p1 = win.getMouse()
p1.draw(win)

p2 = win.getMouse()
p2.draw(win)

p3 = win.getMouse()
p3.draw(win)

p4 = win.getMouse()
p4.draw(win)

p5 = win.getMouse()
p5.draw(win)

polygon = Polygon(p1,p2,p3,p4,p5)
polygon.setFill('black')
polygon.setOutline('yellow')
polygon.draw(win)


message.setText("any to quit")
win.getMouse()
