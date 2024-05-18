import sys
from cx_Freeze import setup, Executable

# Dependências a serem incluídas
build_exe_options = {
    "includes": ["tkinter","customtkinter", "PIL", "os", "time"],
}

base = None
if sys.platform == "win32":
    base = "Win32GUI"  # Para ocultar a janela de console no Windows

# Configurar o executável
executables = [
    Executable("Visualizador.py", base=base)
]

setup(
    name="Visualizador 1.0.0.1",
    version="1.0",
    description="Visualizador de Imagens",
    options={"build_exe": build_exe_options},
    executables=executables
)
