#Proyecto 01 - "Your own adventure": Colinas Silenciosas

#Importo los módulos que voy a utilizar a lo largo de mi programa

import os
import time
import colorama
from colorama import *
import random
import pygame
from pygame import mixer 


#Inicio colorama y pygame
colorama.init(autoreset=True)
pygame.init()
pygame.mixer.init()

#Portada del juego

print(Fore.GREEN + '''

    ████  █████  ██    █████ ██    █  █████ █████   
    █     █   █  ██      █   █ █   █  █   █ █       
    █     █   █  ██      █   █  █  █  █████ █████   
    █     █   █  ██      █   █   █ █  █   █     █   
    ████  █████  █████ █████ █    ██  █   █ █████   
                                                    
                                                    
  ███ ███ █   ███  ██ █ ████ ███ ███  ███ ████  ████
  █    █  █   █    ██ █ █     █ █   █ █   █  █  █   
  ███  █  █   ███  ██ █ █     █ █   █ ███ ████  ████
    █  █  █   █    █ ██ █     █ █   █   █ █  █     █
  ███ ███ ███ ███  █  █ ████ ███ ███  ███ █  █  ████ 
                                                         
                                                             
             ▓▓                                              
▓    ▓       ▓▓ ▓    ▒▒                  ▒▒░ █  ▒▓▓   ▒▒     
█▓▒░ ▓      ▓▓▓▓▓▓  ▒▒▒▒▓ ██ ░░    ▓▓▓░ ▓▒▒▒▓▓▓ ▓▓▓▓▓▓▒▒▒░   
█▒▒▒▓▓▓▓  ▒▓▓▓▓▓▓ ▒ ▒▒▒▒▓▓██ ░░░▒▒ ▓▓▓░ ▒▒▒▒▒▓▒▒▓▓▓▓▓▒▒▒▒▒▒▒ 
█▒▒▓▓▓▓▓▓▓▒▓▓▓▓▓▓▒▒▒▒▒▒▒▒▓▓▓ ░░▒▒▒▒▓▓▓▓▒▒▒▒▒▒▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒
▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒
██▓█▓▓▓▓▓▒▓▒▓▓▓▓▓▓▒▒▒▒▒▒▒▒▓▓▓▓░▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒
▓         ░   ▓ ▓▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▒▒▒▓▓▒▒▒▒▒▒▒▒▒▓▓▓▓  ▓        
                     ▓▓ ▓  ▓ █▓▒░▒▓▒▓  ▓  ▓▓ ▓               
                                                          
  
  
  ''')
pygame.mixer.music.load("audio/Soundrack_corto.mp3")
pygame.mixer.music.play(1)                                                 

#Borro la información anterior 
input()
os.system("cls")


#Comprobar si es mayor de edad el jugador, solo podrá si es mayor

while True:
    
    edad = int(input("Este juego corresponde a una clasificación por edades PEGI 18, antes de continuar por favor escribe tu edad: "))

    if edad >= 18:
      
        print("\n\nCumples con las condiciones de edad, así que puedes continuar con la aventura")
        pygame.mixer.music.load("audio/bien.mp3")
        pygame.mixer.music.play(1)                                                 

        print( Fore.RED + '''                                                                                                                         
                                                     
      █▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█      
      █▓▓▓▓▓▓▓▓▓     ▓▓▓▓▓▓▓▓           ▒▓▓▓▓▓█      
      █▓▓▓▓▓▓▓▓      ▓▓▓▓▓▓                ▓▓▓█      
      █▓▓▓▓░         ▓▓▓▓▓        ▓▓        ▓▓█      
      █▒             ▓▓▓▓      ▓▓▓▓▓▓▓      ▒▓█      
      █▒             ▓▓▓▓      ▓▓▓▓▓▓▓▓     ░▓█      
      █▓▓▓▓▓▓▓▓      ▓▓▓▓      ▓▓▓▓▓▓▓      ▓▓█      
      █▓▓▓▓▓▓▓▓      ▓▓▓▓▓       ▒▓▓       ▓▓▓█      
      █▓▓▓▓▓▓▓▓      ▓▓▓▓▓▓▓             ▓▓▓▓▓█      
      █▓▓▓▓▓▓▓▓      ▓▓▓▓▓▒                ▒▓▓█      
      █▓▓▓▓▓▓▓▓      ▓▓▓▓       ▒▓▓▓▓        ▓█      
      █▓▓▓▓▓▓▓▓      ▓▓▓       ▓▓▓▓▓▓▓▓      ▓█      
      █▓▓▓▓▓▓▓▓      ▓▓▓      ▓▓▓▓▓▓▓▓▓      ░█      
      █▓▓▓▓▓▓▓▓      ▓▓▓      ░▓▓▓▓▓▓▓▓      ▒█      
      █▓▓▓▓▓▓▓▓      ▓▓▓░      ▓▓▓▓▓▓▓       ▓█      
      █▓▓▓▓▓▓▓▓      ▓▓▓▓                   ▓▓█      
      █▓▓▓▓▓▓▓▓      ▓▓▓▓▓▒                ▓▓▓█      
      █▓▓▓▓▓▓▓▓      ▓▓▓▓▓▓▓▓           ▒▓▓▓▓▓█      
      █▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█                              
                                              ''')
        break

    else:

        print("\n\nNo tienes la edad suficiente para jugar a Colinas Silenciosas, por favor vuelve en un par de años")
        pygame.mixer.music.load("audio/mal.mp3")
        pygame.mixer.music.play(1)
        print(Fore.RED + '''                                                                      
                                       
                   ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                   
               ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓               
            ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓            
          ▓▓▓▓▓▓▓▓▓               ▓▓▓▓▓▓▓▓▓          
        ▓▓▓▓▓▓▓▓                     ▓▓▓▓▓▓▓▓        
       ▓▓▓▓▓▓▓▓▓▓                      ▒▓▓▓▓▓▓       
      ▓▓▓▓▓▓▓▓▓▓▓▓▓███      ███████      ▓▓▓▓▓▓      
     ▓▓▓▓▓▓   ▓▓▓▓▓▓▓█    ███████████     ▓▓▓▓▓▓     
    ▓▓▓▓▓▓     █▓▓▓▓▓▓▓  █████    ████     ▓▓▓▓▓▓    
    ▓▓▓▓▓     ███▓▓▓▓▓▓▓▒████     ████      ▓▓▓▓▓    
    ▓▓▓▓▓     ███ █▓▓▓▓▓▓▓████    ████      ▓▓▓▓▓    
   ▓▓▓▓▓          ███▓▓▓▓▓▓▓█████████        ▓▓▓▓▓   
   ▓▓▓▓▓          ████ ▓▓▓▓▓▓▓███████        ▓▓▓▓▓   
   ▓▓▓▓▓          ████   ▓▓▓▓▓▓▓██████       ▓▓▓▓▓   
    ▓▓▓▓▓         ████  ███▓▓▓▓▓▓▓█████     ▓▓▓▓▓    
    ▓▓▓▓▓         ████  ████▓▓▓▓▓▓▓▓███     ▓▓▓▓▓    
    ▓▓▓▓▓▓        ████   █████▓▓▓▓▓▓▓█▓    ▓▓▓▓▓▓    
     ▓▓▓▓▓▓       ████    ██████▓▓▓▓▓▓▓   ▓▓▓▓▓▓     
      ▓▓▓▓▓▓       ███      ██████▓▓▓▓▓▓▓▓▓▓▓▓▓      
       ▓▓▓▓▓▓▒                      ▓▓▓▓▓▓▓▓▓▓       
        ▓▓▓▓▓▓▓▓                     ▓▓▓▓▓▓▓▓        
          ▓▓▓▓▓▓▓▓▓               ▓▓▓▓▓▓▓▓▓          
            ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓            
               ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓               
                   ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                   

                                            ''')
        input("\nPara volver a intentarlo, pulsa ENTER ")
        os.system("cls")
        

#Borro la información anterior 

input()
os.system("cls")


#Doy las opciones de dificultad para que elija el usuario pero redirigen a la dificultad normal

