import webbrowser
import random #Modulo para seleccionar las preguntas de forma aleatoria
from kivy.lang import Builder
from kivymd.app import MDApp    #Importamos a KivyMD
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, FallOutTransition, SlideTransition, SwapTransition #Manejo de pantallas y transiciones
from kivy.uix.scrollview import ScrollView #Vista Scroll
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.label import MDLabel
#------------------------------------Cosas de webview---------------------------------------------------------
from kivy.uix.modalview import ModalView
from kivy.clock import Clock
# from android.runnable import run_on_ui_thread #Descomentar
# from jnius import autoclass, cast, PythonJavaClass, java_method #Descomentar
# from webview import WebView #Descomentar
from kivy.uix.widget import Widget
from kivymd.uix.screen import MDScreen




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


#-----------------------------------------------------------------------------------------------------
#                                   Codigo pjnius para el webview (RECORDAR DESCOMENTAR)
#-----------------------------------------------------------------------------------------------------

# WebViewA = autoclass('android.webkit.WebView')
# WebViewClient = autoclass('android.webkit.WebViewClient')
# LayoutParams = autoclass('android.view.ViewGroup$LayoutParams')
# LinearLayout = autoclass('android.widget.LinearLayout')
# KeyEvent = autoclass('android.view.KeyEvent')
# ViewGroup = autoclass('android.view.ViewGroup')
# DownloadManager = autoclass('android.app.DownloadManager')
# DownloadManagerRequest = autoclass('android.app.DownloadManager$Request')
# Uri = autoclass('android.net.Uri')
# Environment = autoclass('android.os.Environment')
# Context = autoclass('android.content.Context')
# PythonActivity = autoclass('org.kivy.android.PythonActivity')


# class DownloadListener(PythonJavaClass):
#     #https://stackoverflow.com/questions/10069050/download-file-inside-webview
#     __javacontext__ = 'app'
#     __javainterfaces__ = ['android/webkit/DownloadListener']

#     @java_method('(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;J)V')
#     def onDownloadStart(self, url, userAgent, contentDisposition, mimetype,
#                         contentLength):
#         mActivity = PythonActivity.mActivity 
#         context =  mActivity.getApplicationContext()
#         visibility = DownloadManagerRequest.VISIBILITY_VISIBLE_NOTIFY_COMPLETED
#         dir_type = Environment.DIRECTORY_DOWNLOADS
#         uri = Uri.parse(url)
#         filepath = uri.getLastPathSegment()
#         request = DownloadManagerRequest(uri)
#         request.setNotificationVisibility(visibility)
#         request.setDestinationInExternalFilesDir(context,dir_type, filepath)
#         dm = cast(DownloadManager,
#                   mActivity.getSystemService(Context.DOWNLOAD_SERVICE))
#         dm.enqueue(request)


# class KeyListener(PythonJavaClass):
#     __javacontext__ = 'app'
#     __javainterfaces__ = ['android/view/View$OnKeyListener']

#     def __init__(self, listener):
#         super().__init__()
#         self.listener = listener

#     @java_method('(Landroid/view/View;ILandroid/view/KeyEvent;)Z')
#     def onKey(self, v, key_code, event):
#         if event.getAction() == KeyEvent.ACTION_DOWN and\
#            key_code == KeyEvent.KEYCODE_BACK: 
#             return self.listener()
        
# class WebView(ModalView):
#     # https://developer.android.com/reference/android/webkit/WebView
    
#     def __init__(self, url, enable_javascript = False, enable_downloads = False,
#                  enable_zoom = False, **kwargs):
#         super().__init__(**kwargs)
#         self.url = url
#         self.enable_javascript = enable_javascript
#         self.enable_downloads = enable_downloads
#         self.enable_zoom = enable_zoom
#         self.webview = None
#         self.enable_dismiss = True
#         self.open()

