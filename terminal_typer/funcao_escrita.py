from time import sleep

def gerador(texto: str, tempo: float):
    for i in texto:
        yield i  # vai soltando caractere por caractere
        sleep(tempo)


def escrever(texto, tempo=0.05):
    for pedaco in gerador(texto, tempo):
        print(pedaco, end="", flush=True)  # flush força a saída imediata

if __name__ == "__main__":
    escrever('Fábrica de Programadores')