while True:
    os.system("cls")
    dificultad = int(input("\nElija la dificultad a la que va a enfrentarse a través de un número: \n1. Fácil, \n2. Normal, \n3. Difícil\n Quiero que mi juego sea: "))

    if dificultad == 1:
        os.system("cls")
        pygame.mixer.music.load("audio/easy.mp3")
        pygame.mixer.music.play(1)
        print(Fore.LIGHTCYAN_EX + '''    
                                                                                                                                                    
                ████                         ████  ███                              
                ░███                        ░░███  ░░░                               
                ░███   ██████   ██████    ███████  ████  ████████    ███████         
                ░███  ███░░███ ░░░░░███  ███░░███ ░░███ ░░███░░███  ███░░███         
                ░███ ░███ ░███  ███████ ░███ ░███  ░███  ░███ ░███ ░███ ░███         
                ░███ ░███ ░███ ███░░███ ░███ ░███  ░███  ░███ ░███ ░███ ░███         
                █████░░██████ ░░████████░░████████ █████ ████ █████░░███████ ██ ██ ██
                ░░░░░  ░░░░░░   ░░░░░░░░  ░░░░░░░░ ░░░░░ ░░░░ ░░░░░  ░░░░░██░░ ░░ ░░ 
                                                                    ███ ░███         
                                                                    ░░██████          
                                                                    ░░░░░░              \n
                            
                ███████   ██████    █████  █████ ████
                ███░░███ ░░░░░███  ███░░  ░░███ ░███ 
                ░███████   ███████ ░░█████  ░███ ░███ 
                ░███░░░   ███░░███  ░░░░███ ░███ ░███ 
                ░░██████ ░░████████ ██████  ░░███████ 
                ░░░░░░   ░░░░░░░░ ░░░░░░    ░░░░░███ 
                                            ███ ░███ 
                                            ░░██████  
                                            ░░░░░░   ''')
        print("\n¿¿No crees que es demasiado fácil??, inténtalo de nuevo ")
        input("Vuelve al menú y selecciona otra dificultad pulsando ENTER ")
        
    
    elif dificultad == 2:
        os.system("cls")
        pygame.mixer.music.load("audio/Waiting.mp3")
        pygame.mixer.music.play(1)
        print(Fore.LIGHTCYAN_EX + '''                                                                                                                    
                                                                                                                                                
                ████                         ████  ███                              
                ░███                        ░░███  ░░░                               
                ░███   ██████   ██████    ███████  ████  ████████    ███████         
                ░███  ███░░███ ░░░░░███  ███░░███ ░░███ ░░███░░███  ███░░███         
                ░███ ░███ ░███  ███████ ░███ ░███  ░███  ░███ ░███ ░███ ░███         
                ░███ ░███ ░███ ███░░███ ░███ ░███  ░███  ░███ ░███ ░███ ░███         
                █████░░██████ ░░████████░░████████ █████ ████ █████░░███████ ██ ██ ██
                ░░░░░  ░░░░░░   ░░░░░░░░  ░░░░░░░░ ░░░░░ ░░░░ ░░░░░  ░░░░░██░░ ░░ ░░ 
                                                                    ███ ░███         
                                                                    ░░██████          
                                                                    ░░░░░░                           
              
              
                     \n

                                                                        ████ 
                                                                        ░███ 
                ████████    ██████  ████████  █████████████    ██████   ░███ 
                ░███░░███  ███░░███░░██░░██░░  ███░░██░ ░██     ░░░░███ ░███ 
                ░███ ░███ ░███ ░███ ░███ ░░░  ░███ ░███ ░███   ███████  ░███ 
                ░███ ░███ ░███ ░███ ░███      ░███ ░███ ░███  ███░░███  ░███ 
                ████ █████░░██████  █████     █████░███ █████░░████████ █████
                ░░░░ ░░░░░  ░░░░░░  ░░░░░     ░░░░░ ░░░ ░░░░░  ░░░░░░░░ ░░░░░ 
                                                                                       
              ''') 
        print("\nEl juego se está iniciando...\n Recuerde tomar pausas después de varias horas de juego...")
        break

    elif dificultad == 3:
        os.system("cls")
        pygame.mixer.music.load("audio/hard.mp3")
        pygame.mixer.music.play(1)
        print(Fore.LIGHTCYAN_EX + '''                                                                                                                   
                                                                                                                                                   
                ████                         ████  ███                              
                ░███                        ░░███  ░░░                               
                ░███   ██████   ██████    ███████  ████  ████████    ███████         
                ░███  ███░░███ ░░░░░███  ███░░███ ░░███ ░░███░░███  ███░░███         
                ░███ ░███ ░███  ███████ ░███ ░███  ░███  ░███ ░███ ░███ ░███         
                ░███ ░███ ░███ ███░░███ ░███ ░███  ░███  ░███ ░███ ░███ ░███         
                █████░░██████ ░░████████░░████████ █████ ████ █████░░███████ ██ ██ ██
                ░░░░░  ░░░░░░   ░░░░░░░░  ░░░░░░░░ ░░░░░ ░░░░ ░░░░░  ░░░░░██░░ ░░ ░░ 
                                                                    ███ ░███         
                                                                    ░░██████          
                                                                    ░░░░░░              
              \n 
                                                                                                        
                █████                              █████
                ░░███                              ░░███ 
                ░███████    ██████   ████████   ███████ 
                ░███░░███  ░░░░░███ ░░███░░███ ███░░███ 
                ░███ ░███   ███████  ░███ ░░░ ░███ ░███ 
                ░███ ░███  ███░░███  ░███     ░███ ░███ 
                ████ █████░░████████ █████    ░░████████
                ░░░░ ░░░░░  ░░░░░░░░ ░░░░░      ░░░░░░░░ 
                            \n
              ''')
        print("Tendrás que pasarte el juego base para poder elegir esta dificultad, \nasí como obtener el DLC: Colinas Terroríficas, inténtalo de nuevo pulsando ENTER ")
        input()
        
    else:
        print(Fore.LIGHTCYAN_EX + '''                                                                                                                    
                                                                                                                                                    
                ████                         ████  ███                              
                ░███                        ░░███  ░░░                               
                ░███   ██████   ██████    ███████  ████  ████████    ███████         
                ░███  ███░░███ ░░░░░███  ███░░███ ░░███ ░░███░░███  ███░░███         
                ░███ ░███ ░███  ███████ ░███ ░███  ░███  ░███ ░███ ░███ ░███         
                ░███ ░███ ░███ ███░░███ ░███ ░███  ░███  ░███ ░███ ░███ ░███         
                █████░░██████ ░░████████░░████████ █████ ████ █████░░███████ ██ ██ ██
                ░░░░░  ░░░░░░   ░░░░░░░░  ░░░░░░░░ ░░░░░ ░░░░ ░░░░░  ░░░░░██░░ ░░ ░░ 
                                                                    ███ ░███         
                                                                    ░░██████          
                                                                    ░░░░░░              
              \n
                                
                  ██████  ████████  ████████   ██████  ████████           
                 ███░░███░░███░░███░░███░░███ ███░░███░░███░░███          
                ░███████  ░███ ░░░  ░███ ░░░ ░███ ░███ ░███ ░░░           
                ░███░░░   ░███      ░███     ░███ ░███ ░███               
                ░░██████  █████     █████    ░░██████  █████     █████████
                ░░░░░░  ░░░░░     ░░░░░      ░░░░░░  ░░░░░     ░░░░░░░░░ 
                                                                        
               \n                                                         
                                                                        
                █████ █████     █████    █████ █████                     
                ░███ ░░███    ███░░░███ ░░███ ░░███                      
                ░███  ░███ █ ███   ░░███ ░███  ░███ █                    
                ░███████████░███    ░███ ░███████████                    
                ░░░░░░░███░█░███    ░███ ░░░░░░░███░█                    
                      ░███░ ░░███   ███        ░███░                     
                      █████  ░░░█████░         █████                     
                      ░░░░░     ░░░░░░         ░░░░░                      
                            
              


              \n''')
        print("No has seleccionado un número correcto, elige entre 1, 2 y 3 para proseguir ")
        pygame.mixer.music.load("audio/Error.mp3")
        pygame.mixer.music.play(1)
        input("Vuelve al menú y selecciona otra dificultad pulsando ENTER ")
        
input()
os.system ("cls")

#Almaceno el nombre del / de la protagonista y del personaje secundario

print(Fore.LIGHTWHITE_EX + '''

       ░░▒▒▒▒             
      ▒░░▒▒▓▓▒            
       ▒░░░▓▓▒            
       ░░░░▒▒             
       ▓▓▒▒▓▓▓█▓█▓▓       
     ▓▓▒█░▒▓▒▓▒▒▒▒▓█▓     
    ▓▓▒▒▓▒▓▒▒▒░▒▒▓██▓▓    
    ██▓▓▓▒▓▒▒▒▒▓█▓███▓▓   
    ▓█▓▓█▒▒▒▒▒▓▓▓█████▓▓  
    ███▓█▓▒▒▒▓██████████  
   ▓▒▓█▓██▓▓▒▓███████████ 
   ▒▒█████▓▓▓▓███████████ 
  ▒▒███████▓▒▓▓███████▓███
 ▓▒▓██▓███▓▒▒▒▒███████▓███
  ░████████▒▒▒▒▓▓█████▓▓▓▓
░▓▓▓  █████▓▓▓▓▓▓▓████ ▒▒░
      ███████▓▒▓██████░▒░░
       ██████▓▒▓███▓▒   ░ 
       ▓▓████▓▒▓▓██       
       ▓▓████▒▒▓▓██       
       ▓▓███▓▒▒▓▓█        
       ▓▓███▓▓▓▓██        
       ██████▓▓███        
        █████▓▓███        
         █████▓███▓       
         █████▓███        
          ████▓▓██        
           ███▓███▓       
         █████▓███▓       
         ████▓▓▓██▓       
             ████         
                 
      ''')        



nombre_prota = input("Para comenzar esta aventura, elige el nombre del protagonista y presiona ENTER para continuar: ") 
nombre_prota_mayus = nombre_prota.capitalize()


nombre_amigo = input("\nAhora piensa en el nombre de un amigo o amiga al que le tengas aprecio, \n puesto que ha desaparecido y serás tú la única persona que podrá resolver este misterio: ")
nombre_amigo_mayus = nombre_amigo.capitalize()

os.system("cls")


#Contextualizo sobre el juego

print(Fore.LIGHTRED_EX + '''                                                                
                                                                
                                                                
                                                                
               ░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░                       
               ░▓▓▓▓▓▓▓▒▓▓▓▓▒▓▓▒▒▓▓▓▓▓▓▓░                       
               ░▓▓▓▓▓▓▓▒▓▓▓▒░▓▓▒▓▓▓▓▓▓▓▓░                       
               ░▓▓▓▓▓▓▓▒▒▒▓▒▒▓▓▓░▓▓▓▓▓▓▓░                       
               ░▓▓▓▓▓▓▓▓▒▓▓▓▓▒▓▒▒▓▓▓▓▓▓▓░                       
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
    ░░                    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  
    ░░                    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  
    ░░                    ░░░░░▓████████████████████████▒░░░░░  
    ░░                    ░░░░░▓██████████████████████▓▓▒░░░░░  
    ░░▓▓▓▓                ░░░░░▓█████████████████████▓▓▓▒░░░░░  
    ░▓▓██▓▓               ░░░░░▓██████▓▓███████████▓▓▓▓▓▒░░░░░  
    ░▒▓▓▓▓▓▓              ░░░░░▓███▓▓▓▓▓▓▓██████▓▓▓▓▓▓▓▓▒░░░░░  
 ▒ ▓▓▓▓▓▓▓▓▓▓             ░░░░░▓███▓███▓▓▓███▓▓▓▓▓▓▓▓▓▓▓▒░░░░░  
▒▒▓▓░░░▒░░░▒▓▓            ░░░░░▓███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░░░░░  
▒▒▓▓░░░░░░░▒▓▓            ░░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░░░  
▒▒▓▓▒▒▒▒▒▒▒▒▓▓            ░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░  
 ▓▓▓▓▓▓▓▓▓▓▓▓▓            ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  
 █▓▓▒▓▓▓▓▓▓▓▓▓            ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  
 █▓▓▒▓▓▓▓▓▓▓▓▓            ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  
 █▓▓▓▓▓▓▓▓▓▓▓▓            ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  
 █▓▓▓▓▓▓▓▓▓▓▓▓            ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  
  ▓▓▓▓▓▓▓▓▓▓▓▓            ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  
▒▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒_                                           
                                                                
                                                                ''')

pygame.mixer.music.load("audio/keyboard.mp3")
pygame.mixer.music.play(2)
print(f"Mi nombre es {Fore.LIGHTMAGENTA_EX}{nombre_prota_mayus}{Style.RESET_ALL}, no consigo recordar cuándo llegué a este sitio, ni siquiera aparecía en el mapa,\nsolo vine buscando a una persona muy importante para mí: {Fore.LIGHTBLUE_EX}{nombre_amigo_mayus}{Style.RESET_ALL}, lleva en paradero desconocido un par de meses…")
contexto = "\nAl principio, todos pensábamos que era algo temporal. \nEra de esas personas que desaparecían durante semanas, siempre pensando en ideas extrañas o proyectos secretos, así que nadie se preocupó demasiado."
for letra in contexto:
    print(letra, end="", flush=True)
    time.sleep(0.01)
    

#Continúo con el contexto
input()
os.system ("cls")
print(Fore.LIGHTRED_EX + '''                                                                
                                                                
                                                                
                                                                
               ░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░                       
               ░▓▓▓▓▓▓▓▒▓▓▓▓▒▓▓▒▒▓▓▓▓▓▓▓░                       
               ░▓▓▓▓▓▓▓▒▓▓▓▒░▓▓▒▓▓▓▓▓▓▓▓░                       
               ░▓▓▓▓▓▓▓▒▒▒▓▒▒▓▓▓░▓▓▓▓▓▓▓░                       
               ░▓▓▓▓▓▓▓▓▒▓▓▓▓▒▓▒▒▓▓▓▓▓▓▓░                       
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
    ░░                    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  
    ░░                    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  
    ░░                    ░░░░░▓████████████████████████▒░░░░░  
    ░░                    ░░░░░▓██████████████████████▓▓▒░░░░░  
    ░░▓▓▓▓                ░░░░░▓█████████████████████▓▓▓▒░░░░░  
    ░▓▓██▓▓               ░░░░░▓██████▓▓███████████▓▓▓▓▓▒░░░░░  
    ░▒▓▓▓▓▓▓              ░░░░░▓███▓▓▓▓▓▓▓██████▓▓▓▓▓▓▓▓▒░░░░░  
 ▒ ▓▓▓▓▓▓▓▓▓▓             ░░░░░▓███▓███▓▓▓███▓▓▓▓▓▓▓▓▓▓▓▒░░░░░  
▒▒▓▓░░░▒░░░▒▓▓            ░░░░░▓███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░░░░░  
▒▒▓▓░░░░░░░▒▓▓            ░░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░░░  
▒▒▓▓▒▒▒▒▒▒▒▒▓▓            ░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░  
 ▓▓▓▓▓▓▓▓▓▓▓▓▓            ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  
 █▓▓▒▓▓▓▓▓▓▓▓▓            ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  
 █▓▓▒▓▓▓▓▓▓▓▓▓            ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  
 █▓▓▓▓▓▓▓▓▓▓▓▓            ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  
 █▓▓▓▓▓▓▓▓▓▓▓▓            ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  
  ▓▓▓▓▓▓▓▓▓▓▓▓            ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  
▒▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒_                                           
                                                                
                                                                ''')