#     @run_on_ui_thread        
#     def on_open(self):
#         mActivity = PythonActivity.mActivity 
#         webview = WebViewA(mActivity)
#         webview.setWebViewClient(WebViewClient())
#         webview.getSettings().setJavaScriptEnabled(self.enable_javascript)
#         webview.getSettings().setBuiltInZoomControls(self.enable_zoom)
#         webview.getSettings().setDisplayZoomControls(False)
#         webview.getSettings().setAllowFileAccess(True) #default False api>29
#         layout = LinearLayout(mActivity)
#         layout.setOrientation(LinearLayout.VERTICAL)
#         layout.addView(webview, self.width, self.height)
#         mActivity.addContentView(layout, LayoutParams(-1, -1))
#         webview.setOnKeyListener(KeyListener(self._back_pressed))
#         if self.enable_downloads:
#             webview.setDownloadListener(DownloadListener())
#         self.webview = webview
#         self.layout = layout
#         try:
#             webview.loadUrl(self.url)
#         except Exception as e:            
#             print('Webview.on_open(): ' + str(e))
#             self.dismiss()  
        
#     @run_on_ui_thread        
#     def on_dismiss(self):
#         if self.enable_dismiss:
#             self.enable_dismiss = False
#             parent = cast(ViewGroup, self.layout.getParent())
#             if parent is not None: parent.removeView(self.layout)
#             self.webview.clearHistory()
#             self.webview.clearCache(True)
#             self.webview.clearFormData()
#             self.webview.destroy()
#             self.layout = None
#             self.webview = None
        
#     @run_on_ui_thread
#     def on_size(self, instance, size):
#         if self.webview:
#             params = self.webview.getLayoutParams()
#             params.width = self.width
#             params.height = self.height
#             self.webview.setLayoutParams(params)

#     def pause(self):
#         if self.webview:
#             self.webview.pauseTimers()
#             self.webview.onPause()

#     def resume(self):
#         if self.webview:
#             self.webview.onResume()       
#             self.webview.resumeTimers()

#     def downloads_directory(self):
#         # e.g. Android/data/org.test.myapp/files/Download
#         dir_type = Environment.DIRECTORY_DOWNLOADS
#         context =  PythonActivity.mActivity.getApplicationContext()
#         directory = context.getExternalFilesDir(dir_type)
#         return str(directory.getPath())

#     def _back_pressed(self):
#         if self.webview.canGoBack():
#             self.webview.goBack()
#         else:
#             self.dismiss()  
#         return True




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

#---------------------------------------------Parte de Webview-------------------------------------------
class MyWebView(MDScreen):
    pass

#---------------------------------------------------------------------------------------------------------
class UI(ScreenManager): #Clase para manejar diferentes pantallas
    pass

# --------------------------------------------------APP-----------------------------------------------------

