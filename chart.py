import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set style for professional appearance
sns.set_style("whitegrid")
sns.set_context("talk")

# Generate synthetic customer engagement data
np.random.seed(42)
data = {
    "Website Visits": np.random.randint(50, 200, 100),
    "Email Opens": np.random.randint(30, 150, 100),
    "Purchases": np.random.randint(10, 80, 100),
    "Support Tickets": np.random.randint(5, 50, 100),
    "App Logins": np.random.randint(40, 180, 100),
}

df = pd.DataFrame(data)

# Compute correlation matrix
corr = df.corr()

# Create heatmap
plt.figure(figsize=(8, 8))  # 8x8 inches @ 64 dpi = 512x512 pixels
sns.heatmap(
    corr,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    square=True,
    linewidths=0.5,
    cbar_kws={"shrink": 0.7}
)

# Add title
plt.title("Customer Engagement Correlation Matrix", fontsize=16, pad=20)

# Save chart
plt.savefig("chart.png", dpi=64, bbox_inches="tight")
plt.close()
