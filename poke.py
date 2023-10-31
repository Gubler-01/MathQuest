from OpenGL.GL import *
from OpenGL import *
from OpenGL.GLU import gluPerspective
import pygame
import math
from math import *


class Pintamos():
    @staticmethod
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

    @staticmethod
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


    @staticmethod
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
        
        
    @staticmethod
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
        
        
        
    @staticmethod
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
            
    @staticmethod
    def draw_pickaxe_tip(radius, height, segments=16):
        glBegin(GL_TRIANGLE_FAN)
        glVertex(0, 0, height)  # Vértice superior del cono
        for i in range(segments + 1):
            angle = 2 * math.pi * i / segments
            x = radius * math.cos(angle)
            y = radius * math.sin(angle)
            glVertex(x, y, 0)
        glEnd()
        
    @staticmethod
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
        
    @staticmethod
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


    @staticmethod
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
                
                
    @staticmethod
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
    @staticmethod
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

    @staticmethod
    def flecha():
            glPushMatrix()
            glColor3f(0.0, 0.0, 0.0)  # Color gris claro
            glTranslate(1, -1.4, 1)  # Ajustar la posición de la punta del pico
            
            glPopMatrix()
            glPushMatrix()
            glColor3f(0.6, 0.3, 0.0)  # Color marrón
            glTranslate(1, -1.4, 1)  # Ajustar la posición del palo del pico
             
            glPopMatrix()