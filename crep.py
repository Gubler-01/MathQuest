import pygame
from OpenGL.GL import *

class Dibujar:
    @staticmethod
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

    @staticmethod
    def draw_arm(position, scale, rota):
        position_variable = position
        scale_variable = scale
        drota = rota
        glColor4f(0.0, 0.0, 1.0, 1.0)  # Cambia el color a azul para el nuevo cubo
        glPushMatrix()
        glTranslatef(position[0], position[1], position[2])
        glScalef(scale[0], scale[1], scale[2])
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


    @staticmethod
    def draw_body(position, scale, color):
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
        
    @staticmethod  
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
        
        
    @staticmethod
    def draw_pie(position, scale, rota):
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
        
        
    @staticmethod
    def draw_pe2(position, scale, rota):
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
        
    @staticmethod
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
        
        
    @staticmethod
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
        
        
    @staticmethod
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
        
    @staticmethod
    def draw_exp1():
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
             
    @staticmethod
    def draw_exp2():
           glColor4f(0.0, 0.1, 0.1, 1.0)  # Color rojo para el rectángulo
           glPushMatrix()
           glTranslatef(1.1, -0.56, 0.9)  # Mueve el cubo hacia abajo
           glScalef(0.6, 0.6, 0.1)  # Escala el cubo para hacerlo más largo en el eje z
           glRotatef(45, 0.0, 1.0, 0.0)
           glBegin(GL_QUADS)
           glVertex3f(-0.75, -0.75, -1)  # Esquina inferior izquierda
           glVertex3f(0.75, -0.75, -1)   # Esquina inferior derecha
           glVertex3f(0.75, -0.75, -2)   # Esquina superior derecha
           glVertex3f(-0.75, -0.75, -2)  # Esquina superior izquierda
           glEnd()
           glPopMatrix()
            
            
           glColor4f(0.0, 0.1, 0.1, 1.0)  # Color rojo para el rectángulo
           glPushMatrix()
           glTranslatef(0.3, -0.56, 0.9)  # Mueve el cubo hacia abajo
           glScalef(0.6, 0.6, 0.1)  # Escala el cubo para hacerlo más largo en el eje z
           glRotatef(45, 0.0, 1.0, 0.0)
           glBegin(GL_QUADS)
           glVertex3f(-0.75, -0.75, -1)  # Esquina inferior izquierda
           glVertex3f(0.75, -0.75, -1)   # Esquina inferior derecha
           glVertex3f(0.75, -0.75, -2)   # Esquina superior derecha
           glVertex3f(-0.75, -0.75, -2)  # Esquina superior izquierda
           glEnd()
           glPopMatrix()
           glColor4f(0.0, 1.0, 0.0, 1.0)  # Restablece el color a verde    
          
   
    @staticmethod
    def draw_cejas():
            glColor4f(0.0, 0.1, 0.1, 1.0)  # Color rojo para el rectángulo
            glPushMatrix()
            glTranslatef(-0.5, -0.56, 0.9)  # Mueve el cubo hacia abajo
            glScalef(0.6, 0.6, 0.1)  # Escala el cubo para hacerlo más largo en el eje z
            glBegin(GL_QUADS)
            glVertex3f(-0.75, -0.75, -1)  # Esquina inferior izquierda
            glVertex3f(0.75, -0.75, -1)   # Esquina inferior derecha
            glVertex3f(0.75, -0.75, -2)   # Esquina superior derecha
            glVertex3f(-0.75, -0.75, -2)  # Esquina superior izquierda
            glEnd()
            glPopMatrix()
            
            
            glColor4f(0.0, 0.1, 0.1, 1.0)  # Color rojo para el rectángulo
            glPushMatrix()
            glTranslatef(0.5, -0.56, 0.9)  # Mueve el cubo hacia abajo
            glScalef(0.6, 0.6, 0.1)  # Escala el cubo para hacerlo más largo en el eje z
            glBegin(GL_QUADS)
            glVertex3f(-0.75, -0.75, -1)  # Esquina inferior izquierda
            glVertex3f(0.75, -0.75, -1)   # Esquina inferior derecha
            glVertex3f(0.75, -0.75, -2)   # Esquina superior derecha
            glVertex3f(-0.75, -0.75, -2)  # Esquina superior izquierda
            glEnd()
            glPopMatrix()
            glColor4f(0.0, 1.0, 0.0, 1.0)  # Restablece el color a verde