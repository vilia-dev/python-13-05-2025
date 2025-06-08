# ===========================================
# 🧪 Cvičení 1: Odpočítávání – základní `while`
# 
# 🧭 Kontext:
# Chceme si vyzkoušet úplně základní smyčku `while`.
# Program má odpočítat čísla od 5 do 1 a pak vypsat "Start!".
#
# 💡 Úkol:
# - Vytvoř proměnnou `cislo` s hodnotou 5.
# - Pomocí `while` smyčky:
#   - vypisuj hodnotu `cislo`, dokud je větší než 0,
#   - v každém kroku sniž hodnotu o 1.
# - Po skončení smyčky vypiš: "Start!"
# ===========================================

# cislo = 5

# Sem doplň while smyčku

cislo = 5

while cislo > 0:
    print(cislo)
    cislo = cislo - 1

print("Start!")



# ===========================================
# 🧪 Cvičení 2: Požádej, dokud nedostaneš "ano"
#
# 🧭 Kontext:
# Chceme, aby uživatel potvrdil, že chce pokračovat.
# Program se opakuje, dokud nezadá "ano".
#
# 💡 Úkol:
# - Vytvoř proměnnou `odpoved`, nastav na prázdný řetězec.
# - Pomocí `while`:
#   - opakovaně se ptej uživatele: "Chceš pokračovat? (ano/ne):"
#   - pokud napíše "ano", smyčka skončí.
# ===========================================

# odpoved = ""

# Sem doplň while smyčku

odpoved = ""

while odpoved != "ano":
    odpoved = input("Chceš pokračovat? (ano/ne): ")

# ===========================================
# 🧪 Cvičení 3: Hádej tajné číslo
#
# 🧭 Kontext:
# Tvoříme jednoduchou hru.
# Program si "myslí" tajné číslo, uživatel hádá, dokud se netrefí.
#
# 💡 Úkol:
# - Nastav proměnnou `tajne_cislo` na hodnotu 7.
# - Vytvoř proměnnou `tip` a nastav na `None`.
# - Pomocí `while`:
#   - ptej se uživatele: "Hádej číslo: "
#   - převedený vstup uložíš do proměnné `tip`.
#   - pokud `tip` není správný, vypiš: "Zkus to znovu."
#   - pokud `tip` je správný, vypiš: "Uhodl/a jsi!" a smyčka skončí.
# ===========================================

# tajne_cislo = 7
# tip = None

# Sem doplň while smyčku

tajne_cislo = 7
tip = None

while tip != tajne_cislo:
    tip = int(input("Hádej číslo: "))
    if tip != tajne_cislo:
        print("Zkus to znovu.")

print("Uhodl/a jsi!")


# ===========================================
# 🧪 Cvičení 4: Reakce na vstup pomocí `if` v `while`
#
# 🧭 Kontext:
# V předchozí části lekce jsme se naučili, že v těle `while` smyčky
# můžeme používat podmínky pomocí `if` a `else`.
# 
# Toto cvičení navazuje – vyzkoušíme si kombinaci `while` + `if/elif/else`.
#
# 💡 Úkol:
# - Vytvoř proměnnou `text`, nastav ji na prázdný řetězec.
# - Pomocí `while`:
#   - opakovaně se ptej uživatele na vstup: "Zadej odpověď: "
#   - Pokud napíše `"ano"`, vypiš `"Pokračujeme!"`
#   - Pokud napíše `"ne"`, vypiš `"Škoda."`
#   - Pokud napíše `"konec"`, smyčka se ukončí bez reakce
# ===========================================

# text = ""

# Sem doplň while smyčku s podmínkami

text = ""

while text != "konec":
    text = input("Zadej odpověď: ")

    if text == "ano":
        print("Pokračujeme!")
    elif text == "ne":
        print("Škoda.")
    # pokud zadá "konec", neuděláme nic – smyčka skončí


# ===========================================
# 🧪 Cvičení 5: Sčítání čísel od uživatele
#
# 🧭 Kontext:
# V tomto úkolu si procvičíme `while` smyčku společně s podmínkami `if` a `else`.
# Program bude postupně přijímat vstupy od uživatele a přičítat je k součtu.
#
# 💡 Úkol:
# - Vytvoř proměnnou `soucet` a nastav ji na 0.
# - Vytvoř proměnnou `vstup`, nastav ji na prázdný řetězec.
# - Pomocí `while`:
#   - opakovaně se ptej: "Zadej číslo (nebo 'konec'):"
#   - pokud uživatel zadá číslo (pouze číslice), převeď na `int` a přičti k `soucet`,
#   - pokud zadá `"konec"`, vypiš `"Dokončuji..."`,
#   - jinak vypiš `"To není platné číslo."`
# - Po skončení smyčky (tedy **mimo tělo smyčky**) vypiš:
#   `"Součet je: X"` – kde X je výsledná hodnota proměnné `soucet`.
# ===========================================

