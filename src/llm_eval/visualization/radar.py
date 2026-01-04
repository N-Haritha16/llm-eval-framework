import matplotlib.pyplot as plt
import math

def plot_radar(results, path):
    labels = list(results.keys())
    values = [v["mean"] for v in results.values()]
    angles = [n / float(len(labels)) * 2 * math.pi for n in range(len(labels))]
    values += values[:1]
    angles += angles[:1]

    plt.polar(angles, values)
    plt.fill(angles, values, alpha=0.25)
    plt.savefig(path)
    plt.clf()
