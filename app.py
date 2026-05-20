import streamlit as st
import pickle
import pandas as pd
import base64   #this library use to convert image into another format

# importing our created modules (cleans text,cleans text,gives rating,finds category,checks fake,store & fetch data)  
from preprocess import preprocess
from utils import (
    get_sentiment,
    detect_fake_review,
    predict_rating,
    detect_category
)
from database import create_table, insert_review, fetch_reviews


# BACKGROUND + UI 
def set_background(image_file):
    # with open image file in read binary mode as f
    with open(image_file, "rb") as f:
        #Needed because Streamlit CSS can’t directly load local images
        encoded = base64.b64encode(f.read()).decode()

    #insert image into app background using CSS
    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}

    /* 🌫 Glass Effect Container */
    .block-container {{
        background: rgba(0, 0, 0, 0.45);
        backdrop-filter: blur(12px);
        border-radius: 15px;
        padding: 25px;
    }}

    /* Text Colors */
    h1, h2, h3, h4, h5, h6, p, label {{
        color: white !important;
    }}

    /* Input Box */
    textarea {{
        background-color: rgba(255,255,255,0.1) !important;
        color: white !important;
        border-radius: 10px !important;
    }}

    /* Buttons */
    button {{
        background-color: #1f77b4 !important;
        color: white !important;
        border-radius: 10px !important;
    }}

    /* Dataframe */
    .stDataFrame {{
        background-color: rgba(255,255,255,0.1);
        border-radius: 10px;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)


# 👉 SET YOUR IMAGE PATH
set_background("assets/bg.jpg")



#Uses CREATE TABLE IF NOT EXISTS no duplicate DB will be create
create_table()

#Loads trained ML model
with open("model/model.pkl", "rb") as f:
    model = pickle.load(f)

with open("model/vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)


# UI 
# Main title
st.title("🛒 E-commerce Review Intelligence System")
st.markdown("Analyze reviews with AI + store insights + view analytics")

# input User enters review
st.subheader("✍️ Enter Review")
review = st.text_area("Type your review here:")

#Runs analysis only when clicked
if st.button("Analyze Review"):
    if review.strip() == "":
        st.warning("Please enter a review")
    else:
        processed = preprocess(review)
        #it will clean the text in lowercase and remoe stopwords
        
        vec = vectorizer.transform([processed])
        #convert text into numerical features

        prediction = model.predict(vec)[0]
        #Model predicts 1=neg+ve , 2=pos+ve

        proba = model.predict_proba(vec)[0]
        confidence = max(proba)
        #Get probability (confidence level)

        #Converts to Positive / Negative / Neutral
        sentiment = get_sentiment(prediction, confidence)
        
        #Converts into rating (1–5)
        rating = predict_rating(prediction, confidence)

        #Delivery / Quality / Pricing / etc.
        category = detect_category(review)

        #Detects fake patterns
        fake_status = detect_fake_review(review)

        # Save to DB
        insert_review(review, sentiment, category, rating, confidence, fake_status)

        # Output
        st.subheader("📊 Analysis Result")

        col1, col2 = st.columns(2)

        with col1:
            st.success(f"Sentiment: {sentiment}")
            st.info(f"Confidence: {round(confidence * 100, 2)}%")

        with col2:
            st.write(f"⭐ Rating: {'⭐' * rating} ({rating}/5)")
            st.write(f"📦 Category: {category}")

        st.warning(f"🚨 Fake Detection: {fake_status}")


# DASHBOARD 
st.subheader("📊 Analytics Dashboard")

data = fetch_reviews()
#Fetch all stored reviews from DB

if data:
    #Convert DB data into table
    df = pd.DataFrame(data, columns=[
        "ID", "Review", "Sentiment", "Category", "Rating", "Confidence", "Fake"
    ])

    # Filters
    st.markdown("### 🔍 Filters")

    col1, col2 = st.columns(2)

    with col1:
        #Dropdown filter for sentiment
        sentiment_filter = st.selectbox(
            "Filter by Sentiment",
            ["All"] + list(df["Sentiment"].unique())
        )

    with col2:
        #Dropdown filter for category
        category_filter = st.selectbox(
            "Filter by Category",
            ["All"] + list(df["Category"].unique())
        )

    filtered_df = df.copy()
    #Create copy for filtering

    #Apply filter condition
    if sentiment_filter != "All":
        filtered_df = filtered_df[filtered_df["Sentiment"] == sentiment_filter]

    if category_filter != "All":
        filtered_df = filtered_df[filtered_df["Category"] == category_filter]

    # Show Data
    st.markdown("### 📄 Filtered Reviews")
    st.dataframe(filtered_df)

    # Stats
    st.markdown("### 📈 Insights")

    col1, col2 = st.columns(2)

    with col1:
        st.write("#### Sentiment Distribution")
        st.write(df["Sentiment"].value_counts())

    with col2:
        st.write("#### Rating Distribution")
        st.write(df["Rating"].value_counts())

else:
    st.info("No data yet. Add reviews above 👆")