contexto_2 = "\nPero con el tiempo, el silencio se volvió insoportable. Algo no encajaba... \nSus mensajes dejaron de llegar, no contestaba a las llamadas. Me acerqué a su casa y todo el mundo me decía que no tenían ni idea de dónde podría estar.\n\nSin embargo, había una pista: un cuaderno olvidado en el suelo, lleno de anotaciones extrañas y referencias a un lugar del que nunca había oído hablar: 'Colinas Silenciosas' \nAl leerlo, una sensación de inquietud se apoderó de mí. Era como si las páginas intentaran advertirme de algo, pero también me guiaban. \nEse era el último lugar donde había estado. No puedo ignorarlo más. \nTengo que ir allí y descubrir qué le pasó. Tal vez esté vivo… tal vez no. Pero no voy a quedarme de brazos cruzados"

for letra in contexto_2:
    print(letra, end="", flush=True)
    time.sleep(0.01)

input()
os.system("cls")


#Indico la mecánica / recomendaciones del juego

print(Fore.LIGHTRED_EX + '''                                                                
                                                                
                                                                
                                                                
               ░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░                       
               ░▓▓▓▓▓▓▓▒▓▓▓▓▒▓▓▒▒▓▓▓▓▓▓▓░                       
               ░▓▓▓▓▓▓▓▒▓▓▓▒░▓▓▒▓▓▓▓▓▓▓▓░                       
               ░▓▓▓▓▓▓▓▒▒▒▓▒▒▓▓▓░▓▓▓▓▓▓▓░                       
               ░▓▓▓▓▓▓▓▓▒▓▓▓▓▒▓▒▒▓▓▓▓▓▓▓░                       
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
    ░░                    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  
    ░░                    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  
    ░░                    ░░░░░▓████████████████████████▒░░░░░  
    ░░                    ░░░░░▓██████████████████████▓▓▒░░░░░  
    ░░▓▓▓▓                ░░░░░▓█████████████████████▓▓▓▒░░░░░  
    ░▓▓██▓▓               ░░░░░▓██████▓▓███████████▓▓▓▓▓▒░░░░░  
    ░▒▓▓▓▓▓▓              ░░░░░▓███▓▓▓▓▓▓▓██████▓▓▓▓▓▓▓▓▒░░░░░  
 ▒ ▓▓▓▓▓▓▓▓▓▓             ░░░░░▓███▓███▓▓▓███▓▓▓▓▓▓▓▓▓▓▓▒░░░░░  
▒▒▓▓░░░▒░░░▒▓▓            ░░░░░▓███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░░░░░  
▒▒▓▓░░░░░░░▒▓▓            ░░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░░░  
▒▒▓▓▒▒▒▒▒▒▒▒▓▓            ░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░  
 ▓▓▓▓▓▓▓▓▓▓▓▓▓            ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  
 █▓▓▒▓▓▓▓▓▓▓▓▓            ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  
 █▓▓▒▓▓▓▓▓▓▓▓▓            ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  
 █▓▓▓▓▓▓▓▓▓▓▓▓            ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  
 █▓▓▓▓▓▓▓▓▓▓▓▓            ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  
  ▓▓▓▓▓▓▓▓▓▓▓▓            ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  
▒▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒_                                           
                                                                
                                                                ''')
pygame.mixer.music.load("audio/Walking.mp3")
pygame.mixer.music.play(3)

mecanica = "Mecánica del juego:\n\nVidas limitadas: Cada vez que atacas o te defiendes de un enemigo perderás vida, vigila tu indicador de vida para proseguir con tu aventura\n\nExploración: Navega por un mundo oscuro y lleno de secretos. Cada rincón puede contener respuestas sobre tu amigo o hundirte más en el misterio.\n\nDecisiones: Las elecciones que tomes moldearán el desenlace.\n¿Descubrirás la verdad a tiempo, o quedarás atrapado en el mismo lugar que él?, a veces dependerán del azar, así que:\n\nAl atacar podrás hacerle daño al enemigo, al defenderte tú perderas menos vida, todo depende de ti."


for letra in mecanica:
    print(letra, end="", flush=True)
    time.sleep(0.01)


input()
os.system("cls")


pygame.mixer.music.load("audio/gong.mp3")
pygame.mixer.music.play(1)


#Inserto la frase del sabio

print(Fore.YELLOW + ''' 
                                              
                                            
                     ███████                
                    █████▓▓██               
                   ████▓▓▓▓▓▓               
                   █▒█▓▓▒▒▓▓▓▓              
                    ▒▒▓▒▒▒▓▒▓▓           ▒▓ 
                    ▓▓▒▒▒▒▒▓▓           ▒▓  
                    ▒▒▒▓▓▓▓▓▓           ▒▓  
                  ▒▓▒▒░░▒▓▓            ▒▒▒▒ 
                 ▓░▒▒▒▒▒▒▒▓▒          ▒▒▒▒▓ 
                ▒▒▒▒▒░▒▒▒▒▒▒▒    ▒▒▒░▒▒▒▓▓  
                ▒▓▒▒▒░▒▒▒▒▒▒▒▒▒▒░░░░░▒▒     
               ░▒▓▒▒▒▒▒░░▒▒░▒░░░░░░░░▒      
               ░░▒▒▒▒▒▒▒▒░░░░░░░░░░░░░      
               ▒░░▒▒▒▒▓▒▒▒░░░░░░░░░░░░▒     
               ▒░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒         
              ▒▒░░░░░░░░▒▒▒▒▒▒▒▒▒░▒▒        
              ▒░░▒░░░░░░▒▒▒▒▒▒▒░░▒▒▒▒       
              ▒▒░▒░▒░░░░▒▒▒▒░▒▒░░▒▒▒▒       
             ▒▒░░░░░░░░░▒▒▒▒▒▒▒▒▒▒░░░▒▒     
             ▒▒░░░░░░░░▒░▒▒▒▒▒▒▒▒▒░░░░▒▒    
            ▒▒░░░▒░░░░░▒░▒▒▒▒▒▒  ▒▒▒░░▓▓▓   
            ▒▒░░░░░░░░░▒▒▒▒▒▒▒▒▒  ▒▒▒▓▓▓▓▓▓▓
            ░░░▒▒░░░░░░▒░▒▒▒▒░▒▒      ▓     
           ▒░▒▒░░░░░░░░░▒▒░▒▒▒░░▒▒          
           ░░░░░░░░░░░░░▒▒░░░░░░░░▒         
          ▒▒░░░░░░░░░▒░░▒▒▒░░░░▒▒▒▒▒        
         ▒░░░░░░░░░░░░░▒░░▒░░▒▒▒▒░░▒▒       
         ░░░░░░░░▒▒▒      ▒▒▒▒▒░░░░░▒▒      
        ▒▒░░░░░▒▒▒         ▒▒▒░░░░░▒▒▒      
      ▓▒▒░░░░▒▒▒▒           ▒▒▒░░░▒▒▒▒      
     ▓▓▓▒▒▒▒▒▒▒▒             ▒░░░▒▒░▒▒      
    ▓▒▒▒▒▒▒▒▒▒▒              ▒▒▒▒░░▒▒       
   ▓▒▒▒▒▒▒▒▒▒▒              ▒▒▒▒░░▒▒▒       
   ▓▓▒▒▒▒▒▒▒      ████████   ▒▒░▒▒░▒▒       
 ▒▒▒▒▒▒▒▒▒   ███████████████▒▒▒▒▒▒▒▒        
▒▒▒▒▒▒▒▒▓ ██████████████████▒▒▒▒▒▓▒         
▒▒▒▒▓█████████            ██▒▒▒▒▒▒▒         
                            █▒▒▒▒░▒▒▒       
                                 ▒░░▒▒      

 ''')
print(Fore.LIGHTBLUE_EX + "\n'Al saber lo llaman suerte'")

input()
os.system("cls")




vida_jugador = 100
  
#Al ser un bucle muy grande, en primer lugar los lugares para visitar y en su interior: qué puerta elige y si ataca o defiende para obtener las placas

