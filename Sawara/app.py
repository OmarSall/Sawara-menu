from flask import Flask, render_template

app = Flask(__name__)

# Sample menu data
menu_items = [
    {"id": 1, "name": "Gyros", "category": "Dania Mięsne", "price": "34zł", "image": "gyros_duzy.jpg", "desc":
     "<ul class='menu-description'><li>🍟 Frytki, ryż lub kasza</li><li>🥗 Surówka</li><li>🧄 Sos</li></ul> <strong><span class='red-text'><ins>Standarowo polewamy sosem czosnkowym</ins></span></strong> <br>W przypadku innych preferencji, proszę poinformować osobę przyjmującą zamówienie."},
    {"id": 2, "name": "Gyros mały", "category": "Dania Mięsne", "price": "24zł", "image": "gyros_maly.jpg", "desc":
     "<ul class='menu-description'><li>🍟 Frytki, ryż lub kasza</li><li>🥗 Surówka</li><li>🧄 Sos</li></ul> <strong><span class='red-text'><ins>Standarowo polewamy sosem czosnkowym</ins></span></strong> <br>W przypadku innych preferencji, proszę poinformować osobę przyjmującą zamówienie."},
    {"id": 3, "name": "Petra", "category": "Dania Mięsne", "price": "36.50zł", "image": "petra.jpg", "desc":
     "<ul class='menu-description'><li>🥙 Hommos</li><li>🍖 Gyros</li><li>🥗 Surówka</li><li>🍞 Chleb arabski</li><li>🧄 Sos</li></ul><strong><span class='red-text'><ins>Standarowo polewamy sosem czosnkowym</ins></span></strong><br>W przypadku innych preferencji, proszę poinformować osobę przyjmującą zamówienie."},
    {"id": 4, "name": "Petra mała", "category": "Dania Mięsne", "price": "26zł", "image": "petra.jpg", "desc":
     "<ul class='menu-description'><li>🥙 Hommos</li><li>🍖 Gyros</li><li>🥗 Surówka</li><li>🍞 Chleb arabski</li><li>🧄 Sos</li></ul><strong><span class='red-text'><ins>Standarowo polewamy sosem czosnkowym</ins></span></strong><br>W przypadku innych preferencji, proszę poinformować osobę przyjmującą zamówienie."},
    {"id": 5, "name": "Filet z kurczaka", "category": "Dania Mięsne", "price": "34.50", "image": "IMG_6226.jpg", "desc":
     "<ul class='menu-description'><li>🍟 Frytki, ryż lub kasza</li><li>🥗 Surówka</li><li>🧄 Sos</li></ul> <strong><span class='red-text'><ins>Standarowo serwujemy z sosem majonezowym</ins></span></strong> <br>W przypadku innych preferencji, proszę poinformować osobę przyjmującą zamówienie."},
    {"id": 6, "name": "Filet z kurczaka mały", "category": "Dania Mięsne", "price": "24.50zł", "image": "IMG_6226.jpg", "desc":
     "<ul class='menu-description'><li>🍟 Frytki, ryż lub kasza</li><li>🥗 Surówka</li><li>🧄 Sos</li></ul> <strong><span class='red-text'><ins>Standarowo serwujemy z sosem majonezowym</ins></span></strong> <br>W przypadku innych preferencji, proszę poinformować osobę przyjmującą zamówienie."},
    {"id": 7, "name": "Devolay", "category": "Dania Mięsne", "price": "36zł", "image": "IMG_6256.jpg", "desc":
     "<ul class='menu-description'><li>🍟 Frytki, ryż lub kasza</li><li>🥗 Surówka</li><li>🧄 Sos</li></ul> <strong><span class='red-text'><ins>Standarowo serwujemy z sosem majenowym</ins></span></strong> <br>W przypadku innych preferencji, proszę poinformować osobę przyjmującą zamówienie."},
    {"id": 8, "name": "Pita Gyros", "category": "Dania Mięsne", "price": "20zł", "image": "pita.jpg", "desc":
     "<ul class='menu-description'><li>🍖 Gyros</li><li>🍅 Pomidor</li><li>🥒 Ogórek</li><li>🥗 Surówka</li><li>🧄 Sos</li></ul><strong><span class='red-text'><ins>Standarowo pita zawiera sos czosnkowy</ins></span></strong><br>W przypadku innych preferencji, proszę poinformować osobę przyjmującą zamówienie."},
    {"id": 9, "name": "Tortilla Gyros", "category": "Dania Mięsne", "price": "24zł", "image": "tortilla.jpg", "desc":
     "<ul class='menu-description'><li>🍖 Gyros</li><li>🥙 Hommos</li><li>🍅 Pomidor</li><li>🥬 Kapustka pekińska</li><li>🧄 Sos</li></ul><strong><span class='red-text'><ins>Standarowo tortilla zawiera sos czosnkowy</ins></span></strong><br>W przypadku innych preferencji, proszę poinformować osobę przyjmującą zamówienie."},
    {"id": 10, "name": "Tortilla Max", "category": "Dania Mięsne", "price": "26zł", "image": "tortilla.jpg", "desc":
     "<ul class='menu-description'><li>🍖 Gyros</li><li>🥙 Hommos</li><li>🍅 Pomidor</li><li>🥬 Kapustka pekińska</li><li>🍟 Frytki</li><li>🧄 Sos</li></ul><strong><span class='red-text'><ins>Standarowo torilla zawiera sos czosnkowy</ins></span></strong><br>W przypadku innych preferencji, proszę poinformować osobę przyjmującą zamówienie."},
    {"id": 11, "name": "Pizza Margarita", "category": "Pizza", "price": "30zł", "image": "IMG_6347.jpg", "desc":
     "<ul class='menu-descripti7n'><li>🍅 Sos pomidorowy</li><li>🧀 Ser</li></ul>Średnica pizzy 32 cm<br><strong><span class='red-text'><ins>Sos za dodatkową opłatą</ins></span></strong><br>W przypadku innych preferencji, proszę poinformować osobę przyjmującą zamówienie."},
    {"id": 12, "name": "Pizza z Gyrosem", "category": "Pizza", "price": "32zł", "image": "IMG_6427.jpg", "desc":
     "<ul class='menu-description'><li>🍅 Sos pomidorowy</li><li>🧀 Ser</li><li>🍖 Gyros</li></ul>Średnica pizzy 32 cm<br><strong><span class='red-text'><ins>Sos za dodatkową opłatą</ins></span></strong><br>W przypadku innych preferencji, proszę poinformować osobę przyjmującą zamówienie."},
    {"id": 13, "name": "Pizza z Szynką", "category": "Pizza", "price": "32zł", "image": "IMG_6363.jpg", "desc":
     "<ul class='menu-description'><li>🍅 Sos pomidorowy</li><li>🧀 Ser</li><li>🥩 Szynka</li><li>🍍 Kawałki ananasa</li></ul>Średnica pizzy 32 cm<br><strong><span class='red-text'><ins>Sos za dodatkową opłatą</ins></span></strong><br>W przypadku innych preferencji, proszę poinformować osobę przyjmującą zamówienie."},
    {"id": 14, "name": "Pizza Sawara", "category": "Pizza", "price": "37zł", "image": "IMG_6466.jpg", "desc":
     "<ul class='menu-description'><li>🍅 Sos pomidorowy</li><li>🧀 Ser</li><li>🍖 Gyros</li> <li>🌶️ Peperoni</li><li>🫒 Oliwki</li><li>🧀 Ser Favita</li><li>🫑 Papryka</li></ul>Średnica pizzy 32 cm<br><strong><span class='red-text'><ins>Sos za dodatkową opłatą</ins></span></strong><br>W przypadku innych preferencji, proszę poinformować osobę przyjmującą zamówienie."},
    {"id": 15, "name": "Pizza Hawajska", "category": "Pizza", "price": "35zł", "image": "IMG_6285.jpg", "desc":
     "<ul class='menu-description'><li>🍅 Sos pomidorowy</li><li>🧀 Ser</li><li>🥩 Szynka</li><li>🍍 Kawałki ananasa</li></ul>Średnica pizzy 32 cm<br><strong><span class='red-text'><ins>Sos za dodatkową opłatą</ins></span></strong><br>W przypadku innych preferencji, proszę poinformować osobę przyjmującą zamówienie."},
    {"id": 16, "name": "Pizza Wegetariańska", "category": "Pizza", "price": "35zł", "image": "IMG_6372.jpg", "desc":
     "<ul class='menu-description'><li>🍅 Sos pomidorowy</li><li>🧀 Ser</li><li>🌿 Szpinak</li><li>🍅 Pomidor</li><li>🌻 Słonecznik</li></ul>Średnica pizzy 32 cm<br><strong><span class='red-text'><ins>Sos za dodatkową opłatą</ins></span></strong><br>W przypadku innych preferencji, proszę poinformować osobę przyjmującą zamówienie."},
    {"id": 17, "name": "Sfiha Mięsna", "category": "Sfiha", "price": "14zł", "image": "IMG_6436.jpg", "desc":
    "<ul> <li>🥩 Aromatyczne mięso przyprawione orientalnymi ziołami</li> <li>🍅 Sos pomidorowy</li> <li>🧀 Ser</li> <li>🌿 Świeże zioła</li> </ul><br>mini pizza arabska z mięsem"},
    {"id": 18, "name": "Sfiha ze szpinakiem", "category": "Sfiha", "price": "14zł", "image": "IMG_6448.jpg", "desc":
    "<ul> <li>🍞 Tradycyjne ciasto chlebowe</li> <li>🌿 Świeży szpinak</li> <li>🧀 Ser</li> <li>🧄 Aromatyczne przyprawy</li> </ul><br>chlebowa łódeczka ze szpinakiem i serem"},
    {"id": 18, "name": "Sfiha z ziołami", "category": "Sfiha", "price": "14zł", "image": "IMG_6488.jpg", "desc":
    "<ul> <li>🍞 Tradycyjne ciasto chlebowe</li> <li>🌿 Mieszanka aromatycznych ziół</li> <li>🫒 Oliwa z oliwek</li> <li>🧄 Delikatne przyprawy</li> </ul><br>mini pizza arabska z ziołami"},
    {"id": 19, "name": "Zestaw sfiha + zupa", "category": "Sfiha", "price": "42zł", "image": "zestaw sfiha.png", "desc":
    "sfiha 3 szt., zupa z soczewicy"},
    {"id": 20, "name": "Falafel (5szt. + sos)", "category": "Wege", "price": "20zł", "image": "falafel.jpg", "desc":
    "<ul> <li>🧆 Smażony kotlet z ciecierzycy</li> </ul>"},
    {"id": 21, "name": "Zestaw Falafel", "category": "Wege", "price": "36.5zł", "image": "zestaw falafel.jpg", "desc":
    "<ul> <li>🧆 5x Smażony kotlet z ciecierzycy</li> <li>🥣 Kremowy hommos</li> <li>🥗 Świeża surówka</li> <li>🥖 Tradycyjny chleb arabski</li> </ul>"},
    {"id": 22, "name": "Pita Falafel", "category": "Wege", "price": "20zł", "image": "pita falafel.jpg", "desc":
    "<ul><li>🧆 Falafel (3 szt.)</li><li>🥬 Sałata</li><li>🍅 Pomidor</li><li>🥒 Ogórek</li><li>🌰 Rzepa</li><li>🥣 Hommos</li><li>🧄 Sos</li></ul><br><strong><span class='red-text'><ins>Standarowo pita falafel zawiera sos czosnkowy</ins></span></strong><br>W przypadku innych preferencji, proszę poinformować osobę przyjmującą zamówienie."},
    {"id": 23, "name": "Hommos", "category": "Wege", "price": "20zł", "image": "hommos.jpg", "desc":
    "<ul><li>🥣 Pasta z ciecierzycy (Hommos)</li><li>🥖 Chleb arabski</li></ul>"},
    {"id": 24, "name": "Mtabbal (5szt. + sos)", "category": "Wege", "price": "20zł", "image": "mtabbal.jpg", "desc":
    "<ul><li>🍆 Pasta z bakłażana</li><li>🥖 Chleb arabski</li></ul>"},
    {"id": 25, "name": "Tortilla Warzywna", "category": "Wege", "price": "24zł", "image": "IMG_6221.jpg", "desc":
    "<ul><li>🥬 Kapusta pekińska</li><li>🍅 Pomidor</li><li>🌽 Kukurydza</li><li>🥣 Hommos</li><li>🧀 Ser Feta</li><li>🥒 Ogórek</li><li>🧄 Sos</li></ul><strong><span class='red-text'><ins>Standarowo tortilla warzywna zawiera sos czosnkowy</ins></span></strong><br>W przypadku innych preferencji, proszę poinformować osobę przyjmującą zamówienie."},
    {"id": 26, "name": "Zupa z soczewicy", "category": "Wege", "price": "15zł", "image": "IMG_6518.jpg", "desc":
    ""},
    {"id": 27, "name": "Filet z mintaja", "category": "Ryba", "price": "28.5zł", "image": "mintaj.jpg", "desc":
    "<ul class='menu-description'><li>🍟 Frytki, ryż lub kasza</li><li>🥗 Surówka</li><li>🧄 Sos</li></ul> <strong><span class='red-text'><ins>Standarowo do ryby serwujemy sos majonezowy</ins></span></strong> <br>W przypadku innych preferencji, proszę poinformować osobę przyjmującą zamówienie."},
    {"id": 28, "name": "Filet z miruny", "category": "Ryba", "price": "38zł", "image": "zestaw miruna.jpg", "desc":
    "<ul class='menu-description'><li>🍟 Frytki, ryż lub kasza</li><li>🥗 Surówka</li><li>🧄 Sos</li></ul> <strong><span class='red-text'><ins>Standarowo do ryby serwujemy sos majonezowy</ins></span></strong> <br>W przypadku innych preferencji, proszę poinformować osobę przyjmującą zamówienie."},
    {"id": 29, "name": "Mały filet z dorsza", "category": "Ryba", "price": "25zł", "image": "IMG_1025.JPG", "desc":
    "<ul class='menu-description'><li>🍟 Frytki, ryż lub kasza</li><li>🥗 Surówka</li><li>🧄 Sos</li></ul> <strong><span class='red-text'><ins>Standarowo do ryby serwujemy sos majonezowy</ins></span></strong> <br>W przypadku innych preferencji, proszę poinformować osobę przyjmującą zamówienie."},
    {"id": 30, "name": "Zestaw Tortilla Gyros", "category": "Dania Mięsne", "price": "33zł", "image": "zestaw tortilla.jpg", "desc":
    "<ul class='menu-description'><li>🍟 Małe frytki</li><li>🥤 Coca Cola Zero 0.5l</li><li>🧄 Sos</li></ul> <strong><span class='red-text'><ins>Standarowo tortilla zawiera sos czosnkowy </ins></span></strong> <br>W przypadku innych preferencji, proszę poinformować osobę przyjmującą zamówienie."},
    {"id": 31, "name": "Sałatka Petra", "category": "Sałatki", "price": "31zł", "image": "salatka petra.jpg", "desc":
    "<ul class='menu-description'><ul><li>🥬 Kapusta pekińska</li><li>🥒 Ogórek</li><li>🍅 Pomidor</li><li>🧀 Ser żółty</li><li>🍖 Gyros</li><li>🧄 Sos</li></ul> <strong><span class='red-text'><ins>Standarowo sałatka Petra zawiera sos czosnkowy </ins></span></strong><br>W przypadku innych preferencji, proszę poinformować osobę przyjmującą zamówienie."},
    {"id": 32, "name": "Sałatka Orientalna", "category": "Sałatki", "price": "24zł", "image": "salatka orientalna.jpg", "desc":
    "<ul class='menu-description'><li>🥬 Kapusta pekińska</li><li>🥒 Ogórek</li><li>🍅 Pomidor</li><li>🧀 Ser Favita</li><li>🌶️ Peperoni</li><li>🫒 Oliwki</li><li>🧄 Sos</li></ul> <strong><span class='red-text'><ins>Standarowo sałatka Orientalna zawiera sos czosnkowy </ins></span></strong> <br>W przypadku innych preferencji, proszę poinformować osobę przyjmującą zamówienie."},
    {"id": 33, "name": "Sałatka Meksykańska", "category": "Sałatki", "price": "24zł", "image": "salatka meksykanska.jpg", "desc":
    "<ul class='menu-description'> <li>🥬 Kapusta pekińska</li><li>🥒 Ogórek</li><li>🍅 Pomidor</li><li>🫘 Fasola</li><li>🌽 Kukurydza</li><li>🧄 Sos</li></ul> <strong><span class='red-text'><ins>Standarowo Sałatka Meksykańska zawiera sos czosnkowy </ins></span></strong> <br>W przypadku innych preferencji, proszę poinformować osobę przyjmującą zamówienie."},
    {"id": 34, "name": "Sałatka Grecka", "category": "Sałatki", "price": "31zł", "image": "IMG_6319.jpg", "desc":
    "<ul class='menu-description'><li>🥬 Sałata lodowa</li><li>🧅 Cebula</li><li>🍅 Pomidor</li><li>🥒 Ogórek</li><li>🫒 Czarne oliwki</li><li>🧀 Ser grecki</li><li>🥗 Sos winegret</li></ul> <strong><span class='red-text'><ins>Standarowo Sałatka Grecka zawiera sos winegret </ins></span></strong> <br>W przypadku innych preferencji, proszę poinformować osobę przyjmującą zamówienie."},
    {"id": 35, "name": "Frytki Duże", "category": "Dodatki", "price": "10zł", "image": "frytki.jpg", "desc":
    "<ul class='menu-description'><li>🍟 Duża porcja frytek</li></ul>"},
    {"id": 36, "name": "Frytki Małe", "category": "Dodatki", "price": "7zł", "image": "frytki.jpg", "desc":
    "<ul class='menu-description'><li>🍟 Mała porcja frytek</li></ul>"},
    {"id": 37, "name": "Ryż", "category": "Dodatki", "price": "10zł", "image": "ryz.jpg", "desc":
    "<ul class='menu-description'><li>🍚 Porcja ryżu</li></ul>"},
    {"id": 38, "name": "Surówka", "category": "Dodatki", "price": "8zł", "image": "surowka.jpg", "desc":
    "<ul class='menu-description'><li>🥗 Surówka z białej kapusty</li></ul>"},
    {"id": 39, "name": "Sos", "category": "Dodatki", "price": "4zł", "image": "sos.jpg", "desc":
    "<ul class='menu-description'><li>🧄 Sos czosnkowy, majonezowy, pomidorowy, chilli</li></ul> "},
    {"id": 40, "name": "Kasza arabska", "category": "Dodatki", "price": "10zł", "image": "kasza.jpg", "desc":
    "<ul class='menu-description'><li>🍚 Kasza arabska</li></ul>"},
    {"id": 41, "name": "Baklawa", "category": "Desery", "price": "?zł", "image": "IMG_6574.jpg", "desc":
    "<ul class='menu-description'><li>🍪 Ciastko arabskie z pistacjami</li></ul>"},
    {"id": 42, "name": "Mammul", "category": "Desery", "price": "?zł", "image": "mammul.jpg", "desc":
    "<ul class='menu-description'><li>🍪 Babeczka nadziewana daktylami</li></ul>"},
    {"id": 43, "name": "Napoje 0.25l", "category": "Napoje", "price": "6.50zł", "image": "napoje butelka.jpg", "desc":
    "<ul class='menu-description'><li>Coca Cola, Fanta, Sprite, FuzeTea 0.25l</li></ul>"},
    {"id": 44, "name": "Napoje 0.33l", "category": "Napoje", "price": "7.50zł", "image": "napoje puszka.jpg", "desc":
    "<ul class='menu-description'><li>Coca Cola, Fanta, Sprite, FuzeTea 0.33l</li></ul>"},
    {"id": 45, "name": "Napoje 0.5l", "category": "Napoje", "price": "8.50zł", "image": "napoje butelka.jpg", "desc":
    "<ul class='menu-description'><li>Coca Cola, Fanta, Sprite, FuzeTea 0.5l</li></ul>"},
    {"id": 46, "name": "Kinley 0.5l", "category": "Napoje", "price": "8.50zł", "image": "kinley.png", "desc":
    "<ul class='menu-description'><li>Tonic Water, Elderflower ZERO CUKRU, Pink Grapefruit & Mint, Lime & Mint</li>"},
    {"id": 47, "name": "Kropla Beskidu 0.33l", "category": "Napoje", "price": "7.50zł", "image": "woda.jpg", "desc":
    "<ul class='menu-description'><li>Woda niegazowana, musująca, gazowana 0.33l</li></ul>"},
    {"id": 48, "name": "Kropla Beskidu 0.5l", "category": "Napoje", "price": "8.50zł", "image": "woda.jpg", "desc":
    "<ul class='menu-description'><li>Woda niegazowana, musująca, gazowana 0.33l</li></ul>"},
    {"id": 49, "name": "FuzeTea 0.5l", "category": "Napoje", "price": "8.50zł", "image": "fuzetea.jpg", "desc":
    "<ul class='menu-description'>FuzeTea 0.5l o smaku:<li>🍑🌺 Brzoskwini i Hibiskusa</li><li>🍋 Cytryny</li><li>🫐🌿 Borówki i Lawendy BEZ CUKRU</li><li>🍉🌿 Arbuza i Mięty BEZ CUKRU</li><li>🍊🍋 Owoców Cytrusowych</li></ul>"},
    {"id": 50, "name": "Cappy 0.25l", "category": "Napoje", "price": "6.50zł", "image": "cappy.jpg", "desc":
    "<ul class='menu-description'>Cappy o smaku:<li>🍊 pomarańczowym</li><li>🍏 jabłkowym</li><li>🌟 multiwitamina</li></ul>"},
    {"id": 51, "name": "Cappy 0.33l", "category": "Napoje", "price": "8zł", "image": "cappy.jpg", "desc":
    "<ul class='menu-description'>Cappy o smaku:<li>🍊 pomarańczowym</li><li>🍏 jabłkowym</li><li>🌟 multiwitamina</li></ul>"},
    {"id": 52, "name": "Burn 0.25l", "category": "Napoje", "price": "6.5zł", "image": "burn.gif", "desc":
    "<ul class='menu-description'>⚡ Napój energetyzujący</ul>"},
    {"id": 53, "name": "Monster 0.5l", "category": "Napoje", "price": "8.5zł", "image": "monster.png", "desc":
    "<ul class='menu-description'>⚡ Napój energetyzujący</ul>"},
    {"id": 54, "name": "Herbata", "category": "Napoje", "price": "?zł", "image": "IMG_6540.jpg", "desc":
    "<ul class='menu-description'>Herbata - filiżanka 200ml</ul>"},
    {"id": 55, "name": "Kawa / Cappuccino", "category": "Napoje", "price": "?zł", "image": "IMG_6555.jpg", "desc":
    "<ul class='menu-description'>Kawa / Cappucino - filiżanka 150ml</ul>"},
    {"id": 56, "name": "Kawa Latte", "category": "Napoje", "price": "?zł", "image": "IMG_6548.jpg", "desc":
    "<ul class='menu-description'>Kawa Latte - szklanka 200ml</ul>"},
    {"id": 57, "name": "Chleb arabski", "category": "Dodatki", "price": "4zł", "image": "IMG_6525.jpg", "desc":
    "<ul class='menu-description'><li>🧄 W zestawie z masłem czosnkowym</li></ul> "},

]

@app.route('/')
def home():
    return render_template('index.html', background_script=True)

@app.route('/menu')
def menu():
    return render_template('menu.html', menu_items=menu_items, background_script=True)

if __name__ == '__main__':
    app.run(debug=True)
