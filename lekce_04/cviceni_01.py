# FOR ELSE 
# BREAK
# ===========================================
# ===========================================
# Cvičení 1: Detekce typu a délka řetězce

# Máš seznam různých hodnot:
hodnoty = ["Python", 123, True, "programování", None, 3.14, "AI"]

# Úkol:
# Pomocí smyčky `for` projdi všechny prvky v seznamu.
# - Pokud je položka typu `str`, vypiš např.:
#     "Řetězec 'Python' má 6 znaků."
# - Pokud není typu `str`, vypiš např.:
#     "Hodnota 123 je typu <class 'int'> – nemohu spočítat znaky."

# Nápověda:
# - Použij funkci `type()` pro zjištění typu položky.
# - Pro zjištění počtu znaků použij `len()`.

# Prostor pro tvé řešení:



# ===========================================
# ===========================================
# Cvičení 2: Najdi jméno – case-insensitive

# Máš seznam jmen:
jmena = ["Anna", "Petr", "Lucie", "Tomáš"]

# Uživatel zadal jméno (např. velkými písmeny):
zadane_jmeno = "PETR"

# Úkol:
# Pomocí smyčky `for` zjisti, zda se jméno zadané uživatelem nachází v seznamu.

# Nápověda:
# - Nepoužívej "if jmeno in jmena"
# - Porovnávej jména bez ohledu na velikost písmen.
#   ➝ Nejlepší je převést obě jména na malá písmena pomocí .lower()
#
# - Pokud najdeš shodu, vypiš:
#     "Jméno PETR bylo nalezeno v seznamu."
#
# - Pokud jméno v seznamu není, vypiš:
#     "Jméno PETR nebylo nalezeno."

# Prostor pro tvé řešení:




# CONTINUE
# ===========================================
# ===========================================
# 🧪 Cvičení 1: Zpracuj jen aktivní produkty

# 🧭 Kontext:
# Představ si, že pracuješ v e-shopu. Máš seznam produktů,
# ale některé z nich jsou neaktivní (např. vyprodané).
# Chceš zpracovat jen ty, které jsou aktivní (aktivni == True).

produkty = [
    {"nazev": "Notebook", "aktivni": True},
    {"nazev": "Tablet", "aktivni": False},
    {"nazev": "Myš", "aktivni": True},
]

# 💡 Úkol:
# Projdi všechny produkty a:
# - Pokud produkt není aktivní, přeskoč ho.
# - Pokud je aktivní, vypiš jeho název.





# ===========================================
# ===========================================
# 🧪 Cvičení 2: Přeskoč uživatele bez vyplněného jména

# 🧭 Kontext:
# Máš seznam uživatelů z formuláře.
# Někteří nevyplnili své jméno (je prázdný řetězec nebo None).
# Chceš vypsat jen jména, která jsou opravdu zadána.

uzivatele = ["Anna", "", "Petr", None, "Lucie"]

# 💡 Úkol:
# Projdi seznam uživatelů a:
# - Pokud jméno není zadáno (je prázdné nebo None), přeskoč ho.
# - Jinak vypiš: "Uživatel: <jméno>"





# ===========================================
# ===========================================
# 🧪 Cvičení 3: Posílej e-maily jen na platné adresy

# 🧭 Kontext:
# Chceš poslat hromadný e-mail, ale seznam obsahuje
# i neplatné nebo prázdné e-mailové adresy.
# Nechceš zbytečně odesílat na špatné adresy.

emails = ["info@example.com", "", "admin@", None, "user@gmail.com"]

# 💡 Úkol:
# Projdi seznam e-mailů a:
# - Pokud e-mail je prázdný, None, nebo neobsahuje "@", přeskoč ho.
# - Jinak vypiš: "Odesílám e-mail na: <email>"



# PASS
# ===========================================
# ===========================================
# Cvičení 1: Zpracování úloh podle stavu

# 🧭 Kontext:
# Máš seznam úkolů a jejich aktuální stav:
# Každá úloha je označena jako: "hotovo", "čeká", nebo "neznámý stav".

