import pygame, sys

from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import gluPerspective
from android import Android

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from PIL import Image  # Asegúrate de tener la biblioteca Pillow instalada
import tkinter as tk
import math
from math import cos, sin, radians, pi 


def draw_rectangular_prism(width, height, depth):
    half_width = width / 2
    half_height = height / 2
    half_depth = depth / 2
    
    glBegin(GL_QUADS)
    # Cara frontal
    glVertex3f(-half_width, -half_height, half_depth)
    glVertex3f(half_width, -half_height, half_depth)
    glVertex3f(half_width, half_height, half_depth)
    glVertex3f(-half_width, half_height, half_depth)
    
    # Cara trasera
    glVertex3f(-half_width, -half_height, -half_depth)
    glVertex3f(half_width, -half_height, -half_depth)
    glVertex3f(half_width, half_height, -half_depth)
    glVertex3f(-half_width, half_height, -half_depth)
    
    # Cara lateral izquierda
    glVertex3f(-half_width, -half_height, half_depth)
    glVertex3f(-half_width, -half_height, -half_depth)
    glVertex3f(-half_width, half_height, -half_depth)
    glVertex3f(-half_width, half_height, half_depth)
    
    # Cara lateral derecha
    glVertex3f(half_width, -half_height, half_depth)
    glVertex3f(half_width, -half_height, -half_depth)
    glVertex3f(half_width, half_height, -half_depth)
    glVertex3f(half_width, half_height, half_depth)
    glEnd()

#creeper3000
def draw_cube(position, scale):

    
    
    glPushMatrix()
    # Dibuja un cubo con iluminación interpolada
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_NORMALIZE)
    glTranslatef(position[0], position[1], position[2])
    glScalef(scale[0], scale[1], scale[2])  # Escala el rectángulo para hacerlo más pequeño
    glBegin(GL_QUADS)
    glColor4f(0.0, 1.0, 0.0, 1.0)  # Color verde para el cubo
    glNormal3f(0, 0, -1)
    glVertex3f(-1, -1, -1)
    glVertex3f(1, -1, -1)
    glVertex3f(1, 1, -1)
    glVertex3f(-1, 1, -1)

    glNormal3f(0, 0, 1)
    glVertex3f(-1, -1, 1)
    glVertex3f(1, -1, 1)
    glVertex3f(1, 1, 1)
    glVertex3f(-1, 1, 1)

    glNormal3f(0, -1, 0)
    glVertex3f(-1, -1, -1)
    glVertex3f(1, -1, -1)
    glVertex3f(1, -1, 1)
    glVertex3f(-1, -1, 1)

    glNormal3f(0, 1, 0)
    glVertex3f(-1, 1, -1)
    glVertex3f(1, 1, -1)
    glVertex3f(1, 1, 1)
    glVertex3f(-1, 1, 1)

    glNormal3f(-1, 0, 0)
    glVertex3f(-1, -1, -1)
    glVertex3f(-1, 1, -1)
    glVertex3f(-1, 1, 1)
    glVertex3f(-1, -1, 1)

    glNormal3f(0, 1, 1)
    glVertex3f(1, -1, -1)
    glVertex3f(1, 1, -1)
    glVertex3f(1, 1, 1)
    glVertex3f(1, -1, 1)
    glEnd()
        
    glDisable(GL_LIGHTING)
    glDisable(GL_LIGHT0)
    glDisable(GL_NORMALIZE)
    glPopMatrix()

def draw_arm(position, scale, rota):
     # Dibuja brazo izquierdo 
        position_variable = position
        scale_variable = scale
        drota=rota
        glColor4f(0.0, 0.0, 1.0, 1.0)  # Cambia el color a azul para el nuevo cubo
        glPushMatrix()
        #glTranslatef(-0.7, 0, -2.6)  # Mueve el cubo hacia la izquierda y hacia abajo
        glTranslatef(position[0], position[1], position[2])
        glScalef(scale[0], scale[1], scale[2])  # Escala el cubo para hacerlo más largo en el eje z
        glRotatef(rota[0], rota[1], rota[2], rota[3])

        glBegin(GL_QUADS)
        glVertex3f(-1, -1, -1)
        glVertex3f(1, -1, -1)
        glVertex3f(1, 1, -1)
        glVertex3f(-1, 1, -1)

        glVertex3f(-1, -1, 1)
        glVertex3f(1, -1, 1)
        glVertex3f(1, 1, 1)
        glVertex3f(-1, 1, 1)

        glVertex3f(-1, -1, -1)
        glVertex3f(1, -1, -1)
        glVertex3f(1, -1, 1)
        glVertex3f(-1, -1, 1)

        glVertex3f(-1, 1, -1)
        glVertex3f(1, 1, -1)
        glVertex3f(1, 1, 1)
        glVertex3f(-1, 1, 1)

        glVertex3f(-1, -1, -1)
        glVertex3f(-1, 1, -1)
        glVertex3f(-1, 1, 1)
        glVertex3f(-1, -1, 1)

        glVertex3f(1, -1, -1)
        glVertex3f(1, 1, -1)
        glVertex3f(1, 1, 1)
        glVertex3f(1, -1, 1)
        glEnd()

        glPopMatrix()
