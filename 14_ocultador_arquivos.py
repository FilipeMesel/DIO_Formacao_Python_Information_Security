#Biblioteca que fornece tipos de dados compatíveis com C e permite funções de chamada em DLLs ou
#bibliotecas compartilhadas
import ctypes

atributo_ocultar = 0x02

retorno = ctypes.windll.kernel32.SetFileAttributesW('14_ocutar.txt', atributo_ocultar)

if retorno:
    print("Arquivo foi ocultado")
else:
    print("Arquivo não foi ocultado")