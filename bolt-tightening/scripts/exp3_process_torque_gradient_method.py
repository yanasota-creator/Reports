import csv
import pathlib

# 実験3（トルク勾配法によるねじ締結）
# 生データはナット回転角θ[°]を10°刻みで与え、そのときの締付トルクTf・
# CH1（圧縮ひずみε1）・CH2（ねじりひずみε2）を測定したもの。
# F・Tr（被締結物とボルト軸の残留トルク）は生データの時点でEc・Ac・Zp・νを用いて
# 計算済み（bolt-tightening/data/dimensions.csv の確定値と同一。Trは実験1のTwと同じ
# 式ε2・Ec・Zp/(1+ν)で算出しているが、指導書の実験2・3では「残留トルク」と呼ぶため
# 表記をTrに統一する）。実験手順④の終了判定に用いる勾配ΔTf/Δθをここで追加算出する。

# (角度θ, CH1, CH2, F[N]（符号付き）, Tf[Nm], Tw[Nm]（符号付き）, 備考)
bolts_raw = {
    "1本目": dict(material="亜鉛電気メッキ", grade="4.8", rows=[
        (0, -229, -7, -3201.152224, 10, -0.189334576, "スナグトルク"),
        (10, -347, -149, -4850.654243, 14, -4.030121697, ""),
        (20, -515, -202, -7199.097796, 18, -5.463654918, ""),
        (30, -667, -218, -9323.880058, 24, -5.896419664, ""),
        (40, -752, -218, -10512.08066, 26, -5.896419664, ""),
        (50, -771, -182, -10777.67845, 27, -4.922698986, ""),
        (60, -741, -204, -10358.31353, 26, -5.517750511, ""),
        (70, -702, -171, -9813.139131, 27, -4.625173223, ""),
        (80, -661, -188, -9240.007074, 28, -5.084985765, ""),
        (90, -631, -213, -8820.642154, 28, -5.761180681, ""),
        (100, -600, -163, -8387.298403, 27, -4.40879085, ""),
        (110, -583, -164, -8149.658281, 28, -4.435838646, ""),
        (120, -571, -163, -7981.912313, 26, -4.40879085, ""),
        (130, -537, -182, -7506.632071, 26, -4.922698986, ""),
    ]),
    "2本目": dict(material="亜鉛電気メッキ", grade="8.8", rows=[
        (0, -222, -27, -3103.300409, 10, -0.730290509, "スナグトルク"),
        (10, -312, -128, -4361.395169, 11, -3.462117968, ""),
        (20, -452, -169, -6318.431463, 19, -4.57107763, ""),
        (30, -641, -191, -8960.43046, 24, -5.166129155, ""),
        (40, -853, -27, -11923.94256, 21, -0.730290509, ""),
        (50, -974, -273, -13615.38107, 38, -7.384048479, ""),
        (60, -1013, -251, -14160.55547, 40, -6.788996953, ""),
        (70, -1007, -247, -14076.68249, 41, -6.680805766, ""),
        (80, -992, -229, -13867.00003, 39, -6.193945427, ""),
        (90, -1001, -226, -13992.8095, 35, -6.112802037, ""),
    ]),
    "3本目": dict(material="溶融亜鉛メッキ", grade="8.8", rows=[
        (0, -176, -77, -2460.274198, 10, -2.08268034, "スナグトルク"),
        (10, -421, -168, -5885.087713, 16, -4.544029833, ""),
        (20, -588, -217, -8219.552435, 21, -5.869371868, ""),
        (30, -801, -270, -11197.04337, 26, -7.302905089, ""),
        (40, -978, -307, -13671.2964, 30, -8.303673564, ""),
        (50, -1132, -317, -15824.03632, 31, -8.57415153, ""),
        (60, -1223, -344, -17096.10991, 36, -9.304442039, ""),
        (70, -1228, -348, -17166.00406, 39, -9.412633225, ""),
        (80, -1226, -323, -17138.0464, 39, -8.73643831, ""),
        (90, -1265, -334, -17683.2208, 39, -9.033964073, ""),
    ]),
    "4本目": dict(material="四三酸化鉄メッキ", grade="10.9", rows=[
        (0, -400, -97, -5591.532269, 10, -2.623636273, "スナグトルク"),
        (10, -572, -154, -7995.891144, 15, -4.16536068, ""),
        (20, -756, -207, -10567.99599, 19, -5.598893901, ""),
        (30, -963, -228, -13461.61394, 23, -6.16689763, ""),
        (40, -1157, -272, -16173.50709, 27, -7.357000682, ""),
        (50, -1338, -267, -18703.67544, 31, -7.221761699, ""),
        (60, -1503, -290, -21010.1825, 32, -7.843861021, ""),
        (70, -1600, -367, -22366.12907, 39, -9.926541361, ""),
        (80, -1690, -210, -23624.22383, 38, -5.680037291, ""),
        (90, -1721, -380, -24057.56759, 42, -10.27816272, ""),
        (100, -1686, -345, -23568.30851, 40, -9.331489835, ""),
        (110, -1728, -330, -24155.4194, 42, -8.925772886, ""),
        (120, -1737, -376, -24281.22888, 44, -10.16997153, ""),
    ]),
    "5本目": dict(material="四三酸化鉄メッキ", grade="12.9", rows=[
        (0, -322, -56, -4501.183476, 10, -1.514676611, "スナグトルク"),
        (10, -497, -171, -6947.478844, 12, -4.625173223, ""),
        (20, -713, -222, -9966.906269, 16, -6.004610851, ""),
        (30, -944, -257, -13196.01615, 22, -6.951283733, ""),
        (40, -1177, -101, -16453.0837, 24, -2.731827459, ""),
        (50, -1366, -313, -19095.0827, 27, -8.465960343, ""),
        (60, -1517, -312, -21205.88613, 27, -8.438912547, ""),
        (70, -1635, -345, -22855.38815, 30, -9.331489835, ""),
        (80, -1730, -369, -24183.37706, 32, -9.980636954, ""),
        (90, -1800, -345, -25161.89521, 35, -9.331489835, ""),
        (100, -1843, -323, -25762.98493, 34, -8.73643831, ""),
        (110, -1854, -359, -25916.75206, 34, -9.710158988, ""),
        (120, -1866, -361, -26084.49803, 38, -9.764254581, ""),
        (130, -1854, -359, -25916.75206, 39, -9.710158988, ""),
        (140, -1848, -347, -25832.87908, 35, -9.385585429, ""),
        (150, -1833, -254, -25623.19662, 33, -6.870140343, ""),
    ]),
}


