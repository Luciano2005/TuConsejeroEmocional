import kivy
from kivy.app import App
from kivy.uix.widget import Widget 
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
#from kivy.uix.image import Image #Importar imagenes, esto solo se hace cuando voy a usar imagenes con python, si solo voy a usar el .kv no es necesario.
#from kivy.uix.floatlayout import FloatLayout  #Esto es por si vamos a escribir codigo de esto en este archivo.

#Vamos a configurar el tamaño de la app, recordar importar Window de kivy.
Window.size = (500, 700) #Ancho por alto


Builder.load_file('calculadora.kv')

class MyLayout(Widget):
    #Función para limpiar el input
    def clear(self):
        self.ids.calc_input.text = '0'
    
    #Función para cuando se presiona algún botón de número
    def bottom_press(self, num):
        #Variable que contenga la entrada de texto
        entrada = self.ids.calc_input.text

        #Condicionales que definan si el 0 está en el textinput
        if entrada == '0' or entrada == 'ERROR':
            self.ids.calc_input.text = ''
            self.ids.calc_input.text = f'{num}'
        else:
            self.ids.calc_input.text += f'{num}'

    #Función de añadir (+, -, *, /, %)
    def add(self, simbolo): 
        self.ids.calc_input.text += f'{simbolo}'

    #Función resultado
    def resultado(self):
        operacion = self.ids.calc_input.text
        try:
            resultado = eval(operacion)
            self.ids.calc_input.text = str(resultado)
        except:
            self.ids.calc_input.text = 'ERROR'
        '''
        if '+' in operacion:
            separar_nums = operacion.split('+')
            for numero in separar_nums:
                resultado += float(numero)
        elif '-' in operacion:
            separar_nums = operacion.split('-')
            for numero in separar_nums:
                if numero == separar_nums[0]:
                    resultado = float(numero)
                else:
                    resultado -= float(numero)
        elif 'X' in operacion:
            resultado = 1
            separar_nums = operacion.split('X')
            for numero in separar_nums:
                resultado *= float(numero)
        elif '/' in operacion:
            resultado = 1
            separar_nums = operacion.split('/')
            for numero in separar_nums:
                if numero == separar_nums[0]:
                    resultado = float(numero)
                else:
                    resultado /= float(numero)
        else:
            separar_nums = operacion.split('%')
            for numero in separar_nums:
                if numero == separar_nums[0]:
                    resultado = float(numero)
                else:
                    resultado %= float(numero)

        self.ids.calc_input.text = str(resultado)
        '''

    #Función punto
    def punto(self, simbolo):
        operacion = self.ids.calc_input.text
        
        
        separar_nums = operacion.split('+')

        for i in separar_nums:
            if '.' in i:
                pass
            else:
                self.ids.calc_input.text += f'{simbolo}'

    #Función botón CE
    def delete(self):
        operacion = self.ids.calc_input.text
        self.ids.calc_input.text = operacion[:-1]
        if '' is self.ids.calc_input.text:
            self.ids.calc_input.text = '0'

    #Función cambio signo
    def cambio_signo(self):
        operacion = self.ids.calc_input.text
        if '-' in operacion:
             self.ids.calc_input.text = operacion.replace('-', '')
        else:
            self.ids.calc_input.text = f'-{operacion}'



class CalculadoraApp(App):
    def build(self):
        Window.clearcolor = ('#1FBA86')
        return MyLayout()

if __name__ == '__main__':
    CalculadoraApp().run()





