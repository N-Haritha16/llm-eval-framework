import matplotlib.pyplot as plt

def plot_histograms(results, output_dir):
    for metric, stats in results.items():
        plt.hist([stats["mean"]])
        plt.title(metric)
        plt.savefig(f"{output_dir}/{metric}_hist.png")
        plt.clf()
