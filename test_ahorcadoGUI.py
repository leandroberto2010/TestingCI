import pyautogui as pag
import subprocess as sp
import pytest
import time


@pytest.fixture(scope="function")

def iniciar_aplicacion():
    """Inicia la aplicación antes de cada prueba y la cierra después."""
    print("iniciando")
    process = sp.Popen(['python', 'Ahorcado/AhorcadoApp.py'])
    time.sleep(1) #Tiempo de espera
    yield process
    process.terminate()
    process.wait()
    time.sleep(2)

def test_ganar_letra(iniciar_aplicacion):
    textInput = pag.locateOnScreen('Ahorcado/textInput.png')
    pag.click(pag.center(textInput))
    pag.write("PALABRA")

    startButton = pag.locateOnScreen('Ahorcado/empezar_juego.png')
    pag.click(pag.center(startButton))

    letraInput = pag.locateOnScreen("Ahorcado/letra_input.png")
    
    letraButton = pag.locateOnScreen("Ahorcado/adivinar_letra.png")

    for letra in "PALBR":
        pag.click(pag.center(letraInput))
        pag.write(letra)
        pag.click(pag.center(letraButton))

    ganasteMsg = pag.locateOnScreen("Ahorcado/ganaste.png")
    
    assert ganasteMsg is not pag.ImageNotFoundException

def test_adivinar_palabra(iniciar_aplicacion):
    textInput = pag.locateOnScreen("Ahorcado/textInput.png")
    pag.click(pag.center(textInput))
    pag.write("PALABRA")

    startButton = pag.locateOnScreen('Ahorcado/empezar_juego.png')
    pag.click(pag.center(startButton))

    palabraInput = pag.locateOnScreen("Ahorcado/palabra_input.png")
    pag.click(pag.center(palabraInput))
    pag.write("PALABRA")

    adivinarPalabraButton = pag.locateOnScreen("Ahorcado/adivinar_palabra.png")
    pag.click(pag.center(adivinarPalabraButton))

    ganasteMsg = pag.locateOnScreen("Ahorcado/ganaste.png")

    assert ganasteMsg is not pag.ImageNotFoundException

def test_perder_por_letra(iniciar_aplicacion):
    textInput = pag.locateOnScreen("Ahorcado/textInput.png")
    pag.click(pag.center(textInput))
    pag.write("PALABRA")

    startButton = pag.locateOnScreen("Ahorcado/empezar_juego.png")
    pag.click(pag.center(startButton))
    
    letraInput = pag.locateOnScreen("Ahorcado/letra_input.png")
    letraButton = pag.locateOnScreen("Ahorcado/adivinar_letra.png")

    for letra in "TFDGHJK":
        pag.click(pag.center(letraInput))
        pag.write(letra)
        pag.click(pag.center(letraButton))

    perdisteMsg = pag.locateOnScreen("Ahorcado/perdiste.png")

    assert perdisteMsg is not pag.ImageNotFoundException

def test_perder_por_palabra(iniciar_aplicacion):
    textInput = pag.locateOnScreen("Ahorcado/textInput.png")
    pag.click(pag.center(textInput))
    pag.write("PALABRA")

    startButton = pag.locateOnScreen('Ahorcado/empezar_juego.png')
    pag.click(pag.center(startButton))

    palabraInput = pag.locateOnScreen("Ahorcado/palabra_input.png")
    pag.click(pag.center(palabraInput))
    pag.write("ERROR")

    adivinarPalabraButton = pag.locateOnScreen("Ahorcado/adivinar_palabra.png")
    pag.click(pag.center(adivinarPalabraButton))

    perdisteMsg = pag.locateOnScreen("Ahorcado/perdiste.png")

    assert perdisteMsg is not pag.ImageNotFoundException
