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

cislo = 5

# Sem doplň while smyčku

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

odpoved = ""

# Sem doplň while smyčku



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

tajne_cislo = 7
tip = None

# Sem doplň while smyčku


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

text = ""

# Sem doplň while smyčku s podmínkami


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

soucet = 0
vstup = ""

# Sem doplň while smyčku a podmínky





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




