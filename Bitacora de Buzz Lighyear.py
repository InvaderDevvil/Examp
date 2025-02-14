# Bitacora de Buzz Lightyear
import winsound
import threading
import random
from datetime import datetime, timedelta

def play_sound():
    winsound.PlaySound("Buzz_theme.wav", winsound.SND_FILENAME)

thread = threading.Thread(target=play_sound)

def random_date():
    start_date = datetime.now()
    random_days = random.randint(0, 365)
    random_date = start_date + timedelta(days=random_days)
    return random_date.strftime("%b %d %Y")

def random_num():
    ran_num = random.randint(0, 127596)
    return ran_num

def random_planet_str():
    choices = ['Alpha-', 'Beta-', 'Gama-', 'Riplon-', 'Styvix-', 'Reduxo-', 'Paragon-', 'Xeno-', 'Neo-', 'Cyber-', 'Quantum-', 'Hyper-', 'Nano-', 'Astro-', 'Mecha-', 'Synth-', 'Stellar-', 'Galacto-', 'Proto-', 'Virtu-', 'Electro-', 'Orbi-']
    return random.choice(choices)

def random_climates_str():
    sci_fi_climates = [
        'Tempestoso Iónico', 'Desértico Cristalino', 'Nébula Gélida', 
        'Selva Fluorescente', 'Océano de Ácido', 'Tundra de Cristales de Hielo', 
        'Llanuras de Vapor', 'Bosque de Gas Tóxico', 'Montañas Volcánicas', 
        'Planicie de Nieve Eterna', 'Pantano Bioluminiscente', 'Desierto de Ceniza', 
        'Archipiélago Flotante', 'Región de Tormentas de Arena', 'Pradera de Lluvia Radiactiva']
    return random.choice(sci_fi_climates)

b_random_date = random_date()
b_random_num = random_num()
b_planet_random_str = random_planet_str()
b_climates_random_str = random_climates_str()

print(f'''
                    Bitacora de Buzz Lightyear
                    Fecha: {b_random_date}
                    Sector: {b_planet_random_str}{b_random_num}''')
print(f'***El terreno de este planeta es de clase: {b_climates_random_str}***')

buzz_phrases = [
    "¡Al infinito y más allá!",
    "Este planeta parece estar lleno de misterios.",
    "¡Cuidado! Este terreno es peligroso.",
    "La atmósfera aquí es bastante hostil.",
    "Parece que hemos aterrizado en un lugar inhóspito.",
    "Este lugar está lleno de sorpresas.",
    "¡Increíble! Nunca había visto algo así.",
    "La superficie de este planeta es fascinante.",
    "Debemos proceder con cautela.",
    "Este ambiente es perfecto para una misión de exploración.",
    "¡Atención! Detecto actividad inusual.",
    "El clima aquí es extremo.",
    "Este terreno es un desafío para cualquier explorador.",
    "La fauna y flora de este lugar son únicas.",
    "¡Vaya! Este planeta es realmente impresionante.",
    "Debemos estar preparados para cualquier cosa.",
    "Este lugar parece sacado de una película de ciencia ficción.",
    "La tecnología aquí es avanzada.",
    "Este planeta tiene un ecosistema muy diverso.",
    "¡Qué aventura tan emocionante nos espera!"
]

actions = [
    "investigar",
    "correr",
    "disparar láser",
    "volar",
    "escanear el área",
    "establecer un campamento",
    "reparar la nave",
    "comunicarse con la base",
    "explorar el terreno",
    "recoger muestras",
    "analizar datos",
    "cartografiar el planeta",
    "establecer una baliza",
    "defenderse de enemigos",
    "realizar un reconocimiento",
    "buscar recursos",
    "construir una base temporal",
    "realizar un experimento",
    "documentar hallazgos",
    "responder a la señal de socorro"
]

thread.start()

print(f'***Buzz Lightyear dice: {random.choice(buzz_phrases)}***')

def inicio():
    print("Buzz Lightyear está en una misión para salvar el universo.")
    print("En su camino, se encuentra con varios desafíos.")
    print("Tus decisiones determinarán el destino de Buzz.")
    print("¡Buena suerte, cadete espacial!\n")
    primer_desafio()

