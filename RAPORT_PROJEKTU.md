# Wykorzystanie Modeli Fundacyjnych (Time-Series Foundation Models) w prognozowaniu cen ETF

## Wstęp: Nowa Era Inwestowania Aktywnego

W świecie finansów przewaga informacyjna jest kluczem do sukcesu. Tradycyjne metody analizy technicznej (oparte na wskaźnikach takich jak średnie kroczące czy RSI) często zawodzą w obliczu złożoności i zmienności współczesnych rynków. Tutaj z pomocą przychodzi **Sztuczna Inteligencja (AI)**, a w szczególności jej najnowsza odsłona – **Modele Fundacyjne**.

Niniejszy raport opisuje projekt wykorzystujący model **Kronos** – zaawansowane narzędzie AI zaprojektowane do analizy szeregów czasowych (takich jak ceny akcji czy ETF-ów), którego celem jest wspieranie aktywnego inwestora w podejmowaniu lepszych decyzji.

---

## Czym są Modele Fundacyjne w Finansach?

Aby zrozumieć innowacyjność tego podejścia, warto odnieść się do popularnych modeli językowych, takich jak ChatGPT.

*   **Modele Językowe (LLM):** Uczą się na ogromnych zbiorach tekstu (książki, internet), aby rozumieć gramatykę, kontekst i znaczenie słów. Dzięki temu potrafią pisać wiersze, tłumaczyć teksty czy odpowiadać na pytania.
*   **Time-Series Foundation Models (np. Kronos):** Działają na podobnej zasadzie, ale zamiast słów "czytają" sekwencje liczb – historyczne ceny, wolumeny i inne dane rynkowe.

**Kluczowa różnica:** Zamiast uczyć się sztywnych reguł (np. "kupuj, gdy cena przetnie średnią"), model fundacyjny uczy się **uniwersalnych wzorców** zachowań rynku na podstawie gigantycznej ilości danych historycznych z różnych aktywów. Potrafi dostrzec subtelne zależności niewidoczne dla ludzkiego oka ani prostych algorytmów.

---

## Analiza Projektu: Jak działa Twój Asystent Inwestycyjny?

Nasz system inwestycyjny opiera się na trzech filarach: **Danych**, **Inteligencji (Model Kronos)** oraz **Strategii**.

### 1. Dane wejściowe (Paliwo)
System pobiera dane rynkowe dla wybranego funduszu ETF (np. ceny otwarcia, zamknięcia, najwyższe, najniższe oraz wolumen). Dane te są "oknem na świat" dla modelu – zazwyczaj analizuje on ostatnie ~50 dni (tzw. *lookback context*), aby zrozumieć bieżącą sytuację.

### 2. Inteligentna Prognoza (Silnik)
Sercem systemu jest model **Kronos**.
*   Model otrzymuje sekwencję ostatnich cen.
*   Przetwarza je przez sieć neuronową, szukając analogii do milionów sytuacji rynkowych, które widział podczas treningu.
*   **Wynik:** Generuje prognozę ceny zamknięcia na przyszłość (np. za 21 dni).

### 3. Decyzja Inwestycyjna (Strategia)
Sama prognoza to nie wszystko. System przekształca ją w konkretny sygnał handlowy:
*   Jeśli model przewiduje wzrost ceny powyżej określonego progu -> **Sygnał KUPNA (1)**.
*   W przeciwnym wypadku -> **Sygnał NEUTRALNY/SPRZEDAŻY (0)**.

Strategia regularnie (np. codziennie lub co tydzień) sprawdza te sygnały i automatycznie zarządza portfelem, decydując o wejściu lub wyjściu z rynku.

---

## Wizualizacja Procesu

Poniższy diagram obrazuje przepływ informacji w systemie:

```mermaid
graph TD
    A[Dane Rynkowe (Yahoo Finance)] -->|Historyczne ceny OHLCV| B(Przygotowanie Danych)
    B -->|Kontekst (np. ostatnie 50 dni)| C{Model AI: Kronos}
    C -->|Analiza Wzorców| D[Prognoza Ceny (np. +21 dni)]
    D -->|Czy wzrost > 0%?| E{Generator Sygnałów}
    E -- Tak --> F[Sygnał: KUP (1)]
    E -- Nie --> G[Sygnał: CZEKAJ (0)]
    F --> H[Strategia Inwestycyjna]
    G --> H
    H -->|Backtesting| I[Wynik Finansowy & Raport]
```

---

## Dlaczego warto? (Wnioski)

Zastosowanie modeli fundacyjnych w inwestowaniu oferuje kilka kluczowych przewag:

1.  **Obiektywizm:** AI nie kieruje się emocjami (strachem czy chciwością), które są głównym wrogiem inwestora.
2.  **Głębia Analizy:** Model potrafi analizować nieliniowe zależności, które są zbyt skomplikowane dla tradycyjnych wskaźników.
3.  **Adaptacyjność:** Dzięki wstępnemu treningowi na ogromnych zbiorach danych, model lepiej radzi sobie w nowych, nieznanych warunkach rynkowych (tzw. *zero-shot forecasting*).

---

## Appendix: Zastosowanie Prompt Engineering

Niniejszy raport został przygotowany przy współpracy z asystentem AI, wykorzystując techniki **Prompt Engineering** w celu zapewnienia jasności i dopasowania do odbiorcy. Poniżej przedstawiono przykłady promptów (poleceń), które mogłyby posłużyć do wygenerowania poszczególnych sekcji.

### Przykład 1: Generowanie prostego wyjaśnienia technologii
*Celem było wytłumaczenie skomplikowanego pojęcia "Time-Series Foundation Model" osobie nietechnicznej.*

> **Prompt:** "Jesteś ekspertem finansowym specjalizującym się w AI. Wyjaśnij inwestorowi, który zna podstawy giełdy, czym są 'Modele Fundacyjne dla Szeregów Czasowych' (Time-Series Foundation Models). Użyj analogii do ChatGPT, aby pokazać różnicę między tradycyjnym algorytmem a modelem uczącym się wzorców. Język ma być prosty, polski i zachęcający."

### Przykład 2: Opis procesu decyzyjnego
*Celem było opisanie logiki działania skryptu `predictor.py` i `strategy.py`.*

> **Prompt:** "Na podstawie załączonego kodu (predictor.py), opisz krok po kroku, jak system podejmuje decyzję. Skup się na przepływie: Dane -> Model -> Prognoza -> Sygnał. Nie używaj żargonu programistycznego (jak 'pandas dataframe'), zamiast tego używaj pojęć biznesowych (np. 'historia cen'). Stwórz z tego sekcję do raportu."

### Przykład 3: Wizualizacja
*Celem było stworzenie diagramu Mermaid.*

> **Prompt:** "Stwórz kod diagramu w formacie Mermaid, który wizualizuje proces inwestycyjny: od pobrania danych z Yahoo Finance, przez analizę w modelu Kronos, aż do decyzji kupna/sprzedaży w strategii backtestingowej. Diagram ma być czytelny i pionowy."

Wykorzystanie takich precyzyjnych instrukcji pozwala na transformację surowego kodu i technicznej dokumentacji w przystępny materiał edukacyjny.
