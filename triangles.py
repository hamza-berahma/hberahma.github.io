import random
import matplotlib.pyplot as plt

def cdf(x):
    if x <= 0:
        return 0
    if x <= 2.5:
        return x**2 / 25.0
    if x <= 5:
        return 0.5 - (5 - x)**2 / 25.0
    if x <= 7.5:
        return 0.5 + (x - 5)**2 / 25.0
    if x <= 10:
        return 1.0 - (10 - x)**2 / 25.0
    return 1

num_samples = 10000000
delta = 0.01 
samples = []
total_prob = 0

for _ in range(num_samples):
    x = random.uniform(0, 10)
    prob = cdf(x + delta) - cdf(x)
    samples.append((x, prob))
    total_prob += prob

num_bins = 100
bin_width = 10 / num_bins
bins = [0] * num_bins

for x, prob in samples:
    idx = int(x / bin_width)
    if idx >= num_bins:
        idx = num_bins - 1
    bins[idx] += prob

bins = [b / total_prob for b in bins]

bin_positions = [i * bin_width for i in range(num_bins)]
plt.bar(bin_positions, bins, width=bin_width, align="edge", edgecolor="black")
plt.xlabel("x")
plt.ylabel("pmf")
plt.title("Randomized two triangles distribution")
plt.show()
