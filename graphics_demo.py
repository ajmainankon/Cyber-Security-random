from graphics import *

def main():
    win = GraphWin ("Sample", 500, 500)
    #Everything should be coded here in between
    win.setBackground(color_rgb(255, 255, 255))
    pt = Point(100,200)
    pt2 = Point(200,70)
    

    pt.setFill(color_rgb(0,0,0))
    pt2.setFill(color_rgb(0,0,0))
    # cir = Circle(pt, 50)
    # cir.setFill(color_rgb(100,255,50))
    # # cir.draw(win)

    # line = Line(pt, Point(0, 0))
    # line.setFill(color_rgb(0,0,0))
    # line.draw(win)
    pt.draw(win)
    pt2.draw(win)












    win.getMouse()
    win.close()


main()