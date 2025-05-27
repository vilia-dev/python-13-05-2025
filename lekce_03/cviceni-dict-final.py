# 🎬 FILMOVÁ DATABÁZE – cvičení se slovníkem v Pythonu
# -----------------------------------------------------
# Pracujete pro malou online videotéku, která eviduje filmy, jejich hodnocení a žánr.
# Vaším úkolem bude postupně rozšiřovat slovník `filmy` a provádět s ním různé operace.


# -----------------------------------------------------
# 🔹 1. KROK – výpis původní databáze
# Slovník `filmy` je už připravený níže.
# 📌 ÚKOL: Vypište celý slovník pomocí funkce `print()`, abyste viděli původní obsah.

filmy = {
    "Matrix": 9.0,
    "Inception": 8.8
}

print("🎬 Původní databáze:")
print(filmy)


# -----------------------------------------------------
# 🔹 2. KROK – přidání nového filmu přes vstup od uživatele
# 📌 ÚKOL: Požádejte uživatele o:
# - název filmu (pomocí `input()`)
# - jeho hodnocení (pomocí `input()`, převedené na `float`)
# 📌 Poté přidejte tento nový film do slovníku `filmy`
# Nakonec vypište aktualizovaný slovník.

nazev1 = input("Zadejte název filmu: ")
hodnoceni = float(input("Zadejte jeho hodnocení: "))
filmy[nazev1] = hodnoceni

print("📥 Databáze po přidání filmu:")
print(filmy)


# -----------------------------------------------------
# 🔹 3. KROK – úprava struktury pro přidání žánru
# Zjistíme, že jen hodnocení nestačí – potřebujeme ukládat i žánr.
# 📌 ÚKOL: Upravíme hodnoty ve slovníku tak, aby místo čísla obsahovaly vnořený slovník.

# Nová struktura bude vypadat takto:
# "Matrix": {
#     "hodnoceni": 9.0,
#     "zanr": "sci-fi"
# }

# ➕ Převeďte původní filmy na tuto novou strukturu:
filmy["Matrix"] = {
    "hodnoceni": 9.0,
    "zanr": "sci-fi"
}

filmy["Inception"] = {
    "hodnoceni": 8.8,
    "zanr": "sci-fi"
}

# ➕ Také převedeme nově přidaný film na stejnou strukturu,
# ale zatím bez žánru – ten přidáme v dalším kroku:
filmy[nazev1] = {
    "hodnoceni": hodnoceni
}

# 📌 ÚKOL: Přidejte klíč `"zanr"` k nově přidanému filmu a nastavte ho na `"drama"`
filmy[nazev1]["zanr"] = "drama"  # můžete změnit na jiný žánr dle libosti

print("📂 Rozšířená databáze (s žánry):")
print(filmy)


# -----------------------------------------------------
# 🔹 4. KROK – vyhledávání filmu podle názvu
# 📌 ÚKOL: Nechte uživatele zadat název filmu, který chce najít.
# Použijte `.get()` k bezpečnému získání údajů o filmu.
# Pokud film existuje, vypište: 🎞️ Film Matrix má hodnocení 9.0
# Pokud neexistuje, vypište: ❌ Film XY nebyl nalezen v databázi.

jmeno = input("🔍 Zadejte název filmu: ")
film = filmy.get(jmeno)

if film is not None:
    print("🎞️ Film", jmeno, "má hodnocení", film["hodnoceni"])
else:
    print("❌ Film", jmeno, "nebyl nalezen v databázi.")


# -----------------------------------------------------
# 🔹 5. KROK – odstranění filmu z databáze
# 📌 ÚKOL: Nechte uživatele zadat název filmu, který chce smazat.
# Použijte `.pop()` – pokud film existuje, zobrazte zprávu:
# 🧹 Film Matrix byl odstraněn.
# 📌 Vypište také poslední známé údaje: žánr a hodnocení.
# Pokud film neexistuje, vypište: ⚠️ Film XY nebyl nalezen v databázi.

jmeno = input("🗑️ Zadejte název filmu, který chcete odstranit z databáze: ")
film = filmy.pop(jmeno, None)

if film is not None:
    print("🧹 Film", jmeno, "byl odstraněn.")
    print("📌 Poslední známé údaje:")
    print("Žánr:", film["zanr"])
    print("Hodnocení:", film["hodnoceni"])
else:
    print(f"⚠️ Film {jmeno} nebyl nalezen v databázi.")


# -----------------------------------------------------
# 🔹 6. KROK – zálohování a vymazání databáze
# 📌 ÚKOL:
# - Vytvořte kopii slovníku `filmy` pomocí `.copy()` a uložte ji do proměnné `zalohovano`
# - Poté smažte původní slovník pomocí `.clear()`
# - Vypište obsah obou proměnných (`filmy` i `zalohovano`)

zalohovano = filmy.copy()
filmy.clear()

print("🧾 Po vymazání:")
print("Aktuální databáze:", filmy)
print("Zálohovaná databáze:", zalohovano)


# -----------------------------------------------------
# 🔹 7. KROK – výpis ze zálohy
# 📌 ÚKOL: Vypište z `zalohovano`:
# - názvy všech filmů pomocí `.keys()`
# - údaje o filmech pomocí `.values()`
# - kompletní záznamy pomocí `.items()`

print("📄 Názvy filmů:")
print(zalohovano.keys())

print("📄 Údaje o filmech (hodnocení + žánr):")
print(zalohovano.values())

print("📄 Kompletní katalog:")
print(zalohovano.items())


# -----------------------------------------------------
# ✅ HOTOVO!
# Právě jste vytvořili jednoduchou, ale užitečnou databázi filmů. Skvělá práce! 🎉