while True:
        #Menú principal donde elegir por donde empezar y también salir del bucle
        
          os.system("cls")
          pygame.mixer.music.load("audio/pajaros.mp3")
          pygame.mixer.music.play(1)

          print(Fore.LIGHTWHITE_EX +"Llegué a través de la ruta secundaria en la salida de una gasolinera, todo parece estar desolado y lleno de niebla,\nencontré un mapa que indicaba los lugares principales de este pequeño pueblo, debería elegir primero hacia donde ir: ")
          eleccion = int(input("\n1.Hospital\n2.Centro Comercial\n3.Ya he terminado de explorar ambos\nEmpezaré por: "))

          #Opción para salir del bucle
          
          if eleccion == 3:
              print("\n\nYa has reunido todo lo necesario para continuar la aventura, te diriges hacia tu coche")
              break
            
          #Opción hospital
          
          elif eleccion == 1:
                  os.system("cls")
                  print("Has decidido comenzar la búsqueda en el Hospital")
                  
                  
                  print(Fore.LIGHTBLUE_EX + '''\n                                                                             
                                                        
                                                                    
                    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                 
                    ▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█                
                    ▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓█                
                    ██▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓█                
        ██▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░▒▓▓▓▓▓▓▓▓▓▓▓▓█     
        ▓▓▒▒▒▒▒▒▒▒▒▒▒▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░▒▓▒▒▒▒▒▒▒▒▒▒▒▓▓    
        ▓▓▒▒▒▒▒▒▒▒▒▒▒▓▓░░░░░░░░░░▒▓▓▓▓▓░░░░░░░░░░▒▓▒▒▒▒▒▒▒▒▒▒▒▓▓    
        █▓▓▒▒▒▒▒▒▒▒▒▓▓░░░░░░░░▒▒▓▓▒▒▓▓▒▒░░░░░░░░▒▓▒▒▒▒▒▒▒▒▒▓▓█     
          ▓▒░░░▒▒▒░░░▓▓░░░░░░░▓▓▒▒▒▒▒▒▒▒▓▓░░░░░░░▒▓░░░▒▒▒░░░▒█▓     
          ▓▒░░▓▓▓▓▓░░▓▓░░░░░░░▓▓▒▒▒▒▒▒▒▒▓▓░░░░░░░▒▓░░▓▓▓▓▓░░▒█▓     
          ▓▒░░▓▓▒▓▓░░▓▓░░░░░░░░▒▒▓▓▒▒▓▓▒▒░░░░░░░░▒▓░░▓▓▒▒▓░░▒█▓     
          ▓▒░░▓▓▒▓▓░░▓▓░░░░░░░░░░▒▓▓▓▓▓░░░░░░░░░░▒▓░░▓▓▒▒▓░░▒█▓     
          ▓▒░░▒▓▓▓░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░▒▓░░░▓▓▓▒░░▒█▓     
          ▓▒░░░░░░░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░▒▓░░░░░░░░░▒█▓     
          ▓▒░░▓▓▓▓▓░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░▒▓░░▓▓▓▓▓░░▒█▓     
          ▓▒░░▓▓▒▓▓░░▓▓░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░▒▓░░▓▓▒▓▓░░▒█▓     
          ▓▒░░▓▓▒▓▓░░▓▓░░░▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓░░░▒▓░░▓▓▒▒▓░░▒█▓     
          ▓▒░░▒▓▓▓░░░▓▓░░░▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓░░░▒▓░░░▓▓▓▒░░▒█▓     
          ▓▒░░░░░░░░░▓▓░░░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░░░▒▓░░░░░░░░░▒█▓     
          ▓▒░░▓▓▓▓▓░░▓▓░░░░▒▓▒▒▒▒▒▒▓▓▒▒▒▒▒▒▓▓░░░░▒▓░░▓▓▓▓▓░░▒█▓     
          ▓▒░░▓▓▒▓▓░░▓▓░░░░▒▓▒▒▒▒▒▒▓▓▒▒▒▒▒▒▓▓░░░░▒▓░░▓▓▒▓▓░░▒█▓     
          ▓▒░░▓▓▒▓▓░░▓▓░░░░▒▓▒▒▒▒▒▒▓▓▒▒▒▒▒▒▓▓░░░░▒▓░░▓▓▒▒▓░░▒█▓     
          ▓▒░░▓▓▓▓▒░░▓▓░░░░▒▓▒▒▒▒▒▒▓▓▒▒▒▒▒▒▓▓░░░░▒▓░░▒▓▓▓▓░░▒█▓     
          ▓▒░░░░░░░░░▓▓░░░░▒▓▒▒▒▒▒▒▓▓▒▒▒▒▒▒▓▓░░░░▒▓░░░░░░░░░▒█▓     
          ▓▒░░░░░░░░░▓▓░░░░▒▓▒▒▒▒▒▒▓▓▒▒▒▒▒▒▓▓░░░░▒▓░░░░░░░░░▒█▓     
          ▓▒░░░░░░░░░▓▓░░░░▒▓▒▒▒▒▒▒▓▓▒▒▒▒▒▒▓▓░░░░▒▓░░░░░░░░░▒█▓     
          ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      
          ███▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███▓████''')                                   

    
                  input()
                  os.system("cls")
                  
                  
                  pygame.mixer.music.load("audio/hospital_corto.mp3")
                  pygame.mixer.music.play(1)
                  
                  #Contexto del hospital
                  
                  print(Fore.LIGHTCYAN_EX + '''
                                  
                                  
                    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
                    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
                    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
                    ░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▓░░░░░
                    ░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▓▓░░░░░
                    ░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▓▓░░░░░
                    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒░░░░░
                    ░░▒░░░░░░░░▒▒░░░░░░░▒▒░░▓▓▓▓▓▓▓▓▓▓▓▒░░░░░
                    ░░▒░░░░░░░░▒▒░░░░░░░░▒░░▓▓▓▓▓▓▓▓▓▓▓░░░░░░
                    ░░▒░░░░░░░░░▒░░░░░░▒▒▓▓▓▓▓▓▓▓▓▒▒▓▓▓░░░░░░
                    ░░▒░░░░░░░░▒▒░░░░░░░▒▒▒▒▒▒▒▓▓▓▒▒▒▒░░░░░░░
                    ░░▒░░░░░░░▒▒▒░░░░░░░▒▒░░░░░▒▒░░▒░░░░░░░░░
                    ░░▒░░░░░░░▒▒▒░░░░░░░▒▒░░░░░▒▓░░▒░░░░░░░░░
                    ░░▒░░░░░░░▒▒▒░░░░░░░▒▒░▒▒▒▓▓▓▓▒▒▒░░░░░░░░
                    ░░▒░░░░░░▒▒▒▒░░░░░░░▒▓▒░░▓▒░░▒▒▒░▓▒░░░░░░             
                      
                        
                        ''')
                  
                  hospital = "Al atravesar la puerta del hospital, el mundo parece detenerse, el silencio invade el vestíbulo, \nno percibes ninguna presencia humana, no hay nadie en recepción, las luces no dejan de parpadear \n\nFrente a ti hay dos puertas: una a la izquierda cuya madera parece hinchada por el tiempo y a la derecha, una desgastada puerta metálica.\nAlgo te dice que lo que investigues detrás de esas puertas podría ayudarte en tu búsqueda..."
                  
                  for letra in hospital:
                    print(letra, end="", flush=True)
                    time.sleep(0.01)
                    
                  
                  input()
                  os.system("cls")

                  #Aquí empieza el bucle de elegir puertas dentro del hospital que continúa hasta agotar turnos
                  
                  while True:
                    
                    #Menú de puertas y salir del bucle para volver al menú principal
                    
                      print("\n¿Qué puerta vas a elegir primero?:")
                      print("1. Abrir la puerta izquierda")
                      print("2. Abrir la puerta derecha")
                      print("3.Ya he explorado ambas puertas, quiero seguir.")
                      puerta = int(input("Elijo la opción: "))

                      #Puerta izquierda
                      if puerta == 1:
                          os.system("cls")
                          print(Fore.LIGHTYELLOW_EX + '''

                             ▓▒▓▒▓             
                           ▓▓▓▓▒▓▓▓            
                           ▓▓▓▒▒█▓██           
                            █▓▒▓▓██            
                            ▓▓▒▓██             
                            ▓▓▓▓██             
                             ▓▓▓█              
                            ▓▒▒▒▓▓▓▓▓          
                        ▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓        
                       ▓▒▓▒▒▒▓▒▒▓▓▒▒▓▓█        
 ▓                     ▓▓█▓▓▓▒▒▓▒▓▒░███        
   ▒▓                 ▓▓▓█▓▓▓▓▓███▓▓███        
      ▓              ▒▒▒▓  ▓▒▓▒▒▒▒▒▒▓▓█        
        ▓▓▓          ▒▒▓    ▓▓▒▒▓▒▓▒████       
         ▓▓▓█    ▓▓▓▒▒█      ▓▒▒▒▓▓▓▓██▓▒▒     
           ▓▓██▒▒▓▓▓▓        ▒▒▒▓▓▓▓▓█▓  ▒▒▒▓  
                            ▓▒▒▒▒▒▓▓▓▓▓    ▓▓▓ 
                            ▓▒▒▓▒▓▓▓█▓▓▓    ▓▓▓
                            ▓▒▒▓▓▓▓▓▓▓▓▓       
                           ▓▒▒▒▓▒▓▒▓▓▒▓▓█      
                           ▓▓▒▒▓▓▓▓▓▒▓▒▒▓      
                          ▒▓▓▒▒▓▓▓▒▒▓▒▒▒▓      
                          ▓▒▒▒▒▓▓▒▓▓▒▒▒▒▓▓     
                          ▓▒▓▒▓█    ▓▓▒▒▓▓     
                          ▓▒▒▒▓█    ▓▓▒▒▓█     
                          ▓▓▓▓▓      ▓▓▒▓█     
                          ▓▓▓▓█       ▓▓▓█     
                         ▓▒▓▓█        ▓▓▓██    
                         ▓▓▓█          ▓▓▓▓    
                         ▓▓█           ▓▓▓     
                         ▓▓             ▓▓     
                        ▒▓▓             ▓▒▓    
                        ▒▒              ▓▒▓    
                        ▓▓█              ▒▓▓   
                         ▒                ▒    ''')
                          print(Fore.LIGHTBLUE_EX + "\n¡¡Oh no!!, te has encontrado con una enfermera loca, tiene muchas ganas de luchar contigo, no hay una razón lógica para ello. \nDispones de una vida de 100, la enfermera tiene 50, tenlo presente y ten cuidado en el combate puesto que constará de 3 turnos.")
                          pygame.mixer.music.load("audio/risa mujer.mp3")
                          pygame.mixer.music.play(1)
                          vida_enemigo = 50
                          turnos = 3
                          
                          #Pelea puerta izquierda
                          
                          while turnos > 0 and vida_enemigo > 0 and vida_jugador > 0:
                              print(f"\nTu vida: {vida_jugador} | Vida enemiga: {vida_enemigo}")
                              accion = int(input("¿Qué quieres hacer? (1. Atacar, 2. Defenderte): "))
                              os.system("cls")
                              
                              if accion == 1:
                                
                                #Ataque
                                  os.system("cls")
                                  pygame.mixer.music.load("audio/pipe.mp3")
                                  pygame.mixer.music.play(1)
                                  print(Fore.LIGHTYELLOW_EX + '''

                             ▓▒▓▒▓             
                           ▓▓▓▓▒▓▓▓            
                           ▓▓▓▒▒█▓██           
                            █▓▒▓▓██            
                            ▓▓▒▓██             
                            ▓▓▓▓██             
                             ▓▓▓█              
                            ▓▒▒▒▓▓▓▓▓          
                        ▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓        
                       ▓▒▓▒▒▒▓▒▒▓▓▒▒▓▓█        
 ▓                     ▓▓█▓▓▓▒▒▓▒▓▒░███        
   ▒▓                 ▓▓▓█▓▓▓▓▓███▓▓███        
      ▓              ▒▒▒▓  ▓▒▓▒▒▒▒▒▒▓▓█        
        ▓▓▓          ▒▒▓    ▓▓▒▒▓▒▓▒████       
         ▓▓▓█    ▓▓▓▒▒█      ▓▒▒▒▓▓▓▓██▓▒▒     
           ▓▓██▒▒▓▓▓▓        ▒▒▒▓▓▓▓▓█▓  ▒▒▒▓  
                            ▓▒▒▒▒▒▓▓▓▓▓    ▓▓▓ 
                            ▓▒▒▓▒▓▓▓█▓▓▓    ▓▓▓
                            ▓▒▒▓▓▓▓▓▓▓▓▓       
                           ▓▒▒▒▓▒▓▒▓▓▒▓▓█      
                           ▓▓▒▒▓▓▓▓▓▒▓▒▒▓      
                          ▒▓▓▒▒▓▓▓▒▒▓▒▒▒▓      
                          ▓▒▒▒▒▓▓▒▓▓▒▒▒▒▓▓     
                          ▓▒▓▒▓█    ▓▓▒▒▓▓     
                          ▓▒▒▒▓█    ▓▓▒▒▓█     
                          ▓▓▓▓▓      ▓▓▒▓█     
                          ▓▓▓▓█       ▓▓▓█     
                         ▓▒▓▓█        ▓▓▓██    
                         ▓▓▓█          ▓▓▓▓    
                         ▓▓█           ▓▓▓     
                         ▓▓             ▓▓     
                        ▒▓▓             ▓▒▓    
                        ▒▒              ▓▒▓    
                        ▓▓█              ▒▓▓   
                         ▒                ▒    ''')
                                  daño = random.randint(10, 30)
                                  vida_enemigo -= daño
                                  print(f"Atacas al enemigo y le haces {Fore.RED}{daño}{Style.RESET_ALL} de daño.")
                                  daño_enemigo = random.randint(0, 10)
                                  vida_jugador -= daño_enemigo
                                  print(f"\nEl enemigo contraataca y te hace {Fore.RED}{daño_enemigo}{Style.RESET_ALL} de daño.")
                                  
                              elif accion == 2:
                                  os.system("cls")
                                  #Defensa
                                  
                                  pygame.mixer.music.load("audio/defensa.mp3")
                                  pygame.mixer.music.play(3)
                                  daño = random.randint(0,5)
                                  vida_jugador -= daño
                                  print(Fore.LIGHTYELLOW_EX + '''

                             ▓▒▓▒▓             
                           ▓▓▓▓▒▓▓▓            
                           ▓▓▓▒▒█▓██           
                            █▓▒▓▓██            
                            ▓▓▒▓██             
                            ▓▓▓▓██             
                             ▓▓▓█              
                            ▓▒▒▒▓▓▓▓▓          
                        ▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓        
                       ▓▒▓▒▒▒▓▒▒▓▓▒▒▓▓█        
 ▓                     ▓▓█▓▓▓▒▒▓▒▓▒░███        
   ▒▓                 ▓▓▓█▓▓▓▓▓███▓▓███        
      ▓              ▒▒▒▓  ▓▒▓▒▒▒▒▒▒▓▓█        
        ▓▓▓          ▒▒▓    ▓▓▒▒▓▒▓▒████       
         ▓▓▓█    ▓▓▓▒▒█      ▓▒▒▒▓▓▓▓██▓▒▒     
           ▓▓██▒▒▓▓▓▓        ▒▒▒▓▓▓▓▓█▓  ▒▒▒▓  
                            ▓▒▒▒▒▒▓▓▓▓▓    ▓▓▓ 
                            ▓▒▒▓▒▓▓▓█▓▓▓    ▓▓▓
                            ▓▒▒▓▓▓▓▓▓▓▓▓       
                           ▓▒▒▒▓▒▓▒▓▓▒▓▓█      
                           ▓▓▒▒▓▓▓▓▓▒▓▒▒▓      
                          ▒▓▓▒▒▓▓▓▒▒▓▒▒▒▓      
                          ▓▒▒▒▒▓▓▒▓▓▒▒▒▒▓▓     
                          ▓▒▓▒▓█    ▓▓▒▒▓▓     
                          ▓▒▒▒▓█    ▓▓▒▒▓█     
                          ▓▓▓▓▓      ▓▓▒▓█     
                          ▓▓▓▓█       ▓▓▓█     
                         ▓▒▓▓█        ▓▓▓██    
                         ▓▓▓█          ▓▓▓▓    
                         ▓▓█           ▓▓▓     
                         ▓▓             ▓▓     
                        ▒▓▓             ▓▒▓    
                        ▒▒              ▓▒▓    
                        ▓▓█              ▒▓▓   
                         ▒                ▒    ''')
                                  
                                  print(f"Te defiendes, pero recibes {daño} de daño.")
                                
                                  
                              #Si no elige ni 1 ni 2  
                              else:
                                  os.system("cls")
                                  print("Acción no válida, pierdes un turno.")
                                
                                  
                              turnos -= 1

                          
                              input()
                              os.system("cls")
                            
                              #Si se agotan los turnos
                              if turnos == 0 or (turnos <3 and vida_enemigo<=0):
                                  os.system("cls")
                                  print("\nPodrías haberlo hecho mejor, aunque te lo dejo pasar por esta vez")
                                  print(Fore.BLUE + '''\n
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
                      XX X  X X    X  XX XXXXX    XX
                      XX XX X XX  XX  XX XXXXXX   XX
                      XXXXX X XXXXXXXXXXXXXX  X   XX
                      XX  XXXX  XX    XXXXXXXX X  XX
                      XXXX  X  XX   XX  XX  XXXX  XX
                      XX  XX XX     XX  X  XXXX XXXX
                      XX  XX X XX   X   X   X   XXXX
                      XXX    XXX    X XXX  XX   X XX
                      XX    XX  XXX  XXXXXX    X  XX
                      XX   XXXX   XXXX XX   XXX XXXX
                      XX X X   X X  X        XXX  XX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX''')
                                  print(Fore.BLUE + "\n\n\nHas obtenido la placa color azul")
                                  input("\n\nPulsa ENTER para regresar al menú de puertas...")
                                  os.system("cls")
                                  break
                             
                                  # Regresar al menú de puertas
                                  
                            
                      # Puerta derecha
                      elif puerta == 2:
                          os.system("cls")
                          print("Has decidido entrar por la puerta derecha: ")
                          pygame.mixer.music.load("audio/risa virus.mp3")
                          pygame.mixer.music.play(1)
                          print(Fore.LIGHTGREEN_EX +'''\n

                          █████████                      
                          █▒▒▒▒▒▒▒██                     
            ████           ███▒▒███          ████        
          ██░░░█        ██████▒▒█████        ██▒▒██      
          █▓░░░██      ░█░░░░░░░░░░▒▒▒████    ██▒▒▒▒██    
        ██░░▓░░▓████░░░░░░░░░░░░░░░░░░▒▒▒█████▒▒▒▒▒▒█    
          ███ ██░░▒░░░░░░░░░░░░░░░░░░░░░░▒▒▒█▒▒▒██████    
              ██░░░░░███▒░░░░░░░░░░░░░░░░░▒▒▒██          
              █▓░░░███▒▒▒▓██░░░░░░░░░░░░░░░░▒▒▒██         
            █▒░░░██▒▒▒▒▒▒▒██░░░░░░░░░░░░░░░░▒▒▒▒█        
            ██░░░░██▒▒▒▒▒▒▒██░░░░░░░░░░░░░░░░░▒▒▒██       
          ██░░░░░░██▒▒▒▒▒▓█░░░░░░░░░░░░░░░░░░▒▒▒▒██      
      █▓██ █▒░░░░░░░███████░░░░░░░░░░░░░░░░░░░░▒▒▒▒█ ████ 
      ██░░███░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒███▒▒██
      ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒██
      ██░░███░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█████▒▒▒▒███▒▒██
      ████ █▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░██▒▒▒█▒▒▒▒█ ████ 
          ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█████▒▒▒██      
            ██░░░░░░░░░░░░░░░░░░░░░▒██░░░░░░░░▒▒▒██       
            █▒░░░░░░░░░░░░░░░░░░██▒▒▒██░░░░░▒▒▒▒█        
              ██░░░░░░░░░░░░░░░░░█▒▒▒▒▒██░░░▒▒▒██         
              ██░░░░░░░░░░░░░░░░██▒▒▒▒██░░▒▒▒██          
        ██████▒░░█░░░░░░░░░░░░░░░▓████░░▒▒▒▒▒▒██ ███     
        █░░░░░░█████░░░░░░░░░░░░░░░░░░▒▒▒████▓▒▒▓▒▒██    
        ██▒░░░██    ████░░░░░░░░░░░▒▒████    ██▒▒▒▒█     
          ██▒░██        █████▒▒██████        █▒▒▒▒       
            ████          ███▒▒███           ████        
                          ██▒▒▒▒▒▒▒█                      
                          █████████                      ''')
                          print(f"\n ¡¡Oh no!!, te has encontrado con Don Virus, cuidado porque quiere contagiarte de un virus desconocido, con la salud como un roble que tienes tú.\nDispones de una vida de limitada, y Don Virus de 40, tenlo presente y ten cuidado en el combate puesto que constará de 3 turnos.\nSi fuera tú no querría contagiarme")
                          
                          vida_enemigo = 40
                          turnos = 3

                          #Combate ataque / defensa hasta agotar turnos
                          
                          while turnos > 0 and vida_enemigo > 0 and vida_jugador > 0:
                              print(f"\nTu vida: {vida_jugador} | Vida enemiga: {vida_enemigo}")
                              accion = int(input("¿Qué quieres hacer? (1. Atacar, 2. Defenderte): "))
                              os.system("cls")
                              
                              #Ataque

                              if accion == 1:
                                  os.system("cls")
                                  pygame.mixer.music.load("audio/pipe.mp3")
                                  pygame.mixer.music.play(1)
                                  print(Fore.LIGHTGREEN_EX +'''

                          █████████                      
                          █▒▒▒▒▒▒▒██                     
            ████           ███▒▒███          ████        
          ██░░░█        ██████▒▒█████        ██▒▒██      
          █▓░░░██      ░█░░░░░░░░░░▒▒▒████    ██▒▒▒▒██    
        ██░░▓░░▓████░░░░░░░░░░░░░░░░░░▒▒▒█████▒▒▒▒▒▒█    
          ███ ██░░▒░░░░░░░░░░░░░░░░░░░░░░▒▒▒█▒▒▒██████    
              ██░░░░░███▒░░░░░░░░░░░░░░░░░▒▒▒██          
              █▓░░░███▒▒▒▓██░░░░░░░░░░░░░░░░▒▒▒██         
            █▒░░░██▒▒▒▒▒▒▒██░░░░░░░░░░░░░░░░▒▒▒▒█        
            ██░░░░██▒▒▒▒▒▒▒██░░░░░░░░░░░░░░░░░▒▒▒██       
          ██░░░░░░██▒▒▒▒▒▓█░░░░░░░░░░░░░░░░░░▒▒▒▒██      
      █▓██ █▒░░░░░░░███████░░░░░░░░░░░░░░░░░░░░▒▒▒▒█ ████ 
      ██░░███░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒███▒▒██
      ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒██
      ██░░███░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█████▒▒▒▒███▒▒██
      ████ █▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░██▒▒▒█▒▒▒▒█ ████ 
          ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█████▒▒▒██      
            ██░░░░░░░░░░░░░░░░░░░░░▒██░░░░░░░░▒▒▒██       
            █▒░░░░░░░░░░░░░░░░░░██▒▒▒██░░░░░▒▒▒▒█        
              ██░░░░░░░░░░░░░░░░░█▒▒▒▒▒██░░░▒▒▒██         
              ██░░░░░░░░░░░░░░░░██▒▒▒▒██░░▒▒▒██          
        ██████▒░░█░░░░░░░░░░░░░░░▓████░░▒▒▒▒▒▒██ ███     
        █░░░░░░█████░░░░░░░░░░░░░░░░░░▒▒▒████▓▒▒▓▒▒██    
        ██▒░░░██    ████░░░░░░░░░░░▒▒████    ██▒▒▒▒█     
          ██▒░██        █████▒▒██████        █▒▒▒▒       
            ████          ███▒▒███           ████        
                          ██▒▒▒▒▒▒▒█                      
                          █████████                      ''')
                                  daño = random.randint(10, 30)
                                  vida_enemigo -= daño
                                  print(f"Atacas al enemigo y le haces {Fore.RED}{daño}{Style.RESET_ALL} de daño.")
                                  daño_enemigo = random.randint(0, 10)
                                  vida_jugador -= daño_enemigo
                                  print(f"\nEl enemigo contraataca y te hace {Fore.RED}{daño_enemigo}{Style.RESET_ALL} de daño.")
                                  
                              #Defensa    
                              
                              elif accion == 2:  
                                  os.system("cls")
                                  pygame.mixer.music.load("audio/defensa.mp3")
                                  pygame.mixer.music.play(3)
                                  daño = random.randint(0,5)
                                  vida_jugador -= daño
                                  print(Fore.LIGHTGREEN_EX +'''

                          █████████                      
                          █▒▒▒▒▒▒▒██                     
            ████           ███▒▒███          ████        
          ██░░░█        ██████▒▒█████        ██▒▒██      
          █▓░░░██      ░█░░░░░░░░░░▒▒▒████    ██▒▒▒▒██    
        ██░░▓░░▓████░░░░░░░░░░░░░░░░░░▒▒▒█████▒▒▒▒▒▒█    
          ███ ██░░▒░░░░░░░░░░░░░░░░░░░░░░▒▒▒█▒▒▒██████    
              ██░░░░░███▒░░░░░░░░░░░░░░░░░▒▒▒██          
              █▓░░░███▒▒▒▓██░░░░░░░░░░░░░░░░▒▒▒██         
            █▒░░░██▒▒▒▒▒▒▒██░░░░░░░░░░░░░░░░▒▒▒▒█        
            ██░░░░██▒▒▒▒▒▒▒██░░░░░░░░░░░░░░░░░▒▒▒██       
          ██░░░░░░██▒▒▒▒▒▓█░░░░░░░░░░░░░░░░░░▒▒▒▒██      
      █▓██ █▒░░░░░░░███████░░░░░░░░░░░░░░░░░░░░▒▒▒▒█ ████ 
      ██░░███░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒███▒▒██
      ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒██
      ██░░███░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█████▒▒▒▒███▒▒██
      ████ █▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░██▒▒▒█▒▒▒▒█ ████ 
          ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█████▒▒▒██      
            ██░░░░░░░░░░░░░░░░░░░░░▒██░░░░░░░░▒▒▒██       
            █▒░░░░░░░░░░░░░░░░░░██▒▒▒██░░░░░▒▒▒▒█        
              ██░░░░░░░░░░░░░░░░░█▒▒▒▒▒██░░░▒▒▒██         
              ██░░░░░░░░░░░░░░░░██▒▒▒▒██░░▒▒▒██          
        ██████▒░░█░░░░░░░░░░░░░░░▓████░░▒▒▒▒▒▒██ ███     
        █░░░░░░█████░░░░░░░░░░░░░░░░░░▒▒▒████▓▒▒▓▒▒██    
        ██▒░░░██    ████░░░░░░░░░░░▒▒████    ██▒▒▒▒█     
          ██▒░██        █████▒▒██████        █▒▒▒▒       
            ████          ███▒▒███           ████        
                          ██▒▒▒▒▒▒▒█                      
                          █████████                      ''')
                                  print(f"Te defiendes, pero recibes {daño} de daño.")
                                  
                              #Si no elige ni 1 ni 2
                              else:
                                  os.system("cls")
                                  print("Acción no válida, pierdes un turno.")
                              
                              turnos -= 1

                             
                              input()
                              os.system("cls")
                              
                              #Si los turnos llegan a 0
                              
                              if turnos == 0 or (turnos <3 and vida_enemigo<=0):
                                  os.system("cls")
                                  print("\nPodrías haberlo hecho mejor, aunque te lo dejo pasar por esta vez")
                                  print(Fore.GREEN + '''
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
                      XX X  X X    X  XX XXXXX    XX
                      XX XX X XX  XX  XX XXXXXX   XX
                      XXXXX X XXXXXXXXXXXXXX  X   XX
                      XX  XXXX  XX    XXXXXXXX X  XX
                      XXXX  X  XX   XX  XX  XXXX  XX
                      XX  XX XX     XX  X  XXXX XXXX
                      XX  XX X XX   X   X   X   XXXX
                      XXX    XXX    X XXX  XX   X XX
                      XX    XX  XXX  XXXXXX    X  XX
                      XX   XXXX   XXXX XX   XXX XXXX
                      XX X X   X X  X        XXX  XX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX''')
                                  print(Fore.GREEN + "\n\n\nHas obtenido la placa color verde")
                                  input("Pulsa ENTER para regresar al menú de puertas...")
                                  os.system("cls")
                                  break
                                
                            # Regresar al menú de puertas

                            
                            
                         
                      # Volver al menú principal
                      elif puerta == 3:
                          print("Regresarás al menú principal.")
                          break
                          
                      #Si se elige fuera de 1, 2 o 3
                      else:
                          print("Opción no válida, volverás al menú de puertas")
                          input()
                          os.system("cls")
          
          #Opción Centro Comercial
          
          elif eleccion == 2:
            os.system("cls")
            print("Has decidido comenzar la búsqueda en el Centro Comercial")
            print(Fore.LIGHTMAGENTA_EX + '''
                  
                  
███████████████                   ██████████████
█             █                   █            █
█ ████  ████  █                   █ ████  ████ █
█ █  █  █  █  █                   █ █  █  █  █ █
█ ████  ████  █                   █ ████  ████ █
█             █████████████████████            █
█ ████  ████  █     CENTRO       ██ ████  ████ █
█ █  █  █  █  █    COMERCIAL     ██ █  █  █  █ █
█ ████  ████  █    █████████     ██ ████  ████ █
█             █    █████████     ██            █
█             █     ███████      ██            █
█             █     █  █  █      ██            █
█             █     █  █  █      ██            █
█             █     █  █  █      ██            █
████████████████████████████████████████████████''')
                                         

            input()
            os.system("cls")
  
            #Contexto Centro Comercial
            
            print(Fore.LIGHTMAGENTA_EX + '''
                                                                                      
                               ░▓▓▓▒                                    
                               ▒▒▒▒▒░                                   
                               ▓▒░░▓░                                   
                               ▒▓▒░▒░                                   
                                ▓▓▓▒                                    
                                ▓▓██▒                                   
                            ░▓██████▓██▓▒░                              
                           ▒▒██████████▓ ▒                              
                          ░▒▒▓█████████▒▒░░                             
                          ▒░▒▓█░███████▒▒ ▒                             
                          ▒░▒▒███▓█▓███░▒ ░                             
                          ▒▒░░███░▒▒███  ░ ░                            
                         ░░░░ ▓███████▒  ▒▒                             
                         ░░▒░░████████▓  ▒▒░                            
                         ░░▒░█▓██▓█████▒ ▒▒░                            
                         ░░░▒██████████▒ ▒▒░                            
                         ░░░▓█▓███▓▓▓▓▓▓ ░▒░                            
                         ░░ ▓▓▓▓▓▓▓▒▓▓▓▓  ▒░                            
                         ░░░▒▓▓▓█████▓▒█  ▒░                            
                         ▒▒ ░██▓██ ██▓▒█  ░▒                            
                          ░  ▓█▓██ ░██▓█░  ░                            
                             ▓█▓▓▓  ▓█▓█▓                               
                              █▓▓▓   ████                               
                              ▒▓▒▓   ▒█▓█                               
                              ░█▓▓░  ░▓▓█░                              
                               ▓▓▓░   ▓▓█▒                              
                               █▓█░    ▓▓█░                             
                               ▓▓▓▒    ▒▓▓▓                             
                               ▒▓▓▒     ▓▓▓░                            
                                ▓▒▒      █▒▓                            
                                ▒▒▒      ▒▓▓                            
                                ░▒▒       ▓▒▒                           
                                 ▓▓        ▒▒                           
                                ░█▓        ▒▓░                          
                               ▒▓▓▓▓▒▒▒▒▒▒▒▓▓▓                          
                               ▒▒█▓▓▒▒▒▒▒▒▒▒▓▓▒                         
                               ▒▒▓▓▓▒▒▒▒▒▒▒▒▓▓█                         
                               ▒░░▒░▒░▒░░▒░▒▒▓▓▒    ''')
            
            pygame.mixer.music.load("audio/junes.mp3")
            pygame.mixer.music.play(1)
            contexto_centro = f"\n\nEl centro comercial está desolado, abandonado, polvoriento, solo se oye el eco de tus pasos.\nLos escaparates y las vitrinas están rotas y te da la sensación de que algo te observaba desde las sombras.\nLa luz de tu linterna revela pasillos interminables, maniquíes torcidos y escombros esparcidos por el suelo. recordando a tu amigo perdido {nombre_amigo_mayus}\nLas huellas en el polvo eran la única señal de que alguien más había estado aquí.\nEl aire es pesado y cada rincón oscuro parece esconder algo.\n\nParece que las mejores opciones están eligiendo entre dos puertas: una a la izquierda que parece una antigua tienda de moda, y a la derecha, una antigua tienda de música\nAlgo te dice que lo que investigues detrás de esas puertas podría ayudarte en tu búsqueda..."
            for letra in contexto_centro:
              print(letra, end="", flush=True)
              time.sleep(0.01)

            input()
            os.system("cls")
            

            #Bucle elegir puerta o volver al menú principal

            while True:
                pygame.mixer.music.load("audio/pajaros.mp3")
                pygame.mixer.music.play(1)
                print("\n¿Qué puerta vas a elegir primero?:")
                print("1. Abrir la puerta izquierda: Tienda de moda")
                print("2. Abrir la puerta derecha: Tienda de música")
                print("3.Ya he explorado ambas puertas, quiero seguir.")
                puerta = int(input("Elijo la opción: "))

                # Puerta izquierda
                if puerta == 1:
                    os.system("cls")
                    pygame.mixer.music.load("audio/hey you.mp3")
                    pygame.mixer.music.play(1)
                    print(Fore.LIGHTGREEN_EX + '''
                          
                                                                         
                            ▒▒▒▒▒                             
                          ▒▒▒▒▒▒▒▒                            
                          ▒▒▒▒▒▓▓▓▒                           
                           ▒▒▒▓▓▓▓▒                           
                           ▒▒▒▒▓█▓▒                           
                           ▒▒▒▒▒▓▓▓                           
                         ████▓▓▓▓▓▓██                         
                        █████▓▓▓▓▓▓████    ▓▓████             
             ████      ████▓▓▓▓▓▓▓▓████▓█▓▓█▓▓▒▒▒             
             ▓▓▓▓▓██▓█▓███▓▓▓▓▓▓▓▓▓▓ ██▓▓▓▓▒▒▒▒▒▒▒▒           
            ▓▓▓▓▓▓▓▒▒▓▓▓▓ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▓▒▒▒▒          
          ▓▓▓▓▒▒▓▓▒▒▒▒▒▒▒▒ ▓▓▓▓▓▓▓▓ ▓▓▓▓▓▓▓▓▒▒▒▒▓▒▒▒▒         
         ▓▓▓▓▒▒▓▓▒▒▒▒▒▒▒▒▒ ▓▓▓▓▓▓▓▓ ▓▓▓▓▓▓▓▓▓▒▒▒▒▓▒▒▒▒        
        ▓▓▓▓▒▒▓▓▒▒▒▒▒▒▒▒▒▒▓█▓▓▓▓▓▓▓█ ▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓▒▒▒       
       ▓▓▓▓▒▒▓▓▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓ ▓▓▓▓▓▓▓▓▓▓▒▒▒▓▓▓▓        
        ▓▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓█▓▓▓▓▓▓▓▓▓▓▓▓▓             
            ▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓ ▓▓                      
                  ▒▒ ▒▒▒▒█▓▓▓▓▓▓▓▓▓▓▓                         
                         █▓▓▓▓▓▓▓▓▓▓▓                         
                          ▓▓▓▓▓▓▓▓▓▓▓                         
                          ▓▓▓▓▓▓▓▓▓▓▓█                        
                          ▓▓▓▓▓▓▓▓▓▓▓▓█                       
                          ▓▓▓▓▓▓▓▓▓▓▓▓▓                       
                          ▓▓▓▓▓▓▓▓▓▓▓▓▓▓                      
                          ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                     
                            ██▓▓▓▓▓▓▓▓▓▓▓                     
                            ███      ████                     
                            ███       ███                     
                            ███       ████                    
                             ██        ████                   
                             ▓▓▓█       ██▓██                 
                               ███               ''')
                    print("\n¡¡Oh no!!, te has encontrado con una loca por las rebajas y se cree que vas a robarle las ofertas,\n hará lo que sea para ello. Dispones de una vida limitada, la adicta tiene una vida de 30, tenlo presente y ten cuidado en el combate puesto que constará de 3 turnos.")
                    
                    vida_enemigo = 50
                    turnos = 3
                    
                    #Combate ataque / defensa o volver al menú de puertas
                    
                    while turnos > 0 and vida_enemigo > 0 and vida_jugador > 0:
                        print(f"\nTu vida: {vida_jugador} | Vida enemiga: {vida_enemigo}")
                        accion = int(input("¿Qué quieres hacer? (1. Atacar, 2. Defenderte): "))
                        os.system("cls")
                        
                        #Atacar
                        
                        if accion == 1:
                            os.system("cls")
                            pygame.mixer.music.load("audio/pipe.mp3")
                            pygame.mixer.music.play(1)
                            print(Fore.LIGHTGREEN_EX + '''
                          
                                                                         
                            ▒▒▒▒▒                             
                          ▒▒▒▒▒▒▒▒                            
                          ▒▒▒▒▒▓▓▓▒                           
                           ▒▒▒▓▓▓▓▒                           
                           ▒▒▒▒▓█▓▒                           
                           ▒▒▒▒▒▓▓▓                           
                         ████▓▓▓▓▓▓██                         
                        █████▓▓▓▓▓▓████    ▓▓████             
             ████      ████▓▓▓▓▓▓▓▓████▓█▓▓█▓▓▒▒▒             
             ▓▓▓▓▓██▓█▓███▓▓▓▓▓▓▓▓▓▓ ██▓▓▓▓▒▒▒▒▒▒▒▒           
            ▓▓▓▓▓▓▓▒▒▓▓▓▓ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▓▒▒▒▒          
          ▓▓▓▓▒▒▓▓▒▒▒▒▒▒▒▒ ▓▓▓▓▓▓▓▓ ▓▓▓▓▓▓▓▓▒▒▒▒▓▒▒▒▒         
         ▓▓▓▓▒▒▓▓▒▒▒▒▒▒▒▒▒ ▓▓▓▓▓▓▓▓ ▓▓▓▓▓▓▓▓▓▒▒▒▒▓▒▒▒▒        
        ▓▓▓▓▒▒▓▓▒▒▒▒▒▒▒▒▒▒▓█▓▓▓▓▓▓▓█ ▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓▒▒▒       
       ▓▓▓▓▒▒▓▓▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓ ▓▓▓▓▓▓▓▓▓▓▒▒▒▓▓▓▓        
        ▓▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓█▓▓▓▓▓▓▓▓▓▓▓▓▓             
            ▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓ ▓▓                      
                  ▒▒ ▒▒▒▒█▓▓▓▓▓▓▓▓▓▓▓                         
                         █▓▓▓▓▓▓▓▓▓▓▓                         
                          ▓▓▓▓▓▓▓▓▓▓▓                         
                          ▓▓▓▓▓▓▓▓▓▓▓█                        
                          ▓▓▓▓▓▓▓▓▓▓▓▓█                       
                          ▓▓▓▓▓▓▓▓▓▓▓▓▓                       
                          ▓▓▓▓▓▓▓▓▓▓▓▓▓▓                      
                          ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                     
                            ██▓▓▓▓▓▓▓▓▓▓▓                     
                            ███      ████                     
                            ███       ███                     
                            ███       ████                    
                             ██        ████                   
                             ▓▓▓█       ██▓██                 
                               ███               ''')
                            daño = random.randint(10, 30)
                            vida_enemigo -= daño
                            print(f"Atacas al enemigo y le haces {Fore.RED}{daño}{Style.RESET_ALL} de daño.")
                            daño_enemigo = random.randint(0, 10)
                            vida_jugador -= daño_enemigo
                            print(f"\nEl enemigo contraataca y te hace {Fore.RED}{daño_enemigo}{Style.RESET_ALL} de daño.")
                            
                        #Defensa     
                        
                        elif accion == 2:  
                          
                            os.system("cls")
                            print(Fore.LIGHTGREEN_EX + '''
                          
                                                                         
                            ▒▒▒▒▒                             
                          ▒▒▒▒▒▒▒▒                            
                          ▒▒▒▒▒▓▓▓▒                           
                           ▒▒▒▓▓▓▓▒                           
                           ▒▒▒▒▓█▓▒                           
                           ▒▒▒▒▒▓▓▓                           
                         ████▓▓▓▓▓▓██                         
                        █████▓▓▓▓▓▓████    ▓▓████             
             ████      ████▓▓▓▓▓▓▓▓████▓█▓▓█▓▓▒▒▒             
             ▓▓▓▓▓██▓█▓███▓▓▓▓▓▓▓▓▓▓ ██▓▓▓▓▒▒▒▒▒▒▒▒           
            ▓▓▓▓▓▓▓▒▒▓▓▓▓ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▓▒▒▒▒          
          ▓▓▓▓▒▒▓▓▒▒▒▒▒▒▒▒ ▓▓▓▓▓▓▓▓ ▓▓▓▓▓▓▓▓▒▒▒▒▓▒▒▒▒         
         ▓▓▓▓▒▒▓▓▒▒▒▒▒▒▒▒▒ ▓▓▓▓▓▓▓▓ ▓▓▓▓▓▓▓▓▓▒▒▒▒▓▒▒▒▒        
        ▓▓▓▓▒▒▓▓▒▒▒▒▒▒▒▒▒▒▓█▓▓▓▓▓▓▓█ ▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓▒▒▒       
       ▓▓▓▓▒▒▓▓▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓ ▓▓▓▓▓▓▓▓▓▓▒▒▒▓▓▓▓        
        ▓▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓█▓▓▓▓▓▓▓▓▓▓▓▓▓             
            ▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓ ▓▓                      
                  ▒▒ ▒▒▒▒█▓▓▓▓▓▓▓▓▓▓▓                         
                         █▓▓▓▓▓▓▓▓▓▓▓                         
                          ▓▓▓▓▓▓▓▓▓▓▓                         
                          ▓▓▓▓▓▓▓▓▓▓▓█                        
                          ▓▓▓▓▓▓▓▓▓▓▓▓█                       
                          ▓▓▓▓▓▓▓▓▓▓▓▓▓                       
                          ▓▓▓▓▓▓▓▓▓▓▓▓▓▓                      
                          ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                     
                            ██▓▓▓▓▓▓▓▓▓▓▓                     
                            ███      ████                     
                            ███       ███                     
                            ███       ████                    
                             ██        ████                   
                             ▓▓▓█       ██▓██                 
                               ███               ''')
                            pygame.mixer.music.load("audio/defensa.mp3")
                            pygame.mixer.music.play(1)
                            daño = random.randint(0,5)
                            vida_jugador -= daño
                            print(f"Te defiendes, pero recibes {daño} de daño.")
                        
                        #Si no elige ni 1 ni 2    
                        else:
                                  os.system("cls")
                                  print("Acción no válida, pierdes un turno.")
                                  input()
                                  os.system("cls")
    
                        
                        turnos -= 1

                    
                        input()
                        os.system("cls")
                        
                        
                        if turnos == 0 or (turnos <3 and vida_enemigo<=0):
                            os.system("cls")
                            print("\nPodrías haberlo hecho mejor, aunque te lo dejo pasar por esta vez")
                            print(Fore.RED + '''
                XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
                XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
                XX X  X X    X  XX XXXXX    XX
                XX XX X XX  XX  XX XXXXXX   XX
                XXXXX X XXXXXXXXXXXXXX  X   XX
                XX  XXXX  XX    XXXXXXXX X  XX
                XXXX  X  XX   XX  XX  XXXX  XX
                XX  XX XX     XX  X  XXXX XXXX
                XX  XX X XX   X   X   X   XXXX
                XXX    XXX    X XXX  XX   X XX
                XX    XX  XXX  XXXXXX    X  XX
                XX   XXXX   XXXX XX   XXX XXXX
                XX X X   X X  X        XXX  XX
                XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
                XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX''')
                            print(Fore.RED + "\n\n\nHas obtenido la placa color rojo")
                            input("Pulsa ENTER para regresar al menú de puertas...")
                            os.system("cls")
                            break
                       
                      
                # Puerta derecha
                elif puerta == 2:
                    os.system("cls")
                    pygame.mixer.music.load("audio/jiji.mp3")
                    pygame.mixer.music.play(1)
                    print('''     
                               
                         ░█████▒  
                       ▒▓██████▓  
                       ▒███████▓  
                      ▓█████████▓░
                 ▒▓█████████▓▒▒   
                ▒█████████▒▓▓     
               ▒██████████░░█▒    
              ░▓██████████░ █▒    
             ░░░ ░████████░ █▒    
            ░███▒░████████░ ▓▒    
            ▓███░▓████████░ ▓▒    
           ▒███▒▒█████████░ ▓▒    
           ▓██▓▒██████████░ ▓░    
          ░███▓██████████████░    
          ░█████████████████▓░    
         ░██████████████████▓     
        ░██░▓███████████████░     
         ░ ▒███████████▓▓░░░      
          ▓██████████░ ▒░░        
        ░██████████▒              
       ▒█████████▓                
     ░▓████████▓░                 
    ░█████████▓                   
   ░█████████░                    
  ░████████▓░                     
 ▒███▓███▒                        
 ▒██▓▓█████░                      
░▓██▒ ░░▒▓██░                     
                                  ''')
                    print("\n¡¡Oh no!!, te has encontrado con Miguel Jackson, un antiguo fan de la música, aunque parece más bien un fantasma\nEl caso es que se te está acercando de una manera muy extraña\nDispones de una vida limitada, Miguel tiene una vida de 50, tenlo presente y ten cuidado en el combate puesto que constará de 3 turnos.")
                    
                    vida_enemigo = 50
                    turnos = 3
                    
                    #Combate ataque / defensa y volver al menú puertas
                    
                    while turnos > 0 and vida_enemigo > 0 and vida_jugador > 0:
                        print(f"\nTu vida: {vida_jugador} | Vida enemiga: {vida_enemigo}")
                        accion = int(input("¿Qué quieres hacer? (1. Atacar, 2. Defenderte): "))
                        os.system("cls")
                        
                        #Atacar
                        
                        if accion == 1:
                            os.system("cls")
                            pygame.mixer.music.load("audio/miguel.mp3")
                            pygame.mixer.music.play(1)
                            print('''     
                               
                         ░█████▒  
                       ▒▓██████▓  
                       ▒███████▓  
                      ▓█████████▓░
                 ▒▓█████████▓▒▒   
                ▒█████████▒▓▓     
               ▒██████████░░█▒    
              ░▓██████████░ █▒    
             ░░░ ░████████░ █▒    
            ░███▒░████████░ ▓▒    
            ▓███░▓████████░ ▓▒    
           ▒███▒▒█████████░ ▓▒    
           ▓██▓▒██████████░ ▓░    
          ░███▓██████████████░    
          ░█████████████████▓░    
         ░██████████████████▓     
        ░██░▓███████████████░     
         ░ ▒███████████▓▓░░░      
          ▓██████████░ ▒░░        
        ░██████████▒              
       ▒█████████▓                
     ░▓████████▓░                 
    ░█████████▓                   
   ░█████████░                    
  ░████████▓░                     
 ▒███▓███▒                        
 ▒██▓▓█████░                      
░▓██▒ ░░▒▓██░                     
                                  ''')
                            daño = random.randint(10, 30)
                            vida_enemigo -= daño
                            print(f"Atacas al enemigo y le haces {Fore.RED}{daño}{Style.RESET_ALL} de daño.")
                            daño_enemigo = random.randint(0, 10)
                            vida_jugador -= daño_enemigo
                            print(f"El enemigo contraataca y te hace {Fore.RED}{daño_enemigo}{Style.RESET_ALL} de daño.")
                         
                        #Defensa    
                        elif accion == 2:  
                            
                            os.system("cls")
                            print('''     
                               
                         ░█████▒  
                       ▒▓██████▓  
                       ▒███████▓  
                      ▓█████████▓░
                 ▒▓█████████▓▒▒   
                ▒█████████▒▓▓     
               ▒██████████░░█▒    
              ░▓██████████░ █▒    
             ░░░ ░████████░ █▒    
            ░███▒░████████░ ▓▒    
            ▓███░▓████████░ ▓▒    
           ▒███▒▒█████████░ ▓▒    
           ▓██▓▒██████████░ ▓░    
          ░███▓██████████████░    
          ░█████████████████▓░    
         ░██████████████████▓     
        ░██░▓███████████████░     
         ░ ▒███████████▓▓░░░      
          ▓██████████░ ▒░░        
        ░██████████▒              
       ▒█████████▓                
     ░▓████████▓░                 
    ░█████████▓                   
   ░█████████░                    
  ░████████▓░                     
 ▒███▓███▒                        
 ▒██▓▓█████░                      
░▓██▒ ░░▒▓██░                     
                                  ''')
                            pygame.mixer.music.load("audio/au.mp3")
                            pygame.mixer.music.play(1)
                            daño = random.randint(0,5)
                            vida_jugador -= daño
                            print(f"Te defiendes, pero recibes {Fore.RED}{daño}{Style.RESET_ALL} de daño.")
                        
                        #Si no elige 1 o 2
                        else:
                                  os.system("cls")
                                  print("Acción no válida, pierdes un turno.")
                                  

                    
                        input()
                        os.system("cls")
                        
                        if turnos == 0 or (turnos <3 and vida_enemigo<=0):
                            os.system("cls")
                            print("\nPodrías haberlo hecho mejor, aunque te lo dejo pasar por esta vez")
                            print(Fore.YELLOW + '''
                XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
                XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
                XX X  X X    X  XX XXXXX    XX
                XX XX X XX  XX  XX XXXXXX   XX
                XXXXX X XXXXXXXXXXXXXX  X   XX
                XX  XXXX  XX    XXXXXXXX X  XX
                XXXX  X  XX   XX  XX  XXXX  XX
                XX  XX XX     XX  X  XXXX XXXX
                XX  XX X XX   X   X   X   XXXX
                XXX    XXX    X XXX  XX   X XX
                XX    XX  XXX  XXXXXX    X  XX
                XX   XXXX   XXXX XX   XXX XXXX
                XX X X   X X  X        XXX  XX
                XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
                XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX''')
                            print(Fore.YELLOW+ "\n\n\nHas obtenido la placa color amarillo")
                            input("Pulsa ENTER para regresar al menú de puertas...")
                            os.system("cls")
                            break
                          
                      
                       
          # Volver al menú principal
                elif puerta == 3:
                    print("Regresas al menú principal.")
                    break
                  
                #Si no elige 1, 2 o 3

                else:
                    os.system("cls")
                    print("Opción no válida.")
                    
                    
                    
                    
