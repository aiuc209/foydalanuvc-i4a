def foydalanuvchi_ma_lumotlari(foydalanuvchilar):
    natija = []
    for foydalanuvchi in foydalanuvchilar:
        ism = foydalanuvchi['ism']
        familiya = foydalanuvchi['familiya']
        yosh = foydalanuvchi['yosh']
        ball = foydalanuvchi['ball']
        satr = f"{ism} {familiya} — {yosh} yoshda, Ball: {ball}"
        natija.append(satr)
    return natija

foydalanuvchilar = [
    {'ism': 'Ali', 'familiya': 'Valiyev', 'yosh': 20, 'ball': 85},
    {'ism': 'Bobur', 'familiya': 'Tojiboyev', 'yosh': 22, 'ball': 90},
    {'ism': 'Sardor', 'familiya': 'Rahimov', 'yosh': 21, 'ball': 88}
]

print(foydalanuvchi_ma_lumotlari(foydalanuvchilar))
