import matplotlib.pyplot as plt

def plot_trend(df):
    plt.figure(figsize=(12,6))
    plt.plot(df['date'], df['temperature'], alpha=0.5)
    plt.title("Global Temperature Trend")
    plt.show()