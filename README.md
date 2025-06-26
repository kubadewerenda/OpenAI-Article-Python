# OpenAI
Opis działania:<br>
Program spełnia warunki podane w zadaniu rekrutacyjnym. Wybrałem język python.
Pierwsza część programu polega na pobraniu z pliku .txt zawartości artykułu a potem przekazanie tego do sztucznej inteligencji wraz z kompletnym promptem,
który musi spełniać wymogi w zadaniu. Używamy tutaj oczywiście biblioteki OpenAi. Kolejna część zadania(czyli dodatkowa) polega na stworzeniu gotowego szablonu(w moim przypadku stworzyłem funkcję zwracająca szablon strony html) strony pliku .html i połączenio tego w całość z artykul.html. Z racji na dowolnośc wykonania tego etapu zdecydowałem się na wygenerowanie pliku index.css też przy uzyciu openai,
który generuje kod css pod dokładnie te tagi które występują w artykul.html, do tego stworzyłem funkcje, która wykrywa jakie tagi zostają użyte przez sztuczną inteligencję. Ostatecznie łączy wszystko w jedność-dzięki funkcji join_html(która wstawia w miejsce body kod artykulu) i tak powstaje plik podglad.html.
Za działanie programu odpowiada funkcja głowna, czyli OpenAiArticle().

Instukcja:<br>
-pobranie wszystkich plików z repozytorium<br>
-wklejenie klucza api OpenAi do pliku api_key.txt(ze względów bezpieczeństwa nie podawałem otrzymanego)<br>
-skompilowanie pliku Zad_Oxido.py
