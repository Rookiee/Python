from graphics import *
def main():
	win = GraphWin("Click Mouse")
	for i in range(10):
		p = win.getMouse()
		print p.getX(), p.getY()

main()