def draw_body(position, scale, color):
            # Dibuja un cubo verde debajo del cubo azul

        
        
        
        
                        # Dibuja un cubo con iluminación interpolada
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glEnable(GL_NORMALIZE)
        
        glPushMatrix()

        # Dibuja un cubo verde debajo del cubo azul
        glColor4f(0.0, 1.0, 0.0, 1.0)  # Color verde para el nuevo cubo
        
        glTranslatef(position[0], position[1], position[2])
        glScalef(0.5, 0.5, 2.0)  # Escala el cubo para hacerlo más largo en el eje z
        glBegin(GL_QUADS)
        
        glNormal3f(0, 0, -1)
        glVertex3f(-1, -1, -1)
        glVertex3f(1, -1, -1)
        glVertex3f(1, 1, -1)
        glVertex3f(-1, 1, -1)

        glNormal3f(0, 0, 1)
        glVertex3f(-1, -1, 1)
        glVertex3f(1, -1, 1)
        glVertex3f(1, 1, 1)
        glVertex3f(-1, 1, 1)
        
        glNormal3f(0, -1, 0)
        glVertex3f(-1, -1, -1)
        glVertex3f(1, -1, -1)
        glVertex3f(1, -1, 1)
        glVertex3f(-1, -1, 1)
        
        
        glNormal3f(0, 1, 0)
        glVertex3f(-1, 1, -1)
        glVertex3f(1, 1, -1)
        glVertex3f(1, 1, 1)
        glVertex3f(-1, 1, 1)

        glVertex3f(-1, -1, -1)
        glVertex3f(-1, 1, -1)
        glVertex3f(-1, 1, 1)
        glVertex3f(-1, -1, 1)

        glVertex3f(1, -1, -1)
        glVertex3f(1, 1, -1)
        glVertex3f(1, 1, 1)
        glVertex3f(1, -1, 1)
        glEnd()

        
        
        glDisable(GL_LIGHTING)
        glDisable(GL_LIGHT0)
        glDisable(GL_NORMALIZE)
        glPopMatrix()
        
        
def draw_arm2(position, scale, rota):
      # Dibuja brazo derecho
        drota=rota
        position_variable = position
        scale_variable = scale
        glColor4f(0.0, 0.0, 1.0, 1.0)  # Cambia el color a azul para el nuevo cubo

        glPushMatrix()
        glTranslatef(position[0], position[1], position[2])
        glScalef(0.2, 0.2, 1.0)  # Escala el cubo para hacerlo más largo en el eje z
        glRotatef(rota[0], rota[1], rota[2], rota[3])

        glBegin(GL_QUADS)
        glVertex3f(-1, -1, -1)
        glVertex3f(1, -1, -1)
        glVertex3f(1, 1, -1)
        glVertex3f(-1, 1, -1)

        glVertex3f(-1, -1, 1)
        glVertex3f(1, -1, 1)
        glVertex3f(1, 1, 1)
        glVertex3f(-1, 1, 1)

        glVertex3f(-1, -1, -1)
        glVertex3f(1, -1, -1)
        glVertex3f(1, -1, 1)
        glVertex3f(-1, -1, 1)

        glVertex3f(-1, 1, -1)
        glVertex3f(1, 1, -1)
        glVertex3f(1, 1, 1)
        glVertex3f(-1, 1, 1)

        glVertex3f(-1, -1, -1)
        glVertex3f(-1, 1, -1)
        glVertex3f(-1, 1, 1)
        glVertex3f(-1, -1, 1)

        glVertex3f(1, -1, -1)
        glVertex3f(1, 1, -1)
        glVertex3f(1, 1, 1)
        glVertex3f(1, -1, 1)
        glEnd()

        glPopMatrix()
def draw_pie(position, scale,rota):
        position_variable = position
        scale_variable = scale
        rotad=rota
        
                              # Dibuja brazo derecho
        glColor4f(0.0, 0.0, 1.0, 1.0)  # Cambia el color a azul para el nuevo cubo
        glPushMatrix()
        glTranslatef(position[0], position[1], position[2])
        glScalef(0.2, 0.2, 0.5)  # Escala el cubo para hacerlo más largo en el eje z
        glRotatef(rota[0], rota[1], rota[2], rota[3])


        glBegin(GL_QUADS)
        glVertex3f(-1, -1, -1)
        glVertex3f(1, -1, -1)
        glVertex3f(1, 1, -1)
        glVertex3f(-1, 1, -1)

        glVertex3f(-1, -1, 1)
        glVertex3f(1, -1, 1)
        glVertex3f(1, 1, 1)
        glVertex3f(-1, 1, 1)

        glVertex3f(-1, -1, -1)
        glVertex3f(1, -1, -1)
        glVertex3f(1, -1, 1)
        glVertex3f(-1, -1, 1)

        glVertex3f(-1, 1, -1)
        glVertex3f(1, 1, -1)
        glVertex3f(1, 1, 1)
        glVertex3f(-1, 1, 1)

        glVertex3f(-1, -1, -1)
        glVertex3f(-1, 1, -1)
        glVertex3f(-1, 1, 1)
        glVertex3f(-1, -1, 1)

        glVertex3f(1, -1, -1)
        glVertex3f(1, 1, -1)
        glVertex3f(1, 1, 1)
        glVertex3f(1, -1, 1)
        glEnd()

        glPopMatrix()
def draw_pe2(position, scale,rota):  
                      # Dibuja pie izquierdo 
        position_variable = position
        scale_variable = scale
        rotad=rota
        glColor4f(0.0, 0.0, 1.0, 1.0)  # Cambia el color a azul para el nuevo cubo
        glPushMatrix()
        glTranslatef(position[0], position[1], position[2])
        glScalef(0.2, 0.2, 0.5)  # Escala el cubo para hacerlo más largo en el eje z
        glRotatef(rota[0], rota[1], rota[2], rota[3])
        
        glBegin(GL_QUADS)
        glVertex3f(-1, -1, -1)
        glVertex3f(1, -1, -1)
        glVertex3f(1, 1, -1)
        glVertex3f(-1, 1, -1)

        glVertex3f(-1, -1, 1)
        glVertex3f(1, -1, 1)
        glVertex3f(1, 1, 1)
        glVertex3f(-1, 1, 1)

        glVertex3f(-1, -1, -1)
        glVertex3f(1, -1, -1)
        glVertex3f(1, -1, 1)
        glVertex3f(-1, -1, 1)

        glVertex3f(-1, 1, -1)
        glVertex3f(1, 1, -1)
        glVertex3f(1, 1, 1)
        glVertex3f(-1, 1, 1)

        glVertex3f(-1, -1, -1)
        glVertex3f(-1, 1, -1)
        glVertex3f(-1, 1, 1)
        glVertex3f(-1, -1, 1)

        glVertex3f(1, -1, -1)
        glVertex3f(1, 1, -1)
        glVertex3f(1, 1, 1)
        glVertex3f(1, -1, 1)
        glEnd()

        glPopMatrix()  
  
