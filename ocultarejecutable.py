from stegano import lsb

imagen = input("Introduce el nombre la imagen: ")
archivo = input("Introduce el nombre del archivo Python: ")

with open(archivo, "r") as f:
  info = f.read()

lsb.hide(imagen, info).save("imagen_copy.png")