def total_depenses(depenses: list[float]) -> float:
    return sum(depenses)


def reste_budget(budget: float, depenses: list[float]) -> float:
    return budget - total_depenses(depenses)


def main() -> None:
    budget = float(input("Ton budget en euros : "))
    depenses = [12.50, 8.00, 24.90]

    print(f"Total dépensé : {total_depenses(depenses):.2f} €")
    print(f"Budget restant : {reste_budget(budget, depenses):.2f} €")


if __name__ == "__main__":
    main()