def draw_eyes1(position, scale, color):
        position_variable = position
        scale_variable = scale
    
        glColor4f(1.0, 0.0, 0.0, 1.0)  # Color rojo para el rectángulo
        glPushMatrix()
        glScalef(0.5, 0.5, 0.5)  # Escala el rectángulo para hacerlo más pequeño
        glTranslatef(position[0], position[1], position[2])
        glScalef(scale[0], scale[1], scale[2])  # Escala el cubo para hacerlo más largo en el eje z
        glBegin(GL_QUADS)
        glVertex3f(-0.75, -0.75, -1)  # Esquina inferior izquierda
        glVertex3f(0.75, -0.75, -1)   # Esquina inferior derecha
        glVertex3f(0.75, -0.75, -2)   # Esquina superior derecha
        glVertex3f(-0.75, -0.75, -2)  # Esquina superior izquierda
        glEnd()
        glPopMatrix()
       
def draw_eyes2(position, scale, color):
    
        position_variable = position
        scale_variable = scale
    
        glColor4f(1.0, 0.0, 0.0, 1.0)  # Color rojo para el rectángulo
        glPushMatrix()
        glScalef(0.5, 0.5, 0.5)  # Escala el rectángulo para hacerlo más pequeño
        glTranslatef(position[0], position[1], position[2])
        glBegin(GL_QUADS)
        glVertex3f(-0.75, -0.75, -1)  # Esquina inferior izquierda
        glVertex3f(0.75, -0.75, -1)   # Esquina inferior derecha
        glVertex3f(0.75, -0.75, -2)   # Esquina superior derecha
        glVertex3f(-0.75, -0.75, -2)  # Esquina superior izquierda
        glEnd()
        glPopMatrix()  
def draw_mouth(position, scale, rota):
        position_variable = position
        scale_variable = scale
        rotad=rota
        glColor4f(0.0, 0.0, 0.0, 1.0)  # Color rojo para el rectángulo
        glPushMatrix()
        glScalef(0.7, 0.7, 0.3)  # Escala el rectángulo para hacerlo más pequeño
        glTranslatef(position[0], position[1], position[2])
        glRotatef(rota[0], rota[1], rota[2], rota[3])
        glBegin(GL_QUADS)
        glVertex3f(-0.75, -0.75, -1)  # Esquina inferior izquierda
        glVertex3f(0.75, -0.75, -1)   # Esquina inferior derecha
        glVertex3f(0.75, -0.75, -2)   # Esquina superior derecha
        glVertex3f(-0.75, -0.75, -2)  # Esquina superior izquierda
        glEnd()
        glPopMatrix()        

#Richi figura
def ojo1(position, scale):
    position_variable = position
    scale_variable = scale

    glPushMatrix()
    glTranslatef(position[0], position[1], position[2])
    glScalef(scale[0], scale[1], scale[2])  # Escala el rectángulo para hacerlo más pequeño
    glBegin(GL_QUADS)
    glVertex3f(-1, -1, -1)
    glVertex3f(1, -1, -1)
    glVertex3f(1, 1, -1)
    glVertex3f(-1, 1, -1)

    glVertex3f(-1, -1, 1)
    glVertex3f(1, -1, 1)
    glVertex3f(1, 1, 1)
    glVertex3f(-1, 1, 1)

    glVertex3f(-1, -1, -1)
    glVertex3f(1, -1, -1)
    glVertex3f(1, -1, 1)
    glVertex3f(-1, -1, 1)

    glVertex3f(-1, 1, -1)
    glVertex3f(1, 1, -1)
    glVertex3f(1, 1, 1)
    glVertex3f(-1, 1, 1)

    glVertex3f(-1, -1, -1)
    glVertex3f(-1, 1, -1)
    glVertex3f(-1, 1, 1)
    glVertex3f(-1, -1, 1)

    glVertex3f(1, -1, -1)
    glVertex3f(1, 1, -1)
    glVertex3f(1, 1, 1)
    glVertex3f(1, -1, 1)
    glEnd()
    glPopMatrix()

def ojo2(position, scale):
    position_variable = position
    scale_variable = scale

    glPushMatrix()
    glTranslatef(position[0], position[1], position[2])
    glScalef(scale[0], scale[1], scale[2])  # Escala el rectángulo para hacerlo más pequeño
    glBegin(GL_QUADS)
    glVertex3f(-1, -1, -1)
    glVertex3f(1, -1, -1)
    glVertex3f(1, 1, -1)
    glVertex3f(-1, 1, -1)

    glVertex3f(-1, -1, 1)
    glVertex3f(1, -1, 1)
    glVertex3f(1, 1, 1)
    glVertex3f(-1, 1, 1)

    glVertex3f(-1, -1, -1)
    glVertex3f(1, -1, -1)
    glVertex3f(1, -1, 1)
    glVertex3f(-1, -1, 1)

    glVertex3f(-1, 1, -1)
    glVertex3f(1, 1, -1)
    glVertex3f(1, 1, 1)
    glVertex3f(-1, 1, 1)

    glVertex3f(-1, -1, -1)
    glVertex3f(-1, 1, -1)
    glVertex3f(-1, 1, 1)
    glVertex3f(-1, -1, 1)

    glVertex3f(1, -1, -1)
    glVertex3f(1, 1, -1)
    glVertex3f(1, 1, 1)
    glVertex3f(1, -1, 1)
    glEnd()
    glPopMatrix()

