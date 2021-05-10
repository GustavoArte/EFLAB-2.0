# import sys
# from cx_Freeze import setup, Executable

# setup(
#     name = "EFLAB",
#     version = "2.0",
#     author="Gustavo Arteaga",
#     author_email="gustavoarteaga0508@gmail.com",
#     description = "Desktop application for determining the efficient regions of a power transformer, using load profiles.",
#     executables = [Executable("Eflab_01.py")])



import cx_Freeze
import sys
import matplotlib

base = None

if sys.platform == 'win32':

base = "Win32GUI"

executables = [cx_Freeze.Executable("EFLAB.py", base=base, icon="eflab.ico")]

cx_Freeze.setup(
    name = "EFLAB",
    options = {"build_exe": {"packages":["tkinter","matplotlib","pandas"], "include_files":["eflab.ico","img/LOGO.png","img/help_question_1566.png"]}},
    version = "2.0",
    description = "Desktop application for determining the efficient regions of a power transformer, using load profiles..",
    author="Gustavo Arteaga",
    author_email="gustavoarteaga0508@gmail.com",
    executables = executables
    )