class TuConsejeroEmocional(MDApp): #Acá van los métodos o funciones de la APP
    def build(self):    #Constructor
        self.theme_cls.colors = colors
        self.theme_cls.theme_style = 'Dark' #Esto cambia el color del tema, o sea, del fondo que de forma predeterminada es blanco
        self.theme_cls.primary_palette = 'Blue' #Color principal de paleta
        Builder.load_file('prueba_web.kv') #Conexión con el archivo de interfaz .kv
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
        # NO BORRAR print(f'emocional: {puntaje_emo}\nplazo: {puntaje_plazo}\nsocial: {puntaje_sociales}\nactividad: {puntaje_actividad}\ngeneral: {puntaje_generales}', end= "\n\n\n")


    #---------------------------------------Finalizar encuesta---------------------------------------
    
    def finalizar(self, mensaje): #Restricción para que el usuario solo finalice el test cuando responda todas las preguntas
        if 0 == puntaje_emo or 0 == puntaje_plazo or 0 == puntaje_sociales or 0 == puntaje_actividad or 0 == puntaje_generales:
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
        if valor == True:
            self.root.ids.multi.disabled = True

        if self.finalizar('bloqueo') == True:
            self.root.ids.multi.disabled = False
            valor = False
        if aparicion == 0 and valor == False and self.finalizar('bloqueo') == True:
            
            self.root.current = 'mensaje_multi'
            ScreenManager.transition=SwapTransition()
            aparicion += 1

        elif aparicion > 0: 
            self.root.current = 'principal'

        
    
        
    def boton_multi(self): #Calibración de las transiciones (Se estaba bugueando XD)
        ScreenManager.transition=SlideTransition()


    #----------------------------------------------------------------------------------------------------
    #                                          A Sufrir
    #----------------------------------------------------------------------------------------------------
    def unal(self):
        webbrowser.open('https://www.humanas.unal.edu.co/2017/extension/servicio-de-atencion-psicologica/servicios')
        

    #----------Funciones de personalización de interfazces------------------------------------

    def personalizacion_contenido(self):
        global puntaje_emo, puntaje_actividad, puntaje_generales, puntaje_plazo, puntaje_sociales, parte1_emo, parte2_emo, parte3_emo, bandera_emo
        bandera = 0
        # self.root.ids.puntaje_medio_emo.remove_widget(self.root.ids.puntaje_medio_emo.children[0])
        # self.root.ids.articulos_emo.text = 'Dale un vistazo a\nestas lecturas y\nejercicios para\ncomprender y\nmanejar tus\nemociones '
        # self.root.ids.videos_emo.text = 'Consulta\nconsejos y\nbuenos hábitos\nemocionales con\nestos videos'
        
        if puntaje_emo == 10:
             
            parte3_emo = self.root.ids.inter_emocionales.children[0]
            self.root.ids.inter_emocionales.remove_widget(self.root.ids.inter_emocionales.children[0])
            parte2_emo = self.root.ids.inter_emocionales.children[0]
            self.root.ids.inter_emocionales.remove_widget(self.root.ids.inter_emocionales.children[0])
            parte1_emo = self.root.ids.inter_emocionales.children[0]
            self.root.ids.inter_emocionales.remove_widget(self.root.ids.inter_emocionales.children[0])
            self.root.ids.mensaje_emocionales.text = 'Se podría decir que posees una buena inteligencia emocional, ¡felicitaciones!, pero igualmente debes continuar trabajando en ello, por lo que aquí te guiaremos a mejorar cada día más.'
            self.root.ids.mensaje_boton_emocionales1.text = 'Conoce consejos\ny buenos hábitos\npara mantener el\nbuen manejo\nemocional'
            self.root.ids.grid_emocional.row_default_height = 500
            bandera_emo = 1
        elif puntaje_emo == 8 or puntaje_emo == 6:
            self.root.ids.inter_emocionales.remove_widget(self.root.ids.inter_emocionales.children[0])
            self.root.ids.mensaje_emocionales.text = 'Puede que te parezca difícil esto del manejo emocional y la inteligencia emocional, pero trabajarlo lleva a un gran bienestar, por lo que te guiaremos para dar con la mejor versión de ti.'
            self.root.ids.mensaje_boton_emocionales1.text = 'Consulta\nconsejos y\nbuenos hábitos\nemocionales con\nestos videos'
            self.root.ids.mensaje_boton_emocionales2.text = 'Dale un vistazo a\nestas lecturas y\nejercicios, para\ncomprender y\nmanejar tus\nemociones '
            self.root.ids.grid_emocional.row_default_height = 650
            bandera_emo = 2
        elif puntaje_emo <=4:
            if bandera_emo == 1:
                self.root.ids.inter_emocionales.add_widget(parte1_emo)
                self.root.ids.inter_emocionales.add_widget(parte2_emo)
                self.root.ids.inter_emocionales.add_widget(parte3_emo)
            elif bandera_emo == 2:
                pass
            
            self.root.ids.mensaje_emocionales.text = 'Puede que estés pasando un momento difícil, o que no sepas bien cómo manejar tus emociones y reacciones, por lo que aquí tienes material de ayuda que puede llegar a serte útil.'
            self.root.ids.mensaje_boton_emocionales1.text = 'Identifica tus\nsentimientos y\nproblemas con\nestos videos'
            self.root.ids.mensaje_boton_emocionales2.text = 'Infórmate de los\ndiagnósticos e\ninformación de\nprofesionales'
            self.root.ids.grid_emocional.row_default_height = 800
            bandera_emo = 3

        if puntaje_actividad == 10:
            self.root.ids.inter_actividad.remove_widget(self.root.ids.inter_actividad.children[0])
            self.root.ids.inter_actividad.remove_widget(self.root.ids.inter_actividad.children[0])
            self.root.ids.mensaje_actividad.text = 'Excelente, según tus respuestas del test, eres una persona muy organizada, por lo que no necesitas mayor ayuda, solo en la tarea de continuar con los buenos hábitos.'
            self.root.ids.mensaje_boton_actividad1.text = '¡Descubre nuevos\no mejores hábitos\npara mejorar tu\norganización!'
            self.root.ids.grid_actividad.row_default_height = 400
        elif puntaje_actividad == 8 or puntaje_actividad == 6:
            self.root.ids.mensaje_actividad.text = 'Tu organización no es la mejor, pero solo necesitas orientación y algunos cuantos consejos y hábitos adaptables a tus rutinas, con lo que mejorarás considerablemente.'
            self.root.ids.mensaje_boton_actividad1.text = '¡Descubre nuevos\no mejores hábitos\npara mejorar tu\norganización!'
            self.root.ids.mensaje_boton_actividad2.text = 'Infórmate sobre\nestrategias y\nejercicios útiles'
        elif puntaje_actividad <=4:
            self.root.ids.mensaje_actividad.text = 'Necesitas modificar drásticamente tus hábitos organizativos y las malas prácticas como la procrastinación, pero tranquilo, te ayudaremos con el material seleccionado para ti.'
            self.root.ids.mensaje_boton_actividad1.text = 'Aprende e\nimplementa\nhábitos y\nprácticas de estos\nvideos'
            self.root.ids.mensaje_boton_actividad2.text = 'Infórmate sobre\nestrategias y\nejercicios útiles'


        if puntaje_generales == 10:
            self.root.ids.mensaje_generales.text = 'Según tus resultados en el test, esta semana no ha sido muy dura para ti, sin embargo, ¡te recomendamos ver el material selecionado, para que tengas un momento de relajación!'
            self.root.ids.mensaje_boton_generales1.text = 'Tomate un\nmomento para\nrelajarte con\nestos videos'
            self.root.ids.mensaje_boton_generales2.text = 'Mira más tecnicas\ny ejercicios de\nrelajación aquí'
        elif puntaje_generales == 8 or puntaje_generales == 6:
            self.root.ids.mensaje_generales.text = 'Según tus resultados en el test, has tenido una semana más o menos pesada, por lo que deberías tomarte un tiempo para relajarte con los videos y ejercicios que tenemos para ti.'
            self.root.ids.mensaje_boton_generales1.text = 'Tomate un\nmomento para\nrelajarte con\nestos videos'
            self.root.ids.mensaje_boton_generales2.text = 'Mira más tecnicas\ny ejercicios de\nrelajación aquí'
        elif puntaje_generales <=4:
            self.root.ids.mensaje_generales.text = 'Según tus resultados en el test, esta no ha sido de tus mejores semanas, por lo que aquí podrás encontrar un espacio donde descargarte y encontrar como manejar el estrés en situaciones así.'
            self.root.ids.mensaje_boton_generales1.text = 'Tomate un\nmomento para\nrelajarte con\nestos videos'
            self.root.ids.mensaje_boton_generales2.text = 'Mira cómo\nmanejar el estrés\ny técnicas de\nrelajación'


        if puntaje_plazo == 10:
            self.root.ids.mensaje_futuro.text = 'Parece que tienes bien pensado lo que quieres para ti en un futuro, ¡así que es hora de pasar a la acción y empezar a encaminar eso que quieres!'
            self.root.ids.inter_futuro.remove_widget(self.root.ids.inter_futuro.children[0])
            self.root.ids.inter_futuro.remove_widget(self.root.ids.inter_futuro.children[0])
            self.root.ids.mensaje_boton_futuro1.text = '¡Descubre como\nencaminar y\nlograr lo que ya te\nhas propuesto!'
            self.root.ids.grid_futuro.row_default_height = 400
        elif puntaje_plazo == 8 or puntaje_plazo == 6:
            self.root.ids.mensaje_futuro.text = 'Parece que aún no tienes bien pensado lo que quieres para ti en un futuro, por lo que es necesario enfocar lo que realmente quieres y necesitas, para luego ponerlo en acción.'
            self.root.ids.mensaje_boton_futuro1.text = 'Busca ayuda\nacerca de cómo\nbuscar y enfocar\nlo que realmente\nquieres'
            self.root.ids.mensaje_boton_futuro2.text = 'Infórmate sobre\nestrategias útiles '
            self.root.ids.grid_futuro.row_default_height = 600
        elif puntaje_plazo <=4:
            self.root.ids.mensaje_futuro.text = 'Quizá no tienes mucha idea de lo que te depara el futuro, por eso es necesario que estés preparado, y tengas un plan de acción de que es lo que quieres y necesitas.'
            self.root.ids.mensaje_boton_futuro1.text = 'Encuentra que te\nllama la atención\npara tu futuro, y\nque es lo que\nnecesitas '
            self.root.ids.mensaje_boton_futuro2.text = 'Descubre hábitos\norganizativos que\nte permitan ordenar\nlo que quieres y\nnecesitas'
            self.root.ids.grid_futuro.row_default_height = 615

        if puntaje_sociales == 10:
            self.root.ids.inter_sociales.remove_widget(self.root.ids.inter_sociales.children[0])
            self.root.ids.mensaje_sociales.text = 'Quizá no tengas las mejores capacidades sociales, pero esto es solo cuestión de práctica y voluntad, y con la guía de los videos y ejercicios que hemos recopilado, ¡podrás mejorar rápidamente!'
            self.root.ids.mensaje_boton_sociales1.text = 'Socializa y\nmaneja tus\nrelaciones mejor\ncon esta serie de\nconsejos '
            self.root.ids.mensaje_boton_sociales2.text = 'Infórmate acerca\nde técnicas y\nconsejos que\npueden ser útiles'
            self.root.ids.grid_social.row_default_height = 750
        elif puntaje_sociales <= 8:
            self.root.ids.mensaje_sociales.text = 'Puede que para ti, expresarte y relacionarte sea un tema muy complicado, por lo que aquí tienes material de ayuda que puede llegar a serte útil.'
            self.root.ids.mensaje_boton_sociales1.text = 'Identifica tus\ndificultades y\nproblemas con\nestos videos'
            self.root.ids.mensaje_boton_sociales2.text = 'Infórmate de los\ndiagnósticos e\ninformación de\nprofesionales'



    #--------------------------------------------------------------------------------------------------------
    #---------------------------------------Metodos de webview-----------------------------------------------
    #--------------------------------------------------------------------------------------------------------
    def define_videos(self, tipo):
        global puntaje_emo, puntaje_actividad, puntaje_generales, puntaje_plazo, puntaje_sociales, pantalla
        if puntaje_emo == 10 and tipo == 'emocional':
            pantalla = WebView("https://www.youtube.com/playlist?list=PLH9n8q8hK8ae8OJcPOA5GonkeJ--gZtqk",
                                enable_javascript = True,
                                enable_downloads = True,
                                enable_zoom = True)
            return pantalla
        elif (puntaje_emo == 8 or puntaje_emo == 6) and tipo == 'emocional':
            pantalla = WebView("https://www.youtube.com/playlist?list=PLH9n8q8hK8af99jYrwLxWS5NFyiU7iNNS",
                                enable_javascript = True,
                                enable_downloads = True,
                                enable_zoom = True)
            return pantalla
        elif puntaje_emo <=4 and tipo == 'emocional':
            pantalla = WebView("https://www.youtube.com/playlist?list=PLH9n8q8hK8adQP0H7pXaOkvcmKowMANTD",
                                enable_javascript = True,
                                enable_downloads = True,
                                enable_zoom = True)
            return pantalla

        if puntaje_actividad == 10 and tipo == 'actividad':
            pantalla = WebView("https://www.youtube.com/playlist?list=PLH9n8q8hK8acPVctqsFIhLpUJNCqvtmxU",
                                enable_javascript = True,
                                enable_downloads = True,
                                enable_zoom = True)
            return pantalla
        elif (puntaje_actividad == 8 or puntaje_actividad == 6) and tipo == 'actividad':
            pantalla = WebView("https://www.youtube.com/playlist?list=PLH9n8q8hK8acBWK0AwK6VMkecxR_VoUhB",
                                enable_javascript = True,
                                enable_downloads = True,
                                enable_zoom = True)
            return pantalla
        elif puntaje_actividad <=4 and tipo == 'actividad':
            pantalla = WebView("https://www.youtube.com/playlist?list=PLH9n8q8hK8afM2ecqFcmn5sWdg_dqNEZE",
                                enable_javascript = True,
                                enable_downloads = True,
                                enable_zoom = True)
            return pantalla


        if puntaje_generales == 10 and tipo == 'general':
            pantalla = WebView("https://www.youtube.com/playlist?list=PLH9n8q8hK8ad5mlQvnGOG1p_oZO3rejGE",
                                enable_javascript = True,
                                enable_downloads = True,
                                enable_zoom = True)
            return pantalla
        elif (puntaje_generales == 8 or puntaje_generales == 6) and tipo == 'general':
            pantalla = WebView("https://www.youtube.com/playlist?list=PLH9n8q8hK8ad5mlQvnGOG1p_oZO3rejGE",
                                enable_javascript = True,
                                enable_downloads = True,
                                enable_zoom = True)
            return pantalla
        elif puntaje_generales <=4 and tipo == 'general':
            pantalla = WebView("https://www.youtube.com/playlist?list=PLH9n8q8hK8acsKQg2mIUOAvYUZTysZnQL",
                                enable_javascript = True,
                                enable_downloads = True,
                                enable_zoom = True)
            return pantalla

        if puntaje_plazo == 10 and tipo == 'futuro':
            pantalla = WebView("https://www.youtube.com/playlist?list=PLH9n8q8hK8acgTnaJzA-JNZ-zX4Zw-4Ab",
                                enable_javascript = True,
                                enable_downloads = True,
                                enable_zoom = True)
            return pantalla
        elif (puntaje_plazo == 8 or puntaje_plazo == 6) and tipo == 'futuro':
            pantalla = WebView("https://www.youtube.com/playlist?list=PLH9n8q8hK8acqRCYX3PWgc6uSUSAdunjY",
                                enable_javascript = True,
                                enable_downloads = True,
                                enable_zoom = True)
            return pantalla
        elif puntaje_plazo <=4 and tipo == 'futuro':
            pantalla = WebView("https://www.youtube.com/playlist?list=PLH9n8q8hK8af7ShRlg0LCarwgm7QTmNqb",
                                enable_javascript = True,
                                enable_downloads = True,
                                enable_zoom = True)
            return pantalla

        if puntaje_sociales == 10 and tipo == 'social':
            pantalla = WebView("https://www.youtube.com/playlist?list=PLH9n8q8hK8afJCxXCTjfctQfw6lCTL4nF",
                                enable_javascript = True,
                                enable_downloads = True,
                                enable_zoom = True)
            return pantalla
        elif puntaje_sociales <= 8 and tipo == 'social':
            pantalla = WebView("https://www.youtube.com/playlist?list=PLH9n8q8hK8af0ZpKTLkW3g3k8AT29YxRx",
                                enable_javascript = True,
                                enable_downloads = True,
                                enable_zoom = True)
            return pantalla

    def define_ejercicios(self, tipo):
        global puntaje_emo, puntaje_actividad, puntaje_generales, puntaje_plazo, puntaje_sociales, pantalla
        if puntaje_emo == 10 and tipo == 'emocional':
            pantalla = WebView("https://www.youtube.com/playlist?list=PLH9n8q8hK8ae8OJcPOA5GonkeJ--gZtqk",
                                enable_javascript = True,
                                enable_downloads = True,
                                enable_zoom = True)
            return pantalla
        elif (puntaje_emo == 8 or puntaje_emo == 6) and tipo == 'emocional':
            pantalla = WebView("https://www.youtube.com/playlist?list=PLH9n8q8hK8af99jYrwLxWS5NFyiU7iNNS",
                                enable_javascript = True,
                                enable_downloads = True,
                                enable_zoom = True)
            return pantalla
        elif puntaje_emo <=4 and tipo == 'emocional':
            pantalla = WebView("https://justpaste.it/7yo6s",
                                enable_javascript = True,
                                enable_downloads = True,
                                enable_zoom = True)
            return pantalla

        if puntaje_actividad == 10 and tipo == 'actividad':
            pantalla = WebView("https://www.youtube.com/playlist?list=PLH9n8q8hK8acPVctqsFIhLpUJNCqvtmxU",
                                enable_javascript = True,
                                enable_downloads = True,
                                enable_zoom = True)
            return pantalla
        elif (puntaje_actividad == 8 or puntaje_actividad == 6) and tipo == 'actividad':
            pantalla = WebView("https://justpaste.it/5k9t2",
                                enable_javascript = True,
                                enable_downloads = True,
                                enable_zoom = True)
            return pantalla
        elif puntaje_actividad <=4 and tipo == 'actividad':
            pantalla = WebView("https://justpaste.it/3yk5b",
                                enable_javascript = True,
                                enable_downloads = True,
                                enable_zoom = True)
            return pantalla


        if puntaje_generales == 10 and tipo == 'general':
            pantalla = WebView("https://justpaste.it/76rg8",
                                enable_javascript = True,
                                enable_downloads = True,
                                enable_zoom = True)
            return pantalla
        elif (puntaje_generales == 8 or puntaje_generales == 6) and tipo == 'general':
            pantalla = WebView("https://justpaste.it/76rg8",
                                enable_javascript = True,
                                enable_downloads = True,
                                enable_zoom = True)
            return pantalla
        elif puntaje_generales <=4 and tipo == 'general':
            pantalla = WebView("https://justpaste.it/4y9a8",
                                enable_javascript = True,
                                enable_downloads = True,
                                enable_zoom = True)
            return pantalla

        if puntaje_plazo == 10 and tipo == 'futuro':
            pantalla = WebView("https://www.youtube.com/playlist?list=PLH9n8q8hK8acgTnaJzA-JNZ-zX4Zw-4Ab",
                                enable_javascript = True,
                                enable_downloads = True,
                                enable_zoom = True)
            return pantalla
        elif (puntaje_plazo == 8 or puntaje_plazo == 6) and tipo == 'futuro':
            pantalla = WebView("https://justpaste.it/9amyl",
                                enable_javascript = True,
                                enable_downloads = True,
                                enable_zoom = True)
            return pantalla
        elif puntaje_plazo <=4 and tipo == 'futuro':
            pantalla = WebView("https://justpaste.it/96t96",
                                enable_javascript = True,
                                enable_downloads = True,
                                enable_zoom = True)
            return pantalla

        if puntaje_sociales == 10 and tipo == 'social':
            pantalla = WebView("https://justpaste.it/8u8fb",
                                enable_javascript = True,
                                enable_downloads = True,
                                enable_zoom = True)
            return pantalla
        elif puntaje_sociales <= 8 and tipo == 'social':
            pantalla = WebView("https://justpaste.it/9nq99",
                                enable_javascript = True,
                                enable_downloads = True,
                                enable_zoom = True)
            return pantalla



TuConsejeroEmocional().run() #Ejecuto la app