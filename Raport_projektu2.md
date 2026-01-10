# Raport Projektowy: Wykorzystanie Modelu Kronos w Prognozowaniu ETF
**Temat:** Finanse i inwestowanie – analiza szeregów czasowych funduszu QQQ.
**Obszar projektu:** Analiza danych biznesowych i rynki kapitałowe.

---

## CZĘŚĆ I: Poradnik Inwestora – Jak AI wspiera decyzje?
*Celem tej części jest przystępne przedstawienie wybranego problemu dla odbiorcy nietechnicznego (zgodnie z wymogami projektu). Sekcja opracowana z wykorzystaniem narzędzi generatywnej SI oraz świadomego Prompt Engineeringu.*

### 1. Czym są Modele Fundacyjne (np. Kronos)?
W przeciwieństwie do tradycyjnych algorytmów, modele fundacyjne dla szeregów czasowych uczą się uniwersalnych wzorców rynkowych na ogromnych zbiorach danych. Działają one na zasadzie przewidywania kolejnych wartości w sekwencji, podobnie jak modele językowe przewidują słowa.

**Przykład zastosowania Prompt Engineeringu (Prompt 1):**
> **Zapytanie:** *"Wyjaśnij pojęcie Time-Series Foundation Models dla odbiorcy nietechnicznego, używając analogii do ChatGPT"*.
> 
> **Odpowiedź AI:** *"ChatGPT przewiduje kolejne słowa w zdaniu, bo rozumie strukturę języka. Kronos działa identycznie, ale zamiast słów 'czyta' wykresy giełdowe. Rozpoznaje uniwersalne rytmy rynku, których ludzkie oko nie jest w stanie wyłapać"*.

### 2. Korzyści dla inwestora
* **Obiektywizm:** AI eliminuje emocje, takie jak strach czy chciwość, zapewniając spójną strategię.
* **Adaptacyjność:** Model potrafi analizować nowe sytuacje rynkowe, bazując na analogiach z milionów historycznych wzorców.
* **Klarowność:** Złożone dane są przekształcane w proste sygnały inwestycyjne: KUP (1) lub CZEKAJ (0).

---

## CZĘŚĆ II: Analiza przypadku – Fundusz QQQ (2024-2025)
*Praktyczne rozwiązanie problemu z użyciem metod uczenia maszynowego (szeregi czasowe) na rzeczywistych danych.*

### 1. Metodologia i Narzędzia
* **Dane:** Rzeczywiste notowania historyczne OHLCV funduszu Invesco QQQ Trust (NASDAQ-100) pobrane z Yahoo Finance.
* **Metoda ML:** Model szeregów czasowych (Time-Series Foundation Model – Kronos).
* **Zadanie:** Analiza trendu i prognoza ceny z horyzontem 21 dni w celu generowania sygnałów transakcyjnych.

### 2. Wyniki i Interpretacja (Backtesting)
Poniższa tabela przedstawia porównanie naszej aktywnej strategii AI ze strategią pasywną (Kup i Trzymaj):

| Metryka | Strategia Aktywna (AI) | Strategia Pasywna (Buy & Hold) |
| :--- | :--- | :--- |
| **Całkowity Zwrot** | **+21.17%** | **+39.38%** |
| **Maks. Obsunięcie (Max Drawdown)** | **-10.24%** | (Wysoka zmienność rynkowa) |
| **Ekspozycja na rynek** | **70.93%** | 100% |

**Interpretacja wyników (Prompt 2):**
> **Zapytanie:** *"Na podstawie wyników backtestingu QQQ (+21% zysku, -10% drawdown), sformułuj wnioski dotyczące bezpieczeństwa kapitału"*.
> 
> **Wnioski AI:** *"Maksymalne obsunięcie na poziomie -10.24% świadczy o wysokiej stabilności. System potrafi wycofać się z rynku w momentach ryzyka, co chroni inwestora przed głębokimi stratami. Oferuje lepszy profil bezpieczeństwa (risk-adjusted return) niż strategia pasywna w okresach niepewności"*.

---

## PODSUMOWANIE I WNIOSKI
Projekt prezentuje praktyczne zastosowanie umiejętności nabytych podczas zajęć: wykorzystanie generatywnej AI, prompt engineeringu oraz analizy szeregów czasowych.

* **Wniosek główny:** AI w inwestowaniu pełni rolę "bezpiecznika" – pozwala na stabilny wzrost przy ograniczonym ryzyku spadku wartości portfela.
* **Dalszy rozwój:** Wzbogacenie modelu o analizę sentymentu (newsy rynkowe) oraz testowanie modelu na innych klasach aktywów (kryptowaluty, surowce).


