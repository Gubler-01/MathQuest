import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import tkinter as tk

pygame.init()
display = (600, 600)
screen = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

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
gluLookAt(0, -8, 0, 0, 0, 0, 0, 0, 1)
viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)
glLoadIdentity()

# Inicializa el movimiento del mouse y centra el mouse en la pantalla
displayCenter = [screen.get_size()[i] // 2 for i in range(2)]
mouseMove = [0, 0]
pygame.mouse.set_pos(displayCenter)

up_down_angle = 0.0
paused = False
run = True

#metrica del rombo

sphere_pos = [4, 0, 0]  # Posición inicial de la segunda esfera
movement_speed = 0.1  # Velocidad de movimiento de la esfera
collision_message_shown = False


#mterica de interseccion
sphere_pos2 = [-4, 0, 0]  # Posición inicial de la segunda esfera
movement_speed2 = 0.1  # Velocidad de movimiento de la esfera

def check_collision():
    # Coordenadas del centro de la esfera
    sphere_center = [sphere_pos2[0], sphere_pos2[1], sphere_pos2[2]]
    # Coordenadas del cubo (Ajusta las coordenadas según el tamaño y la posición de tu cubo)
    cube_min = [-1, -1, -1]  # Esquina inferior del cubo
    cube_max = [1, 1, 1]     # Esquina superior del cubo
    
    # Comprueba la colisión utilizando intersección de AABB (caja alineada con ejes)
    if (sphere_center[0] > cube_max[0] or sphere_center[0] < cube_min[0] or
        sphere_center[1] > cube_max[1] or sphere_center[1] < cube_min[1] or
        sphere_center[2] > cube_max[2] or sphere_center[2] < cube_min[2]):
        return False  # No hay colisión
    else:
        return True  # Hay colisión

collision_messagein = False






#cajas 


sphere_pos3 = [9, 0, 0]  # Posición inicial de la segunda esfera
movement_speed3 = 0.1  # Velocidad de movimiento de la esfera

# Define las cajas delimitadoras alrededor del cubo y la esfera
cube_bounding_box = {
    "min_x": -1,
    "max_x": 1,
    "min_y": -1,
    "max_y": 1,
    "min_z": -1,
    "max_z": 1
}

sphere_bounding_box = {
    "min_x": sphere_pos3[0] - 1,
    "max_x": sphere_pos3[0] + 1,
    "min_y": sphere_pos3[1] - 1,
    "max_y": sphere_pos3[1] + 1,
    "min_z": sphere_pos3[2] - 1,
    "max_z": sphere_pos3[2] + 1
}

def check_collisioncaja():
    # Verifica la colisión entre las cajas delimitadoras
    if (cube_bounding_box["max_x"] < sphere_bounding_box["min_x"] or
        cube_bounding_box["min_x"] > sphere_bounding_box["max_x"] or
        cube_bounding_box["max_y"] < sphere_bounding_box["min_y"] or
        cube_bounding_box["min_y"] > sphere_bounding_box["max_y"] or
        cube_bounding_box["max_z"] < sphere_bounding_box["min_z"] or
        cube_bounding_box["min_z"] > sphere_bounding_box["max_z"]):
        return False  # No hay colisión
    else:
        return True  # Hay colisión

collision_message_caja = False







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
        
        
        glPushMatrix()
        # Dibuja un cubo
        glColor4f(0.0, 1.0, 0.0, 1.0)  # Color verde para el nuevo cubo
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
        

        # Mover la esfera con las teclas 1 y 2
        if keypress[pygame.K_1]:
            sphere_pos[0] -= movement_speed
        if keypress[pygame.K_2]:
            sphere_pos[0] += movement_speed
                                # Mover la esfera con las teclas 3 y 4
        if keypress[pygame.K_3]:
            sphere_pos2[0] -= movement_speed2
        if keypress[pygame.K_4]:
            sphere_pos2[0] += movement_speed2
                    # Mover la esfera con las teclas 5 y 6
        if keypress[pygame.K_5]:
            sphere_pos3[0] -= movement_speed3
        if keypress[pygame.K_6]:
            sphere_pos3[0] += movement_speed3
            
            
            #rombo

        glPushMatrix()
        glTranslatef(sphere_pos[0], sphere_pos[1], sphere_pos[2])
        glColor4f(1.0, 0.0, 1.0, 1.0)  # Cambia el color de la segunda esfera
        gluSphere(sphere, 1.0, 32, 16)
        glPopMatrix()

        # Comprobar colisión
        if abs(sphere_pos[0]) < 1.0:
            if not collision_message_shown:
                print("¡Chocó!")
                ventana = tk.Tk()
                ventana.title("Advertencia")
                canvas = tk.Canvas(ventana, width=400, height=400)
                canvas.pack()
                # Dibuja texto en el canvas
                texto = canvas.create_text(100, 20, text="resolver: 7*8*4+5", font=("Helvetica", 15), fill="blue")
                ventana.mainloop()
                collision_message_shown = True
                
                #interseccion
                
        glPushMatrix()
        glTranslatef(sphere_pos2[0], sphere_pos2[1], sphere_pos2[2])
        glColor4f(1.0, 0.0, 0.0, 1.0)
        gluSphere(sphere, 1.0, 32, 16)
        glPopMatrix()

        # Comprobar colisión
        if check_collision():
            if not collision_messagein:
                print("¡Chocó!")
                ventana = tk.Tk()
                ventana.title("Advertencia")
                canvas = tk.Canvas(ventana, width=400, height=400)
                canvas.pack()
                # Dibuja texto en el canvas
                texto = canvas.create_text(100, 20, text="resolver: 5*5(6+9)", font=("Helvetica", 15), fill="blue")
                ventana.mainloop()
                collision_messagein = True
                
                
                
                
                #cajas
                
                        # Actualiza la caja delimitadora de la esfera
        sphere_bounding_box["min_x"] = sphere_pos3[0] - 1
        sphere_bounding_box["max_x"] = sphere_pos3[0] + 1

        glPushMatrix()
        glTranslatef(sphere_pos3[0], sphere_pos3[1], sphere_pos3[2])
        glColor4f(0.0, 1.0, 1.0, 1.0)
        gluSphere(sphere, 1.0, 32, 16)
        glPopMatrix()

        # Comprobar colisión
        if check_collisioncaja():
            if not collision_message_caja:
                print("¡Chocó!")
                ventana = tk.Tk()
                ventana.title("Advertencia")
                canvas = tk.Canvas(ventana, width=300, height=100)
                canvas.pack()
                # Dibuja texto en el canvas
                texto = canvas.create_text(150, 20, text="Chocó con metrica de caja", font=("Helvetica", 10), fill="blue")
                ventana.mainloop()
                collision_message_caja = True
                
                
        
        
        
        
        
        
        

        # Dibuja un cubo verde debajo del cubo azul
        glColor4f(0.0, 1.0, 0.0, 1.0)  # Color verde para el nuevo cubo
        glPushMatrix()
        glTranslatef(0, 0, -2.5)  # Mueve el cubo hacia abajo
        glScalef(0.5, 0.5, 2.0)  # Escala el cubo para hacerlo más largo en el eje z
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
        
         # Dibuja brazo izqui 
        glColor4f(0.0, 0.0, 1.0, 1.0)  # Cambia el color a azul para el nuevo cubo
        glPushMatrix()
        glTranslatef(-0.7, 0, -2.6)  # Mueve el cubo hacia la izquierda y hacia abajo
        glScalef(0.2, 0.2, 1.0)  # Escala el cubo para hacerlo más largo en el eje z
        glRotatef(30, 0.0, 0.0, 1.0)
        

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
        
        
                        # Dibuja brazo derecho
        glColor4f(0.0, 0.0, 1.0, 1.0)  # Cambia el color a azul para el nuevo cubo
        glPushMatrix()
        glTranslatef(0.7, 0, -2.6)  # Mueve el cubo hacia la izquierda y hacia abajo
        glScalef(0.2, 0.2, 1.0)  # Escala el cubo para hacerlo más largo en el eje z
        glRotatef(30, 0.0, 0.0, 1.0)

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
        
        
                                # Dibuja brazo derecho
        glColor4f(0.0, 0.0, 1.0, 1.0)  # Cambia el color a azul para el nuevo cubo
        glPushMatrix()
        glTranslatef(0.5, 0, -5)  # Mueve el cubo hacia la izquierda y hacia abajo
        glScalef(0.2, 0.2, 0.5)  # Escala el cubo para hacerlo más largo en el eje z
        glRotatef(-90, 1.0, 0.0, 0.0)


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
        
                        # Dibuja brazo izquierdo 
        glColor4f(0.0, 0.0, 1.0, 1.0)  # Cambia el color a azul para el nuevo cubo
        glPushMatrix()
        glTranslatef(-0.5, 0, -5)  # Mueve el cubo hacia la izquierda y hacia abajo
        glScalef(0.2, 0.2, 0.5)  # Escala el cubo para hacerlo más largo en el eje z
        glRotatef(-90, 1.0, 0.0, 0.0)
        
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
        
        
        glColor4f(1.0, 0.0, 0.0, 1.0)  # Color rojo para el rectángulo
        glPushMatrix()
        glScalef(0.5, 0.5, 0.5)  # Escala el rectángulo para hacerlo más pequeño
        glTranslatef(-0.9, -1.3, 2.0)  # Mueve el cubo hacia abajo
        glBegin(GL_QUADS)
        glVertex3f(-0.75, -0.75, -1)  # Esquina inferior izquierda
        glVertex3f(0.75, -0.75, -1)   # Esquina inferior derecha
        glVertex3f(0.75, -0.75, -2)   # Esquina superior derecha
        glVertex3f(-0.75, -0.75, -2)  # Esquina superior izquierda
        glEnd()
        glPopMatrix()
        
        
        glColor4f(1.0, 0.0, 0.0, 1.0)  # Color rojo para el rectángulo
        glPushMatrix()
        glScalef(0.5, 0.5, 0.5)  # Escala el rectángulo para hacerlo más pequeño
        glTranslatef(1.0, -1.3, 2.0)  # Mueve el cubo hacia abajo
        glBegin(GL_QUADS)
        glVertex3f(-0.75, -0.75, -1)  # Esquina inferior izquierda
        glVertex3f(0.75, -0.75, -1)   # Esquina inferior derecha
        glVertex3f(0.75, -0.75, -2)   # Esquina superior derecha
        glVertex3f(-0.75, -0.75, -2)  # Esquina superior izquierda
        glEnd()
        glPopMatrix()
        
        
        glColor4f(0.0, 0.0, 0.0, 1.0)  # Color rojo para el rectángulo
        glPushMatrix()
        glScalef(0.7, 0.7, 0.3)  # Escala el rectángulo para hacerlo más pequeño
        glTranslatef(-0.01, -0.7, 0.2)  # Mueve el cubo hacia abajo
        glBegin(GL_QUADS)
        glVertex3f(-0.75, -0.75, -1)  # Esquina inferior izquierda
        glVertex3f(0.75, -0.75, -1)   # Esquina inferior derecha
        glVertex3f(0.75, -0.75, -2)   # Esquina superior derecha
        glVertex3f(-0.75, -0.75, -2)  # Esquina superior izquierda
        glEnd()
        glPopMatrix()
        
        

        
        

        
        
        
        
        
        

        pygame.display.flip()
        pygame.time.wait(10)

pygame.quit()