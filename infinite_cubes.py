import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import random

speed = 2


def cube(vertices, cube_color):
    edges = (
        (0, 1),
        (0, 3),
        (0, 4),
        (2, 1),
        (2, 3),
        (2, 7),
        (6, 3),
        (6, 4),
        (6, 7),
        (5, 1),
        (5, 4),
        (5, 7),
    )
    surfaces = (
        (0, 1, 2, 3),
        (3, 2, 7, 6),
        (6, 7, 5, 4),
        (4, 5, 1, 0),
        (1, 5, 7, 2),
        (4, 0, 3, 6),
    )
    glBegin(GL_QUADS)
    for surface in surfaces:
        for vertex in surface:
            glColor3fv(cube_color)
            glVertex3fv(vertices[vertex])
    glEnd()
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()


def set_vertices(max_distance, side):
    s = float(side / 2)
    vertices = (
        (s, -s, -s),
        (s, s, -s),
        (-s, s, -s),
        (-s, -s, -s),
        (s, -s, s),
        (s, s, s),
        (-s, -s, s),
        (-s, s, s),
    )
    x_value_change = random.randrange(-10, 10)
    y_value_change = random.randrange(-10, 10)
    z_value_change = random.randrange(-1 * max_distance, -20)
    new_vertices = []
    for vert in vertices:
        new_vertices.append([vert[0] + x_value_change, vert[1] + y_value_change, vert[2] + z_value_change])
    return new_vertices


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(random.randrange(-5, 5), random.randrange(-5, 5), -40)
    glRotatef(0, 0, 0, 0)
    x_move = 0
    y_move = 0
    max_distance = 100
    cube_list = []
    color_list = []
    for x in range(20):
        cube_list.append(set_vertices(max_distance, random.randrange(1, 5)))
        color_list.append((random.random(), random.random(), random.random()))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_move = 0.3
                if event.key == pygame.K_RIGHT:
                    x_move = -0.3
                if event.key == pygame.K_UP:
                    y_move = -0.3
                if event.key == pygame.K_DOWN:
                    y_move = 0.3
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_move = 0.0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_move = 0.0

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        x = glGetDoublev(GL_MODELVIEW_MATRIX)
        camera_z = x[3][2]
        for each_cube in cube_list:
            i = cube_list.index(each_cube)
            if each_cube[7][2] > camera_z:
                cube_list[i] = (set_vertices(max_distance - int(camera_z), random.randrange(1, 5)))
                color_list[i] = (random.random(), random.random(), random.random())
            cube(cube_list[i], color_list[i])
        glTranslate(x_move, y_move, speed * 0.5)
        pygame.display.flip()
        pygame.time.wait(10)


main()
pygame.quit()
quit()