def mano(position, scale):
    position_variable = position
    scale_variable = scale

    glPushMatrix()
    glTranslatef(position[0], position[1], position[2])
    glScalef(scale[0], scale[1], scale[2])  # Escala el rectángulo para hacerlo más pequeño
    glBegin(GL_QUADS)
    glVertex3f(-1, -1, -1)
    glVertex3f(1, -1, -1)
    glVertex3f(1, 1, -1)
    glVertex3f(-1, 1, -1)

    glVertex3f(-1, -1, 1)
    glVertex3f(1, -1, 1)
    glVertex3f(1, 1, 1)
    glVertex3f(-1, 1, 1)

    glVertex3f(-1, -1, -1)
    glVertex3f(1, -1, -1)
    glVertex3f(1, -1, 1)
    glVertex3f(-1, -1, 1)

    glVertex3f(-1, 1, -1)
    glVertex3f(1, 1, -1)
    glVertex3f(1, 1, 1)
    glVertex3f(-1, 1, 1)

    glVertex3f(-1, -1, -1)
    glVertex3f(-1, 1, -1)
    glVertex3f(-1, 1, 1)
    glVertex3f(-1, -1, 1)

    glVertex3f(1, -1, -1)
    glVertex3f(1, 1, -1)
    glVertex3f(1, 1, 1)
    glVertex3f(1, -1, 1)
    glEnd()
    glPopMatrix()

def draw_smile_mouth(radius, center, start_angle, end_angle, num_segments):
    glPushMatrix()
    glTranslatef(center[0], center[1], center[2])
    glRotatef(90, 1, 0, 0)  # Rota 90 grados alrededor del eje X
    glColor3f(0.0, 0.0, 0.0)  # Color blanco para la boca
    glBegin(GL_TRIANGLE_FAN)
    
    for i in range(num_segments + 1):
        angle = start_angle + (i / num_segments) * (end_angle - start_angle)
        x = radius * cos(angle)
        y = -radius * sin(angle)
        glVertex2f(x, y)
    
    glEnd()
    glPopMatrix()

def draw_smile_mouth1(radius, center, start_angle, end_angle, num_segments):
    glPushMatrix()
    glTranslatef(center[0], center[1], center[2])
    glRotatef(90, 1, 0, 0)  # Rota 90 grados alrededor del eje X
    glColor3f(1.0, 0.5, 0.7)  # Color blanco para la boca
    glBegin(GL_TRIANGLE_FAN)
    
    for i in range(num_segments + 1):
        angle = start_angle + (i / num_segments) * (end_angle - start_angle)
        x = radius * cos(angle)
        y = -radius * sin(angle)
        glVertex2f(x, y)
    
    glEnd()
    glPopMatrix()

def draw_pickaxe_tip(radius, height, segments=16):
    glBegin(GL_TRIANGLE_FAN)
    glVertex(0, 0, height)  # Vértice superior del cono
    for i in range(segments + 1):
        angle = 2 * math.pi * i / segments
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        glVertex(x, y, 0)
    glEnd()

def draw_arr(length, width, depth):
    # Dibuja un prisma rectangular para el brazo
    glBegin(GL_QUADS)

    # Cara frontal
    glVertex3f(-width / 2, -width / 2, 0)
    glVertex3f(width / 2, -width / 2, 0)
    glVertex3f(width / 2, width / 2, 0)
    glVertex3f(-width / 2, width / 2, 0)

    # Cara trasera
    glVertex3f(-width / 2, -width / 2, -length)
    glVertex3f(width / 2, -width / 2, -length)
    glVertex3f(width / 2, width / 2, -length)
    glVertex3f(-width / 2, width / 2, -length)

    # Lados
    glVertex3f(-width / 2, -width / 2, 0)
    glVertex3f(-width / 2, -width / 2, -length)
    glVertex3f(width / 2, -width / 2, -length)
    glVertex3f(width / 2, -width / 2, 0)

    glVertex3f(-width / 2, width / 2, 0)
    glVertex3f(-width / 2, width / 2, -length)
    glVertex3f(width / 2, width / 2, -length)
    glVertex3f(width / 2, width / 2, 0)

    # Extremos
    glVertex3f(-width / 2, -width / 2, 0)
    glVertex3f(-width / 2, -width / 2, -length)
    glVertex3f(-width / 2, width / 2, -length)
    glVertex3f(-width / 2, width / 2, 0)

    glVertex3f(width / 2, -width / 2, 0)
    glVertex3f(width / 2, -width / 2, -length)
    glVertex3f(width / 2, width / 2, -length)
    glVertex3f(width / 2, width / 2, 0)

    glEnd()


