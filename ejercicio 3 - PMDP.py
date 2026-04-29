import hashlib

esperado = "944a1e869969dd8a4b64ca5e6ebc209a"
contenido1 = "Ingredientes de la pocion Feliz Felix:\n- Patas de escarabajo\n- Saliva de bubo\n- Cuerno de bicornio en polvo\n- Pelo de Abisal\n- Asphodel en polvo\n- Zumo de Beleño\n- Hidromiel de salamandra"
contenido2 = "Ingredientes de la pocion Feliz Felix:\n- Patas de escarabajo\n- Saliva de bubo\n- Cuerno de bicornio en polvo\n- Pelo de Abisal\n- Asphodel en polvo\n- Zumo de Beleño\n- Hidromiel de salamandra\n- (modificado)"

with open("potion_felix1.txt", "w") as f:
    f.write(contenido1)
with open("potion_felix2.txt", "w") as f:
    f.write(contenido2)

def md5_file(path):
    h = hashlib.md5()
    with open(path, "rb") as f:
        h.update(f.read())
    return h.hexdigest()

h1 = md5_file("potion_felix1.txt")
h2 = md5_file("potion_felix2.txt")

print(f"Hash MD5 potion_felix1.txt: {h1}")
print(f"Hash MD5 potion_felix2.txt: {h2}")
print(f"Hash esperado             : {esperado}")
print(f"felix1 coincide: {h1 == esperado}")
print(f"felix2 coincide: {h2 == esperado}")