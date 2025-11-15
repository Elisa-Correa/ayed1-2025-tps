import os


ARCHIVO_ENTRADA = "archivos/PERSONAS.TXT"
ARMENIA_FILE = "archivos/ARMENIA.TXT"
ITALIA_FILE = "archivos/ITALIA.TXT"
ESPAÑA_FILE = "archivos/ESPAÑA.TXT"


def clasificar_registros():
    """
    Lee los registros de personas y los clasifica en tres archivos de salida 
    según la terminación de su apellido (IAN, INI, EZ).
    """

    try:
        # Abre el archivo de entrada con las personas cargadas.
        with open(ARCHIVO_ENTRADA, 'rt', encoding='utf-8') as file:

            # Abre los archivos donde se filtran y agregan las personas de el Archivo PERSONAS.TXT.
            with open(ARMENIA_FILE, 'wt', encoding='utf-8-sig') as armenia, \
                    open(ITALIA_FILE, 'wt', encoding='utf-8-sig') as italia, \
                    open(ESPAÑA_FILE, 'wt', encoding='utf-8-sig') as españa:

                # Iterar sobre cada línea del archivo PERSONAS.TXT
                for linea in file:
                    registro = linea.strip()

                    if not registro or ',' not in registro:
                        continue

                    # Separa el apellido y nombre
                    partes = registro.split(',', 1)
                    apellido = partes[0].strip()

                    if apellido.endswith("ian"):
                        armenia.write(registro + '\n')
                    elif apellido.endswith("ini"):
                        italia.write(registro + '\n')
                    elif apellido.endswith("ez"):
                        españa.write(registro + '\n')

        print("Clasificación finalizada.")

    except FileNotFoundError:
        print(
            f"Error - El archivo de entrada '{ARCHIVO_ENTRADA}' no fue encontrado.")

    except Exception as e:
        print(f"Ocurrió un error inesperado durante el procesamiento: {e}")


def verificar_archivos(nombres_archivos: list[str]):
    """
    Imprime el contenido de los archivos de salida generados.
    """
    print("\n--- Contenido de los Archivos Clasificados ---")

    for nombre in nombres_archivos:
        print(f"\n------ Archivo: {nombre} ------")

        try:
            with open(nombre, 'r', encoding='utf-8-sig') as file:
                contenido = file.read()

                if contenido.strip():
                    print(contenido.strip())

                else:
                    print("Archivo vacío.")

        except FileNotFoundError:
            print(f"Archivo no encontrado.")


if __name__ == "__main__":

    clasificar_registros()

    archivos_salida = [ARMENIA_FILE, ITALIA_FILE, ESPAÑA_FILE]
    verificar_archivos(archivos_salida)
