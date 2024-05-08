

import tkinter as tk
import random
import time

# Lista de mantras
mantras = [
    "Respira profundamente, exhala lentamente, y siente como el estrés se disipa.",
    "Enfócate en lo que puedes controlar, deja ir lo que no puedes.",
    "Da un paso a la vez, cada paso es un progreso.",
    "Suelta las preocupaciones del día, concéntrate en el momento presente.",
    "Recuerda, la perfección es una dirección, no un lugar.",
    "Respira paz, exhala estrés.",
    "Con cada respiración, me siento más tranquilo y en paz.",
    "Elijo ser positivo y agradecido por cada momento.",
    "Dejo ir el pasado y me muevo hacia mi futuro con esperanza.",
    "Soy capaz de superar cualquier desafío con calma y claridad.",
    "Cada día es una nueva oportunidad para crecer y mejorar.",
    "El estrés es pasajero, mi paz es permanente.",
    "Me doy permiso para tomar un descanso cuando lo necesito.",
    "La felicidad es una elección que elijo hacer cada día.",
    "Estoy en control de mis emociones y no al revés.",
    "El silencio es a veces la mejor respuesta al estrés.",
    "Hoy, elijo liberarme de viejas heridas y avanzar.",
    "La gratitud transforma lo que tengo en suficiente.",
    "El rechazo es simplemente una redirección a algo mejor.",
    "Mis desafíos me están moldeando para ser más fuerte.",
    "Estoy en paz con quien soy y no necesito la aprobación de los demás.",
    "Cada respiración me trae más paz.",
    "Me permito soltar y confiar en el proceso de la vida.",
    "Mi capacidad para conquistar mis desafíos es ilimitada.",
    "Cada situación es una oportunidad para aprender y crecer.",
    "Me merezco momentos de descanso y no me siento culpable por tomarlos.",
    "Estoy comprometido con mi propio éxito y bienestar.",
    "El equilibrio en mi vida es la clave para mi felicidad y éxito.",
    "Yo defino el éxito a mi manera y trabajo para alcanzarlo.",
    "La paz viene desde adentro, no la busco afuera.",
    "Soy fuerte, soy resiliente, soy capaz.",
    "Decido enfrentar este día con calma y positividad.",
    "Cada momento de calma es un regalo que me doy a mí mismo.",
    "Hoy será un día positivo, no importan los desafíos.",
    "Mi mente está llena de pensamientos positivos y energizantes.",
    "Elijo encontrarme con la paz en cada situación.",
    "Estoy aprendiendo a moverme a través del estrés con gracia.",
    "Mi serenidad es sagrada y la protejo con mis acciones.",
    "Me libero de la necesidad de hacerlo todo perfecto.",
    "Mi bienestar es mi responsabilidad y la tomo en serio.",
    "Cada día trae nuevas posibilidades y estoy abierto a ellas.",
    "Elijo liberarme del estrés y la ansiedad.",
    "La vida fluye con gracia y facilidad cuando me permito relajarme.",
    "Estoy dispuesto a ver las cosas desde una perspectiva más tranquila.",
    "Me perdono y libero las cargas del pasado.",
    "Acepto la paz como mi estado natural.",
    "Estoy aquí ahora, en este momento, completamente presente.",
    "Mis pensamientos crean mi realidad y elijo pensamientos tranquilos.",
    "Me rodeo de tranquilidad y rechazo el caos.",
    "Hoy elijo soltar y dejar que las cosas sucedan.",
    "La vida es un viaje y me tomo mi tiempo para disfrutarlo.",
    "El bienestar es una prioridad en mi vida, y actúo en consecuencia.",
    "Estoy agradecido por cada pequeño momento de paz.",
    "Reconozco mi estrés y gentilmente lo guío hacia la salida.",
    "Estoy en armonía con el ritmo de mi propia vida.",
    "El silencio nutre mi alma y mi mente.",
    "Hoy me doy espacio para simplemente ser.",
    "A través de la respiración, encuentro mi centro y mi paz.",
    "El descanso es parte esencial de mi productividad y creatividad.",
    "Estoy abierto a la tranquilidad en todas las áreas de mi vida.",
    "Cada decisión que tomo está infundida con calma y sabiduría.",
    "Estoy presente en cada tarea, cada descanso y cada encuentro.",
    "Libero mi mente de pensamientos pesados y me lleno de luz.",
    "Hoy, cada paso que doy es ligero y lleno de paz.",
    "Reconozco y respeto mis límites, y esto me trae tranquilidad.",
    "Hoy encuentro placer en las pequeñas victorias y momentos de calma.",
    "Cada acto de bondad hacia mí mismo es un paso hacia la paz.",
    "Soy paciente con mi progreso y confío en mi camino.",
    "Mi mente está despejada, mi corazón está tranquilo.",
    "Agradezco a mi cuerpo y mente por su fortaleza y resiliencia.",
    "Asumo la responsabilidad de mi energía y cómo afecta a mi paz.",
    "Hoy, el estrés no controla mis acciones ni mis pensamientos.",
    "Encuentro fortaleza en la serenidad y la quietud.",
    "Me doy permiso para desconectar y recargar cuando lo necesito.",
    "Mis momentos de pausa son tan importantes como mis momentos de acción.",
    "Hoy, cada respiración me acerca más a la paz interior.",
    "Abrazo la calma y rechazo el tumulto en mi vida diaria.",
    "Me trato a mí mismo con la misma compasión que trataría a un amigo.",
    "Estoy conectado con la naturaleza y esto me trae paz.",
    "El descanso mental es tan valioso como el físico.",
    "Cultivo la paz dentro de mí y esto se refleja en mi exterior.",
    "Aprendo de mis errores y los veo como oportunidades para crecer.",
    "La paz es mi guía y el estrés es solo un visitante pasajero.",
    "Cada día me doy la oportunidad de empezar de nuevo con paz.",
    "Elijo reaccionar a los desafíos con serenidad y pensamiento claro.",
    "Estoy comprometido con mi crecimiento personal y mi tranquilidad.",
    "Reconozco mis emociones sin dejar que ellas me dominen.",
    "La paciencia es mi aliada en tiempos de estrés y cambio.",
    "Acojo la calma y la hago parte de mi rutina diaria.",
    "Soy digno de momentos de total paz y los busco activamente.",
    "A través de la calma, encuentro claridad y dirección.",
    "Permito que mi mente descanse y mi espíritu se renueve.",
    "La aceptación es la llave que libera mi estrés y mi preocupación.",
    "Estoy agradecido por cada oportunidad de vivir en paz."
]


class MantraApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mantra del Día")
        self.root.geometry('800x200')  # Configura el tamaño de la ventana

        self.label = tk.Label(self.root, text='', font=('Arial', 20), wraplength=700)
        self.label.pack(expand=True)

        self.update_mantra()

    def update_mantra(self):
        # Selecciona un mantra al azar y actualiza el texto del label
        self.label['text'] = random.choice(mantras)
        # Re-programa la función para correr cada 120 segundos (2 minutos)
        self.root.after(120000, self.update_mantra)


def main():
    root = tk.Tk()
    app = MantraApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
