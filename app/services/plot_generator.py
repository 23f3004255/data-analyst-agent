import matplotlib.pyplot as plt
import io, base64

def generate_scatter_plot(x, y):
    fig, ax = plt.subplots()
    ax.scatter(x, y)
    # Regression line
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    encoded = base64.b64encode(buf.getvalue()).decode("utf-8")
    return f"data:image/png;base64,{encoded}"
