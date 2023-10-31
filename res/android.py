import sys
sys.path.append('..')
from res.App import App
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from math import *
import numpy as np 

# Inicializa GLUT
glutInit(sys.argv)

class GLUtils:
    @staticmethod
    def InitRender():
        glLoadIdentity()
        gluPerspective(60, (600 / 600), 0.1, 100)
        gluLookAt(0, 0, 4, 0, 0, 0, 0, 1, 0)
        glEnable(GL_DEPTH_TEST)
        glClearColor(0.86, 0.66, 0.54, 1.0)

    @staticmethod
    def PrepareRender():
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    @staticmethod
    def DrawSphere(radius, slices, stacks):
        glutSolidSphere(radius, slices, stacks)

    @staticmethod
    def DrawHalfSphere(radius, slices, stacks):
        glBegin(GL_QUADS)
        # Itera solo para la mitad superior de las stacks
        for i in range(stacks // 2, stacks):
            lat0 = pi * (-0.5 + (i / stacks))
            lat1 = pi * (-0.5 + ((i + 1) / stacks))
            for j in range(slices):
                lng0 = 2 * pi * (j / slices)
                lng1 = 2 * pi * ((j + 1) / slices)

                x0 = radius * cos(lng0) * cos(lat1)
                y0 = radius * sin(lng0) * cos(lat1)
                z0 = radius * sin(lat1)

                x1 = radius * cos(lng0) * cos(lat0)
                y1 = radius * sin(lng0) * cos(lat0)
                z1 = radius * sin(lat0)

                x2 = radius * cos(lng1) * cos(lat0)
                y2 = radius * sin(lng1) * cos(lat0)
                z2 = radius * sin(lat0)

                x3 = radius * cos(lng1) * cos(lat1)
                y3 = radius * sin(lng1) * cos(lat1)
                z3 = radius * sin(lat1)

                # Calcular normales de las caras
                normal0 = [x0, y0, z0]
                normal1 = [x1, y1, z1]
                normal2 = [x2, y2, z2]
                normal3 = [x3, y3, z3]

                # Normalizar las normales de las caras
                normal0 = np.array(normal0) / np.linalg.norm(normal0)
                normal1 = np.array(normal1) / np.linalg.norm(normal1)
                normal2 = np.array(normal2) / np.linalg.norm(normal2)
                normal3 = np.array(normal3) / np.linalg.norm(normal3)

                glNormal3fv(normal0)  # Establecer la normal de la cara
                glVertex3f(x0, y0, z0)

                glNormal3fv(normal1)  # Establecer la normal de la cara
                glVertex3f(x1, y1, z1)

                glNormal3fv(normal2)  # Establecer la normal de la cara
                glVertex3f(x2, y2, z2)

                glNormal3fv(normal3)  # Establecer la normal de la cara
                glVertex3f(x3, y3, z3)
        glEnd()

    @staticmethod
    def DrawTorus(inner_radius, outer_radius, sides, rings):
        glutSolidTorus(inner_radius, outer_radius, sides, rings)

class Android():
    def DrawCabeza(self):
    ########################### Cabeza ########################
        glColor3f(0.0, 0.75, 0)
        glPushMatrix()
        glTranslated(1, 0, 0)
        glRotate(-90, 1, 0, 0)
        GLUtils.DrawHalfSphere(0.5, 30, 30)
        glPopMatrix()

        # Dibujamos dos esferas pequeñas como ojos en la parte frontal de la media esfera
        glColor3f(0.3, 0.3, 0.3)  # Color azul para los ojos frontales
        glPushMatrix()
        # Posición del primer ojo frontal (en la parte de adelante de la media esfera)
        glTranslated(0.58, 0.2, -0.13)
        GLUtils.DrawSphere(0.065, 10, 10)  # Primer ojo frontal
        glPopMatrix()

        glColor3f(0.3, 0.3, 0.3)  # Color azul para los ojos frontales
        glPushMatrix()
        # Posición del primer ojo frontal (en la parte de adelante de la media esfera)
        glTranslated(0.58, 0.2, 0.13)
        GLUtils.DrawSphere(0.065, 10, 10)  # Segundo ojo frontal
        glPopMatrix()

        # Dibujamos dos cilindros delgados como antenas en la parte de arriba de la media esfera, junto a los ojos
        glColor3f(0.0, 0.75, 0)  # Color amarillo para las antenas
        glPushMatrix()
        # Posición de la primera antena (junto al primer ojo frontal)
        glTranslated(1, 0.55, -0.3)
        glRotate(55, 1, 0, 0)
        # Primer cilindro delgado con radio de 0.02 y altura de 0.3
        glutSolidCylinder(0.02, 0.3, 20, 20)
        glPopMatrix()

        # Segunda antena en el lado opuesto
        glPushMatrix()
        # Posición de la segunda antena (en el lado opuesto del primer ojo frontal)
        glTranslated(1, 0.31, 0.1)
        glRotate(-55, 1, 0, 0)  # Rotación en dirección opuesta
        # Segundo cilindro delgado con radio de 0.02 y altura de 0.3
        glutSolidCylinder(0.02, 0.3, 20, 20)
        glPopMatrix()

    def DrawCuerpo(self):
        ################### Cuerpo################################
        # Dibujamos un cilindro más pequeño entre la media esfera y el cilindro grande
        glColor3f(0.3, 0.3, 0.3)  # Color azul para el cilindro pequeño
        glPushMatrix()
        # Posición del cilindro pequeño (misma que la media esfera)
        glTranslated(1, 0, 0)
        glRotate(90, 1, 0, 0)
        # Cilindro pequeño con radio de 0.3 y altura de 0.5
        glutSolidCylinder(0.49, 0.025, 20, 20)
        glPopMatrix()

        # Dibujamos un cilindro debajo de la media esfera
        glColor3f(0, 0.75, 0)  # Color verde para el cilindro
        glPushMatrix()
        # Posición del cilindro (misma que la media esfera)
        glTranslated(1, -0.025, 0)
        glRotate(90, 1, 0, 0)
        # Cilindro con radio de 0.5 y altura de 1
        glutSolidCylinder(0.5, 0.75, 20, 20)
        glPopMatrix()

    def DrawUniones(self):
        ################### Interseccion Derecha ^ Izquierda################################
        glColor3f(0.3, 0.3, 0.3)
        glPushMatrix()
        glTranslatef(1, -0.2, 0.5)  # Posición del cilindro de conexión
        # Rotar 90 grados alrededor del eje X para que el cilindro se extienda hacia el cuerpo
        glRotatef(90, 0, 0, 1)
        glutSolidCylinder(0.025, 0.1, 20, 20)  # Radio de 0.05 y altura de 0.1
        glPopMatrix()

        glPushMatrix()
        glTranslatef(1, -0.2, -0.6)  # Posición del cilindro de conexión
        # Rotar 90 grados alrededor del eje X para que el cilindro se extienda hacia el cuerpo
        glRotatef(90, 0, 0, 1)
        glutSolidCylinder(0.025, 0.1, 20, 20)  # Radio de 0.05 y altura de 0.1
        glPopMatrix()

    def DrawManoder(self):
        
        ################### Mano derecha################################
        glColor3f(0, 0.75, 0)
        # Poner la media esfera encima del cilindro (parte de arriba)
        glPushMatrix()
        # Posición de la media esfera encima del cilindro
        glTranslatef(1, -0.13, 0.62)
        glRotate(270, 1, 0, 0)
        # Radio de 0.1 y 20 slices y 20 stacks
        GLUtils.DrawHalfSphere(0.085, 20, 20)
        glPopMatrix()

        # Dibujar el cilindro
        glPushMatrix()
        # Posición del cilindro debajo de la media esfera
        glTranslatef(1, -0.13, 0.62)
        glRotatef(90, 1, 0, 0)  # Rota el cilindro para que esté de pie
        # Radio de 0.5, altura de 1.0, 20 slices y 20 stacks
        glutSolidCylinder(0.085, 0.25, 20, 20)
        glPopMatrix()

        glColor3f(0, 0.75, 0)
        # Poner la media esfera encima del cilindro (parte de arriba)
        glPushMatrix()
        # Posición de la media esfera encima del cilindro
        glTranslatef(1, -0.38, 0.62)
        glRotate(90, 1, 0, 0)
        # Radio de 0.1 y 20 slices y 20 stacks
        GLUtils.DrawHalfSphere(0.085, 20, 20)
        glPopMatrix()

    def DrawManoizq(self):
        ################### Mano izquierda################################

        glColor3f(0, 0.75, 0)
        # Poner la media esfera encima del cilindro (parte de arriba)
        glPushMatrix()
        # Posición de la media esfera encima del cilindro
        glTranslatef(1, -0.13, -0.62)
        glRotate(270, 1, 0, 0)
        # Radio de 0.1 y 20 slices y 20 stacks
        GLUtils.DrawHalfSphere(0.085, 20, 20)
        glPopMatrix()

        # Dibujar el cilindro
        glPushMatrix()
        # Posición del cilindro debajo de la media esfera
        glTranslatef(1, -0.13, -0.62)
        glRotatef(90, 1, 0, 0)  # Rota el cilindro para que esté de pie
        # Radio de 0.5, altura de 1.0, 20 slices y 20 stacks
        glutSolidCylinder(0.085, 0.25, 20, 20)
        glPopMatrix()

        glColor3f(0, 0.75, 0)
        # Poner la media esfera encima del cilindro (parte de arriba)
        glPushMatrix()
        # Posición de la media esfera encima del cilindro
        glTranslatef(1, -0.38, -0.62)
        glRotate(90, 1, 0, 0)
        # Radio de 0.1 y 20 slices y 20 stacks
        GLUtils.DrawHalfSphere(0.085, 20, 20)
        glPopMatrix()

    def DrawPieder(self):
        ################### Pie derecho################################
        # Dibujar el cilindro
        glPushMatrix()
        # Posición del cilindro debajo de la media esfera
        glTranslatef(1, -0.75, 0.2)
        glRotatef(90, 1, 0, 0)  # Rota el cilindro para que esté de pie
        # Radio de 0.5, altura de 1.0, 20 slices y 20 stacks
        glutSolidCylinder(0.085, 0.25, 20, 20)
        glPopMatrix()

        glColor3f(0, 0.75, 0)
        # Poner la media esfera encima del cilindro (parte de arriba)
        glPushMatrix()
        # Posición de la media esfera encima del cilindro
        glTranslatef(1, -1, 0.2)
        glRotate(90, 1, 0, 0)
        # Radio de 0.1 y 20 slices y 20 stacks
        GLUtils.DrawHalfSphere(0.085, 20, 20)
        glPopMatrix()

    def DrawPieizq(self):
        ################### Pie izquierdo################################
        # Dibujar el cilindro
        glPushMatrix()
        # Posición del cilindro debajo de la media esfera
        glTranslatef(1, -0.75, -0.2)
        glRotatef(90, 1, 0, 0)  # Rota el cilindro para que esté de pie
        # Radio de 0.5, altura de 1.0, 20 slices y 20 stacks
        glutSolidCylinder(0.085, 0.25, 20, 20)
        glPopMatrix()

        glColor3f(0, 0.75, 0)
        # Poner la media esfera encima del cilindro (parte de arriba)
        glPushMatrix()
        # Posición de la media esfera encima del cilindro
        glTranslatef(1, -1, -0.2)
        glRotate(90, 1, 0, 0)
        # Radio de 0.1 y 20 slices y 20 stacks
        GLUtils.DrawHalfSphere(0.085, 20, 20)
        glPopMatrix()

class OpenGLApp(App):
    def Init(self):
        GLUtils.InitRender()

    def Render(self):
        GLUtils.PrepareRender()

	#Aqui va el codigo del dibujo
        glPushMatrix()
        glTranslatef(0, 0, 0)
        glRotate(90, 0,1,0)
        Android.DrawCabeza(self)
        Android.DrawCuerpo(self)
        glPopMatrix()


if __name__ == '__main__':
    app = OpenGLApp("OpenGL en Python", 600, 600, 60)
    app.Run()