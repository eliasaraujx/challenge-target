def contar_a(s):
    contador = 0
    
    for char in s:
        if char == 'a' or char == 'A':
            contador += 1
            
    return f"A letra 'a' aparece {contador} vez(es) na string."


texto = "A raposa marrom salta sobre a cerca."
print(contar_a(texto))