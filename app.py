import streamlit as st
import pandas as pd
import networkx as nx
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules
import plotly.express as px
from textblob import TextBlob

st.set_page_config(layout="wide")

# ---------------- LOAD ----------------
df = pd.read_csv("food_delivery_pattern_analysis_1000_rows.csv")

st.title("🍔 Food AI Smart System")

# ---------------- LAYOUT ----------------
col1, col2 = st.columns([1,2])

# ================= LEFT (INPUT) =================
with col1:
    st.header("🎯 Your Input")

    user_meals = st.multiselect(
        "Choose your meals",
        df["meal_name"].unique()
    )

    user_review = st.text_area("Write your review")

    run_btn = st.button("🚀 Run AI")

# ================= RIGHT (OUTPUT) =================
with col2:
    st.header("🤖 AI Results")

    if run_btn:

        # ---------------- ASSOCIATION ----------------
        transactions = df.groupby("order_id")["meal_name"].apply(list).tolist()

        te = TransactionEncoder()
        te_data = te.fit(transactions).transform(transactions)
        df_te = pd.DataFrame(te_data, columns=te.columns_)

        freq = apriori(df_te, min_support=0.02, use_colnames=True)
        rules = association_rules(freq, metric="lift", min_threshold=1)

        rec = []
        for _, row in rules.iterrows():
            if set(user_meals).issubset(row["antecedents"]):
                rec += list(row["consequents"])

        # ---------------- PAGERANK ----------------
        G = nx.Graph()
        for items in transactions:
            for i in items:
                for j in items:
                    if i != j:
                        G.add_edge(i, j)

        pr = nx.pagerank(G)
        pr_df = pd.DataFrame(pr.items(), columns=["Meal", "Score"]).sort_values(by="Score", ascending=False)

        # ---------------- SENTIMENT ----------------
        sentiment = TextBlob(user_review).sentiment.polarity

        # ================= DISPLAY =================

        c1, c2 = st.columns(2)

        with c1:
            st.subheader("🍽️ Recommendations")
            if rec:
                st.success(list(set(rec)))
            else:
                st.warning("No recommendations")

        with c2:
            st.subheader("⭐ Top Meals")
            st.dataframe(pr_df.head(5))

        # Sentiment
        st.subheader("💬 Sentiment Result")
        if sentiment > 0:
            st.success("😊 Positive")
        elif sentiment < 0:
            st.error("😡 Negative")
        else:
            st.warning("😐 Neutral")

        # Chart
        st.subheader("🔥 Popular Meals Chart")
        fig = px.bar(pr_df.head(10), x="Meal", y="Score")
        st.plotly_chart(fig, use_container_width=True)

    else:
        st.info("👈 Enter input and click Run AI")

        