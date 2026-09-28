x=1
listofzamet=[]
while x!=0:
    v=0
    print("""Написать заметку - 1,\nпосмотреть заметки - 2,\nудалить заметку - 3,\nвыйти  - 4""")
    v=int(input())
    if v==1:
        a = str(input("Напишите заметку: "))
        listofzamet.append(a)
    if v==2:
        print(listofzamet)
    if v==3:
        for index, element in enumerate(listofzamet):
            print(f"Индекс: {index} -> Элемент: {element}")
        index = int(input("Что удаляем: "))
        del listofzamet[index]
    if v==4:
        x=0
    ###else:
      ###  print("Ты ввёл что-то не то ПОЗОР!")
    