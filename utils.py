"""Moduł zawierający proste funkcje matematyczne."""


def add(a: int, b: int) -> int:
    """Dodaje dwie liczby całkowite."""
    return a + b


def subtract(a: int, b: int) -> int:
    """Odejmuje drugą liczbę od pierwszej."""
    return a - b


def multiply(a: int, b: int) -> int:
    """Mnoży dwie liczby całkowite."""
    return a * b


def divide(a: int, b: int) -> float:
    """Dzieli pierwszą liczbę przez drugą."""
    if b == 0:
        raise ValueError("Nie można dzielić przez zero.")
    return a / b
