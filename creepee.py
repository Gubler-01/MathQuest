import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from PIL import Image  # Asegúrate de tener la biblioteca Pillow instalada
import tkinter as tk


class Crerper():

    def draw_cube(position, scale):
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
            
        position_variable = position
        scale_variable = scale
        glColor4f(0.0, 1.0, 0.0, 1.0)  # Color verde para el nuevo cubo
        glPushMatrix()
        #glTranslatef(0, 0, -2.5)  # Mueve el cubo hacia abajo
        glTranslatef(position[0], position[1], position[2])
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
    size *= 8  # Hacer el cubo tres veces más grande
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


    





pygame.init()
# Crea una ventana oculta (no visible) para que pygame funcione
pygame.mixer.init()
display = (600, 600)
screen = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
pygame.display.set_caption("ELCREper3.0--------para mostra info presiona e------------")

#glClearColor(0.5, 0.0, 0.5, 1.0)

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
mouseMove = [10, 10]
pygame.mouse.set_pos(displayCenter)

up_down_angle = 0.0
paused = False
run = True
show_figures = True  # Inicialmente mostrar las figuras

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


sonido = pygame.mixer.Sound('prb1.wav')
sonido2 = pygame.mixer.Sound('muerto.wav')
sonido3 = pygame.mixer.Sound('pipipi.wav')
sonido4 = pygame.mixer.Sound('Creeper.wav')
sonido5 = pygame.mixer.Sound('zombie.wav')
#sonido6 = pygame.mixer.Sound('Melancholy.wav')



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
    "playa.png",
    "left.png",
    "top.png",
    "bottom.png",
    "front.png",
    "back.png"
]

# Define las rutas a las imágenes del cubemap
cubemap_paths2 = [
    "dragon.png",
    "left.png",
    "top.png",
    "bottom.png",
    "front.png",
    "back.png"
]

# Define las rutas a las imágenes del cubemap
cubemap_paths3 = [
    "pintura.png",
    "left.png",
    "top.png",
    "bottom.png",
    "front.png",
    "back.png"
]

