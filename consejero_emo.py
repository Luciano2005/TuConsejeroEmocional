import webbrowser
import random #Modulo para seleccionar las preguntas de forma aleatoria
from kivy.lang import Builder
from kivymd.app import MDApp    #Importamos a KivyMD
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, FallOutTransition, SlideTransition, SwapTransition #Manejo de pantallas y transiciones
from kivy.uix.scrollview import ScrollView #Vista Scroll
from kivymd.uix.gridlayout import MDGridLayout




Window.size = (300, 600) #Tamaño de pantalla

#--------------------------------------------------------------------------------
#                       Algoritmo de las preguntas
#--------------------------------------------------------------------------------

#Definición de variables que van a llevar el puntaje según el tipo de pregunta
puntaje_emo = 0
puntaje_plazo = 0
puntaje_sociales = 0
puntaje_actividad = 0
puntaje_generales = 0

aparicion = 0

#Funciones de asignación de puntos
def puntos_emo(valor):  #Asignación de puntos para las preguntas emocionales
    global puntaje_emo
    if valor == respuestas_emocionales['respuesta1']:
        puntaje_emo = 10
        return puntaje_emo
    elif valor == respuestas_emocionales['respuesta2']:
        puntaje_emo = 8
        return puntaje_emo
    elif valor == respuestas_emocionales['respuesta3']:
        puntaje_emo = 6
        return puntaje_emo
    elif valor == respuestas_emocionales['respuesta4']:
        puntaje_emo = 4
        return puntaje_emo
    else:
        puntaje_emo = 2
        return puntaje_emo


def puntos_plazo(valor):    #Asignación puntos, preguntas a largo plazo
    global puntaje_plazo
    if valor == respuestas_plazo['respuesta1']:
        puntaje_plazo = 10
        return puntaje_plazo
    elif valor == respuestas_plazo['respuesta2']:
        puntaje_plazo = 8
        return puntaje_plazo
    elif valor == respuestas_plazo['respuesta3']:
        puntaje_plazo = 6
        return puntaje_plazo
    elif valor == respuestas_plazo['respuesta4']:
        puntaje_plazo = 4
        return puntaje_plazo
    else:
        puntaje_plazo = 2
        return puntaje_plazo


def puntos_sociales(valor): #Asignación puntos, preguntas sociales
    global puntaje_sociales
    if valor == Respuestas_Sociales['respuesta1']:
        puntaje_sociales = 10
        return puntaje_sociales
    elif valor == Respuestas_Sociales['respuesta2']:
        puntaje_sociales = 8
        return puntaje_sociales
    elif valor == Respuestas_Sociales['respuesta3']:
        puntaje_sociales = 6
        return puntaje_sociales
    elif valor == Respuestas_Sociales['respuesta4']:
        puntaje_sociales = 4
        return puntaje_sociales
    else:
        puntaje_sociales = 2
        return puntaje_sociales


def puntos_actividad(valor):    #Asignación puntos, preguntas de actividad
    global puntaje_actividad
    if valor == Respuestas_Actividad['respuesta1']:
        puntaje_actividad = 10
        return puntaje_actividad
    elif valor == Respuestas_Actividad['respuesta2']:
        puntaje_actividad = 8
        return puntaje_actividad
    elif valor == Respuestas_Actividad['respuesta3']:
        puntaje_actividad = 6
        return puntaje_actividad
    elif valor == Respuestas_Actividad['respuesta4']:
        puntaje_actividad = 4
        return puntaje_actividad
    else:
        puntaje_actividad = 2
        return puntaje_actividad


def puntos_generales(valor): #Asignación puntos, preguntas generales
    global puntaje_generales
    if valor == Respuestas_Generales['respuesta1']:
        puntaje_generales = 10
        return puntaje_generales
    elif valor == Respuestas_Generales['respuesta2']:
        puntaje_generales = 8
        return puntaje_generales
    elif valor == Respuestas_Generales['respuesta3']:
        puntaje_generales = 6
        return puntaje_generales
    elif valor == Respuestas_Generales['respuesta4']:
        puntaje_generales = 4
        return puntaje_generales
    else:
        puntaje_generales = 2
        return puntaje_generales


