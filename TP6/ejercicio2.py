import os
import sys


def dividir_archivo_grande():
    """
    Divide un archivo de texto en múltiples partes, respetando un tamaño máximo 
    por archivo y asegurando que la división se realice solo después de un salto de línea.
    """

    print("--- División de Archivos ---")

    # Se encarga de obtener y validar el archivo

    ruta_directorio_script = os.path.dirname(os.path.abspath(__file__))
    ruta_padre = os.path.abspath(
        os.path.join(ruta_directorio_script, os.pardir))

    # 🌟 NUEVA VARIABLE: Ruta absoluta a la carpeta de destino "archivos"
    ruta_carpeta_salida = os.path.join(ruta_padre, "archivos")

    while True:
        archivo_a_buscar = input(
            "Ingrese el nombre del archivo a dividir: ").strip()
        archivo = os.path.join(ruta_carpeta_salida, archivo_a_buscar)

        try:
            with open(archivo, 'rb') as file:
                print(f"Archivo '{archivo_a_buscar}' encontrado con éxito.")
                break
        except FileNotFoundError:
            print(
                f"Error: No se encontró el archivo. Verifique el nombre y la ruta absoluta intentada: {archivo}")

    # Obtiene y calcula el tamaño para la división por tamaño del archivo
    tamanio_max_bytes = 0
    while True:
        try:
            tamanio_max_mb = float(
                input("Ingrese el tamaño máximo de cada parte (en MB): "))
            if tamanio_max_mb <= 0:
                raise ValueError
            tamanio_max_bytes = int(tamanio_max_mb * 1024 * 1024)
            break
        except ValueError:
            print("Error: El tamaño debe ser un número positivo.")

    # Se encarga de la División
    try:
        with open(archivo, 'rb') as archivo_in:

            nombre_con_ext = os.path.basename(archivo)
            nombre_base, extension = os.path.splitext(nombre_con_ext)

            contador_parte = 1
            buffer_tamanio = 0
            archivo_out = None

            # 🌟 MODIFICACIÓN 1: Construir la ruta completa del archivo de salida
            nombre_parte_salida = f"{nombre_base}_parte{contador_parte}{extension}"
            ruta_archivo_salida = os.path.join(
                ruta_carpeta_salida, nombre_parte_salida)

            print(
                f"-> Generando {nombre_parte_salida} en {os.path.basename(ruta_carpeta_salida)}/...")

            # Abrir el primer archivo con la ruta completa
            archivo_out = open(ruta_archivo_salida, 'wb')

            while True:
                linea = archivo_in.readline()
                if not linea:
                    break
                tamanio_linea = len(linea)

                if buffer_tamanio + tamanio_linea > tamanio_max_bytes and buffer_tamanio > 0:

                    archivo_out.close()

                    contador_parte += 1
                    # 🌟 MODIFICACIÓN 2: Construir la ruta completa del nuevo archivo de salida
                    nombre_parte_salida = f"{nombre_base}_parte{contador_parte}{extension}"
                    ruta_archivo_salida = os.path.join(
                        ruta_carpeta_salida, nombre_parte_salida)

                    print(
                        f"-> Generando {nombre_parte_salida} en {os.path.basename(ruta_carpeta_salida)}/...")

                    archivo_out = open(ruta_archivo_salida, 'wb')
                    buffer_tamanio = 0

                archivo_out.write(linea)
                buffer_tamanio += tamanio_linea

            if archivo_out:
                archivo_out.close()

            print("\nProceso de división finalizado con éxito.")
            print(
                f"Se generaron {contador_parte} partes en la carpeta 'archivos'.")

    except Exception as e:
        print(f"\nERROR - El proceso de división no pudo llevarse a cabo.")
        print(f"Motivo del error: {e}")

    finally:
        if 'archivo_out' in locals() and archivo_out and not archivo_out.closed:
            archivo_out.close()


if __name__ == "__main__":
    dividir_archivo_grande()
