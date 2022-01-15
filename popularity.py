# Samuel Waggoner
# Finished 12/19/21
# Description: This program reads from a file (names-data.txt) and queries a first
#   name, and graphs the popularity of that name from 1900 to 2000. The y-axis
#   is the ranking of the name out of the top 1000 names for that year. If the value is 0, then
#   the name was not in the top 1000 names for that year. The y-axis is the year.
#   Once the graph is open, simply click on the graph to close it.
# This program uses graphics.py.

from graphics import *

# functions for creating a graph from the name data

def drawLine(window,window_xmax,window_ymax,buffer,offset,num):
    vertLine = Line(Point(buffer+(offset*num),buffer),Point(buffer+(offset*num),window_ymax-buffer))
    vertLine.setOutline('black')
    vertLine.draw(window)
    return window

def drawText(window,window_xmax, window_ymax, buffer,offset,num):
    yearLabel = Text(Point(buffer+offset*num-(window_ymax//300),window_ymax-buffer+(window_xmax//75)),str(1900+10*num))
    yearLabel.setSize(10)
    yearLabel.draw(window)
    return window


def drawGraph(graphData): # nameData is a list of the line
    window_xmax = int(input("How large would you like your window to be on the x axis? "))
    window_ymax = int(input("How large would you like your window to be on the y axis? "))
    # window_xmax = 800
    # window_ymax = 800
    win = GraphWin('NameGraph', window_xmax, window_ymax) # give title and dimensions

    """
    x -->

    y
    |
    v
    """

    buffer = 30 # buffer of x px on either side of the graph, I recommend 30
    offset = (window_xmax-(2*buffer))//10 # px between vertical lines

    # outline rectangle
    outlineRectangle = Rectangle(Point(buffer,buffer),Point((window_xmax-buffer),(window_ymax-buffer)))
    outlineRectangle.setOutline('black')
    outlineRectangle.setFill('lightgray')
    outlineRectangle.draw(win)

    # vertical lines and x-axis labels
    for i in range(11):
        win = drawLine(win,window_xmax,window_ymax,buffer,offset,i)
        win = drawText(win,window_xmax,window_ymax,buffer,offset,i)

    # graph points
    prevPoint = None
    for i in range(1,12):
        result = drawPoint(win,graphData,buffer,offset,window_ymax,prevPoint,i)
        win = result[0]
        prevPoint = result[1]

    return win

def drawPoint(win,graphData,buffer,offset,window_ymax,prevPoint,i):
    #draw the dot
    point = Point(buffer + (offset*(i-1)) , int(graphData[i])/1000 * window_ymax + buffer)
    circle = Circle(point, 5) # point, radius
    circle.setFill('purple')
    circle.draw(win)

    # write the number above the dot
    textPoint = Point(buffer + (offset*(i-1)) + 15, int(graphData[i])/1000 * window_ymax + buffer - 10)
    yearLabel = Text(textPoint,str(graphData[i]))
    yearLabel.setSize(10)
    yearLabel.draw(win)

    #draw the line if needed
    if prevPoint is None: # first point on the left, no line needed
        resultList = [win,point]
        return resultList
    else: # draw the line from the previous point to new point
        vertLine = Line(prevPoint,point)
        vertLine.setOutline('blue')
        vertLine.draw(win)
        resultList = [win,point]
        return resultList

# Functions for getting name data from the file

def checkName(line,targetName):
    for i in range(len(targetName)):
        if line[i] != targetName[i]:
            return False
    return True

def getNameData(targetName):
    targetName = targetName.lower()
    upper = targetName[0].upper()
    targetName = upper + targetName[1:]
    f = open('names-data.txt','r')
    for line in f:
        if checkName(line,targetName) == True:
            line = line.rstrip()
            line = line.split(" ")
            return line
    print("The name " + targetName + " was not found in list of top 1,000 names. Please enter another name.")
    return "notFound"



def main():
    print("Welcome to the name popularity grapher.\nYou can search for a name in the file and graph the popularity of that name in the period from 1900 to 2000.")
    targetName = input("Enter a name you would like to search: ")
    nameData = getNameData(targetName)
    if nameData != "notFound":
        win = drawGraph(nameData)
        win.getMouse()
        win.close()
main()
