traductorbrille = {
    'a': '⠁', 'b': '⠃', 'c': '⠉', 'd': '⠙', 'e': '⠑',
    'f': '⠋', 'g': '⠛', 'h': '⠓', 'i': '⠊', 'j': '⠚',
    'k': '⠅', 'l': '⠇', 'm': '⠍', 'n': '⠝', 'o': '⠕',
    'p': '⠏', 'q': '⠟', 'r': '⠗', 's': '⠎', 't': '⠞',
    'u': '⠥', 'v': '⠧', 'w': '⠺', 'x': '⠭', 'y': '⠽',
    'z': '⠵',
    '0': '⠴', '1': '⠁', '2': '⠃', '3': '⠉', '4': '⠙',
    '5': '⠑', '6': '⠋', '7': '⠛', '8': '⠓', '9': '⠊',
    ' ': ' ', 
    '.': '⠲', ',': '⠂', '?': '⠦', '!': '⠖', ';': '⠆',
    ':': '⠒', '-': '⠤', "'": '⠄', '"': '⠶', '/': '⠌',
    '@': '⠈', '#': '⠼', '%': '⠨', '&': '⠯', '(': '⠶', ')': '⠶'
}

def traducir_a_braille(texto):
    resultado = ""
    texto = texto.lower() 
    
    for i in texto:
        if i in traductorbrille:
            resultado += traductorbrille[i]
        else:
            resultado += '?'
    return resultado

def traductor():
    print("Traductor a Braille (Unicode)")
    texto = input("Ingresa el texto a traducir: ")
    
    traduccion = traducir_a_braille(texto)

    print("\nTexto original:")
    print(texto)

    print("\nTexto traducido a Braille:")
    print(traduccion)

    print("Los caracteres no soportados se muestran como '?'")

traductor()