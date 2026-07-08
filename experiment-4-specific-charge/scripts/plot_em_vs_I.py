import pathlib

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib_fontja  # noqa: F401  (日本語フォント対応)
import numpy as np

I = np.array([1.0, 1.2, 1.4, 1.6, 1.8, 2.0])
em = np.array([1.45022, 1.59628, 1.68944, 1.70773, 1.75437, 1.80355])  # ×10^11 C/kg
em_ref = 1.7588  # ×10^11 C/kg
em_avg = 1.66693  # ×10^11 C/kg

fig, ax = plt.subplots(figsize=(9, 6))

ax.scatter(I, em, s=90, color="tab:blue", zorder=3, label="測定値 e/m")
ax.axhline(em_ref, color="tab:red", linestyle="--", linewidth=1.5,
           label=f"文献値 e/m = {em_ref:.4f}$\\times10^{{11}}$ C/kg")
ax.axhline(em_avg, color="tab:green", linestyle=":", linewidth=1.5,
           label=f"測定平均 e/m = {em_avg:.4f}$\\times10^{{11}}$ C/kg")

ax.grid(True, linestyle="-", alpha=0.4)
ax.set_xlabel("コイル電流 I [A]")
ax.set_ylabel("比電荷 e/m [$\\times10^{11}$ C/kg]")
ax.legend(loc="lower right")

fig.tight_layout()

output_path = pathlib.Path(__file__).resolve().parent.parent / "images" / "em_vs_I.png"
fig.savefig(output_path, dpi=150)
print(f"saved to {output_path}")
