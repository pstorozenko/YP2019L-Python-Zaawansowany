1. Niech `x` będzie wektorem.
    * Wypisz wszystkie wartości z przedziału $[-2, -1] \cup [1, 2]$.
    * Wypisz liczbę oraz proporcję ujemnych elementów `x`.
    * Policz średnią z wartości bezwzględnych z `x`.
    * Znajdź element najbardziej oddalony od 0.
    * Znajdź element najbardziej oddalony od 2.
    * Wypisz część ułamkową każdej z liczb.
    * Stwórz wektor `y`, taki, że `y[i]` równa się `nieujemny` dla `x[i] >= 0` oraz `ujemny` w przeciwnym przypadku.
    * Stwórz wektor `z`, taki, że `z[i]` równa się `maly` dla `x[i] < 1`,  `duzy` dla `x[i] > 1` i `sredni` w przeciwnym przypadku.
    Wektor wygeneruj następująco:
    ```python
    import numpy as np
    np.random.seed(123)
    x = np.round(np.random.normal(size = 20), 2)
    ```
2. Napisz funkcję `clamp(x)`, która elementy mniejsze od 0, ustawi na 0, a elementy większe od 1 na 1.
3. Napisz funkcję `approx_pi(n)`, która przybliża liczbę $\pi$ metodą Monte Carlo.
