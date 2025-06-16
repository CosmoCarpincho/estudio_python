texto = "   es el tema de los espacios en blancoo  "

print(texto.strip())
print(texto.rstrip())
print(texto.lstrip())

# tema titulos, mayusculas, minusculas

texto = "ada loVelaCe"
print(texto.title())
print(texto.upper())
print(texto.lower())
print(texto.capitalize())

# remover prefijos

web = "https://miweb.com.ar"
web_limpia = web.removeprefix("https://")
print(web_limpia)

nombre_web = web_limpia.removesuffix(".com.ar")
print(nombre_web)
