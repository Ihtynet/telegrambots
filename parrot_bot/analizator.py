import wikipedia
from aiogram.types import Message
#####################################
# Исправление Москва и Россия
def jhn_moscow(t):
    r=""
    if t.lower()=="москва" or t.lower()=="moscow" or t.lower()=="москва" or t.lower()=="moscow":
        r = jhn_ispr(t)
    else:
        r=t
    return r

#####################################
# делает слово с большой буквы
def jhn_ispr(tx):
    mas = list(tx.lower())
    mas[0] = mas[0].upper()
    return "".join(mas)

#####################################
# Принимает тек т проверяем максимальное сообщение
# и при необходимости делит его на массив сообщений
def jhn_settodim(tx):
    tx = tx.replace("[", "{")
    tx = tx.replace("]", "}")
    rez = []
    if len(tx) < 4096:
        rez.append(tx)
    else:
        mas = list(tx)
        ost = tx

        kol = int(len(tx) // 4096) + 2

        for k in range(kol):
            if len(mas) > 0:
                pos = ost.rfind(".", 0, 4095)
                if pos != -1:
                    ms = mas[0:pos + 1]
                else:
                    ms = mas

                rez.append("".join(ms))

                if pos != -1:
                    for i in range(pos + 1):

                        del mas[0]
                else:
                    for i in range(len(mas)):
                        del mas[0]
                ost = "".join(mas)

    return rez

#####################################
# Анализирует и отвечате на Привет и на как дела
def jhn_analizator(tx):
    lx = tx.lower()
    r=""
    etoumno = False

    if lx.find("привет")>=0 or lx.find("салют")>=0 or lx.find("здорово")>=0 or lx.find("здарова")>=0 or lx.find("здарово")>=0 or lx.find("здаров")>=0 or lx.find("здравствуйте")>=0:
        r = "Салют! "
        etoumno = True

    if lx.find("как дела")>=0 or lx.find("как делы")>=0 or lx.find("как че")>=0:
        r = r + "У меня все отлично! А как тебя? "
        etoumno = True

    if lx.find("как")>=0 and (lx.find("зовут")>=0 or lx.find("звать")>=0 or lx.find("имя")>=0):
        r = r +"Меня зовут Кеша! "
        etoumno = True
    if ((lx.find("что")>=0 or lx.find("Cто")>=0 or lx.find("Што")>=0) and (lx.find("умеешь")>=0 or lx.find("умееш")>=0)) or (lx.find("что")>=0 and lx.find("можешь")>=0):
        r = r +"Я могу общаться с тобой и могу, приветствовать и  ещё отвечать на вопросы. Для этого напиши 'Что такое ...'  или 'Кто такой...'  или 'Кто такая...' и дальше пиши, что тебя интересует.  Например 'Что такое вода' или 'Кто такой Петр I'. И я тебе пришлю ответ"
        etoumno = True
    if lx.find("что") >= 0 and lx.find("такое") >= 0 and len(list(lx))>9:
        r = r + jhn_chto_tak(lx)
        etoumno = True
    if lx.find("кто") >= 0 and lx.find("такой") >= 0 and len(list(lx))>9:
        r = r + jhn_chto_tak(lx)
        etoumno = True
    if lx.find("кто") >= 0 and lx.find("такая") >= 0 and len(list(lx))>9:
        r = r + jhn_chto_tak(lx)
        etoumno = True
    if lx != "/start" and etoumno == False:
        r = r + jhn_bolsheneznau()

    mas = jhn_settodim(r)
    return mas

#####################################
# Отвечает что больше ничего не знает
def jhn_bolsheneznau():
    return "Я не понял"
def jhn_peredraz(mes: Message):
    print(mes)
    new_text = ""
    l = "?!.,@#$%^&*()\"\'№;:<>+={}]["
    b = "АБВГДЕЁЖЗИЙКЛМНОПРСТУХФЦЧШЩЬЫЪЭЮЯABCDEFGHIJKLMNOPQRSTUVWXZY"
    var = ""
    global text
    for leter in mes.text:
        if leter not in l:
            new_text += leter
        elif leter in l:
            var = leter
    text = "Сам, " + new_text.lower() + ", профессор" + var
def jhn_chto_tak(tx):
    rez=""
    tx = tx.replace("что", "")
    tx = tx.replace("такое", "")
    tx = tx.replace("кто", "")
    tx = tx.replace("такой", "")
    tx = tx.replace("кто", "")
    tx = tx.replace("такая", "")
    tx = tx.replace(" ", "")
    tx = tx.replace("   ","")
    wikipedia.set_lang("ru")
    try:
        rez = wikipedia.summary(tx)
    except wikipedia.exceptions.PageError:
        rez = "Я не понял"
    except wikipedia.exceptions.DisambiguationError:
        rez = "Я не понял"
    return rez