def draw_half_spheres(radius, num_segments, num_rings):
    for i in range(num_segments):
        theta1 = i * (180 / num_segments)
        theta2 = (i + 1) * (180 / num_segments)
        for j in range(num_rings // 2):
            phi1 = j * (360 / num_rings)
            phi2 = (j + 1) * (360 / num_rings)

            x1 = radius * math.sin(math.radians(theta1)) * math.cos(math.radians(phi1))
            y1 = radius * math.cos(math.radians(theta1))
            z1 = radius * math.sin(math.radians(theta1)) * math.sin(math.radians(phi1))

            x2 = radius * math.sin(math.radians(theta1)) * math.cos(math.radians(phi2))
            y2 = radius * math.cos(math.radians(theta1))
            z2 = radius * math.sin(math.radians(theta1)) * math.sin(math.radians(phi2))

            x3 = radius * math.sin(math.radians(theta2)) * math.cos(math.radians(phi1))
            y3 = radius * math.cos(math.radians(theta2))
            z3 = radius * math.sin(math.radians(theta2)) * math.sin(math.radians(phi1))

            x4 = radius * math.sin(math.radians(theta2)) * math.cos(math.radians(phi2))
            y4 = radius * math.cos(math.radians(theta2))
            z4 = radius * math.sin(math.radians(theta2)) * math.sin(math.radians(phi2))

            glBegin(GL_TRIANGLES)
            glVertex(x1, y1, z1)
            glVertex(x2, y2, z2)
            glVertex(x3, y3, z3)
            glEnd()

            glBegin(GL_TRIANGLES)
            glVertex(x4, y4, z4)
            glVertex(x3, y3, z3)
            glVertex(x2, y2, z2)
            glColor4f(1.0, 1.0, 1.0, 1.0)
            glEnd()





def draw_half_sphere_lower(radius, num_segments, num_rings):
    for i in range(num_segments):
        theta1 = i * (180 / num_segments)
        theta2 = (i + 1) * (180 / num_segments)
        for j in range(num_rings // 2, num_rings):
            phi1 = j * (360 / num_rings)
            phi2 = (j + 1) * (360 / num_rings)

            x1 = radius * math.sin(math.radians(theta1)) * math.cos(math.radians(phi1))
            y1 = radius * math.cos(math.radians(theta1))
            z1 = radius * math.sin(math.radians(theta1)) * math.sin(math.radians(phi1))

            x2 = radius * math.sin(math.radians(theta1)) * math.cos(math.radians(phi2))
            y2 = radius * math.cos(math.radians(theta1))
            z2 = radius * math.sin(math.radians(theta1)) * math.sin(math.radians(phi2))

            x3 = radius * math.sin(math.radians(theta2)) * math.cos(math.radians(phi1))
            y3 = radius * math.cos(math.radians(theta2))
            z3 = radius * math.sin(math.radians(theta2)) * math.sin(math.radians(phi1))

            x4 = radius * math.sin(math.radians(theta2)) * math.cos(math.radians(phi2))
            y4 = radius * math.cos(math.radians(theta2))
            z4 = radius * math.sin(math.radians(theta2)) * math.sin(math.radians(phi2))

            glBegin(GL_TRIANGLES)
            glColor4f(1.0, 0.0, 0.0, 0.0)  
            glVertex(x1, y1, z1)
            glVertex(x2, y2, z2)
            glVertex(x3, y3, z3)
            glEnd()

            glBegin(GL_TRIANGLES)
            glVertex(x4, y4, z4)
            glVertex(x3, y3, z3)
            glVertex(x2, y2, z2)
            glEnd()

def draw_pickaxe_handle(length, width, depth):
    # Dibuja un prisma rectangular para el palo del pico
    glBegin(GL_QUADS)

    # Cara frontal
    glVertex3f(-width / 2, -width / 2, 0)
    glVertex3f(width / 2, -width / 2, 0)
    glVertex3f(width / 2, width / 2, 0)
    glVertex3f(-width / 2, width / 2, 0)

    # Cara trasera
    glVertex3f(-width / 2, -width / 2, -length)
    glVertex3f(width / 2, -width / 2, -length)
    glVertex3f(width / 2, width / 2, -length)
    glVertex3f(-width / 2, width / 2, -length)

    # Lados
    glVertex3f(-width / 2, -width / 2, 0)
    glVertex3f(-width / 2, -width / 2, -length)
    glVertex3f(width / 2, -width / 2, -length)
    glVertex3f(width / 2, -width / 2, 0)

    glVertex3f(-width / 2, width / 2, 0)
    glVertex3f(-width / 2, width / 2, -length)
    glVertex3f(width / 2, width / 2, -length)
    glVertex3f(width / 2, width / 2, 0)

    # Extremos
    glVertex3f(-width / 2, -width / 2, 0)
    glVertex3f(-width / 2, -width / 2, -length)
    glVertex3f(-width / 2, width / 2, -length)
    glVertex3f(-width / 2, width / 2, 0)

    glVertex3f(width / 2, -width / 2, 0)
    glVertex3f(width / 2, -width / 2, -length)
    glVertex3f(width / 2, width / 2, -length)
    glVertex3f(width / 2, width / 2, 0)

    glEnd()
 




def load_texture(filename):
    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    image = pygame.image.load(filename)
    if image is None:
        print(f"No se pudo cargar la imagen: {filename}")
        return None
    img_data = pygame.image.tostring(image, "RGBA", 1)
    width, height = image.get_size()
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, img_data)
    return texture_id

def configure_lighting():
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, (-1, -1, -1, 0))  # Fuente de luz direccional

def draw_cubo(size):
    size *= 10  # Hacer el cubo tres veces más grande
    glBegin(GL_QUADS)
    
    # Configurar los materiales para el cubo
    glColor3f(1, 1, 1)  # Color base del cubo
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, (1, 1, 1, 1))

    # Resto del código del cubo como lo tenías
    # Cara frontal
    glTexCoord2f(0, 0)
    glVertex3f(-size, -size, -size)
    glTexCoord2f(1, 0)
    glVertex3f(size, -size, -size)
    glTexCoord2f(1, 1)
    glVertex3f(size, size, -size)
    glTexCoord2f(0, 1)
    glVertex3f(-size, size, -size)
    
    # Cara izquierda
    glTexCoord2f(0, 0)
    glVertex3f(-size, -size, -size)
    glTexCoord2f(1, 0)
    glVertex3f(-size, -size, size)
    glTexCoord2f(1, 1)
    glVertex3f(-size, size, size)
    glTexCoord2f(0, 1)
    glVertex3f(-size, size, -size)
    
    # Cara superior
    glTexCoord2f(0, 0)
    glVertex3f(-size, size, -size)
    glTexCoord2f(1, 0)
    glVertex3f(size, size, -size)
    glTexCoord2f(1, 1)
    glVertex3f(size, size, size)
    glTexCoord2f(0, 1)
    glVertex3f(-size, size, size)
    
    # Cara inferior
    glTexCoord2f(0, 0)
    glVertex3f(-size, -size, -size)
    glTexCoord2f(1, 0)
    glVertex3f(size, -size, -size)
    glTexCoord2f(1, 1)
    glVertex3f(size, -size, size)
    glTexCoord2f(0, 1)
    glVertex3f(-size, -size, size)
    
    # Cara trasera
    glTexCoord2f(0, 0)
    glVertex3f(-size, -size, size)
    glTexCoord2f(1, 0)
    glVertex3f(size, -size, size)
    glTexCoord2f(1, 1)
    glVertex3f(size, size, size)
    glTexCoord2f(0, 1)
    glVertex3f(-size, size, size)
    
    # Cara derecha
    glTexCoord2f(0, 0)
    glVertex3f(size, -size, -size)
    glTexCoord2f(1, 0)
    glVertex3f(size, -size, size)
    glTexCoord2f(1, 1)
    glVertex3f(size, size, size)
    glTexCoord2f(0, 1)
    glVertex3f(size, size, -size)
    
    glEnd()












from button import Button

