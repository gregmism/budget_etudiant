import pytest

from budget import reste_budget, total_depenses


def test_total_depenses() -> None:
    assert total_depenses([10.0, 2.5]) == pytest.approx(12.5)


def test_liste_vide() -> None:
    assert total_depenses([]) == 0


def test_reste_budget() -> None:
    assert reste_budget(100.0, [20.0, 5.0]) == pytest.approx(75.0)