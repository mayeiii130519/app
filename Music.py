import streamlit as st
from textblob import TextBlob
import pandas as pd
import random

# 標題
st.title("🎧 AI點歌王：唱你心中的那首歌")

# 使用者輸入
user_input = st.text_input("請輸入一句話，描述你的心情：")

# 歌曲資料（你可以自行擴充）
song_data = {
    "positive": [
        {"title": "Happy", "artist": "Pharrell Williams", "link": "https://youtu.be/ZbZSe6N_BXs"},
        {"title": "Can’t Stop the Feeling!", "artist": "Justin Timberlake", "link": "https://youtu.be/ru0K8uYEZWw"}
    ],
    "negative": [
        {"title": "Someone Like You", "artist": "Adele", "link": "https://youtu.be/hLQl3WQQoQ0"},
        {"title": "Fix You", "artist": "Coldplay", "link": "https://youtu.be/k4V3Mo61fJM"}
    ],
    "neutral": [
        {"title": "Let It Be", "artist": "The Beatles", "link": "https://youtu.be/QDYfEBY9NM4"},
        {"title": "Lost Stars", "artist": "Adam Levine", "link": "https://youtu.be/cL4uhaQ58Rk"}
    ]
}

# 分析情緒
if user_input:
    blob = TextBlob(user_input)
    polarity = blob.sentiment.polarity

    if polarity > 0.1:
        mood = "positive"
        mood_label = "開心 / 積極"
    elif polarity < -0.1:
        mood = "negative"
        mood_label = "悲傷 / 壓力"
    else:
        mood = "neutral"
        mood_label = "平靜 / 中立"

    st.subheader(f"🎭 AI判斷你現在的情緒是：**{mood_label}**")

    # 推薦歌曲
    recommendation = random.choice(song_data[mood])
    st.write(f"🎵 推薦歌曲：**{recommendation['title']}** - {recommendation['artist']}")
    st.video(recommendation["link"])