#Llamado de funciones por tipo de pregunta (Funciona en la consola, pero aún no lo hemos implementado en kivy)
def llamado_puntos(pregunta, respuesta): #Decide qué tipo de función llamar según el tipo de pregunta que se esté respondiendo
    if pregunta in preguntas_emocionales.values(): 
        return puntos_emo(respuesta) #Llama a otra función para que asigne el valor a la respuesta seleccionada por el usuario
    elif pregunta in preguntas_plazo.values():
        return puntos_plazo(respuesta)
    elif pregunta in Preguntas_Sociales.values():
        return puntos_sociales(respuesta)
    elif pregunta in Preguntas_Actividad.values():
        return puntos_actividad(respuesta)
    else:
        return puntos_generales(respuesta)


#Función anula puntos (no es muy util)
def anula_puntos(pregunta): #Reinicia una opción de pregunta cuando es deseleccionada (esto es para los checkbox de kivy)
    if pregunta in preguntas_emocionales.values():
        global puntaje_emo
        puntaje_emo = 0
        
    elif pregunta in Preguntas_Generales.values():
        global puntaje_generales
        puntaje_generales = 0 
    elif pregunta in preguntas_plazo.values():
        global puntaje_plazo 
        puntaje_plazo = 0
    elif pregunta in Preguntas_Sociales.values():
        global puntaje_sociales 
        puntaje_sociales = 0
    elif pregunta in Preguntas_Actividad.values():
        global puntaje_actividad
        puntaje_actividad = 0 



#Preguntas
preguntas_emocionales = {
    'pregunta1': '¿Te sientes satisfecho contigo mismo?',
    'pregunta2' : '¿Has sentido tristeza sin razón alguna?',
    'pregunta3' : '¿En los últimos días, hubo momentos en los que te sentiste feliz y con esperanza?',
    'pregunta4' : '¿Sientes que las personas de tu alrededor te apoyan?',
    'pregunta5' : '¿A diario, crees que tu felicidad la define tu entorno?', 
}
preguntas_plazo = {
    'pregunta1': '¿Tienes metas claras?',
    'pregunta2' : '¿Sientes que puedes lograr tus sueños?',
    'pregunta3' : '¿Crees que la carrera que escogiste es la correcta?',
    'pregunta4' : '¿Sientes que tu futuro depende solo de ti?',
    'pregunta5' : '¿Aprovechas el tiempo?', 
}
Preguntas_Sociales = {
    "pregunta1":"¿Estas satisfecho con tu circulo social en este momento?",
    "pregunta2":"¿Consideras que tus relaciones sociales son sanas y te aportan positivamente?",
    "pregunta3":"¿Consideras que tienes dificultades para relacionarte o expresarte?",
    "pregunta4":"¿Sientes que eres libre de expresarte con tu nucleo familiar cercano?",
    "pregunta5":"¿Sientes que eres libre de expresarte con tus amigos en general?"
}
Preguntas_Actividad = {
    "pregunta1":"¿Lograste cumplir tus tareas u oficios diarios?",
    "pregunta2":"¿Sientes que implementaste correctamente tu tiempo durante la semana?",
    "pregunta3":"¿Completaste los trabajos y proyectos correspondientes a esta semana?",
    "pregunta4":"¿Sientes que organizas correctamente tu tiempo?",
    "pregunta5":"¿Tuviste tiempo de ocio y esparcimiento esta semana?"
}
Preguntas_Generales = {
    "pregunta1":"¿Como te has sentido esta semana?",
    "pregunta2":"¿Como te ha ido hoy?",
    "pregunta3":"¿Conforme a cómo te has desempeñado estos últimos días, como te sientes?",
    "pregunta4":"¿Conforme a tu estado mental en este momento, como te sientes?",
    "pregunta5":"¿Respecto a tu capacidad para hablar con personas de tu confianza, acerca de tus problemas, como te sientes?"
}