def primer_desafio():
    print("Después de varias horas de sobrevolar y explorar el planeta, Buzz detecta una señal de socorro.")
    print("¿Qué debería hacer Buzz?")
    print("1. Responder a la señal de socorro.")
    print("2. Ignorar la señal y continuar explorando.")
    opcion = input("Elige una opción (1/2): ")
    
    if opcion == "1":
        print("Buzz se dirige a la señal y de repente, un grupo de alienígenas hostiles lo rodea.")
        print("Buzz debe tomar una decisión rápida para sobrevivir.")
        print("Saca su pistola de rayos y se prepara para luchar.")
        print("¿Qué debería hacer Buzz?")
        print("1. Intentar dialogar pacíficamente.")
        print("2. Luchar contra los alienígenas.")
        opcion = input("Elige una opción (1/2): ")
        
        if opcion == "1":
            comunicarse()
        elif opcion == "2":
            luchar_alienigenas()
        else:
            print("Opción no válida. Inténtalo de nuevo.")
            primer_desafio()
    elif opcion == "2":
        print("Buzz decide ignorar la señal y continuar explorando.")
        # Aquí puedes agregar más lógica para continuar la exploración
    else:
        print("Opción no válida. Inténtalo de nuevo.")
        primer_desafio()

def comunicarse():
    print("\nBuzz intenta comunicarse pacíficamente con los alienígenas.")
    print('''
        Sorprendentemente, los alienígenas responden de manera amistosa,''')
    print("Luego de entablar una conversacion amistosa, le indican el camino hacia la base de Zorg que queda a unos cuantos Kilometros.")
    print("Buzz sigue las indicaciones y llega a la base de Zorg.")
    def final_amable():
        ultimo_desafio()
    final_amable()
        
def luchar_alienigenas():
    print("\nBuzz decide luchar contra los alienígenas.")
    print("Después de una dura batalla, Buzz logra derrotarlos.")
    print("Sin embargo, queda herido y pierde tiempo valioso.")
    print("Buzz regresa a su nave, para prepararse para el siguiente desafío.")
    print("Hace un reconocimiento del área y alista sus armas y provisiones.")
    tercera_pelea()

def ultimo_desafio():
    print("\nBuzz se infiltra en la base de Zorg y después de investigar descubre que Zorg es en realidad él mismo del futuro.")
    print("Zorg le ofrece unirse a él para conquistar el universo.")
    print("¿Qué debería hacer Buzz?")
    print("1. Unirse a Zorg.")
    print("2. Pelear contra Zorg.")
    print("3. Intentar convencer a Zorg de abandonar sus planes y trabajar juntos para el bien.")
    opcion = input("Elige una opción (1/2/3): ")
    
    if opcion == "1":
        final_unirse_a_zorg()
    elif opcion == "2":
        final_pelear_contra_zorg()
    elif opcion == "3":
        final_trabajar_juntos()
    else:
        print("Opción no válida. Inténtalo de nuevo.")
        ultimo_desafio()

def final_unirse_a_zorg():
    print("\nBuzz decide unirse a Zorg.")
    print("Juntos, planean conquistar el universo.")
    print("Sin embargo, Buzz pronto se da cuenta de que ha cometido un grave error.")
    print("El universo cae en la oscuridad bajo su dominio.")
    print("FIN: Buzz se une a Zorg.")

def final_pelear_contra_zorg():
    print("\nBuzz decide pelear contra Zorg.")
    print("Zorg se prepara para atacar. ¿Qué debería hacer Buzz?")
    print("1. Disparar con su láser.")
    print("2. Atacar con su sable espacial.")
    print("3. Realizar una maniobra evasiva.")
    print("Después de una intensa batalla, Buzz logra derrotar a Zorg.")
    print("El universo está a salvo una vez más gracias a Buzz Lightyear.")
    print("FIN: Buzz derrota a Zorg.")

def final_trabajar_juntos():
    print("\nBuzz intenta convencer a Zorg de abandonar sus planes malvados.")
    print("Después de una larga conversación, Zorg finalmente accede.")
    print("Juntos, deciden trabajar para el bien del universo.")
    print("Sin embargo, su alianza es frágil y su lucha podría continuar en otra galaxia.")
    print("FIN: Buzz y Zorg continuarán su lucha en otra galaxia.")

def batalla(monstruo, fuerza, defensa, defensa_incremento=52):
    print(f"\nBuzz se enfrenta a {monstruo}.")
    print(f"{monstruo} tiene una fuerza de {fuerza} y una defensa de {defensa}.")
    
    buzz_fuerza = random.randint(1000, 3000)
    buzz_defensa = random.randint(1000, 3000)
    
    print(f"Buzz tiene una fuerza de {buzz_fuerza} y una defensa de {buzz_defensa}.")

    while fuerza > 0 and buzz_fuerza > 0:
        ataque_buzz = random.randint(5, buzz_fuerza)
        ataque_monstruo = random.randint(5, max(5, fuerza))
        
        fuerza -= max(0, ataque_buzz - defensa)
        buzz_fuerza -= max(0, ataque_monstruo - buzz_defensa)
        
        print(f"Buzz ataca y causa {max(0, ataque_buzz - defensa)} de daño. {monstruo} tiene {max(0, fuerza)} de fuerza restante.")
        print(f"{monstruo} ataca y causa {max(0, ataque_monstruo - buzz_defensa)} de daño. Buzz tiene {max(0, buzz_fuerza)} de fuerza restante.")
        
        if fuerza > 0 and buzz_fuerza > 0:
            if not buzz_action(fuerza, defensa, buzz_fuerza, buzz_defensa, monstruo):
                return False

    if fuerza <= 0:
        print(f"\nBuzz ha derrotado a {monstruo}!")
        return True
    else:
        print(f"\n{monstruo} ha derrotado a Buzz. ¡Misión fallida!")
        return False

