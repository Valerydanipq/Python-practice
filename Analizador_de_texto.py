text = input("Ingresa un texto a eleccion")
letters = []

text = text.lower()
input("Ingresa la primera letra")
letters.append(input("Ingresa un texto a eleccion"))

letters.append(input("Ingresa la primera letra"))
letters.append(input("Ingresa la segunda letra"))
letters.append(input("Ingresa la tercera letra"))

letters.append(input("Ingresa la primera letra".lower()))
letters.append(input("Ingresa la segunda letra".lower()))
letters.append(input("Ingresa la tercera letra".lower()))

print("\n")
print("CANTIDAD DE LETRA")
cantidad_letters1 = text.count(letters[0])
cantidad_letters2 = text.count(letters[0])
cantidad_letters3 = text.count(letters[0])

print(f" Hemos encontrado la letter'{letters[0]}' repetida{cantidad_letters1} veces")
print(f" Hemos encontrado la letter'{letters[1]}' repetida{cantidad_letters2} veces")
print(f" Hemos encontrado la letter'{letters[2]}' repetida{3} veces")
letters = text.split()
print(f" Hemos encontrado {len(letters)} palabras en tu texto")
print("LETRAS DE INICIO Y DE FIN")
letters_start = text[0]
letters_end = text[-1]
print(f"La letra inicial is '{letters_start}' y la letra final es '{letters_end}' ")

print("\n")
print("TEXTO INVERTIDO")
letters.reverse()
text_invertido= ''.join(letters)
print(f"Si ordenamos tu texto al reves va a decir: '{text_invertido}'")

print("\n")
print("BUSCANDO LA PALABRA PYTHON")
buscar_python = ' python' in text
dic = {True:"si" ,  False: "no"}
print(f"La palabra 'Python' {dic[buscar_python]} se encuentra en el text") 