# Define las rutas a las imágenes del cubemap
cubemap_paths5 = [
    "nieves.png",
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
                sonido.play()
                pygame.time.wait(int(sonido.get_length() * 100))
                
            if event.key == pygame.K_h:
                show_figure_h = not show_figure_h  # Acción para la tecla "h"
                sonido5.play()
                pygame.time.wait(int(sonido.get_length() * 100))
            if event.key == pygame.K_j:
                show_figure_j = not show_figure_j  # Acción para la tecla "j"
                sonido3.play()
                pygame.time.wait(int(sonido.get_length() * 100))
            if event.key == pygame.K_m:
                show_figure_m = not show_figure_m  # Acción para la tecla "m"
            if event.key == pygame.K_n:
                show_figure_n = not show_figure_n  # Acción para la tecla "n"
            if event.key == pygame.K_b:
                show_figure_b = not show_figure_b  # Acción para la tecla "b"
                sonido4.play()
                pygame.time.wait(int(sonido.get_length() * 100))
            if event.key == pygame.K_v:
                show_figure_v = not show_figure_v  # Acción para la tecla "v"
                sonido2.play()
                pygame.time.wait(int(sonido.get_length() * 100))
            if event.key == pygame.K_y:
                #show_sound_y = not show_sound_y  # Acción para la tecla "v"
                #sonido6.play()
                pygame.time.wait(int(sonido.get_length() * 100))
            if event.key == pygame.K_u:
                #show_sound_y = not show_sound_y  # Acción para la tecla "v"
                sonido5.stop()
            if event.key == pygame.K_e:
                ventana = tk.Tk()
                ventana.title("Ventana con Texto")
                canvas = tk.Canvas(ventana, width=400, height=400)
                canvas.pack()
                # Dibuja texto en el canvas
                texto = canvas.create_text(70, 20, text="moviminetos", font=("Helvetica", 15), fill="black")
                texto = canvas.create_text(70, 40, text="h= saca la pansita", font=("Helvetica", 10), fill="black")
                texto = canvas.create_text(100, 60, text="c= hace hacia atras las orejas", font=("Helvetica", 10), fill="black")
                texto = canvas.create_text(100, 80, text="x= mueve un pie delante y uno atras", font=("Helvetica", 8), fill="black")
                texto = canvas.create_text(70, 100, text="n= levanta brazos", font=("Helvetica", 10), fill="black")
                texto = canvas.create_text(70, 120, text="z= levanta un brazo", font=("Helvetica", 10), fill="black")
                
                texto = canvas.create_text(330, 20, text="expresiones", font=("Helvetica", 15), fill="black")
                texto = canvas.create_text(300, 40, text="g=mira sospechoso(cejas)", font=("Helvetica", 10), fill="black")
                texto = canvas.create_text(300, 60, text="j=pone atencion(para orejas)", font=("Helvetica", 10), fill="black")
                texto = canvas.create_text(300, 80, text="m= guiño", font=("Helvetica", 10), fill="black")
                texto = canvas.create_text(300, 100, text="b= enjoao", font=("Helvetica", 10), fill="black")
                texto = canvas.create_text(300, 120, text="v= sorprendido", font=("Helvetica", 10), fill="black")
                
                texto = canvas.create_text(52, 170, text="sonidos", font=("Helvetica", 20), fill="black")
                texto = canvas.create_text(52, 190, text="sonido1=g", font=("Helvetica", 10), fill="black")
                texto = canvas.create_text(52, 210, text="sonido2=h", font=("Helvetica", 10), fill="black")
                texto = canvas.create_text(52, 230, text="sonido3=j", font=("Helvetica", 10), fill="black")
                texto = canvas.create_text(52, 250, text="sonido4=b", font=("Helvetica", 10), fill="black")
                texto = canvas.create_text(52, 270, text="sonido5=v", font=("Helvetica", 10), fill="black")
                texto = canvas.create_text(20, 290, text="on=y", font=("Helvetica", 10), fill="black")
                texto = canvas.create_text(20, 310, text="off=u", font=("Helvetica", 10), fill="black")
                
                texto = canvas.create_text(170, 170, text="Escenarios", font=("Helvetica", 15), fill="black")
                texto = canvas.create_text(170, 190, text="escena5k", font=("Helvetica", 10), fill="black")
                texto = canvas.create_text(170, 210, text="escena4=l", font=("Helvetica", 10), fill="black")
                texto = canvas.create_text(170, 230, text="escena3=i", font=("Helvetica", 10), fill="black")
                texto = canvas.create_text(170, 250, text="escena2=q", font=("Helvetica", 10), fill="black")
                texto = canvas.create_text(170, 270, text="escena original 1", font=("Helvetica", 10), fill="black")
                
                
                texto = canvas.create_text(330, 150, text="Camara", font=("Helvetica", 15), fill="black")
                texto = canvas.create_text(300, 180, text="w=zoom in", font=("Helvetica", 10), fill="black")
                texto = canvas.create_text(300, 200, text="s=zoom out", font=("Helvetica", 10), fill="black")
                texto = canvas.create_text(300, 220, text="a= izquierda", font=("Helvetica", 10), fill="black")
                texto = canvas.create_text(300, 240, text="d= derecha", font=("Helvetica", 10), fill="black")
                texto = canvas.create_text(300, 260, text="mouse= vista izqu", font=("Helvetica", 10), fill="black")
                texto = canvas.create_text(300, 270, text="mouse= vista derech", font=("Helvetica", 10), fill="black")
                texto = canvas.create_text(300, 280, text="mouse= vista arriba", font=("Helvetica", 10), fill="black")
                texto = canvas.create_text(300, 290, text="mouse= vista abajo", font=("Helvetica", 10), fill="black")
                
                
                # Info Desarrollador
                texto = canvas.create_text(190, 340, text="developer:", font=("Helvetica", 20), fill="black")
                texto = canvas.create_text(190, 370, text="Luis Pedro Balderas Gomez", font=("Helvetica", 15), fill="black")
                texto = canvas.create_text(190, 390, text="Graficacion3D", font=("Helvetica", 15), fill="black")

                ventana.mainloop()
                
                
            if event.key == pygame.K_c:
                show_figure_c = not show_figure_c  # Acción para la tecla "v"
                sonido2.play()
                
            if event.key == pygame.K_x:
                show_figure_x = not show_figure_x  # Acción para la tecla "v"
                sonido3.play()
                
            if event.key == pygame.K_z:
                show_figure_z = not show_figure_z  # Acción para la tecla "v"
                sonido4.play()
                
                
            if event.key == pygame.K_i:
                show_figure_i = not show_figure_i
                
            if event.key == pygame.K_l:
                show_figure_l = not show_figure_l
                
            if event.key == pygame.K_k:
                show_figure_k = not show_figure_k
                
            if event.key == pygame.K_q:
                show_figure_q = not show_figure_q
                
                
                
               
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
            
        if show_figure_i:
            
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            for i in range(6):
                glBindTexture(GL_TEXTURE_2D, cubemap_textures3[i])
                draw_cubo(2)
            
            glColor4f(0.0, 1.0, 0.0, 1.0)  # Restablece el color a verde
            

        
         
        



        
        
 




            
        if show_figures:
           
            
            Crerper.draw_cube((0,0,0), (1, 1, 1))
            draw_arm((-0.7, 0, -2.6), (0.2, 0.2, 1.0), (30, 0.0, 0.0, 1.0))
            draw_body((0, 0, -2.5), (1, 1, 1), (1, 1, 1))
            draw_arm2((0.7, 0, -2.6), (1, 1, 1), (0.0, 0.0, 1.0, 1.0))
            draw_pie((0.5, 0, -5), (1, 1, 1), (0.0, 0.0, 1.0, 1.0))
            draw_pe2((-0.5, 0, -5), (1, 1, 1), (0.0, 0.0, 1.0, 1.0))
            draw_eyes1((-0.9, -1.3, 2.0), (1, 1, 1), (0.0, 0.0, 1.0, 1.0))
            draw_eyes2((1.0, -1.3, 2.0), (1, 1, 1), (0.0, 0.0, 1.0, 1.0))
            draw_mouth((-0.01, -0.7, 0.2), (1, 1, 1), (0.0, 0.0, 1.0, 1.0))
            glColor4f(0.0, 1.0, 0.0, 1.0)  # Restablece el color a verde


               


            
            

        if show_figure_j:
           draw_arm2((0.9, 1, 1), (1, 1, 1),(1, 1, 1,1))
           draw_arm2((-0.8, 0.9, 0.9), (1, 1, 1),(0.0, 0.0, 1.0, 1.0))
           # Reproduce el sonido

    

        if show_figure_g:
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

        if show_figure_h:
           Crerper.draw_cube((-0.01, -0.5, -2.8), (0.5, 0.5, 0.5))
           glColor4f(0.0, 1.0, 0.0, 1.0)  # Restablece el color a verde
           
        if show_figure_m:
            
            show_figures = False  # Inicialmente mostrar las figuras
            Crerper.draw_cube((0,0,0), (1, 1, 1))
            draw_arm((-0.7, 0, -2.6), (0.2, 0.2, 1.0), (0, 1.0, 0.0, 1.0))
            draw_body((0, 0, -2.5), (1, 1, 1), (1, 1, 1))
            draw_arm2((0.7, 0, -2.6), (1, 1, 1), (0, 1.0, 0.0, 1.0))
            draw_pie((1.0, 1.0, 1), (1, 1, 1), (115.0, 1.0, 0.0, 0.0))
            draw_pe2((-0.9, 1.0, 1), (1, 1, 1), (115.0, 1.0, 0.0, 0.0))
            draw_eyes1((-0.9, -1.3, 2.0), (0.5, 1, 1), (0.0, 0.0, 1.0, 1.0))
            draw_eyes1((0.8, -1.3, 1.19), (1, 1.0, 0.5), (0.0, 0.0, 1.0, 1.0))
            draw_mouth((-0.01, -0.7, 0.2), (1, 1, 1), (0.0, 0.0, 1.0, 1.0))
            draw_pie((0.5, 0.6, -5), (3, 3, 5), (30, 0.0, 1.0, 1.0))
            draw_pe2((-0.4, -0.4, -5), (1, 1, 1), (45, 0.0, 1.0, 1.0))
            glColor4f(0.0, 1.0, 0.0, 1.0)  # Restablece el color a verde
        
        if show_figure_n:
            
            show_figures = False  # Inicialmente mostrar las figuras
            Crerper.draw_cube((0,0,0), (1, 1, 1))
          
            draw_body((0, 0, -2.5), (1, 1, 1), (1, 1, 1))
            draw_arm((-1.2, 0, -2.2), (0.8, 0.1, 0.2), (0,0,0,0))
            
       
            draw_pie((0.5, 0, -5), (1, 1, 1), (45.0, 1.0, 1.0, 0.0))
            draw_pe2((-0.5, 0, -5), (1, 1, 1), (45.0, 0.0, 1.0, 0.0))
            draw_eyes1((-0.9, -1.3, 2.0), (1, 1, 1), (0.0, 0.0, 1.0, 1.0))
            draw_eyes2((1.0, -1.3, 2.0), (1, 1, 1), (0.0, 0.0, 1.0, 1.0))
            draw_mouth((-0.01, -0.7, 0.2), (1, 1, 1), (0.0, 0.0, 1.0, 1.0))
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
         
        if show_figure_b:
           draw_arm2((0.9, 1, 1), (1, 1, 1),(1, 1, 1,1))
           draw_arm2((-0.8, 0.9, 0.9), (1, 1, 1),(0.0, 0.0, 1.0, 1.0))
           
           
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
            
        if show_figure_v:
            
            show_figures = False  # Inicialmente mostrar las figuras
            Crerper.draw_cube((0,0,0), (1, 1, 1))
            draw_arm((-0.7, 0, -2.6), (0.2, 0.2, 1.0), (30, 0.0, 0.0, 1.0))
            draw_body((0, 0, -2.5), (1, 1, 1), (1, 1, 1))
            draw_arm2((0.7, 0, -2.6), (1, 1, 1), (0.0, 0.0, 1.0, 1.0))
            draw_pie((0.5, 0, -5), (1, 1, 1), (0.0, 0.0, 1.0, 1.0))
            draw_pe2((-0.5, 0, -5), (1, 1, 1), (0.0, 0.0, 1.0, 1.0))
            draw_eyes1((-0.9, -1.3, 2.0), (1.0,1.0, 0.5), (0.0, 0.0, 1.0, 1.0))
            draw_eyes1((1.0, -1.3, 2.0), (1.0,1.0, 0.5), (0.0, 0.0, 1.0, 1.0))
            draw_mouth((1.5, -0.7, -1.0), (1, 1, 1), (95, 0.0, 1.0, 0.0))
            glColor4f(0.0, 1.0, 0.0, 1.0)  # Restablece el color a verde
            
        if show_figure_c:
            
            Crerper.draw_cube((0,0,0), (1, 1, 1))
            draw_arm((-0.7, 0, -2.6), (0.2, 0.2, 1.0), (30, 0.0, 0.0, 1.0))
            draw_body((0, 0, -2.5), (1, 1, 1), (1, 1, 1))
            draw_arm2((0.7, 0, -2.6), (1, 1, 1), (0.0, 0.0, 1.0, 1.0))
            draw_pie((0.5, 0, -5), (1, 1, 1), (0.0, 0.0, 1.0, 1.0))
            draw_pe2((-0.5, 0, -5), (1, 1, 1), (0.0, 0.0, 1.0, 1.0))
            draw_eyes1((-0.9, -1.3, 2.0), (1, 1, 1), (0.0, 0.0, 1.0, 1.0))
            draw_eyes2((1.0, -1.3, 2.0), (1, 1, 1), (0.0, 0.0, 1.0, 1.0))
            draw_mouth((-0.01, -0.7, 0.2), (1, 1, 1), (0.0, 0.0, 1.0, 1.0))
            draw_pie((1.0, 1.0, 1), (1, 1, 1), (115.0, 1.0, 0.0, 0.0))
            draw_pe2((-0.9, 1.0, 1), (1, 1, 1), (115.0, 1.0, 0.0, 0.0))
            glColor4f(0.0, 1.0, 0.0, 1.0)  # Restablece el color a verde
            
        if show_figure_x:
            
            show_figures = False  # Inicialmente mostrar las figuras
            Crerper.draw_cube((0,0,0), (1, 1, 1))
            draw_arm((-0.7, 0, -2.6), (0.2, 0.2, 1.0), (30, 0.0, 0.0, 1.0))
            draw_body((0, 0, -2.5), (1, 1, 1), (1, 1, 1))
            draw_arm2((0.7, 0, -2.6), (1, 1, 1), (0.0, 0.0, 1.0, 1.0))
            draw_pie((0.5, 0.6, -5), (3, 3, 5), (30, 0.0, 1.0, 1.0))
            draw_pe2((-0.4, -0.4, -5), (1, 1, 1), (45, 0.0, 1.0, 1.0))
            draw_eyes1((-0.9, -1.3, 2.0), (1, 1, 1), (0.0, 0.0, 1.0, 1.0))
            draw_eyes2((1.0, -1.3, 2.0), (1, 1, 1), (0.0, 0.0, 1.0, 1.0))
            draw_mouth((-0.01, -0.7, 0.2), (1, 1, 1), (0.0, 0.0, 1.0, 1.0))
            glColor4f(0.0, 1.0, 0.0, 1.0)  # Restablece el color a verde
            
        if show_figure_z:
            show_figures = False  # Inicialmente mostrar las figuras
            
            Crerper.draw_cube((0,0,0), (1, 1, 1))
          
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
        



                
            
            

            
            

            

        glPopMatrix()

        pygame.display.flip()
        pygame.time.wait(10)

pygame.quit()
