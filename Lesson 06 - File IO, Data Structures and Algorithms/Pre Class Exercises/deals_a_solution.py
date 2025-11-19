import math
import webbrowser

def calculate_area(diameter: float) -> float:
    return (diameter / 2) ** 2 * math.pi

def price_per_area(price: float, diameters: list[float]) -> float:
    total_area = sum([calculate_area(diameter) for diameter in diameters])
    return price / total_area

small_cost_per_area = price_per_area(19.99, [10, 10])
print(f"Cost per sq in of smalls is {small_cost_per_area:.2f}")

big_cost_per_area = price_per_area(20.99, [16])
print(f"Cost per sq in of large is {big_cost_per_area:.2f}")

if small_cost_per_area < big_cost_per_area:
    webbrowser.open("https://dominoes.com")
else:
    webbrowser.open("https://papajohns.com")