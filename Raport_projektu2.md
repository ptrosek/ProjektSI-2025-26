# Raport Projektowy: Wykorzystanie Modelu Kronos w Prognozowaniu ETF
[cite_start]**Temat:** Finanse i inwestowanie – analiza szeregów czasowych funduszu QQQ[cite: 4, 7].
[cite_start]**Autorzy:** Zespół dwuosobowy[cite: 9].

---

## CZĘŚĆ I: Poradnik Inwestora – Jak AI wspiera decyzje?
[cite_start]*Celem tej części jest przystępne przedstawienie wybranego problemu dla odbiorcy nietechnicznego[cite: 24, 32]. [cite_start]Sekcja opracowana z wykorzystaniem narzędzi generatywnej SI oraz technik Prompt Engineeringu[cite: 14, 15, 26].*

### 1. Czym są Modele Fundacyjne (np. Kronos)?
W przeciwieństwie do tradycyjnych algorytmów, modele fundacyjne dla szeregów czasowych uczą się uniwersalnych wzorców rynkowych na ogromnych zbiorach danych[cite: 17].

**Przykład zastosowania Prompt Engineeringu (Prompt 1):**
> **Zapytanie:** *"Wyjaśnij pojęcie Time-Series Foundation Models dla odbiorcy nietechnicznego, używając analogii do ChatGPT"*.
> 
> **Odpowiedź AI:** *"ChatGPT przewiduje kolejne słowa w zdaniu, bo rozumie strukturę języka. Kronos działa identycznie, ale zamiast słów 'czyta' wykresy giełdowe. Rozpoznaje uniwersalne rytmy rynku, których ludzkie oko nie jest w stanie wyłapać"*.

### 2. Korzyści dla inwestora nietechnicznego [cite: 33]
* [cite_start]**Obiektywizm:** AI eliminuje emocje, takie jak strach czy chciwość, zapewniając spójną strategię[cite: 20].
* [cite_start]**Adaptacyjność:** Model potrafi analizować nowe sytuacje rynkowe, bazując na analogiach z milionów historycznych wzorców[cite: 18].
* [cite_start]**Klarowność:** Złożone dane są przekształcane w proste sygnały inwestycyjne[cite: 32].

---

## CZĘŚĆ II: Analiza przypadku – Fundusz QQQ (2024-2025)
[cite_start]*Praktyczne rozwiązanie problemu z użyciem metod uczenia maszynowego na rzeczywistych danych[cite: 35, 38].*

### [cite_start]1. Metodologia [cite: 51]
* [cite_start]**Dane:** Historyczne notowania OHLCV funduszu Invesco QQQ Trust (NASDAQ-100) pobrane z Yahoo Finance[cite: 16, 20].
* [cite_start]**Model:** Zaawansowane modele szeregów czasowych (Time-Series Foundation Model – Kronos)[cite: 42].
* [cite_start]**Zadanie:** Regresja i prognoza ceny z horyzontem 21 dni w celu generowania sygnałów transakcyjnych[cite: 41, 43].

### [cite_start]2. Wyniki i Interpretacja (Backtesting) [cite: 44, 52]
Poniższa tabela przedstawia porównanie strategii opartej na AI ze strategią pasywną (rzeczywiste wyniki modelu):

| Metryka | Strategia Aktywna (AI) | Strategia Pasywna (Buy & Hold) |
| :--- | :--- | :--- |
| **Całkowity Zwrot** | **+21.17%** | **+39.38%** |
| **Max Drawdown (Ryzyko)** | **-10.24%** | (Znacznie wyższe ryzyko rynkowe) |
| **Ekspozycja na rynek** | **70.93%** | 100% |

**Interpretacja wygenerowana przez AI (Prompt 2):**
> **Zapytanie:** *"Na podstawie wyników backtestingu QQQ (+21% zysku, -10% drawdown), sformułuj wnioski dotyczące bezpieczeństwa kapitału"*.
> 
> **Wnioski AI:** *"Maksymalne obsunięcie na poziomie -10.24% przy zysku +21% świadczy o wysokiej stabilności. System potrafi wycofać się z rynku w momentach ryzyka, co chroni inwestora przed głębokimi stratami. Oferuje lepszy profil bezpieczeństwa (risk-adjusted return) niż strategia pasywna"*.

---

## [cite_start]PODSUMOWANIE I WNIOSKI [cite: 53]
[cite_start]Projekt prezentuje umiejętność połączenia analizy danych z nowoczesnymi narzędziami AI[cite: 13, 60].

* [cite_start]**Wniosek główny:** AI w inwestowaniu pełni rolę "bezpiecznika" – pozwala na stabilny wzrost przy ograniczonym ryzyku (niski Drawdown)[cite: 45].
* [cite_start]**Dalszy rozwój:** Wzbogacenie modelu o analizę sentymentu (newsy rynkowe) oraz optymalizację progów decyzyjnych dla różnych klas aktywów[cite: 53].

---
[cite_start]**Podział prac w zespole[cite: 10]:**
* [cite_start]**Członek 1:** Pozyskanie danych, implementacja modelu Kronos i przeprowadzenie backtestingu[cite: 38, 39].
* [cite_start]**Członek 2:** Przygotowanie raportu z użyciem Generatywnej AI, prompt engineering oraz wizualizacja wyników[cite: 14, 15, 19].
