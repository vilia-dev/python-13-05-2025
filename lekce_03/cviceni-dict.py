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



# -----------------------------------------------------
# 🔹 2. KROK – přidání nového filmu přes vstup od uživatele
# 📌 ÚKOL: Požádejte uživatele o:
# - název filmu (pomocí `input()`)
# - jeho hodnocení (pomocí `input()`, převedené na `float`)
# 📌 Poté přidejte tento nový film do slovníku `filmy`
# Nakonec vypište aktualizovaný slovník.



print("📥 Databáze po přidání filmu:")



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




# ➕ Také převedeme nově přidaný film na stejnou strukturu,
# ale zatím bez žánru – ten přidáme v dalším kroku:



# 📌 ÚKOL: Přidejte klíč `"zanr"` k nově přidanému filmu a nastavte ho na `"drama"`



print("📂 Rozšířená databáze (s žánry):")
print(filmy)


# -----------------------------------------------------
# 🔹 4. KROK – vyhledávání filmu podle názvu
# 📌 ÚKOL: Nechte uživatele zadat název filmu, který chce najít.
# Použijte `.get()` k bezpečnému získání údajů o filmu.
# Pokud film existuje, vypište: 🎞️ Film Matrix má hodnocení 9.0
# Pokud neexistuje, vypište: ❌ Film XY nebyl nalezen v databázi.




# -----------------------------------------------------
# 🔹 5. KROK – odstranění filmu z databáze
# 📌 ÚKOL: Nechte uživatele zadat název filmu, který chce smazat.
# Použijte `.pop()` – pokud film existuje, zobrazte zprávu:
# 🧹 Film Matrix byl odstraněn.
# 📌 Vypište také poslední známé údaje: žánr a hodnocení.
# Pokud film neexistuje, vypište: ⚠️ Film XY nebyl nalezen v databázi.




# -----------------------------------------------------
# 🔹 6. KROK – zálohování a vymazání databáze
# 📌 ÚKOL:
# - Vytvořte kopii slovníku `filmy` pomocí `.copy()` a uložte ji do proměnné `zalohovano`
# - Poté smažte původní slovník pomocí `.clear()`
# - Vypište obsah obou proměnných (`filmy` i `zalohovano`)




# -----------------------------------------------------
# 🔹 7. KROK – výpis ze zálohy
# 📌 ÚKOL: Vypište z `zalohovano`:
# - názvy všech filmů pomocí `.keys()`
# - údaje o filmech pomocí `.values()`
# - kompletní záznamy pomocí `.items()`

