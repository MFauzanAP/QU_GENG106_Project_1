# phase 2 test

import matplotlib.pyplot as plt

def draw_rectangle(b,h):
    # b = base, h= height
    rectangle=plt.Rectangle((0,0), b, h, fc='red', ec='black')
    # define a recatngle drawn from the origin, red colour with black outline
    plt.gca().add_patch(rectangle)
    # displays the rectangle
    plt.gca().text(0-b*0.25,h,'Rectangular')
    # adds a label with a position
    plt.axis('scaled')
    # meaning the dimensions would not exceed the screen
    plt.axis('off')
    # x or y axis would not be shown
    plt.show()
    # displays the shapes
    input('')

    
def draw_circle(r):
    # only a radius is required to draw a circle
    circle = plt.Circle((0,0), r, fc = 'red', ec='black')
    plt.gca().add_patch(circle)
    plt.gca().text(0-r*1.5,(r*.5),'Circular')
    plt.axis('scaled')
    plt.axis('off')
    plt.show()


def draw_donut(outer_r,inner_r):
    outer_c = plt.Circle((0,0), outer_r, fc = 'red', ec = 'black')
    plt.gca().add_patch(outer_c)
    # the fill colour had to match with the background to appear hollow
    inner_c = plt.Circle((0,0), inner_r, fc = 'white', ec = 'black')
    plt.gca().add_patch(inner_c)
    plt.gca().text(-outer_r*1.6,-inner_r,'Hollow Circular')
    plt.axis('scaled')
    plt.axis('off')
    plt.show()

def draw_t_section(t,h,b,s):
    flange = plt.Rectangle((0,0), b,s ,fc = 'red', ec = 'black')
    plt.gca().add_patch(flange)
    web = plt.Rectangle(((b/2-t/2),-h), t,h, fc = 'red', ec = 'black')
    plt.gca().add_patch(web)
    plt.gca().text(0, 0-h/2,'T-section')
    plt.axis('scaled')
    plt.axis('off')
    plt.show()

def draw_i_section(t,h,b,s):
    flange_u = plt.Rectangle((0,0), b,s,fc = 'red', ec = 'black')
    plt.gca().add_patch(flange_u)
    web = plt.Rectangle(((b/2-t/2),-h), t,h, fc = 'red', ec = 'black')
    plt.gca().add_patch(web)
    flange_b = plt.Rectangle((0,-h-s), b,s,fc = 'red', ec = 'black')
    plt.gca().add_patch(flange_b)
    plt.gca().text(0, 0-h/2,'I-section')
    plt.axis('scaled')
    plt.axis('off')
    plt.show()

    
 	




