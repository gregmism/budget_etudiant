import pytest

from budget import budget_depasse, reste_budget, total_depenses


def test_total_depenses() -> None:
    assert total_depenses([10.0, 2.5]) == pytest.approx(12.5)


def test_liste_vide() -> None:
    assert total_depenses([]) == 0


def test_reste_budget() -> None:
    assert reste_budget(100.0, [20.0, 5.0]) == pytest.approx(75.0)

def test_budget_depasse() -> None:
    assert budget_depasse(100.0, [80.0, 30.0]) is True


def test_budget_non_depasse() -> None:
    assert budget_depasse(100.0, [20.0, 30.0]) is False


def test_budget_exactement_atteint() -> None:
    assert budget_depasse(100.0, [60.0, 40.0]) is False