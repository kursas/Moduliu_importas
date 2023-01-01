# -*- coding: utf-8 -*-
# Sukurti naują projektą (PyCharm programoje) Jame sukurti failą modulis.py, kuriame:
# • Kintamajam kintamasis priskirti reikšmę „Čia yra kintamasis“
# • Sukurti funkciją funkcija(), kuri atspausdina „Čia yra funkcija“.
# • Sukurti klasę Objektas, kurį iniciavus atspausdina „Čia yra klasė“.
# Sukurti failą main.py, kuriame:
# • Importuoti modulį modulis
# • Atspausdinti importuotą kintamąjį kintamasis
# • Paleisti importuotą funkciją funkcija()
# • Inicijuoti importuotos klasės Objektas() objektą

variable="This is variable"
def printing_function():
    print("Here is a function")
class Object:
    def __init__(self,name):
        self.name=name
    def __repr__(self):
        return f"Where is a {self.name}"
      
  #output
  Process finished with exit code 0
