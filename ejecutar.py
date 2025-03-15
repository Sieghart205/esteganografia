from stegano import lsb
import os

imagen = input("Introduce el nombre la imagen: ")

info = lsb.reveal(imagen)

with open("archivo_temporal.py", "w") as f:
  f.write(info)

os.system("python archivo_temporal.py")
os.remove("archivo_temporal.py")