#Puzzle y contexto
input()
os.system("cls")
pygame.mixer.music.load("audio/finale2.mp3")
pygame.mixer.music.play(2)

acertijo = f"{nombre_prota_mayus} dejó atrás el hospital y el centro comercial, sin señales de {nombre_amigo_mayus}. \nYa sin fuerzas te subes al coche, solo para encontrar una nota en el asiento del copiloto:\n{nombre_prota_mayus}, las piezas que recogiste no son simples objetos. Júntalas y descubre la verdad. No confíes en nadie.\n Encuentras una caja con algunas placas incrustadas, justamente tú tienes las que faltan\n\nSe podrá resolver mediante el acertijo que había en la nota.\n\nBuena suerte"
for letra in acertijo:
    print(letra, end="", flush=True)
    time.sleep(0.01)

input()
os.system("cls")
                    
while True: 
    
    pygame.mixer.music.load("audio/tartaro.mp3")
    pygame.mixer.music.play(3)
    print(Fore.LIGHTRED_EX + '''
xxxxxxxxxxxxxxxxx█½½½½½½½½½½½½½½█xxxxxxxxxxxxxxxxx
xx█████████████xx█½½██████████½½█xx█████████████xx
xx█           █xx█½½█        █½½█xx█           █xx
xx█           █xx█½½█        █½½█xx█           █xx
xx█     1     █xx█½½█ BLANCO █½½█xx█     2     █xx
xx█           █xx█½½█        █½½█xx█           █xx
xx█           █xx█½½█        █½½█xx█           █xx
xx█████████████xx█½½██████████½½█xx█████████████xx
xxxxxxxxxxxxxxxxx█½½½½½½½½½½½½½½█xxxxxxxxxxxxxxxxx
██████████████████½½½½½½½½½½½½½½██████████████████
½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½
½½█████████████½½½½½½½½½½½½½½½½½½½½█████████████½½
½½█   NEGRO   █½½½½½½½½½½½½½½½½½½½½█  NARANJA  █½½
½½█████████████½½½½½½½½½½½½½½½½½½½½█████████████½½
½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½
½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½
██████████████████½½½½½½½½½½½½½½██████████████████
xxxxxxxxxxxxxxxxx█½½½½½½½½½½½½½½█xxxxxxxxxxxxxxxxx
xx█████████████xx█½½██████████½½█xx█████████████xx
xx█           █xx█½½█        █½½█xx█           █xx
xx█           █xx█½½█        █½½█xx█           █xx
xx█     4     █xx█½½█ MORADO █½½█xx█     3     █xx
xx█           █xx█½½█        █½½█xx█           █xx
xx█████████████xx█½½██████████½½█xx█████████████xx
xxxxxxxxxxxxxxxxx█½½½½½½½½½½½½½½█xxxxxxxxxxxxxxxxx''')


    print('''\n\n
    Nubes blancas pasando sobre una colina.
    El cielo en un día soleado.
    Amargas mandarinas. 
    Un trébol de cuatro hojas. 
    Violetas en el jardín. 
    Flores amarillas a lo largo de un camino. 
    A esta hora dormir es inevitable.  
    Sale un líquido de un corte en la muñeca.''')

    placa_amarilla = int(input("\nDónde va la placa amarilla: "))
    placa_roja = int(input("\nDónde va la placa roja: "))
    placa_verde = int(input("\nDónde va la placa verde: "))
    placa_azul = int(input("\nDónde va la placa azul: "))

   
            
    if placa_roja == 1 and placa_azul == 2 and placa_verde == 3 and placa_amarilla == 4:
      print("\nHas acertado, se abre la caja: ")
      break
    else:
      print("\nIntentalo de nuevo")
      input()
  