def buzz_action(fuerza, defensa, buzz_fuerza, buzz_defensa, monstruo):
    print("\n¿Qué debería hacer Buzz?")
    print("1. Disparar con su láser.")
    print("2. Atacar con su sable espacial.")
    print("3. Realizar una maniobra evasiva.")
    accion = input("Elige una opción (1/2/3): ")

    if accion == "1":
        ataque_buzz = random.randint(10, 20)
        print(f"Buzz dispara su láser y causa {max(0, ataque_buzz - defensa)} de daño.")
    elif accion == "2":
        ataque_buzz = random.randint(15, 25)
        print(f"Buzz ataca con su sable espacial y causa {max(0, ataque_buzz - defensa)} de daño.")
    elif accion == "3":
        ataque_buzz = random.randint(5, 15)
        buzz_defensa += defensa_incremento  # Incremento de defensa parametrizado
        print(f"Buzz realiza una maniobra evasiva y mejora su defensa. Causa {max(0, ataque_buzz - defensa)} de daño.")
    else:
        print("Opción no válida. Pierdes un turno.")
        ataque_buzz = 0

    fuerza -= max(0, ataque_buzz - defensa)

    if fuerza <= 0:
        print(f"\nBuzz ha derrotado a {monstruo}!")
        return True

    ataque_monstruo = random.randint(10, fuerza)
    buzz_fuerza -= max(0, ataque_monstruo - buzz_defensa)
    print(f"{monstruo} ataca y causa {max(0, ataque_monstruo - buzz_defensa)} de daño. Buzz tiene {max(0, buzz_fuerza)} de fuerza restante.")

    if buzz_fuerza <= 0:
        print(f"\n{monstruo} ha derrotado a Buzz. ¡Misión fallida!")
        return False

    return True

def tercera_pelea():
    print("\nBuzz continúa su misión y se encuentra con un monstruo gigante llamado Gorgona.")
    print("Gorgona tiene tentáculos afilados y una piel escamosa que brilla en la oscuridad.")
    if batalla("Gorgona", 50, 15):
        cuarta_pelea()
    else:
        print("Buzz ha sido derrotado. Fin del juego.")

def cuarta_pelea():
    print("\nBuzz avanza y se encuentra con un dragón espacial llamado Draconis.")
    print("Draconis exhala fuego azul y tiene alas enormes que pueden crear tormentas.")
    if batalla("Draconis", 60, 20):
        quinta_pelea()
    else:
        print("Buzz ha sido derrotado. Fin del juego.")

def quinta_pelea():
    print("\nBuzz se enfrenta a un robot colosal llamado Titanus.")
    print("Titanus está armado con cañones láser y tiene una armadura de titanio.")
    if batalla("Titanus", 70, 25):
        sexta_pelea()
    else:
        print("Buzz ha sido derrotado. Fin del juego.")

def sexta_pelea():
    print("\nBuzz se encuentra con un ser etéreo llamado Fantasma Estelar.")
    print("El Fantasma Estelar puede volverse intangible y atacar con energía oscura.")
    if batalla("Fantasma Estelar", 80, 30):
        septima_pelea()
    else:
        print("Buzz ha sido derrotado. Fin del juego.")

def septima_pelea():
    print("\nBuzz se enfrenta a un enjambre de criaturas insectoides conocidas como los Devastadores.")
    print("Los Devastadores son rápidos y atacan en grandes números.")
    if batalla("Devastadores", 90, 35):
        octava_pelea()
    else:
        print("Buzz ha sido derrotado. Fin del juego.")

def octava_pelea():
    print("\nBuzz llega a la última línea de defensa antes de llegar a Zorg.")
    print("Aquí se enfrenta a un guerrero legendario llamado Ares, el Destructor.")
    print("Ares es conocido por su increíble fuerza y su armadura impenetrable.")
    if batalla("Ares, el Destructor", 100, 40):
        ultimo_desafio()
    else:
        print("Buzz ha sido derrotado. Fin del juego.")

# Iniciar el juego
inicio()


