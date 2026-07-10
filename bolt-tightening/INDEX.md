# INDEX

このリポジトリ内ファイルへのリンク一覧．このファイルのraw URLだけClaudeに送れば，
ここに書かれているリンクを辿って各ファイルを読み込める．

（注）リポジトリ名やファイルを追加・変更したら，このファイルも更新すること．
（注）リンクは必ず `raw.githubusercontent.com/.../main/...` の形式にすること．
　　　`github.com/.../blob/main/...` の形式だと読み込めない．
（注）ファイル名は実験ごとに`exp1_`・`exp2_`・`exp3_`の接頭辞で統一している
　　　（exp1=トルク法、exp2=ナット回転角法、exp3=トルク勾配法）．

## ルール

- STYLE_GUIDE.md
  https://raw.githubusercontent.com/yanasota-creator/Reports/main/STYLE_GUIDE.md

## レポート

- report.md（ねじ締結 実験レポート）
  https://raw.githubusercontent.com/yanasota-creator/Reports/main/bolt-tightening/report.md

- calculation_notes.md（計算根拠まとめ）
  https://raw.githubusercontent.com/yanasota-creator/Reports/main/bolt-tightening/calculation_notes.md

## データ（data/）

- dimensions.csv（ボルト・被締結物の諸元と計算値、全実験共通）
  https://raw.githubusercontent.com/yanasota-creator/Reports/main/bolt-tightening/data/dimensions.csv

- exp1_torque_method.csv（実験1 トルク法の測定・計算データ）
  https://raw.githubusercontent.com/yanasota-creator/Reports/main/bolt-tightening/data/exp1_torque_method.csv

- exp2_nut_rotation_method.csv（実験2 ナット回転角法の測定・計算データ）
  https://raw.githubusercontent.com/yanasota-creator/Reports/main/bolt-tightening/data/exp2_nut_rotation_method.csv

- exp3_torque_gradient_method.csv（実験3 トルク勾配法の測定・計算データ）
  https://raw.githubusercontent.com/yanasota-creator/Reports/main/bolt-tightening/data/exp3_torque_gradient_method.csv

## 画像（images/）

### 実験1（トルク法）

- exp1_F_vs_Tf.png（締付トルクとボルト軸力の関係）
  https://raw.githubusercontent.com/yanasota-creator/Reports/main/bolt-tightening/images/exp1_F_vs_Tf.png

- exp1_Tw_vs_Tf.png（締付トルクと座面摩擦トルクの関係）
  https://raw.githubusercontent.com/yanasota-creator/Reports/main/bolt-tightening/images/exp1_Tw_vs_Tf.png

- exp1_Ts_vs_Tf.png（締付トルクとねじ部トルクの関係）
  https://raw.githubusercontent.com/yanasota-creator/Reports/main/bolt-tightening/images/exp1_Ts_vs_Tf.png

- exp1_muw_vs_Tf.png（締付トルクと座面摩擦係数の関係）
  https://raw.githubusercontent.com/yanasota-creator/Reports/main/bolt-tightening/images/exp1_muw_vs_Tf.png

- exp1_mus_vs_Tf.png（締付トルクとねじ部摩擦係数の関係）
  https://raw.githubusercontent.com/yanasota-creator/Reports/main/bolt-tightening/images/exp1_mus_vs_Tf.png

### 実験2（ナット回転角法）

- exp2_F_vs_theta.png（ナット回転角とボルト軸力の関係）
  https://raw.githubusercontent.com/yanasota-creator/Reports/main/bolt-tightening/images/exp2_F_vs_theta.png

- exp2_Tr_vs_theta.png（ナット回転角と残留トルクの関係）
  https://raw.githubusercontent.com/yanasota-creator/Reports/main/bolt-tightening/images/exp2_Tr_vs_theta.png

- exp2_Z_vs_theta.png（ナット回転角とへたり係数の関係）
  https://raw.githubusercontent.com/yanasota-creator/Reports/main/bolt-tightening/images/exp2_Z_vs_theta.png

### 実験3（トルク勾配法）

- exp3_F_vs_theta.png（ナット回転角とボルト軸力の関係）
  https://raw.githubusercontent.com/yanasota-creator/Reports/main/bolt-tightening/images/exp3_F_vs_theta.png

- exp3_Tf_vs_theta.png（ナット回転角と締付トルクの関係）
  https://raw.githubusercontent.com/yanasota-creator/Reports/main/bolt-tightening/images/exp3_Tf_vs_theta.png

- exp3_Tr_vs_theta.png（ナット回転角と残留トルクの関係）
  https://raw.githubusercontent.com/yanasota-creator/Reports/main/bolt-tightening/images/exp3_Tr_vs_theta.png

- exp3_gradient_vs_theta.png（ナット回転角とトルク勾配の関係）
  https://raw.githubusercontent.com/yanasota-creator/Reports/main/bolt-tightening/images/exp3_gradient_vs_theta.png

## 参考資料（references/）

- screw_tightening_handout.pdf（実験指導書）
  https://raw.githubusercontent.com/yanasota-creator/Reports/main/bolt-tightening/references/screw_tightening_handout.pdf

- screw_tightening_notes.pdf（講義メモ）
  https://raw.githubusercontent.com/yanasota-creator/Reports/main/bolt-tightening/references/screw_tightening_notes.pdf

- screw_tightening_sample_correction.pdf（2本目・3本目の試料メッキ種類の訂正資料）
  https://raw.githubusercontent.com/yanasota-creator/Reports/main/bolt-tightening/references/screw_tightening_sample_correction.pdf

## スクリプト（scripts/）

- exp1_plot_torque_method.py（実験1 グラフ作成スクリプト）
  https://raw.githubusercontent.com/yanasota-creator/Reports/main/bolt-tightening/scripts/exp1_plot_torque_method.py

- exp2_process_nut_rotation_method.py（実験2 データ加工・グラフ作成スクリプト）
  https://raw.githubusercontent.com/yanasota-creator/Reports/main/bolt-tightening/scripts/exp2_process_nut_rotation_method.py

- exp3_process_torque_gradient_method.py（実験3 データ加工・グラフ作成スクリプト）
  https://raw.githubusercontent.com/yanasota-creator/Reports/main/bolt-tightening/scripts/exp3_process_torque_gradient_method.py