input()
os.system("cls")

#Final contexto
pygame.mixer.music.load("audio/finale.mp3")
pygame.mixer.music.play(2)
print(Fore.LIGHTMAGENTA_EX + '''
                                                                             
                                                
    █████████    █████████████████████           
    ██▒▒▒▒▓█▓▓▓▓▓█▓░░░░▓█▒░░▒▒█▓▒▒▒▓███          
    ████████▒░░░▒███████████████▒▒▒▒▓██          
    ██░░░░▒█▒░░░▒█▓▒▒▒▒██▒░░░▒██▓▒▒▒▒██          
    ████████▒░░░▒████████████████▒▒▒▒▓██         
    ██▒▒▒▒▓█▒░░░▒█▓░░░░▓█▒░░▒▒████▒▒▒▒▓██        
    ██▒▒▒▒▓█▒░░░▒█▓░░░░▓█▒░░▒▒████▓▒▒▒▓██        
    ██▒▒▒▒▓▒▒░░░▒█▓░░░░▓█▒░░▒▒██ ██▒▒▒▒▓██       
    ██▒▒▒▒▓█▒░░░▒█▓░░░░▓█▒░░▒▒██ ██▓▒▒▒▓██       
    ██▒▒▒▒▓█▒▒▒▒▒█▓▒▒▒▒▓█▒░░▒▒▓█  ██▓▓▓████      
    ██▒▒▒▒▓█▓▓▓▓▓████████▒░░▒▒██  ███▓▒▒░▓██     
    ██▒▒▒▒▓█▓▒▒▒▓██▓▓▓▓██▒░░▒▒██   ██▓██████     
    ██▒▒▒▒▓█▓▒▒▒▒█▓▒▒▒▒▓█▒░░▒▒██    ██▒▒▒▒▓██    
    ██▒▒▒▒▓█▒░░░▒█▓░░░░▓█▒░░▒▒██    ██▓██████    
██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██
███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓███
  ██████████████████████████████████  █████████  
                                                 ''')
