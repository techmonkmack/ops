import matplotlib.pyplot as plt

steps = [
    "Data Collection",
    "Data Preparation",
    "Model Training",
    "Model Evaluation",
    "Model Registry",
    "Deployment",
    "Monitoring",
    "Retraining"
]

plt.figure(figsize=(8,10))

for i, step in enumerate(steps):
    plt.text(0.5, 0.90-i*0.11, step,
             ha="center", va="center",
             bbox=dict(boxstyle="round", facecolor="lightblue"))

    if i < len(steps)-1:
        plt.annotate("",
                     xy=(0.5, 0.90-(i+1)*0.11+0.025),
                     xytext=(0.5, 0.90-i*0.11-0.025),
                     arrowprops=dict(arrowstyle="->"))

plt.title("MLOps Workflow", pad=20)
plt.axis("off")
plt.show()