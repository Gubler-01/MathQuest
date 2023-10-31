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

from crep import *
from crep import Dibujar
from button import Button
from crep import *
from poke import Pintamos
from poke import *

dibujamos=Dibujar()
pinatmos=Pintamos()
android = Android()


confirmed_number = None

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


confirmed_number = None


def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

def instrucctions():
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
    

def play():
    pygame.quit()  # Cierra la ventana Pygame 2D
    
    
        # Color inicial de la flecha (rojo)
        
    arrow_color = [1.0, 0.0, 0.0, 1.0]
    arrow_color_2 = [1.0, 0.0, 0.0, 1.0]
    arrow_color_3 = [1.0, 0.0, 0.0, 1.0]
    

    def draw_arrow(color,posisi):
        # Dibuja una flecha hacia el cubo
        glPushMatrix()
        glTranslate(posisi, 0, 2.0)  # Ajusta la posición de la flecha en el eje Z
        glScalef(2.0, 2.0, 2.0)  # Escala la flecha
        glRotatef(90, 1.0, 0.0, 0.0)  # Apunta hacia el cubo
        glColor4fv(color)  # Color de la flecha # Color rojo para la flecha
        glBegin(GL_TRIANGLES)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(-0.2, 0.4, 0.0)
        glVertex3f(0.2, 0.4, 0.0)
        glEnd()
        glPopMatrix()
 
    
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
    glLightfv(GL_LIGHT0, GL_AMBIENT, [0.9, 0.9, 0.9, 1])
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0, 1.0, 1.0, 1])

    sphere = gluNewQuadric()

    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

    glMatrixMode(GL_MODELVIEW)
    gluLookAt(0, -16, 0, 0, 0, 0, 0, 0, 1)  # Ajusta la posición de la cámara

    viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)
    glLoadIdentity()

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

    #yo
    show_figure_y = False
    show_figure_u = False
    show_figure_i = False
    
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

    cubemap_paths8 = [
    "./images/fondo1.png"
    ]
    cubemap_paths9 = [
        "./images/fondo2.png"
    ]
    cubemap_paths10 = [
        "./images/fondo3.png"
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
    cubemap_textures8 = [load_texture(filename) for filename in cubemap_paths8]
    cubemap_textures9 = [load_texture(filename) for filename in cubemap_paths9]
    cubemap_textures10 = [load_texture(filename) for filename in cubemap_paths10]

    
    translate_speed = 0.05  # Puedes ajustar la velocidad
    translate_x = -7
    
    
    # Variable para rastrear si se presionó la tecla "1"
    key_1_pressed = False
    key_2_pressed= False
    key_3_pressed= False
    
    
    # Variables para el número seleccionado y la confirmación
    
    selected_number = None
    
    
    
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
                    run = False
                if event.key == pygame.K_PAUSE or event.key == pygame.K_p:
                    paused = not paused
                    
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
                    
                if event.key == pygame.K_x:
                    show_figure_x = not show_figure_x  # Acción para la tecla "n"
                    sonido8.play()
                    
                if event.key == pygame.K_c:
                    show_figure_c = not show_figure_c  # Acción para la tecla "n"
                    sonido8.play()
                    
                    
                if event.key == pygame.K_v:
                    show_figure_v = not show_figure_v
                    sonido8.play()
                    show_figure_t=False
                    
                if event.key == pygame.K_o:
                    show_figure_o = not show_figure_o
                    sonido7.play()
                    
                #richi
                    
                if event.key == pygame.K_b:
                    show_figure_b = not show_figure_b
                    show_figure_l = not show_figure_l
                    sonido8.play()
                    
                if event.key == pygame.K_n:
                    show_figure_n = not show_figure_n
                    
                    sonido8.play()
                    
                if event.key == pygame.K_m:
                    show_figure_m = not show_figure_m
                    sonido8.play()
                    
                if event.key == pygame.K_j:
                    show_figure_j = not show_figure_j
                    show_figure_k = not show_figure_k
                    sonido8.play()
                    
                #yo

                if event.key == pygame.K_y:
                    show_figure_y = not show_figure_y
                if event.key == pygame.K_u:
                    show_figure_u = not show_figure_u

                if event.key == pygame.K_i:        
                    show_figure_i = not show_figure_i
                    
                    
                if event.key == pygame.K_1:
                    # Cambiar el color de la flecha a verde
                    arrow_color = [0.0, 1.0, 0.0, 1.0]
                    arrow_color_2 = [1.0, 0.0, 0.0, 1.0]
                    arrow_color_3 = [1.0, 0.0, 0.0, 1.0]
                    key_1_pressed = True
                    key_2_pressed= False
                    key_3_pressed = False
                    selected_number = 1
                    
                    
                if event.key == pygame.K_2:
                    # Cambiar el color de la flecha a verde
                    
                    arrow_color = [1.0, 0.0, 0.0, 1.0]
                    arrow_color_2 = [0.0, 1.0, 0.0, 1.0]
                    arrow_color_3 = [1.0, 0.0, 0.0, 1.0]
                    key_2_pressed= True
                    key_1_pressed = False
                    key_3_pressed = False
                    selected_number = 2
                    
                if event.key == pygame.K_3:
                    # Cambiar el color de la tercera flecha a verde y las otras a rojo
                    arrow_color = [1.0, 0.0, 0.0, 1.0]
                    arrow_color_2 = [1.0, 0.0, 0.0, 1.0]
                    arrow_color_3 = [0.0, 1.0, 0.0, 1.0]
                    key_1_pressed = False
                    key_2_pressed = False
                    key_3_pressed = True
                    selected_number = 3
                  
                  
                if event.key == pygame.K_r:
                    if selected_number is not None and arrow_color == [0.0, 1.0, 0.0, 1.0]:
                        # Confirmar la selección y almacenar el número en la variable de confirmación
                                # Imprime el valor confirmado en la consola
                        
                        confirmed_number = selected_number
                        print("Número confirmado:", confirmed_number)
                        
                    elif arrow_color_2 == [0.0, 1.0, 0.0, 1.0]:
                        confirmed_number = selected_number
                        print("Número confirmado:", confirmed_number)
                        
                    elif arrow_color_3 == [0.0, 1.0, 0.0, 1.0]:
                        confirmed_number = selected_number
                        print("Número confirmado:", confirmed_number)
                        
                    selected_number = None  # Restablecer la selección   
                    

        if not paused:
            keypress = pygame.key.get_pressed()
            glLoadIdentity()
            up_down_angle = 0.0
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
            
            glMultMatrixf(viewMatrix)
            viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)
            
            glPopMatrix()
            glMultMatrixf(viewMatrix)
            glLightfv(GL_LIGHT0, GL_POSITION, [5, -3, 7, 0])
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
                 # Llama a la función para dibujar la flecha
               draw_arrow(arrow_color,0)
               draw_arrow(arrow_color_2,7.1)
               draw_arrow(arrow_color_3,-7.1)

                #creper
               Dibujar.draw_cube((0, 0, 0), (1, 1, 1))
               Dibujar.draw_arm((-0.7, 0, -2.6), (0.2, 0.2, 1.0), (30, 0.0, 0.0, 1.0))
               Dibujar.draw_body((0, 0, -2.5), (1, 1, 1), (1, 1, 1))
               Dibujar.draw_arm2((0.7, 0, -2.6), (1, 1, 1), (0.0, 0.0, 1.0, 1.0))
               Dibujar.draw_pie((0.5, 0, -5), (1, 1, 1), (0.0, 0.0, 1.0, 1.0))
               Dibujar.draw_pe2((-0.5, 0, -5), (1, 1, 1), (0.0, 0.0, 1.0, 1.0))
               Dibujar.draw_eyes1((-0.9, -1.3, 2.0), (1, 1, 1), (0.0, 0.0, 1.0, 1.0))
               Dibujar.draw_eyes2((1.0, -1.3, 2.0), (1, 1, 1), (0.0, 0.0, 1.0, 1.0))
               Dibujar.draw_mouth((-0.01, -0.7, 0.2), (1, 1, 1), (0.0, 0.0, 1.0, 1.0))
               #fincreper
               
               
               #pokemon
               glColor4f(1.0, 1.0, 0.0, 1.0)
               pinatmos.ojo1((-0.2 - translate_x, -1, 0.3), (.2, .1, .2))
               pinatmos.ojo2((0.4 - translate_x, -1, 0.3), (.2, .1, .2))
               pinatmos.draw_smile_mouth(.5, (.1 - translate_x, -1, -0.1), 0, pi, 100)
               # Dibuja el cuerpo de Pokemon
               glTranslatef(-translate_x, 0, 0)
               pinatmos.draw_half_spheres(1.0, 20, 20)
               pinatmos.draw_half_sphere_lower(1.0, 20, 20)
                #finpoke

               glPushMatrix()
               glTranslatef(-14.1, -2.5, 0)
               glRotate(90, 1,0,0)
               glRotate(90, 0,1,0)
               glScale(2.5, 2.5, 2.5)
               android.DrawCabeza()
               android.DrawCuerpo()
               android.DrawUniones()
               android.DrawManoder()
               android.DrawManoizq()
               android.DrawPieder()
               android.DrawPieizq()
               glPopMatrix()

                            # Dibujar texto en la escena
               glTranslatef(0.0, 0.0, 3)
               render_text("1", -5, 2.0)            # Mover arriba a 1.2
                
               render_text("2", 1.5, 2.0)            # Mover arriba a 1.2

               render_text("3", -13.5, 2.0)            # Mover arriba a 1.2



             # Renderiza el texto si se presionó la tecla "1"
            if key_1_pressed:
                render_text("El Creepr3000",-5, 2.0)  # Personaliza los valores según tu función
                glTranslatef(0.0, 0.0, -2)
                render_text("Movimientos: z,x,c,v",-5, 2.0) 
                if show_figure_z:
                    #creper
                    show_figures = False  # Inicialmente mostrar las figuras
                    Dibujar.draw_cube((0,0,0), (1, 1, 1))
                    Dibujar.draw_body((0, 0, -2.5), (1, 1, 1), (1, 1, 1))
                    Dibujar.draw_pie((0.5, 0, -5), (1, 1, 1), (0.0, 0.0, 1.0, 1.0))
                    Dibujar.draw_pe2((-0.5, 0, -5), (1, 1, 1), (0.0, 0.0, 1.0, 1.0))
                    Dibujar.draw_eyes1((-0.9, -1.3, 2.0), (1, 1, 1), (0.0, 0.0, 1.0, 1.0))
                    Dibujar.draw_eyes2((1.0, -1.3, 2.0), (1, 1, 1), (0.0, 0.0, 1.0, 1.0))
                    Dibujar.draw_mouth((-0.01, -0.7, 0.2), (1, 1, 1), (0.0, 0.0, 1.0, 1.0))
                    Dibujar.draw_eyes1((-0.9, -1.3, 2.0), (1.0,1.0, 0.5), (0.0, 0.0, 1.0, 1.0))
                    Dibujar.draw_eyes1((1.0, -1.3, 2.0), (1.0,1.0, 0.5), (0.0, 0.0, 1.0, 1.0))
                    Dibujar.draw_mouth((1.5, -0.7, -1.0), (1, 1, 1), (95, 0.0, 1.0, 0.0))
                    Dibujar.draw_arm((-1.2, 0, -2.2), (0.8, 0.1, 0.2), (0,0,0,0))
                    Dibujar.draw_arm2((0.7, 0, -2.6), (1, 1, 1), (0.0, 0.0, 1.0, 1.0))
                    Dibujar.draw_pie((1.0, 1.0, 1), (1, 1, 1), (115.0, 1.0, 0.0, 0.0))
                    Dibujar.draw_pe2((-0.9, 1.0, 1), (1, 1, 1), (115.0, 1.0, 0.0, 0.0))
                    
                    glColor4f(0.0, 1.0, 0.0, 1.0)  # Restablece el color a verde
                
                if show_figure_x:
                    #creper
                    show_figure_t=True
                    show_figures = False  # Inicialmente mostrar las figuras
                    Dibujar.draw_cube((0,0,0), (1, 1, 1))
                    Dibujar.draw_cejas()
                    Dibujar.draw_body((0, 0, -2.5), (1, 1, 1), (1, 1, 1))
                    Dibujar.draw_arm((-1.2, 0, -2.2), (0.8, 0.1, 0.2), (0,0,0,0))
                    Dibujar.draw_pie((0.5, 0, -5), (1, 1, 1), (45.0, 1.0, 1.0, 0.0))
                    Dibujar.draw_pe2((-0.5, 0, -5), (1, 1, 1), (45.0, 0.0, 1.0, 0.0))
                    Dibujar.draw_eyes1((-0.9, -1.3, 2.0), (0.3, 1, 1), (0.0, 0.0, 1.0, 1.0))
                    Dibujar.draw_eyes1((1.0, -1.3, 2.0), (0.3, 1, 1), (0.0, 0.0, 1.0, 1.0))
                    glColor4f(0.0, 1.0, 0.0, 1.0)  # Restablece el color a verde
                    Dibujar.draw_exp1()

                if show_figure_c:
                    #creper
                    show_figure_k=True
                    show_figure_t=False
                    show_figures = False  # Inicialmente mostrar las figuras
                    Dibujar.draw_cube((0,0,0), (1, 1, 1))
                    Dibujar.draw_arm((-0.7, 0, -2.6), (0.2, 0.2, 1.0), (0, 1.0, 0.0, 1.0))
                    Dibujar.draw_body((0, 0, -2.5), (1, 1, 1), (1, 1, 1))
                    Dibujar.draw_arm((1.2, 0, -2.2), (0.8, 0.1, 0.2), (0,0,0,0))
                    Dibujar.draw_pie((1.0, 1.0, 1), (1, 1, 1), (115.0, 1.0, 0.0, 0.0))
                    Dibujar.draw_pe2((-0.9, 1.0, 1), (1, 1, 1), (115.0, 1.0, 0.0, 0.0))
                    Dibujar.draw_eyes1((-0.9, -1.3, 2.0), (0.5, 1, 1), (0.0, 0.0, 1.0, 1.0))
                    Dibujar.draw_eyes1((0.8, -1.3, 1.19), (1, 1.0, 0.5), (0.0, 0.0, 1.0, 1.0))
                    Dibujar.draw_mouth((-0.01, -0.7, 0.2), (1, 1, 1), (0.0, 0.0, 1.0, 1.0))
                    Dibujar.draw_pie((0.5, 0.6, -5), (3, 3, 5), (30, 0.0, 1.0, 1.0))
                    Dibujar.draw_pe2((-0.4, -0.4, -5), (1, 1, 1), (45, 0.0, 1.0, 1.0))
                    Dibujar.draw_cejas()
                    glColor4f(0.0, 1.0, 0.0, 1.0)  # Restablece el color a verde
            
                if show_figure_v:
                    #creper
                    show_figure_k=False
                    show_figure_q=True
                    show_figures=False
                    Dibujar.draw_cube((0, 0, 0), (1, 1, 1))
                    Dibujar.draw_arm((-0.7, 0, -2.6), (0.2, 0.2, 1.0), (30, 0.0, 0.0, 1.0))
                    Dibujar.draw_body((0, 0, -2.5), (1, 1, 1), (1, 1, 1))
                    Dibujar.draw_arm2((0.7, 0, -2.6), (1, 1, 1), (0.0, 0.0, 1.0, 1.0))
                    Dibujar.draw_pie((0.5, 0, -5), (1, 1, 1), (0.0, 0.0, 1.0, 1.0))
                    Dibujar.draw_pe2((-0.5, 0, -5), (1, 1, 1), (0.0, 0.0, 1.0, 1.0))

                    Dibujar.draw_arm2((0.9, 1, 1), (1, 1, 1),(1, 1, 1,1))
                    Dibujar.draw_arm2((-0.8, 0.9, 0.9), (1, 1, 1),(0.0, 0.0, 1.0, 1.0))
                    Dibujar.draw_exp2()
                    Dibujar.draw_cube((-0.01, -0.5, -2.8), (0.5, 0.5, 0.5))
                    glColor4f(0.0, 1.0, 0.0, 1.0)  # Restablece el color a verde
                    Dibujar.draw_eyes1((-0.9, -1.3, 2.0), (1.0,1.0, 0.5), (0.0, 0.0, 1.0, 1.0))
                    Dibujar.draw_eyes1((1.0, -1.3, 2.0), (1.0,1.0, 0.5), (0.0, 0.0, 1.0, 1.0))
                    Dibujar.draw_mouth((1.5, -0.7, -1.0), (1, 1, 1), (95, 0.0, 1.0, 0.0))

           

            if key_2_pressed:
                
                render_text("pokemon",3.0, 2.0)  # Personaliza los valores según tu función
                glTranslatef(0.0, 0.0, -2)
                render_text("Movimientos: b,n,m",3.0, 2.5)
                if show_figure_b:
                    glColor4f(1.0, 1.0, 0.0, 1.0)
                    pinatmos.ojo1((-0.2 - translate_x, -1, 0.3), (.2, .1, .2))
                    pinatmos.ojo2((0.4 - translate_x, -1, 0.3), (.2, .1, .2))
                    pinatmos.draw_smile_mouth(.5, (.1 - translate_x, -1, -0.1), 0, pi, 100)
                    glColor4f(0.0, 0.4, 1.0, 0.3)
                    glTranslatef(-translate_x, 0, 0)
                    pinatmos.draw_half_spheres(1.0, 20, 20)
                    pinatmos.draw_half_sphere_lower(1.0, 20, 20)
                    glPushMatrix()
                    show_figures=False
                    glColor3f(0.0, 0.0, 0.0)  # Color gris claro
                    glTranslate(1, -1.4, 1)  # Ajustar la posición de la punta del pico
                    pinatmos.draw_pickaxe_tip(0.5, 1.5)  # Especificar radio y altura
                    glPopMatrix()
                    glPushMatrix()
                    glColor3f(0.6, 0.3, 0.0)  # Color marrón
                    glTranslate(1, -1.4, 1)  # Ajustar la posición del palo del pico
                    pinatmos.draw_pickaxe_handle(1.8, 0.2, 10.0)  # Especificar longitud, ancho y profundidad
                    glPopMatrix()
                    
                if show_figure_n:
                    show_figures=False
                    show_figure_t=True
                    glColor4f(1.0, 1.0, 0.0, 1.0)
                    pinatmos.ojo1((-0.2 - translate_x, -1, 0.3), (.2, .1, .2))
                    pinatmos.ojo2((0.4 - translate_x, -1, 0.3), (.2, .1, .2))
                    pinatmos.draw_smile_mouth(.5, (.1 - translate_x, -1, -0.1), 0, pi, 100)
                    glColor4f(0.0, 0.4, 1.0, 0.3)
                    glTranslatef(-translate_x, 0, 0)
                    pinatmos.draw_half_spheres(1.0, 20, 20)
                    pinatmos.draw_half_sphere_lower(1.0, 20, 20)
                    glColor4f(0.0, 0.4, 1.0, 0.3)
                    pinatmos.mano((1,-0.6,-0.2), (.1, .7, .1))

                if show_figure_m:
                    show_figure_i=True
                    show_figure_t=False
                    show_figures=False
                    glColor4f(1.0, 1.0, 0.0, 1.0)
                    pinatmos.ojo1((-0.2 - translate_x, -1, 0.3), (.2, .1, .2))
                    pinatmos.ojo2((0.4 - translate_x, -1, 0.3), (.2, .1, .2))
                    pinatmos.draw_smile_mouth(.5, (.1 - translate_x, -1, -0.1), 0, pi, 100)
                    glColor4f(0.0, 0.4, 1.0, 0.3)
                    glTranslatef(-translate_x, 0, 0)
                    pinatmos.draw_half_spheres(1.0, 20, 20)
                    pinatmos.draw_half_sphere_lower(1.0, 20, 20)
                    glColor4f(0.0, 0.4, 1.0, 0.3)
                    pinatmos.draw_smile_mouth1(.3, (.1, -1.02, -.3), 0, pi, 100)

                if show_figure_j:
                    show_figures=False
                    glColor4f(1.0, 1.0, 0.0, 1.0)
                    pinatmos.ojo1((-0.2 - translate_x, -1, 0.3), (.2, .1, .2))
                    pinatmos.ojo2((0.4 - translate_x, -1, 0.3), (.2, .1, .2))
                    pinatmos.draw_smile_mouth(.5, (.1 - translate_x, -1, -0.1), 0, pi, 100)
                    glColor4f(0.0, 0.4, 1.0, 0.3)
                    glTranslatef(-translate_x, 0, 0)
                    pinatmos.draw_half_spheres(1.0, 20, 20)
                    pinatmos.draw_half_sphere_lower(1.0, 20, 20)
                    glColor4f(0.0, 0.4, 1.0, 0.3)
                    glColor4f(0.0, 0, 0, 0)
                    pinatmos.mano((0.54,-0.9,0.67), (.3, 0.1, .1))
                    pinatmos.mano((-0.34,-0.9,0.67), (.3, 0.1, .1))
                    glColor3f(0.0, 0.0, 1.0)  # Color gris claro
                    glTranslate(0, 0, .9)  # Ajustar la posición de la punta del pico
                    pinatmos.draw_pickaxe_tip(0.5, 1.5)  # Especificar radio y altura

            if key_3_pressed:
                render_text("android",-13, 2.0)  # Personaliza los valores según tu función
                glTranslatef(0.0, 0.0, -1)
                render_text("Movimientos: y,u,i",-13.5, 2.0)
                if show_figure_y:
                    #show_figures=False

                    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
                    for i in range(1):
                        glBindTexture(GL_TEXTURE_2D, cubemap_textures8[i])
                        draw_cubo(2)
                    
                    glColor4f(0.0, 1.0, 0.0, 1.0)  # Restablece el color a verde

                    glPushMatrix()
                    glTranslatef(-7, -6, -2)
                    glRotate(90, 1,0,0)
                    glRotate(90, 0,1,0)
                    glScale(3, 3, 3)
                    android.feli()
                    android.DrawCuerpo()
                    android.DrawUniones()
                    android.DrawManoder()
                    android.DrawManoizq()
                    android.DrawPieder()
                    android.DrawPieizq()
                    glPopMatrix()

                if show_figure_u:
                    #show_figures=False

                    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
                    for i in range(1):
                        glBindTexture(GL_TEXTURE_2D, cubemap_textures9[i])
                        draw_cubo(2)
                    
                    glColor4f(0.0, 1.0, 0.0, 1.0)  # Restablece el color a verde

                    glPushMatrix()
                    glTranslatef(-7, -6, -2)
                    glRotate(90, 1,0,0)
                    glRotate(90, 0,1,0)
                    glScale(3, 3, 3)
                    android.duda()
                    android.DrawCuerpo()
                    android.DrawUniones()
                    android.levBrazo()
                    android.DrawManoizq()
                    android.DrawPieder()
                    android.DrawPieizq()
                    glPopMatrix()

                if show_figure_i:
                    #show_figures=False

                    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
                    for i in range(1):
                        glBindTexture(GL_TEXTURE_2D, cubemap_textures10[i])
                        draw_cubo(2)
                    
                    glColor4f(0.0, 1.0, 0.0, 1.0)  # Restablece el color a verde

                    glPushMatrix()
                    glTranslatef(-7, -6, -2)
                    glRotate(90, 1,0,0)
                    glRotate(90, 0,1,0)
                    glScale(3, 3, 3)
                    android.llorar()
                    android.DrawCuerpo()
                    android.DrawUniones()
                    android.DrawManoder()
                    android.DrawManoizq()
                    android.DrawPieder()
                    android.DrawPieizq()
                    glPopMatrix()


            glTranslatef(0.0, 0.0, 3)
            render_text("Para elegir escoja de acuerdo al numero", -13, 2.0)            # Mover arriba a 1.2
            

            glTranslatef(0.0, 0.0, -8)
            # Renderiza el texto si se presionó la tecla "1"
            if selected_number is not None:
                render_text(f"Seleccionado: {selected_number}", -7.5, -6.0)  # Personaliza los valores según tu función
     
                
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
                            text_input="Jugar", font=get_font(65), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400),
                            text_input="Instrucciones", font=get_font(45), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550),
                            text_input="Salir", font=get_font(65), base_color="#d7fcd4", hovering_color="White")

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
                    instrucctions()  # Llama a la función de opciones 3D
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()