final= f"\n\nLa inscripción decía: 'En la biblioteca'.\n\nTe inunda la confusión y decides dirigirte hasta allí,\nal entrar te encuentras con {nombre_amigo_mayus} rodeado de libros y frente al ordenador.\n¿Qué haces aquí, {nombre_amigo_mayus}?\n\n¡Sorpresa!, estaba aquí encerrado porque tengo que entregar doscientos trabajos de Homero...\nY aquí hay muy buen internet, aunque no sé a qué te refieres conque has luchado contra unas sombras o enemigos...\n\n¿No serán acaso imaginaciones tuyas?"
for letra in final:
    print(letra, end="", flush=True)
    time.sleep(0.01)
    
input()
os.system("cls")

#Créditos finales
pygame.mixer.music.load("audio/doggo.mp3")
pygame.mixer.music.play(1)


print(Fore.YELLOW + '''

     ▒▒████ ▒▓▓▓                            
     ██▒▓▓▓██▓▓▓                            
    ██▓▓▓▓▓▓███▓▓▓                          
   █▓▒▒▓▓▓▓▓▒██▓▓▓                          
   ▓▒▓▓███▓▓▓▓▓▓▓▓▓                 ░░▒▒▒   
  ▓▓▓▓▓▓▓▓▓█████▓▓▓▓▓              ▒░░▒▒▒▒  
███▒▒▒▒▒▒▒▒█████▓▓▓▓▓▓              ▒░░▒▒▒  
 ▓▓▒▒▒▒▒▒▒▒▒██▓▓▓▓▓▓█▓▓▓▓▓           ▒░▒▒▒▒ 
█    ▒▒▒▒▒▒▒▒▒▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░▒▒▒ 
        ░▒▒▒▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒ 
         ▒▒▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ 
        ███▓▓███▓▓▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
           ░▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
            ░░▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
            ░░░▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
             ░░░▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒ ░▒▒▒▓▓▓
             ▒░░░░▒▒▒▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒░▒▒▒▒▓ 
              ░░▒▒▒░▒▒▓▓▓▓▓      ▒▒▒▒ ░▒▓▒▓ 
              ▒▒▒▒▒ ░▒▒▓▓▓       ▒░▒▒  ░▒▓▓▓
               ▒▒▒▒ ░▒▓▓▓▓        ░▒▒   ░▒▒▓
               ▒▒▒▒ ░▒▓▓▓        ░▒▒▒   ░▒▒▓
               ▒▒▒▒  ▒▓▓▓       ░░▒▒   ░░▒▒▒
               ░▒▒▒  ▒▒▓▒             ░░▒▒▒ 
               ░▒▒▒  ░▒▒▒                   
             ░░▒▒▒   ░▒▒▒                   
             ▒▒▒▒▒ ░░▒▒▒                    
                  ░▒▒▒▒▒                    


      ''')