def process(rows):
    out = []
    prev_theta = prev_Tf = None
    for theta, ch1, ch2, F, Tf, Tr, note in rows:
        Fa, Tra = abs(F), abs(Tr)
        grad = None if prev_theta is None else (Tf - prev_Tf) / (theta - prev_theta)
        out.append(dict(theta=theta, CH1=ch1, CH2=ch2, F=Fa, Tf=Tf, grad=grad,
                         Tr=Tra, note=note))
        prev_theta, prev_Tf = theta, Tf
    return out


root = pathlib.Path(__file__).resolve().parent.parent
data_path = root / "data" / "exp3_torque_gradient_method.csv"

with open(data_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    for label, d in bolts_raw.items():
        rows = process(d["rows"])
        writer.writerow([label, d["material"], f"強度区分{d['grade']}",
                          f"{d['grade']}{d['material']}", "", "", "", "", "", "", ""])
        writer.writerow(["回転角θ[°]", "CH1", "CH2", "F[N]", "Tf[Nm]",
                          "勾配ΔTf/Δθ[Nm/°]", "Tr[Nm]", ""])
        for r in rows:
            gradstr = "" if r["grad"] is None else f"{r['grad']:.4f}"
            writer.writerow([r["theta"], r["CH1"], r["CH2"], f"{r['F']:.4f}",
                              r["Tf"], gradstr, f"{r['Tr']:.6f}", r["note"]])
        writer.writerow([])

print(f"wrote {data_path}")

# ---- 画像用に加工済みデータをまとめて保持 ----
bolts = {}
colors = {"1本目": "tab:blue", "2本目": "tab:orange", "3本目": "tab:green",
          "4本目": "tab:red", "5本目": "tab:purple"}
markers = {"1本目": "o", "2本目": "s", "3本目": "^", "4本目": "D", "5本目": "v"}
linestyles = {"1本目": "-", "2本目": "--", "3本目": ":", "4本目": "-.",
              "5本目": (0, (3, 1, 1, 1, 1, 1))}
for label, d in bolts_raw.items():
    rows = process(d["rows"])
    bolts[f"{label} {d['grade']}（{d['material']}）"] = dict(
        color=colors[label], marker=markers[label], linestyle=linestyles[label],
        theta=[r["theta"] for r in rows],
        F=[r["F"] for r in rows],
        Tf=[r["Tf"] for r in rows],
        Tr=[r["Tr"] for r in rows],
        grad=[r["grad"] for r in rows],
    )

if __name__ == "__main__":
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import matplotlib_fontja  # noqa: F401
    import numpy as np

    images_dir = root / "images"

    def plot_metric(key, ylabel, title, filename):
        fig, ax = plt.subplots(figsize=(9, 6))
        for label, d in bolts.items():
            ax.plot(d["theta"], d[key], color=d["color"], marker=d["marker"],
                     linestyle=d["linestyle"], markersize=7, linewidth=1.4,
                     zorder=3, label=label)
        ax.grid(True, linestyle="-", alpha=0.4)
        ax.set_xlabel("ナット回転角 $\\theta$ [°]")
        ax.set_ylabel(ylabel)
        ax.set_title(title)
        ax.legend(loc="best", fontsize=9)
        fig.tight_layout()
        fig.savefig(images_dir / filename, dpi=150)
        plt.close(fig)
        print(f"saved {filename}")

    plot_metric("F", "ボルト軸力 $F$ [N]", "ナット回転角とボルト軸力の関係", "exp3_F_vs_theta.png")
    plot_metric("Tf", "締付トルク $T_f$ [Nm]", "ナット回転角と締付トルクの関係", "exp3_Tf_vs_theta.png")
    plot_metric("Tr", "被締結物とボルト軸の残留トルク $T_r$ [Nm]",
                "ナット回転角と残留トルクの関係", "exp3_Tr_vs_theta.png")

    fig, ax = plt.subplots(figsize=(9, 6))
    for label, d in bolts.items():
        theta = np.array(d["theta"][1:])
        grad = np.array(d["grad"][1:], dtype=float)
        ax.plot(theta, grad, color=d["color"], marker=d["marker"],
                 linestyle=d["linestyle"], markersize=7, linewidth=1.4,
                 zorder=3, label=label)
    ax.axhline(0, color="gray", linewidth=0.8)
    ax.grid(True, linestyle="-", alpha=0.4)
    ax.set_xlabel("ナット回転角 $\\theta$ [°]")
    ax.set_ylabel("トルク勾配 $\\Delta T_f/\\Delta\\theta$ [Nm/°]")
    ax.set_title("ナット回転角とトルク勾配の関係")
    ax.legend(loc="best", fontsize=9)
    fig.tight_layout()
    fig.savefig(images_dir / "exp3_gradient_vs_theta.png", dpi=150)
    plt.close(fig)

    print("saved exp3_Tf_vs_theta.png, exp3_gradient_vs_theta.png")