#Respuestas
respuestas_emocionales = {
    'respuesta1': 'Siempre',
    'respuesta2': 'A veces',
    'respuesta3': 'Muy pocas veces',
    'respuesta4': 'Casi nunca',
    'respuesta5': 'Definitivamente no', 
}
respuestas_plazo = {
    'respuesta1': 'Si',
    'respuesta2' : 'No estoy muy seguro aún',
    'respuesta3' : 'Estoy en el proceso de descubrirlo',
    'respuesta4' : 'Estoy trabajando en ello',
    'respuesta5' : 'Definitivamente no'
}
Respuestas_Sociales = {
    "respuesta1":"Definitivamente sí",
    "respuesta2":"Se podría decir que sí",
    "respuesta3":"No estoy seguro / Entre sí y no",
    "respuesta4":"Realmente no",
    "respuesta5":"Definitivamente no"
}
Respuestas_Actividad = {
    "respuesta1":"Si, completamente",
    "respuesta2":"Se podría decir que sí",
    "respuesta3":"Sí pero no (De manera no constante o irregular)",
    "respuesta4":"No completamente",
    "respuesta5":"Definitivamente no"
}
Respuestas_Generales = {
    'respuesta1': "Excelente",
    'respuesta2': "Bien",
    'respuesta3': "Regular",
    'respuesta4': "Mal",
    'respuesta5': "Horrible"
}

#Definición de listas donde se almacenan las 5 preguntas que serán mostradas en pantalla.
#Se usaron listas anidadas para hacer más dinamica la muestra de pregunta-respuestas a la vez

preguntas = [[[random.choice(list(preguntas_emocionales.values()))], list(respuestas_emocionales.values())], #La lista que contiene el modulo ramdom está anidada dentro de otra lista previamente anidada para que no se tome como cadena de caracteres en el bucle for de más abajo (Fue algo que costó tiempo de encontrar XD). Lo mismo fue aplicado para las otras preguntas.
            [[random.choice(list(preguntas_plazo.values()))], list(respuestas_plazo.values())], 
            [[random.choice(list(Preguntas_Sociales.values()))], list(Respuestas_Sociales.values())],
            [[random.choice(list(Preguntas_Actividad.values()))], list(Respuestas_Actividad.values())],
            [[random.choice(list(Preguntas_Generales.values()))], list(Respuestas_Generales.values())]]



#---------------------------------------------------------------------------------
#                       CODIGO KIVY-PYTHON (Clases y métodos)
#---------------------------------------------------------------------------------

colors = { #Cambio de colores de tema predeterminados de kivyMD por los colores del prototipo hecho en Figma.
    "Teal": {
        "50": "e4f8f9",
        "100": "bdedf0",
        "200": "97e2e8",
        "300": "79d5de",
        "400": "6dcbd6",
        "500": "6ac2cf",
        "600": "63b2bc",
        "700": "5b9ca3",
        "800": "54888c",
        "900": "486363",
        "A100": "bdedf0",
        "A200": "97e2e8",
        "A400": "6dcbd6",
        "A700": "5b9ca3",
    },
    "Blue": {
        "50": "e3f3f8",
        "100": "b9e1ee",
        "200": "91cee3",
        "300": "72bad6",
        "400": "62acce",
        "500": "589fc6",
        "600": "5191b8",
        "700": "487fa5",
        "800": "426f91",
        "900": "35506d",
        "A100": "b9e1ee",
        "A200": "91cee3",
        "A400": "62acce",
        "A700": "487fa5",
    },
    "Red": {
        "50": "FFEBEE",
        "100": "FFCDD2",
        "200": "EF9A9A",
        "300": "E57373",
        "400": "EF5350",
        "500": "F44336",
        "600": "E53935",
        "700": "D32F2F",
        "800": "C62828",
        "900": "B71C1C",
        "A100": "FF8A80",
        "A200": "FF5252",
        "A400": "FF1744",
        "A700": "D50000",
    },
    "Light": {
        "StatusBar": "E0E0E0",
        "AppBar": "F5F5F5",
        "Background": "FAFAFA",
        "CardsDialogs": "FFFFFF",
        "FlatButtonDown": "cccccc",
    },
    "Dark": {
        "StatusBar": "000000",
        "AppBar": "212121",
        "Background": "232827", #Se cambió el negro por un gris oscuro
        "CardsDialogs": "424242",
        "FlatButtonDown": "999999",
    }
}

class UI(ScreenManager): #Clase para manejar diferentes pantallas
    pass

# --------------------------------------------------APP-----------------------------------------------------

