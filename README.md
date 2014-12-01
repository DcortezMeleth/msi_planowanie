msi_planowanie
==============

Zadanie z planowania stworzone na przedmiot _Metody Sztucznej Inteligencji_.

**Opis domeny:** Mamy różne miasta, a w nich wybrane lokacje, w których mogą się znajdować obiekty naszego zainteresowania - paczki, które mamy przewieźć z jednej lokacji na inną (w tym samym, bądź innym mieście), zgodnie z definicją problemu logistycznego. Po wybranym mieście paczki przewożą ciężarówki, ale tylko te ciężarówki, które są przypisane do konkretnego miasta - każda przewozi na raz jedną paczkę. Na początku transportu ciężarówką, paczkę się do niej pakuje, na końcu przewozu _ rozpakowuje. Wybrana lokacja w mieście zawiera lotnisko. Między miastami kursują samoloty i to one tylko mogą przewieźć paczkę między różnymi miastami (a dokładniej od lotniska miasta 1 do lotniska miasta 2). Przed rozpoczęciem lotu następuje załadowanie na pokład paczki, po zakończeniu lotu _ rozładunek paczki.

**Uruchomienie:** Program uruchamiamy poleceniem _python logistic.py_.

Problem który chcemy rozwiązać definiujemy w ostatniej lini pliku _logistic.py_.
Przykładowy problem transportu dwóch paczek.

_pyhop.pyhop(state1, [('transport', 'package1', 'loc1', 'loc6'), ('transport', 'package2', 'loc4', 'loc2')], verbose=1)_
