# 🎓 KONFERENCE – cvičení s množinami v Pythonu
# -----------------------------------------------------
# Organizujete vývojářskou konferenci s workshopy.
# Účastníci si vybírali z následujících témat:
# - Python
# - JavaScript
# - AI a strojové učení
# Budete spravovat účastníky pomocí datového typu `set`.


# -----------------------------------------------------
# 🔹 1. KROK – definice přihlášek
# 📌 ÚKOL: Níže jsou připraveny tři množiny s přihlášenými účastníky.
# Pro začátek je pouze vypište pomocí funkce `print()`.

workshop_python = {"Anna", "Petr", "Lucie", "Jan", "Marek"}
workshop_js = {"Lucie", "Tomáš", "Jan", "Klára"}
workshop_ai = {"Marek", "Tomáš", "Ivana", "Anna"}

print("🐍 Python:", workshop_python)
print("🖥️ JavaScript:", workshop_js)
print("🤖 AI:", workshop_ai)


# -----------------------------------------------------
# 🔹 2. KROK – základní manipulace s množinou
# 📌 ÚKOL:
# - Přidejte účastníka "Radek" do workshopu Python
# - Odeberte "Anna" z Python workshopu
# - Pokuste se odebrat "Klára" z Python pomocí .discard()
# - Nakonec vypište nový stav workshopu Python

workshop_python.add("Radek")
workshop_python.remove("Anna")
workshop_python.discard("Klára")

print("Aktuální Python workshop:", workshop_python)


# -----------------------------------------------------
# 🔹 3. KROK – sjednocení účastníků
# 📌 ÚKOL: Spočítejte, kolik unikátních lidí se přihlásilo celkem.

vsichni = workshop_python | workshop_js | workshop_ai
vsichni = workshop_python.union(workshop_js, workshop_ai)
print("✅ Celkem unikátních úcastníků:", len(vsichni))


# -----------------------------------------------------
# 🔹 4. KROK – společné účasti
# 📌 ÚKOL: Vypište, kdo byl přihlášen na všechny tři workshopy současně.

vsichni_trikrat = workshop_python & workshop_js & workshop_ai
vsichni_trikrat = workshop_python.intersection(workshop_js, workshop_ai)

print("⭐ Na všech třech workshopech:", vsichni_trikrat)


# -----------------------------------------------------
# 🔹 5. KROK – jen jeden workshop
# 📌 ÚKOL: Vypište, kdo byl pouze na Python workshopu (a na žádném jiném).

jen_python = workshop_python - (workshop_js | workshop_ai)
ostatni = workshop_js.union(workshop_ai)
jen_python = workshop_python.difference(ostatni)
print("🔹 Jen Python:", jen_python)


# -----------------------------------------------------
# 🔹 6. KROK – symetrický rozdíl
# 📌 ÚKOL: Vypište, kdo si vybral pouze Python nebo pouze AI (ale ne oba).
rozliseni = workshop_python.symmetric_difference(workshop_ai)
rozliseni = workshop_python ^ workshop_ai
print("🌐 Jen Python nebo AI (ale ne oba):", rozliseni)


# -----------------------------------------------------
# 🔹 7. KROK – izolovaní účastníci
# 📌 ÚKOL: Zjistěte, zda je celá skupina přihlášených na JavaScript zcela oddělená
# od ostatních workshopů – tedy zda žádný účastník není zároveň v Python nebo AI.
ostatni = workshop_python.union(workshop_ai)
izolovani = workshop_js.isdisjoint(ostatni)

izolovani = workshop_js.isdisjoint(workshop_python | workshop_ai)
print("❓ JavaScript je zcela oddělený?", izolovani)


# -----------------------------------------------------
# 🔹 8. KROK – podmnožiny
# 📌 ÚKOL: Ověřte, zda `jen_python` je podmnožinou všech účastníků.

print("⬇ Jen Python ∈ vsichni?", jen_python.issubset(vsichni))


# -----------------------------------------------------
# 🔹 9. KROK – záloha a mazání
# 📌 ÚKOL:
# - Vytvořte kopii množiny `workshop_python` do proměnné `zaloha`
# - Vymažte původní množinu pomocí `.clear()`
# - Vypište obě množiny

zaloha = workshop_python.copy()
workshop_python.clear()

print("🔧 Vymazaný workshop_python:", workshop_python)
print("📃 Záloha:", zaloha)

