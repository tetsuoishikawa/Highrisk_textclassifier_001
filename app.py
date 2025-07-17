import streamlit as st
from transformers import pipeline

# タイトル
st.title("🩺 ハイリスク分類モデル（日本語の医療会話文が対象）")

# モデル情報
model_name = "Tetsuo3003/highrisk_textclassifier_medical_japanese"

# モデル読み込み
@st.cache_resource
def load_model():
    return pipeline("text-classification", model=model_name, tokenizer=model_name)

classifier = load_model()

# ユーザー入力
user_input = st.text_area("📝 判定したい文章を入力してください：", height=150)

# 推論
if st.button("分類する"):
    if user_input.strip() == "":
        st.warning("文章を入力してください。")
    else:
        with st.spinner("推論中..."):
            result = classifier(user_input)[0]
            label = result["label"]
            score = result["score"]

            st.markdown(f"### 🔍 判定結果： `{label}`")
            st.markdown(f"### 📊 確信度： `{score:.2%}`")