# soucet = 0
# vstup = ""

# Sem doplň while smyčku a podmínky


soucet = 0
vstup = ""

while vstup != "konec":
    vstup = input("Zadej číslo (nebo 'konec'): ")

    if vstup.isdigit():
        cislo = int(vstup)
        soucet = soucet + cislo
    elif vstup == "konec":
        print("Dokončuji...")
    else:
        print("To není platné číslo.")

print("Součet je:", soucet)


# ===========================================
# 🧪 Cvičení 6: Násob hodnotu pomocí `*=`
#
# 🧭 Kontext:
# Tentokrát budeme počítat součin všech čísel zadaných uživatelem.
#
# 💡 Úkol:
# - Vytvoř proměnnou `soucin`, nastav na 1.
# - Použij `while`, která poběží, dokud vstup není `"konec"`.
# - Pokud je vstup číslo, převeď na `int` a pomocí `*=` přenásob `soucin`.
# - Pokud zadá `"konec"`, smyčka končí.
# - Nakonec vypiš: `"Výsledný součin je: X"`
# ===========================================

soucin = 1
vstup = ""

while vstup != "konec":
    vstup = input("Zadej číslo (nebo 'konec'): ")
    if vstup.isdigit():
        soucin *= int(vstup)
    elif vstup != "konec":
        print("To není platné číslo.")

print("Výsledný součin je:", soucin)



# ===========================================
# 🧪 Cvičení 7: Odečítej body pomocí `-=`
#
# 🧭 Kontext:
# Uživatel začíná s 20 body. Za každou chybnou odpověď ztrácí 1 bod.
#
# 💡 Úkol:
# - Nastav proměnnou `body` na 20.
# - V cyklu `while`, dokud `body > 0`:
#   - Ptej se: "Napiš 'python':"
#   - Pokud odpověď není `"python"`, odečti 1 bod pomocí `-=` a vypiš počet zbývajících bodů.
#   - Pokud uživatel napíše správně `"python"`, vypiš "Správně!" a ukonči smyčku pomocí `break`.
# - Pokud uživatel ztratí všechny body, vypiš "Prohrál/a jsi!"
# ===========================================

body = 20

while body > 0:
    odpoved = input("Napiš 'python': ")
    if odpoved == "python":
        print("Správně!")
        break
    else:
        body -= 1
        print("Špatně. Zbývá ti", body, "bodů.")

if body == 0:
    print("Prohrál/a jsi!")

# ===========================================

body = 20
odpoved = ""

while odpoved != "python" and body > 0:
    odpoved = input("Napiš 'python': ")
    if odpoved != "python":
        body -= 1
        print("Špatně. Zbývá ti", body, "bodů.")

if odpoved == "python":
    print("Správně!")
else:
    print("Prohrál/a jsi!")


# ===========================================
# 🧪 Cvičení 8: Klasický cyklus vs comprehension
#
# 🧭 Kontext:
# Chceme vytvořit seznam čísel od 1 do 10 dvěma způsoby –
# klasickým cyklem a pomocí list comprehension.
#
# 💡 Úkol:
# - Pomocí `for` cyklu vytvoř seznam `cisla_klasicky` s čísly 1–10.
# - Poté stejný seznam vytvoř pomocí list comprehension do `cisla_comprehension`.
# - Na konci vypiš oba seznamy.
# ===========================================

cisla_klasicky = []
for i in range(1, 11):
    cisla_klasicky.append(i)

cisla_comprehension = [i for i in range(1, 11)]

print("Klasický:", cisla_klasicky)
print("Comprehension:", cisla_comprehension)


# ===========================================
# 🧪 Cvičení 9: Sudá čísla pomocí list comprehension a `if`
#
# 🧭 Kontext:
# Chceme vytvořit seznam všech sudých čísel od 0 do 20.
#
# ℹ️ Poznámka:
# Číslo je sudé, pokud je beze zbytku dělitelné dvěma.
# V Pythonu to ověříme pomocí:
#   i % 2 == 0
# (`%` znamená zbytek po dělení)
#
# 💡 Úkol:
# - Pomocí list comprehension vytvoř seznam `suda_cisla`,
#   který obsahuje pouze čísla dělitelná dvěma.
# - Na konci vypiš výsledek.
# ===========================================

suda_cisla = [i for i in range(21) if i % 2 == 0]

print("Sudá čísla:", suda_cisla)