time.sleep(2)
print(Fore.LIGHTCYAN_EX +'''\n\n
      
 ██████╗ ██████╗  █████╗  ██████╗██╗ █████╗ ███████╗
██╔════╝ ██╔══██╗██╔══██╗██╔════╝██║██╔══██╗██╔════╝
██║  ███╗██████╔╝███████║██║     ██║███████║███████╗
██║   ██║██╔══██╗██╔══██║██║     ██║██╔══██║╚════██║
╚██████╔╝██║  ██║██║  ██║╚██████╗██║██║  ██║███████║
 ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝╚═╝  ╚═╝╚══════╝
                                                    
██████╗  ██████╗ ██████╗                            
██╔══██╗██╔═══██╗██╔══██╗                           
██████╔╝██║   ██║██████╔╝                           
██╔═══╝ ██║   ██║██╔══██╗                           
██║     ╚██████╔╝██║  ██║                           
╚═╝      ╚═════╝ ╚═╝  ╚═╝                           
                                                    
     ██╗██╗   ██╗ ██████╗  █████╗ ██████╗           
     ██║██║   ██║██╔════╝ ██╔══██╗██╔══██╗          
     ██║██║   ██║██║  ███╗███████║██████╔╝          
██   ██║██║   ██║██║   ██║██╔══██║██╔══██╗          
╚█████╔╝╚██████╔╝╚██████╔╝██║  ██║██║  ██║          
 ╚════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝          ''')


input()
os.system("cls")
pygame.quit()  
                    
input()