class TuConsejeroEmocional(MDApp): #Acá van los métodos o funciones de la APP
    def build(self):    #Constructor
        self.theme_cls.colors = colors
        self.theme_cls.theme_style = 'Dark' #Esto cambia el color del tema, o sea, del fondo que de forma predeterminada es blanco
        self.theme_cls.primary_palette = 'Blue' #Color principal de paleta
        Builder.load_file('consejero_emo.kv') #Conexión con el archivo de interfaz .kv
        return UI() 
    
    
    #--------------------------Mostrar preguntas y respuestas en pantalla-------------------------------------------
        
    def preguntas_definicion(self): #Función que pone las preguntas y respuestas antes definidas
        asigna_pregunta = 0
        contador_tipo = 0
        posicion = 0

        for i in range(5): #Este bucle representa el número de preguntas a mostrar (5)
            for j in preguntas[i][0]: #Este bucle representa las preguntas
                if asigna_pregunta == 0: #Pregunta 1
                    self.root.ids.pregunta1.text = j  #Muestra la pregunta escogida de forma aleatoria dentro de un tipo especifico
                elif asigna_pregunta == 1:  #Pregunta 2
                    self.root.ids.pregunta2.text = j
                elif asigna_pregunta == 2:  #Pregunta 3
                    self.root.ids.pregunta3.text = j
                elif asigna_pregunta == 3:  #Pregunta 4
                    self.root.ids.pregunta4.text = j
                elif asigna_pregunta == 4:  #Pregunta 5
                    self.root.ids.pregunta5.text = j
            
                for k in preguntas[i][1]: #Bucle que imprime las respuestas a cada tipo de pregunta
                    if asigna_pregunta == 0:    #Respuestas a la pregunta 1
                        if posicion == 0:
                            self.root.ids.respuesta1_1.text = k     #Muestra las opciones de respuesta que existen para la pregunta previamente mostrada
                        elif posicion == 1:
                            self.root.ids.respuesta2_1.text = k
                        elif posicion == 2:
                            self.root.ids.respuesta3_1.text = k
                        elif posicion == 3:
                            self.root.ids.respuesta4_1.text = k
                        elif posicion == 4:
                            self.root.ids.respuesta5_1.text = k
                        posicion += 1    #Suma 1 al contador para que en la proxima iteración se imprima la 
                                         #siguente opción de respuesta.                    

                    elif asigna_pregunta == 1: #Respuestas a la pregunta 2
                        if posicion == 0:
                            self.root.ids.respuesta1_2.text = k
                        elif posicion == 1:
                            self.root.ids.respuesta2_2.text = k
                        elif posicion == 2:
                            self.root.ids.respuesta3_2.text = k
                        elif posicion == 3:
                            self.root.ids.respuesta4_2.text = k
                        elif posicion == 4:
                            self.root.ids.respuesta5_2.text = k
                        posicion += 1  

                    elif asigna_pregunta == 2:  #Respuestas a la pregunta 3
                        if posicion == 0:
                            self.root.ids.respuesta1_3.text = k
                        elif posicion == 1:
                            self.root.ids.respuesta2_3.text = k
                        elif posicion == 2:
                            self.root.ids.respuesta3_3.text = k
                        elif posicion == 3:
                            self.root.ids.respuesta4_3.text = k
                        elif posicion == 4:
                            self.root.ids.respuesta5_3.text = k
                        posicion += 1  

                    elif asigna_pregunta == 3:  #Respuestas a la pregunta 4
                        if posicion == 0:
                            self.root.ids.respuesta1_4.text = k
                        elif posicion == 1:
                            self.root.ids.respuesta2_4.text = k
                        elif posicion == 2:
                            self.root.ids.respuesta3_4.text = k
                        elif posicion == 3:
                            self.root.ids.respuesta4_4.text = k
                        elif posicion == 4:
                            self.root.ids.respuesta5_4.text = k
                        posicion += 1  

                    elif asigna_pregunta == 4:  #Respuestas a la pregunta 5
                        if posicion == 0:
                            self.root.ids.respuesta1_5.text = k
                        elif posicion == 1:
                            self.root.ids.respuesta2_5.text = k
                        elif posicion == 2:
                            self.root.ids.respuesta3_5.text = k
                        elif posicion == 3:
                            self.root.ids.respuesta4_5.text = k
                        elif posicion == 4:
                            self.root.ids.respuesta5_5.text = k
                        posicion += 1  

            asigna_pregunta +=1 #Sumo 1 a la variable para imprimir las siguientes preguntas y respuestas. 
            posicion = 0 #Reinicio la variable para volver a imprimir las y respuestas del siguiente tipo de pregunta


    #-------------------------------Enviar resultados de encuesta----------------------------------------------

    def enviar_resultado(self, instance, value, pregunta, respuesta): #Método para asignar puntajes o quitarlos cuando se deseleccionan
        if value == True:
            llamado_puntos(pregunta, respuesta)
        else:
            anula_puntos(pregunta)
            
        #Prueba para verificar que el valor de las preguntas cuando son elegidas o cuando no hay ninguna seleccionada
        print(f'emocional: {puntaje_emo}\nplazo: {puntaje_plazo}\nsocial: {puntaje_sociales}\nactividad: {puntaje_actividad}\ngeneral: {puntaje_generales}', end= "\n\n\n")


    #---------------------------------------Finalizar encuesta---------------------------------------
    
    def finalizar(self, mensaje): #Restricción para que el usuario solo finalice el test cuando responda todas las preguntas
        if 0 is puntaje_emo or 0 is puntaje_plazo or 0 is puntaje_sociales or 0 is puntaje_actividad or 0 is puntaje_generales:
            # print('Le falto responder una pregunta')
            return False
        else:
            if mensaje == 'bloqueo':
                return True
            else:
                self.root.current = 'finalizar'
                return True


    #----------------------------------Multimedia----------------------------------------------------------

    def volver(self): #Función para salir de las secciones hijas de multimedia
        ScreenManager.transition=FallOutTransition()
        self.root.current = 'principal'
        ScreenManager.transition=SlideTransition()
        # self.root.transition.direction = 'right'

    def inicio_multi(self, valor): #Función para que el mensaje de bienvenida de multimedia solo aparezca una vez.
        global aparicion
        print(valor)
        if valor == True:
            self.root.ids.multi.disabled = True

        if self.finalizar('bloqueo') == True:
            self.root.ids.multi.disabled = False
            valor = False
        if aparicion == 0 and valor == False and self.finalizar('bloqueo') == True:
            
            self.root.current = 'mensaje_multi'
            ScreenManager.transition=SwapTransition()
            aparicion += 1
            self.root.ids.kk.remove_widget(MDGridLayout)
            KV = """
Screen:
    name: 'futuro'
    MDGridLayout:
        cols: 1
        rows: 2
        MDTopAppBar:
            title: 'TuConsejeroEmocional'
            left_action_items: [['arrow-left', lambda x: app.volver()]]
            md_bg_color: rgba(0,0,1,0)
        BoxLayout:
            orientation: 'vertical'
            size: root.width, root.height
            padding: 20,20, 20, 20
            spacing: 20
            
        
            MDLabel:
                text: 'Planeación de vida y vista al futuro'
                size_hint: (1, .05)
                font_size: 24
                bold: True
                halign: 'center'
            MDLabel:
                text: 'Parece que tienes bien pensado lo que quieres para ti en un futuro, ¡asi que es hora de pasar a la acción y empezar a encaminar eso que quieres!'
                font_size: 20
                size_hint: (1,.6)
                # haling: 'justify'

            MDLabel:
                text: 'Videos:'
                size_hint: (1,.05)
                font_size: 24
                bold: True
            
                
            MDLabel:
                text: 'Ejercicios:'
                size_hint: (1, .05)
                font_size: 24
                bold: True
            MDRaisedButton:
                text: 'Mira más tecnicas y ejercicios de relajación aquí'
                font_size: 20
                bold: True
                size_hint: (0.7, .4)
                pos_hint: {'center_x': .5}
                haling: 'center'
                md_bg_color: 1,1,1,1
                text_color: 0,0,0,1
            
            """
            return Builder.load_string(KV)
        elif aparicion > 0: 
            self.root.current = 'principal'

    
        
    def boton_multi(self): #Calibración de las transiciones (Se estaba bugueando XD)
        ScreenManager.transition=SlideTransition()


    #----------------------------------------------------------------------------------------------------
    #                                          A Sufrir
    #----------------------------------------------------------------------------------------------------
    def unal(self):
        webbrowser.open('https://www.humanas.unal.edu.co/2017/extension/servicio-de-atencion-psicologica/servicios')
        

TuConsejeroEmocional().run() #Ejecuto la app