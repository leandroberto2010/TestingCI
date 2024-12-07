from behave import *
import pyautogui as pag
import subprocess as sp
from time import sleep
import os

def iniciar_aplicacion():
    print("Iniciando la aplicación...")
    script_path = os.path.abspath("AhorcadoApp.py")
    
    process = sp.Popen(['python', script_path], stdout=sp.PIPE, stderr=sp.PIPE)
    sleep(1)  # Tiempo de espera para cargar la aplicación
    print("Aplicación iniciada correctamente.")
    return process

def cerrar_aplicacion(process):
    #Cierra la aplicación después de la prueba.
    if process:
        process.terminate()
        process.wait()
        print("Aplicación cerrada.")

def palabraInicial(palabraTest):
    textInput = pag.locateOnScreen("textInput.png")
    pag.click(pag.center(textInput))
    sleep(1)
    pag.write(palabraTest)

    startButton = pag.locateOnScreen("empezar_juego.png")

    pag.click(pag.center(startButton))

def adivinaPalabra(palabraTest):
    # Localizar el campo de entrada para la palabra
    palabraInput = pag.locateOnScreen("palabra_input.png")

    pag.click(pag.center(palabraInput))
    pag.write(palabraTest)

    # Localizar el botón para adivinar la palabra
    adivinarPalabraButton = pag.locateOnScreen("adivinar_palabra.png")

    pag.click(pag.center(adivinarPalabraButton))

@fixture
def before_scenario(context,scenario):
    context.process = iniciar_aplicacion()
    pag.screenshot('debug_screenshot.png')
    sleep(1)

def after_scenario(context,scenario):
    cerrar_aplicacion(context.process)

def before_step(context,step):
    #sleep(1)
    if ('Reiniciar juego luego de' in context.scenario.name):
        if (step.step_type == 'given' and 'se muestra pantalla' in step.name):
            palabraInicial('PALABRA')
            if ('perder' in context.scenario.name):
                adivinaPalabra('MANZANA')
            else:
                adivinaPalabra('PALABRA')