ukoly = {
    "Zálohovat databázi": "čeká",
    "Odeslat e-maily": "hotovo",
    "Vyčistit logy": "čeká",
    "Nastavit CI/CD": "neznámý stav",
    "Zkontrolovat faktury": "hotovo",
    "Připravit prezentaci": "čeká"
}

# 💡 Úkol:
# Projdi všechny úkoly a:
# - Pokud je úloha "hotovo", vypiš: "✅ <název úkolu> je splněna."
# - Pokud je úloha "čeká", vypiš: "⌛ <název úkolu> čeká na zpracování."
# - Pokud stav neznáme, **použij `pass`** (zatím neřešíme neznámé stavy)

# Nápověda:
# - Použij `for nazev, stav in ukoly.items()`
# - Použij `if` → `elif` → `else`
# - Použij `pass` pouze v jedné větvi – u neznámého stavu

# Prostor pro tvé řešení:





# RANGE
# ===========================================
# ===========================================
# Cvičení 1: Tiskni každé třetí číslo
# Chceš vytisknout každé třetí číslo od 0 do 30 (včetně).

# Úkol:
# Pomocí range() vytvoř sekvenci čísel od 0 do 30.
# Vypiš jen každé třetí číslo (tedy 0, 3, 6, 9...).

# Prostor pro řešení:





# ===========================================
# ===========================================
# Cvičení 2: Odpočítávání k odpálení rakety
# Vesmírná raketa se chystá ke startu!

# Úkol:
# Použij range(), aby se odpočítalo od 10 do 1 (pozpátku).
# Po skončení vypiš: "Start!"

# Prostor pro řešení:





# ===========================================
# ===========================================
# Cvičení 3: Generování kódů objednávek
# Ve skladu se připravují objednávky. Každá objednávka má jedinečný číselný kód.
# Chceš pro ně vytvořit označení.

# Úkol:
# - Použij `range()` a smyčku `for`, abys vygeneroval kódy od OBJ-1001 do OBJ-1005.
# - Každý kód vypiš na samostatný řádek.

# Ukázka výstupu:
# OBJ-1001
# OBJ-1002
# OBJ-1003
# OBJ-1004
# OBJ-1005

# Prostor pro řešení:





# ENUMERATE
# ===========================================
# ===========================================
# Cvičení 1: Očísluj seznam jmen
# Máš seznam jmen účastníků kurzu.

jmena = ["Anna", "Petr", "Lucie", "Tomáš"]

# Úkol:
# Pomocí `enumerate()` vypiš seznam tak, aby u každého jména byl jeho pořadí:
# 1. Anna
# 2. Petr
# 3. Lucie
# 4. Tomáš

# Nápověda:
# - Použij enumerate(jmena, start=1)

# Prostor pro řešení:






# ===========================================
# ===========================================
# Cvičení 2: Detekce prázdných hodnot se zpětnou vazbou
# Máš seznam odpovědí od studentů.
# Některé odpovědi jsou prázdné – to chceme označit číslem otázky.

odpovedi = ["Ano", "", "Ne", "", "Nevím"]

# Úkol:
# Pomocí `enumerate()` projdi všechny odpovědi a vypiš:
# - Pokud je odpověď neprázdná, vypiš např.:
#     "Otázka 1: Ano"
# - Pokud je prázdná (""), vypiš např.:
#     "Otázka 2: (žádná odpověď)"

# Nápověda:
# - Číslování otázek začíná od 1

# Prostor pro řešení:





# ZIP
# ===========================================
# ===========================================
# Cvičení 1: Přelož dvojjazyčný seznam
# Máš dva seznamy – česká slova a jejich anglické překlady.
# Chceš vytvořit jednoduchý překladač, který vypíše dvojice slov.

cesky = ["jablko", "kočka", "dům"]
anglicky = ["apple", "cat", "house"]

# Úkol:
# Pomocí funkce `zip()` a smyčky `for` vypiš každou dvojici ve formátu:
#     jablko → apple
#     kočka → cat
#     dům → house

# Prostor pro tvé řešení:
