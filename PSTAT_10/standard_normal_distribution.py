import math

def standard_normal_distribution(x):
    return (1 / math.sqrt(2 * math.pi)) * math.exp(-0.5 * x**2)

def cumulative_standard_normal(x, num_steps=1000):
    step = x / num_steps
    total = 0
    for i in range(num_steps):
        total += standard_normal_distribution(i * step) * step
    return total

def evaluate_standard_normal(x):
    pdf = standard_normal_distribution(x)
    cdf = cumulative_standard_normal(x)
    return {"PDF": pdf, "CDF": cdf}

x_values = [-3, -2, -1, 0, 1, 2, 3]
for x in x_values:
    result = evaluate_standard_normal(x)
    print(f"x = {x}, PDF = {result['PDF']}, CDF = {result['CDF']}"
