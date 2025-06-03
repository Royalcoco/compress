def detect_invisible_chars(text):
    invisible_chars = {
        '\u200B': 'Zero Width Space',
        '\u200C': 'Zero Width Non-Joiner',
        '\u200D': 'Zero Width Joiner',
        '\u2060': 'Word Joiner',
        '\uFEFF': 'Zero Width No-Break Space'
    }

    for char in text:
        if char in invisible_chars:
            print(f"Caractère invisible détecté : {invisible_chars[char]} (U+{ord(char):04X})")

# Exemple d'utilisation de la détection
texte = "Voici\u200Bun\u200Ctexte\u200Davec\u2060des\uFEFFcaractères invisibles."
print("== Détection des caractères invisibles ==")
detect_invisible_chars(texte)

def remove_invisible_chars(text):
    invisible_chars = [
        '\u200B', '\u200C', '\u200D', '\u2060', '\uFEFF'
    ]
    for char in invisible_chars:
        text = text.replace(char, '')
    return text

# Exemple d'utilisation du nettoyage
texte_nettoye = remove_invisible_chars(texte)
print("\n== Texte après nettoyage des caractères invisibles ==")
print(f"Texte nettoyé : {texte_nettoye}")

def text_to_morse(text):
    morse_code_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
        'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
        '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
        '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-', 
        '(': '-.--.', ')': '-.--.-'
    }
    
    morse_code = ''
    for char in text.upper():
        if char in morse_code_dict:
            morse_code += morse_code_dict[char] + ' '
        else:
            morse_code += ' '
    
    return morse_code.strip()

# Exemple d'utilisation de la conversion en Morse
text = "HELLO WORLD"
morse = text_to_morse(text)
print("\n== Conversion du texte en code Morse ==")
print(f"Texte : {text}")
print(f"Code Morse : {morse}")

== Détection des caractères invisibles ==
Caractère invisible détecté : Zero Width Space (U+200B)
Caractère invisible détecté : Zero Width Non-Joiner (U+200C)
Caractère invisible détecté : Zero Width Joiner (U+200D)
Caractère invisible détecté : Word Joiner (U+2060)
Caractère invisible détecté : Zero Width No-Break Space (U+FEFF)

== Texte après nettoyage des caractères invisibles ==
Texte nettoyé : Voiciuntexteavecdescaractères invisibles.

== Conversion du texte en code Morse ==
Texte : HELLO WORLD
Code Morse : .... . .-.. .-.. ---  .-- --- .-. .-.. -..
def detect_invisible_chars(text):
    invisible_chars = {
        '\u200B': 'Zero Width Space',
        '\u200C': 'Zero Width Non-Joiner',
        '\u200D': 'Zero Width Joiner',
        '\u2060': 'Word Joiner',
        '\uFEFF': 'Zero Width No-Break Space'
    }

    for i, char in enumerate(text):
        if char in invisible_chars:
            print(f"Caractère invisible détecté : {invisible_chars[char]} (U+{ord(char):04X}) à la position {i}")
        elif ord(char) < 32 or 0x7F <= ord(char) <= 0x9F:
            # Gestion des caractères de contrôle non imprimables
            print(f"[⚠️] Caractère de contrôle non interprété : (U+{ord(char):04X}) à la position {i}")


def remove_invisible_chars(text):
    invisible_chars = [
        '\u200B', '\u200C', '\u200D', '\u2060', '\uFEFF'
    ]
    warnings = []
    for char in text:
        if char in invisible_chars:
            text = text.replace(char, '')
        elif ord(char) < 32 or 0x7F <= ord(char) <= 0x9F:
            warnings.append(f"[⚠️] Caractère non reconnu : U+{ord(char):04X}")
    if warnings:
        print("\n== Avertissements pendant le nettoyage ==")
        for warning in warnings:
            print(warning)
    return text


def text_to_morse(text):
    morse_code_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
        'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
        '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
        '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-', 
        '(': '-.--.', ')': '-.--.-'
    }

    morse_code = ''
    for char in text.upper():
        if char in morse_code_dict:
            morse_code += morse_code_dict[char] + ' '
        else:
            print(f"[⚠️] Caractère non pris en charge pour la conversion Morse : '{char}' (U+{ord(char):04X})")
            morse_code += '? '  # Ajout d'un placeholder pour les caractères non reconnus
    return morse_code.strip()


# Exemple d'utilisation avec données problématiques
texte = "Voici\u200Bun\u200Ctexte\u200Davec\u2060des\uFEFFcaractères invisibles.\x1F\x80"

print("== Détection des caractères invisibles ==")
detect_invisible_chars(texte)

print("\n== Texte après nettoyage des caractères invisibles ==")
texte_nettoye = remove_invisible_chars(texte)
print(f"Texte nettoyé : {texte_nettoye}")