class Sphere:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed = 5

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        if keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.y += self.speed

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.png")
BG2 = pygame.image.load("assets/Background3.png")
BG3 = pygame.image.load("assets/Background2.png")


def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

def play():
    while True:
        sphere = Sphere(640, 360, 30, (255, 0, 0))  # Crea una instancia de la esfera
        clock = pygame.time.Clock()

        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        keys = pygame.key.get_pressed()
        sphere.move(keys)

        SCREEN.fill("black")
        SCREEN.blit(BG2, (0, 0))

        PLAY_TEXT = get_font(35).render("Aqui se seleciona el nivel", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        sphere.draw(SCREEN)  # Dibuja la esfera en la pantalla

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()
        clock.tick(60)  # Limita el juego a 60 frames por segundo
    
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")
        SCREEN.blit(BG3, (0, 0))

        OPTIONS_TEXT = get_font(35).render("Aqui se seleccionara el personaje.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def options_3d():
    pygame.quit()  # Cierra la ventana Pygame 2D
    
    def render_text(text, x, y):
        text_surface = font.render(text, False, (255, 255, 255))
        text_data = pygame.image.tostring(text_surface, "RGBA", True)
        glRasterPos2d(x, y)
        glDrawPixels(text_surface.get_width(), text_surface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, text_data)


    
    pygame.init()
    display = (1280, 720)  # Ajusta la resolución
    screen = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Observar")


    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glShadeModel(GL_SMOOTH)
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_AMBIENT, [0.5, 0.5, 0.5, 1])
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0, 1.0, 1.0, 1])

    sphere = gluNewQuadric()

    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

    glMatrixMode(GL_MODELVIEW)
    gluLookAt(0, -8, 0, 0, 0, 0, 0, 0, 1)  # Ajusta la posición de la cámara

    viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)
    glLoadIdentity()

    displayCenter = [screen.get_size()[i] // 2 for i in range(2)]
    mouseMove = [0, 0]
    pygame.mouse.set_pos(displayCenter)

    up_down_angle = 0.0
    paused = False
    run = True
    show_figures = True  # Inicialmente mostrar las figuras
    
    # Configuración de la fuente
    font = pygame.font.Font(None, 36)
    
    # Definir variables para controlar las acciones con las teclas "g" y "h"
    show_figure_g = False
    show_figure_h = False
    show_figure_j = False
    show_figure_o= False
    show_figure_m= False
    show_figure_n= False
    show_figure_b= False
    show_figure_v= False
    show_sound_y= False
    show_sound_u= False
    show_figure_e= False
    show_figure_c= False
    show_figure_x= False
    show_figure_z= False
    show_figure_l= False
    show_figure_k= False
    show_figure_i = False
    show_figure_q = False
    show_figure_r= False
    show_figure_t= False
    
    sonido = pygame.mixer.Sound('prb1.wav')
    sonido2 = pygame.mixer.Sound('muerto.wav')
    sonido3 = pygame.mixer.Sound('pipipi.wav')
    sonido4 = pygame.mixer.Sound('Creeper.wav')
    sonido5 = pygame.mixer.Sound('zombie.wav')
    sonido6 = pygame.mixer.Sound('Company.wav')
    sonido7 = pygame.mixer.Sound('laser.wav')
    sonido8 = pygame.mixer.Sound('29960.wav')
    
    # Configuración de la fuente
    font = pygame.font.Font(None, 36)
    
        # Define las rutas a las imágenes del cubemap
    cubemap_paths = [
        "right.png",
        "left.png",
        "top.png",
        "bottom.png",
        "front.png",
        "back.png"
    ]


    # Define las rutas a las imágenes del cubemap
    cubemap_paths1 = [
        "mine4.jpg",
        "left.png",
        "top.png",
        "bottom.png",
        "front.png",
        "back.png"
    ]

    # Define las rutas a las imágenes del cubemap
    cubemap_paths2 = [
        "mine2.jpg",
        "left.png",
        "top.png",
        "bottom.png",
        "front.png",
        "back.png"
    ]

    # Define las rutas a las imágenes del cubemap
    cubemap_paths3 = [
        "coliseo.jpg",
        "left.png",
        "top.png",
        "bottom.png",
        "front.png",
        "back.png"
    ]

    # Define las rutas a las imágenes del cubemap
    cubemap_paths5 = [
        "mine3.jpg",
        "left.png",
        "top.png",
        "bottom.png",
        "front.png",
        "back.png"
    ]

    # Define las rutas a las imágenes del cubemap
    cubemap_paths6 = [
        "dragon.jpg",
        "left.png",
        "top.png",
        "bottom.png",
        "front.png",
        "back.png"
    ]

    # Define las rutas a las imágenes del cubemap
    cubemap_paths7 = [
        "minecra.jpg",
        "left.png",
        "top.png",
        "bottom.png",
        "front.png",
        "back.png"
    ]
    
    glEnable(GL_TEXTURE_2D)

    configure_lighting()  # Configurar la iluminación

    cubemap_textures = [load_texture(filename) for filename in cubemap_paths]
    cubemap_textures1 = [load_texture(filename) for filename in cubemap_paths1]
    cubemap_textures2 = [load_texture(filename) for filename in cubemap_paths2]
    cubemap_textures3 = [load_texture(filename) for filename in cubemap_paths3]
    cubemap_textures5 = [load_texture(filename) for filename in cubemap_paths5]
    cubemap_textures6 = [load_texture(filename) for filename in cubemap_paths6]
    cubemap_textures7 = [load_texture(filename) for filename in cubemap_paths7]

    
    translate_speed = 0.05  # Puedes ajustar la velocidad
    translate_x = -7
    android = Android()
    
    
    
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
                    run = False
                if event.key == pygame.K_PAUSE or event.key == pygame.K_p:
                    paused = not paused
                    pygame.mouse.set_pos(displayCenter)
                    
                if event.key == pygame.K_f:
                    show_figures = not show_figures  # Cambiar el estado de mostrar/ocultar figuras
            
                if event.key == pygame.K_g:
                    show_figure_g = not show_figure_g  # Acción para la tecla "g"
                    sonido8.play()
                    pygame.time.wait(int(sonido.get_length() * 100))
                    
                if event.key == pygame.K_q:
                    show_figure_q = not show_figure_q
                    sonido8.play()
                    show_figure_t=False
                    
                if event.key == pygame.K_z:
                    show_figure_z = not show_figure_z  # Acción para la tecla "v"
                    sonido4.play()
                    show_figure_l = not show_figure_l
                    
                if event.key == pygame.K_n:
                    show_figure_n = not show_figure_n  # Acción para la tecla "n"
                    sonido8.play()
                    
                if event.key == pygame.K_o:
                    show_figure_o = not show_figure_o
                    sonido7.play()
                    
                    
                    
                    
                    
            if not paused:
                if event.type == pygame.MOUSEMOTION:
                    mouseMove = [event.pos[i] - displayCenter[i] for i in range(2)]
                pygame.mouse.set_pos(displayCenter)

        if not paused:
            keypress = pygame.key.get_pressed()
            glLoadIdentity()
            up_down_angle += mouseMove[1] * 0.1
            glRotatef(up_down_angle, 1.0, 0.0, 0.0)
            glPushMatrix()
            glLoadIdentity()
            if keypress[pygame.K_w]:
                glTranslatef(0, 0, 0.1)
            if keypress[pygame.K_s]:
                glTranslatef(0, 0, -0.1)
            if keypress[pygame.K_d]:
                glTranslatef(-0.1, 0, 0)
            if keypress[pygame.K_a]:
                glTranslatef(0.1, 0, 0)
            
            glRotatef(mouseMove[0] * 0.1, 0.0, 1.0, 0.0)
            glMultMatrixf(viewMatrix)
            viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)
            
            glPopMatrix()
            glMultMatrixf(viewMatrix)
            glLightfv(GL_LIGHT0, GL_POSITION, [1, -1, 1, 0])
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

            # Aquí deberías agregar el código para dibujar tus figuras 3D, similar a lo que ya tienes.
                  #aqui comienza donde se pinta la figura dentro de los escenarios
            glPushMatrix()

            #aqui comienza donde se pintan los escenarios
            
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

            for i in range(6):
                glBindTexture(GL_TEXTURE_2D, cubemap_textures[i])
                draw_cubo(2)
                
            glColor4f(0.0, 1.0, 0.0, 1.0)  # Restablece el color a verde
            
            if show_figure_q:
            
                glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
                for i in range(6):
                    glBindTexture(GL_TEXTURE_2D, cubemap_textures5[i])
                    draw_cubo(2)
                
                glColor4f(0.0, 1.0, 0.0, 1.0)  # Restablece el color a verde
            
            if show_figure_l:
            
                glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
                for i in range(6):
                    glBindTexture(GL_TEXTURE_2D, cubemap_textures1[i])
                    draw_cubo(2)
                
                glColor4f(0.0, 1.0, 0.0, 1.0)  # Restablece el color a verde
                
            if show_figure_k:
            
                glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
                for i in range(6):
                    glBindTexture(GL_TEXTURE_2D, cubemap_textures2[i])
                    draw_cubo(2)
                
                glColor4f(0.0, 1.0, 0.0, 1.0)  # Restablece el color a verde
                
                
            if show_figure_t:
            
                glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
                for i in range(6):
                    glBindTexture(GL_TEXTURE_2D, cubemap_textures7[i])
                    draw_cubo(2)
                
                glColor4f(0.0, 1.0, 0.0, 1.0)  # Restablece el color a verde
                
                
            
            
            
            
            if show_figures:
            
                #Creper
                draw_cube((0,0,0), (1, 1, 1))
                draw_arm((-0.7, 0, -2.6), (0.2, 0.2, 1.0), (30, 0.0, 0.0, 1.0))
                draw_body((0, 0, -2.5), (1, 1, 1), (1, 1, 1))
                draw_arm2((0.7, 0, -2.6), (1, 1, 1), (0.0, 0.0, 1.0, 1.0))
                draw_pie((0.5, 0, -5), (1, 1, 1), (0.0, 0.0, 1.0, 1.0))
                draw_pe2((-0.5, 0, -5), (1, 1, 1), (0.0, 0.0, 1.0, 1.0))
                draw_eyes1((-0.9, -1.3, 2.0), (1, 1, 1), (0.0, 0.0, 1.0, 1.0))
                draw_eyes2((1.0, -1.3, 2.0), (1, 1, 1), (0.0, 0.0, 1.0, 1.0))
                draw_mouth((-0.01, -0.7, 0.2), (1, 1, 1), (0.0, 0.0, 1.0, 1.0))
                glColor4f(0.0, 1.0, 0.0, 1.0)  # Restablece el color a verde
                render_text("El Creepr3000", 1.5, 2.0)            # Mover arriba a 1.2
                
                
                #pokemon
                glColor4f(1.0, 1.0, 0.0, 1.0)
                ojo1((-0.2 - translate_x, -1, 0.3), (.2, .1, .2))
                ojo2((0.4 - translate_x, -1, 0.3), (.2, .1, .2))
                draw_smile_mouth(.5, (.1 - translate_x, -1, -0.1), 0, pi, 100)
                glColor4f(0.0, 0.4, 1.0, 0.3)
                glTranslatef(-translate_x, 0, 0)
                draw_half_spheres(1.0, 20, 20)
                draw_half_sphere_lower(1.0, 20, 20)
                render_text("Pokemon", 1.5, 2.0)            # Mover arriba a 1.2
                
                #andy
                #primero llamamos los demtodos de la clase android con el obj android 
                #despues usando el push y pop podemos hacer una traslacion en el punto que queramos
                # por ultimo hacemos una rotacion para que se visualice correctamente el persoanje 
                glPushMatrix()
                glTranslatef(-13, -2, 0)
                glRotate(90, 1,0,0)
                glRotate(90, 0,1,0)
                glScale(3, 3, 3)
                android.DrawCabeza()
                android.DrawCuerpo()
                android.DrawUniones()
                android.DrawManoder()
                android.DrawManoizq()
                android.DrawPieder()
                android.DrawPieizq()
                glPopMatrix()
                
                
            if show_figure_z:
                show_figures = False  # Inicialmente mostrar las figuras
                
                draw_cube((0,0,0), (1, 1, 1))
            
                draw_body((0, 0, -2.5), (1, 1, 1), (1, 1, 1))
            
                draw_pie((0.5, 0, -5), (1, 1, 1), (0.0, 0.0, 1.0, 1.0))
                draw_pe2((-0.5, 0, -5), (1, 1, 1), (0.0, 0.0, 1.0, 1.0))
                draw_eyes1((-0.9, -1.3, 2.0), (1, 1, 1), (0.0, 0.0, 1.0, 1.0))
                draw_eyes2((1.0, -1.3, 2.0), (1, 1, 1), (0.0, 0.0, 1.0, 1.0))
                draw_mouth((-0.01, -0.7, 0.2), (1, 1, 1), (0.0, 0.0, 1.0, 1.0))
                draw_eyes1((-0.9, -1.3, 2.0), (1.0,1.0, 0.5), (0.0, 0.0, 1.0, 1.0))
                draw_eyes1((1.0, -1.3, 2.0), (1.0,1.0, 0.5), (0.0, 0.0, 1.0, 1.0))
                draw_mouth((1.5, -0.7, -1.0), (1, 1, 1), (95, 0.0, 1.0, 0.0))
                draw_arm((-1.2, 0, -2.2), (0.8, 0.1, 0.2), (0,0,0,0))
                
                draw_arm2((0.7, 0, -2.6), (1, 1, 1), (0.0, 0.0, 1.0, 1.0))
                
                
                draw_pie((1.0, 1.0, 1), (1, 1, 1), (115.0, 1.0, 0.0, 0.0))
                draw_pe2((-0.9, 1.0, 1), (1, 1, 1), (115.0, 1.0, 0.0, 0.0))
                
                glColor4f(0.0, 1.0, 0.0, 1.0)  # Restablece el color a verde
                
            if show_figure_n:
            
                show_figure_t=True
                
                show_figures = False  # Inicialmente mostrar las figuras
                draw_cube((0,0,0), (1, 1, 1))
            
                draw_body((0, 0, -2.5), (1, 1, 1), (1, 1, 1))
                draw_arm((-1.2, 0, -2.2), (0.8, 0.1, 0.2), (0,0,0,0))
                
        
                draw_pie((0.5, 0, -5), (1, 1, 1), (45.0, 1.0, 1.0, 0.0))
                draw_pe2((-0.5, 0, -5), (1, 1, 1), (45.0, 0.0, 1.0, 0.0))
                draw_eyes1((-0.9, -1.3, 2.0), (0.3, 1, 1), (0.0, 0.0, 1.0, 1.0))
                draw_eyes1((1.0, -1.3, 2.0), (0.3, 1, 1), (0.0, 0.0, 1.0, 1.0))
                glColor4f(0.0, 1.0, 0.0, 1.0)  # Restablece el color a verde
                
                
                # Dibuja brazo izqui 
                glColor4f(0.0, 0.0, 1.0, 1.0)  # Cambia el color a azul para el paralelepípedo
                glPushMatrix()
                glTranslatef(1.2, 0, -2.2)  # Mueve el paralelepípedo hacia atrás en el eje z
                glScalef(0.8, 0.1, 0.2)  # Escala el cubo para hacerlo más largo en el eje z

                # Dibuja el paralelepípedo en posición horizontal
                glBegin(GL_QUADS)
                # Cara frontal
                glVertex3f(-1, -1, -1)
                glVertex3f(1, -1, -1)
                glVertex3f(1, 1, -1)
                glVertex3f(-1, 1, -1)

                # Cara posterior
                glVertex3f(-1, -1, 1)
                glVertex3f(1, -1, 1)
                glVertex3f(1, 1, 1)
                glVertex3f(-1, 1, 1)

                # Cara superior
                glVertex3f(-1, 1, -1)
                glVertex3f(1, 1, -1)
                glVertex3f(1, 1, 1)
                glVertex3f(-1, 1, 1)

                # Cara inferior
                glVertex3f(-1, -1, -1)
                glVertex3f(1, -1, -1)
                glVertex3f(1, -1, 1)
                glVertex3f(-1, -1, 1)
    
                # Cara izquierda
                glVertex3f(-1, -1, -1)
                glVertex3f(-1, 1, -1)
                glVertex3f(-1, 1, 1) 
                glVertex3f(-1, -1, 1)

                # Cara derecha
                glVertex3f(1, -1, -1)
                glVertex3f(1, 1, -1)
                glVertex3f(1, 1, 1)
                glVertex3f(1, -1, 1)
                glEnd()

                glPopMatrix()
                
                glColor4f(0.0, 0.0, 0.0, 1.0)  # Color rojo para el rectángulo
                glPushMatrix()
                glScalef(0.7, 0.7, 0.3)  # Escala el rectángulo para hacerlo más pequeño
                glTranslatef(-0.01, -0.7, 0.1)
                glBegin(GL_QUADS)
                glVertex3f(-0.75, -0.75, -1)  # Esquina inferior izquierda
                glVertex3f(0.75, -0.75, -1)   # Esquina inferior derecha
                glVertex3f(0.75, -0.75, -2)   # Esquina superior derecha
                glVertex3f(-0.75, -0.75, -2)  # Esquina superior izquierda
                glEnd()
                glPopMatrix()     
                
            if show_figure_o:
            
                # Dibujar texto en la escena
                render_text("El Creepr3000", 1.5, 2.0)            # Mover arriba a 1.2

        
                
                
                
            glPopMatrix()

            pygame.display.flip()
            pygame.time.wait(10)
    
    
    
    










def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("Math Quest", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250),
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400),
                            text_input="PERSONAJE 3D", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550),
                            text_input="SALIR", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options_3d()  # Llama a la función de opciones 3D
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    

        pygame.display.update()

main_menu()