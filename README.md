# Highrisk_textclassifier_001

# Medical Risk Classifier Web App

このアプリは、Hugging Face 上に公開された日本語テキスト分類モデル [`Tetsuo3003/highrisk_textclassifier_medical_japanese`](https://huggingface.co/Tetsuo3003/highrisk_textclassifier_medical_japanese) を使用し、Streamlit Cloud 上で「リスクあり／なし」の判定を行うWebアプリです。

## 🔧 使用方法

1. このリポジトリを GitHub にアップロード
2. [Streamlit Cloud](https://streamlit.io/cloud) にログインし、「New app」→ このリポジトリを選択
3. `app.py` を実行エントリとしてデプロイ

## ✅ 必要ライブラリ

- streamlit
- transformers
- fugashi
- unidic-lite

## ✨ 使い方の例

> 夜1時頃トイレに行った時寒気と足の震えが強くて、ズボンが下げられず困ったそうです。

→ 🔍 判定結果：リスクあり

---

© 2025 Tetsuo Ishikawa
