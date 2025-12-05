#Parser y lexer hecho por:
# Santiago Barrientos, Juan Esteban Rayo y Manuel Gutiérrez

import re #libreria para expresiones regulares
import json #libreria para manejar json
from pathlib import Path #libreria para manejar rutas de archivos

# ---------------------------
# LEXER (convierte texto a tokens)
# ---------------------------
class Lexer:
    # reglas para reconocer los tokens
    reglas = [
    ('STRING',   r'"[^"]*"|\'[^\']*\''),   # texto entre comillas
    ('NUMBER',   r'[0-9]+(\.[0-9]+)?'),    # números
    ('BOOLEAN',  r'\b(true|false|si|no)\b'), # booleanos
    ('IDENT',    r'[A-Za-z_][A-Za-z0-9_]*'), # identificadores
    ('LBRACE',   r'\{'), # llave izquierda
    ('RBRACE',   r'\}'), # llave derecha
    ('LBRACKET', r'\['), # corchete izquierdo
    ('RBRACKET', r'\]'), # corchete derecho
    ('COLON',    r':'), # dos puntos que es el asignador
    ('COMMA',    r','), # coma

    ('NEWLINE',  r'\n'), # salto de línea
    ('SKIP',     r'[ \t]+'), # espacios y tabs
    ('MISMATCH', r'.'), # cualquier otro carácter
]


    # armamos el patrón maestro
    partes = []
    for nombre, regla in reglas:
        partes.append(f"(?P<{nombre}>{regla})")
    master_pattern = re.compile("|".join(partes))

    def __init__(self, texto):
        self.texto = texto
        self.tokens = []

    def quitar_comentarios(self):
        resultado = []
        dentro_string = False
        comilla = None
        i = 0
        while i < len(self.texto):
            ch = self.texto[i]
            # detectar inicio/fin de string
            if not dentro_string and ch in ('"', "'"):
                dentro_string = True
                comilla = ch
                resultado.append(ch)
            elif dentro_string:
                resultado.append(ch)
                if ch == comilla:
                    dentro_string = False
                    comilla = None
            elif ch == '#':
                # saltar hasta el fin de línea (comentario)
                while i < len(self.texto) and self.texto[i] != '\n':
                    i += 1
                continue
            else:
                resultado.append(ch)
            i += 1
        return "".join(resultado)

    def tokenize(self):
        limpio = self.quitar_comentarios()
        for match in self.master_pattern.finditer(limpio):
            tipo = match.lastgroup
            valor = match.group(0)

            if tipo == 'NEWLINE' or tipo == 'SKIP':
                continue
            if tipo == 'STRING':
                self.tokens.append(('STRING', valor[1:-1]))
            elif tipo == 'NUMBER':
                if '.' in valor:
                    self.tokens.append(('NUMBER', float(valor)))
                else:
                    self.tokens.append(('NUMBER', int(valor)))
            elif tipo == 'BOOLEAN':
                val = valor.lower()
                self.tokens.append(('BOOLEAN', val in ('true', 'si')))
            elif tipo == 'IDENT':
                self.tokens.append(('IDENTIFIER', valor))
            elif tipo in ('LBRACE', 'RBRACE', 'LBRACKET', 'RBRACKET', 'COLON', 'COMMA'):
                self.tokens.append((tipo, valor))
            elif tipo == 'MISMATCH':
                if valor == '=':  # por si aparece "=" en vez de ":"
                    self.tokens.append(('COLON', ':'))
        return self.tokens


# ---------------------------
# PARSER (convierte tokens en estructura tipo diccionario)
# ---------------------------
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def ver(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return (None, None)

    def avanzar(self):
        tok = self.ver()
        self.pos += 1
        return tok

    def esperar(self, tipo):
        if self.ver()[0] == tipo:
            return self.avanzar()[1]
        else:
            raise SyntaxError(f"Se esperaba {tipo}, encontrado {self.ver()}")

    def parsear(self):
        resultado = {}
        while self.pos < len(self.tokens):
            if self.ver()[0] == 'COMMA':
                self.avanzar()
                continue
            clave = self.parsear_clave()
            if clave is None:
                break
            self.esperar('COLON')
            valor = self.parsear_valor()
            resultado[clave] = valor
        return resultado

    def parsear_clave(self):
        tipo, val = self.ver()
        if tipo == 'IDENTIFIER':
            self.avanzar()
            return val
        if tipo == 'LBRACKET':
            self.avanzar()
            nombre = self.esperar('IDENTIFIER')
            self.esperar('RBRACKET')
            return nombre
        return None

    def parsear_valor(self):
        tipo, val = self.ver()
        if tipo in ('STRING', 'NUMBER', 'BOOLEAN'):
            self.avanzar()
            return val
        if tipo == 'LBRACE':
            return self.parsear_objeto()
        if tipo == 'LBRACKET':
            return self.parsear_lista()
        # si no reconoce, avanza igual
        self.avanzar()
        return val

    def parsear_objeto(self):
        self.esperar('LBRACE')
        obj = {}
        while True:
            if self.ver()[0] == 'RBRACE':
                self.avanzar()
                break
            if self.ver()[0] == 'COMMA':
                self.avanzar()
                continue
            clave = self.parsear_clave()
            if clave is None:
                raise SyntaxError("Se esperaba una clave dentro de {}")
            self.esperar('COLON')
            valor = self.parsear_valor()
            obj[clave] = valor
        return obj

    def parsear_lista(self):
        self.esperar('LBRACKET')
        lista = []
        while True:
            if self.ver()[0] == 'RBRACKET':
                self.avanzar()
                break
            if self.ver()[0] == 'COMMA':
                self.avanzar()
                continue
            lista.append(self.parsear_valor())
        return lista

#Guardar como archivo arbol ast
def save_ast_to_file(ast, filepath):
    """
    Guarda el AST en un archivo de texto en formato JSON.
    """
    try:
        with open(filepath, 'w', encoding='utf-8') as file:
            json.dump(ast, file, indent=4)
        print(f"AST guardado exitosamente en '{filepath}'")
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")

# ---------------------------
# PROGRAMA PRINCIPAL
# ---------------------------
archivos = ["snake.brik", "tetris.brik"]

for ruta in archivos:
    p = Path(ruta)
    if not p.exists():
        print(f"No se encontró el archivo: {ruta}")
        continue

    texto = p.read_text(encoding="utf-8")

    # Lexer
    lexer = Lexer(texto)
    tokens = lexer.tokenize()

    # Parser
    print(f"\n=== Tokens para {ruta} ===")
    for i, tok in enumerate(tokens):
        print(f"{i:03d}: {tok}")

    parser = Parser(tokens)
    resultado = parser.parsear()

    print("\nResultado en JSON :")
    print(json.dumps(resultado, indent=2, ensure_ascii=False))

    #guardar el AST en un archivo
    save_ast_to_file(resultado, p.with_suffix('.ast.json'))