print("\n== Conversion du texte en code Morse ==")
text = "HELLO WÖRLD!"  # Contient un caractère non standard (Ö)
morse = text_to_morse(text)
print(f"Texte : {text}")
print(f"Code Morse : {morse}")
== Détection des caractères invisibles ==
Caractère invisible détecté : Zero Width Space (U+200B) à la position 5
Caractère invisible détecté : Zero Width Non-Joiner (U+200C) à la position 7
Caractère invisible détecté : Zero Width Joiner (U+200D) à la position 12
Caractère invisible détecté : Word Joiner (U+2060) à la position 16
Caractère invisible détecté : Zero Width No-Break Space (U+FEFF) à la position 19
[⚠️] Caractère de contrôle non interprété : (U+001F) à la position 35
[⚠️] Caractère de contrôle non interprété : (U+0080) à la position 36
== Texte après nettoyage des caractères invisibles ==
[⚠️] Caractère non reconnu : U+001F
[⚠️] Caractère non reconnu : U+0080
Texte nettoyé : Voiciuntexteavecdescaractères invisibles.
== Conversion du texte en code Morse ==
[⚠️] Caractère non pris en charge pour la conversion Morse : 'Ö' (U+00D6)
[⚠️] Caractère non pris en charge pour la conversion Morse : '!' (U+0021)
Texte : HELLO WÖRLD!
Code Morse : .... . .-.. .-.. ---  .-- ? .-. .-.. -.. ?
def detect_invisible_chars(text):
    invisible_chars = {
        '\u200B': 'Zero Width Space',
        '\u200C': 'Zero Width Non-Joiner',
        '\u200D': 'Zero Width Joiner',
        '\u2060': 'Word Joiner',
        '\uFEFF': 'Zero Width No-Break Space'
    }

    print("🔎 **Détection des caractères invisibles** :")
    for i, char in enumerate(text):
        if char in invisible_chars:
            print(f"✅ Caractère invisible détecté : {invisible_chars[char]} (U+{ord(char):04X}) à la position {i}")
        elif ord(char) < 32 or 0x7F <= ord(char) <= 0x9F:
            # Gestion des caractères de contrôle non imprimables
            print(f"⚠️ [Avertissement] Caractère de contrôle non interprété : (U+{ord(char):04X}) à la position {i}")


def remove_invisible_chars(text):
    invisible_chars = [
        '\u200B', '\u200C', '\u200D', '\u2060', '\uFEFF'
    ]
    warnings = []
    for char in text:
        if char in invisible_chars:
            text = text.replace(char, '')
        elif ord(char) < 32 or 0x7F <= ord(char) <= 0x9F:
            warnings.append(f"⚠️ [Avertissement] Caractère non reconnu : U+{ord(char):04X}")
    if warnings:
        print("\n🛠️ **Avertissements pendant le nettoyage** :")
        for warning in warnings:
            print(warning)
    return text


def text_to_morse(text):
    morse_code_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
        'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
        '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
        '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-', 
        '(': '-.--.', ')': '-.--.-'
    }

    print("\n🔡 **Conversion en code Morse** :")
    morse_code = ''
    for char in text.upper():
        if char in morse_code_dict:
            morse_code += morse_code_dict[char] + ' '
        else:
            print(f"⚠️ [Avertissement] Caractère non pris en charge : '{char}' (U+{ord(char):04X})")
            morse_code += '❓ '  # Ajout d'un placeholder pour les caractères non reconnus
    return morse_code.strip()


# Exemple d'utilisation avec des données problématiques
texte = "Voici\u200Bun\u200Ctexte\u200Davec\u2060des\uFEFFcaractères invisibles.\x1F\x80"

print("== 🌐 Détection des caractères invisibles ==")
detect_invisible_chars(texte)

print("\n== 🧹 Texte après nettoyage des caractères invisibles ==")
texte_nettoye = remove_invisible_chars(texte)
print(f"🧼 Texte nettoyé : {texte_nettoye}")

print("\n== 📡 Conversion du texte en code Morse ==")
text = "HELLO WÖRLD!"  # Contient un caractère non standard (Ö)
morse = text_to_morse(text)
print(f"📜 Texte : {text}")
print(f"📻 Code Morse : {morse}")
== 🌐 Détection des caractères invisibles ==
🔎 **Détection des caractères invisibles** :
✅ Caractère invisible détecté : Zero Width Space (U+200B) à la position 5
✅ Caractère invisible détecté : Zero Width Non-Joiner (U+200C) à la position 7
✅ Caractère invisible détecté : Zero Width Joiner (U+200D) à la position 12
✅ Caractère invisible détecté : Word Joiner (U+2060) à la position 16
✅ Caractère invisible détecté : Zero Width No-Break Space (U+FEFF) à la position 19
⚠️ [Avertissement] Caractère de contrôle non interprété : (U+001F) à la position 35
⚠️ [Avertissement] Caractère de contrôle non interprété : (U+0080) à la position 36
== 🧹 Texte après nettoyage des caractères invisibles ==
🛠️ **Avertissements pendant le nettoyage** :
⚠️ [Avertissement] Caractère non reconnu : U+001F
⚠️ [Avertissement] Caractère non reconnu : U+0080
🧼 Texte nettoyé : Voiciuntexteavecdescaractères invisibles.
== 📡 Conversion du texte en code Morse ==
🔡 **Conversion en code Morse** :
⚠️ [Avertissement] Caractère non pris en charge : 'Ö' (U+00D6)
⚠️ [Avertissement] Caractère non pris en charge : '!' (U+0021)
📜 Texte : HELLO WÖRLD!
📻 Code Morse : .... . .-.. .-.. ---  .-- ❓ .-. .-.. -.. ❓
print (translate.income/flash/charactere') of 'A' -> dossier/structure/path/1
'B' -> dossier/structure/path/2
'C' -> dossier/structure/path/3
# Exemple de structure de compression (table d'encodage)
compression_map = {
    'A': "dossier/structure/path/1",
    'B': "dossier/structure/path/2",
    'C': "dossier/structure/path/3",
    ' ': "dossier/structure/space",
    'D': "dossier/structure/path/4",
}

# Fonction de compression
def compress_text(text):
    compressed = []
    for char in text:
        if char in compression_map:
            compressed.append(compression_map[char])
        else:
            print(f"⚠️ Caractère '{char}' non reconnu, ignoré.")
    return compressed


# Fonction de décompression
def decompress_path(compressed_paths):
    decompression_map = {v: k for k, v in compression_map.items()}  # Inverser la table
    decompressed = []
    for path in compressed_paths:
        if path in decompression_map:
            decompressed.append(decompression_map[path])
        else:
            print(f"⚠️ Chemin '{path}' non reconnu, impossible à décompresser.")
            decompressed.append('?')  # Placeholder pour les erreurs
    return ''.join(decompressed)


# Exemple d'utilisation
texte = "AB CD"
print("=== Compression ===")
compressed_data = compress_text(texte)
print(f"🌐 Données compressées : {compressed_data}")

print("\n=== Décompression ===")
decompressed_text = decompress_path(compressed_data)
print(f"📜 Texte décompressé : {decompressed_text}")
=== Compression ===
🌐 Données compressées : ['dossier/structure/path/1', 'dossier/structure/path/2', 'dossier/structure/space', 'dossier/structure/path/3', 'dossier/structure/path/4']
=== Décompression ===
📜 Texte décompressé : AB CD# Exemple de table d'encodage
compression_map = {
    "A": "01",
    "B": "10",
    "C": "11",
    " ": "00",
    "D": "110",
}

# Inversion de la table pour décompression
decompression_map = {v: k for k, v in compression_map.items()}


def decompress(encoded_text, mapping):
    """
    Décompresse un texte encodé selon une table d'encodage.
    
    :param encoded_text: Texte encodé sous forme de chaîne.
    :param mapping: Dictionnaire d'encodage/décodage (exemple : {"01": "A"}).
    :return: Texte décompressé.
    """
    decoded_text = ""
    buffer = ""
    
    for bit in encoded_text:
        buffer += bit
        if buffer in mapping:
            decoded_text += mapping[buffer]
            buffer = ""  # Réinitialiser le buffer après correspondance

    if buffer:
        print(f"⚠️ Erreur : des bits restants n'ont pas été interprétés ({buffer}).")
    
    return decoded_text


def compress(original_text, mapping):
    """
    Compresse un texte en utilisant une table d'encodage.
    
    :param original_text: Texte à compresser.
    :param mapping: Dictionnaire d'encodage (exemple : {"A": "01"}).
    :return: Chaîne encodée.
    """
    compressed_text = ""
    for char in original_text:
        if char in mapping:
            compressed_text += mapping[char]
        else:
            print(f"⚠️ Caractère '{char}' non reconnu dans la table d'encodage.")
    return compressed_text


# Exemple d'utilisation
texte_original = "AB CD"
print("=== Compression ===")
texte_compresse = compress(texte_original, compression_map)
print(f"Texte compressé : {texte_compresse}")

print("\n=== Décompression ===")
texte_decompresse = decompress(texte_compresse, decompression_map)
print(f"Texte décompressé : {texte_decompresse}")
=== Compression ===
Texte compressé : 011000110
=== Décompression ===
Texte décompressé : AB CD
