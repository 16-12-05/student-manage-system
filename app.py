import streamlit as st
import plotly.express as px
import time

# ---------------------- PAGE CONFIG ---------------------- #
st.set_page_config(
    page_title="Student Feedback Sentiment Analysis",
    page_icon="🎓",
    layout="wide"
)

# ---------------------- CUSTOM CSS ---------------------- #
custom_css = """
<style>
/* Global dark gradient background */
.stApp {
    background: radial-gradient(circle at top left, #1f2933 0%, #020617 40%, #000000 100%);
    color: #e5e7eb;
    font-family: "Inter", system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}

/* Remove default padding */
.block-container {
    padding-top: 1.5rem;
    padding-bottom: 1.5rem;
}

/* Glassmorphism container */
.glass-card {
    background: rgba(15, 23, 42, 0.75);
    border-radius: 18px;
    padding: 1.5rem 1.8rem;
    border: 1px solid rgba(148, 163, 184, 0.35);
    box-shadow: 0 18px 45px rgba(15, 23, 42, 0.9);
    backdrop-filter: blur(18px);
}

/* Header gradient text */
.app-title {
    font-size: 2.8rem;
    font-weight: 800;
    background: linear-gradient(90deg, #38bdf8, #a855f7, #f97316);
    -webkit-background-clip: text;
    color: transparent;
    letter-spacing: 0.03em;
}

.app-subtitle {
    font-size: 0.98rem;
    color: #9ca3af;
}

/* Text area styling */
.stTextArea textarea {
    background: rgba(15, 23, 42, 0.85) !important;
    border-radius: 16px !important;
    border: 1px solid rgba(148, 163, 184, 0.5) !important;
    color: #e5e7eb !important;
    box-shadow: 0 0 0 1px rgba(15, 23, 42, 0.6);
    transition: all 0.25s ease;
}

.stTextArea textarea:focus {
    border-color: #38bdf8 !important;
    box-shadow: 0 0 18px rgba(56, 189, 248, 0.7);
}

/* Analyze button styling */
.stButton>button {
    width: 100%;
    border-radius: 999px;
    padding: 0.8rem 1.2rem;
    border: none;
    background: linear-gradient(135deg, #22c55e, #0ea5e9, #a855f7);
    color: white;
    font-weight: 700;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    box-shadow: 0 12px 30px rgba(56, 189, 248, 0.45);
    transition: all 0.25s ease;
}

.stButton>button:hover {
    transform: translateY(-1px) scale(1.01);
    box-shadow: 0 18px 40px rgba(56, 189, 248, 0.75);
}

/* Result sentiment cards with neon glow */
.result-card {
    border-radius: 18px;
    padding: 1.4rem 1.6rem;
    text-align: center;
    font-size: 1.2rem;
    font-weight: 600;
}

.result-positive {
    background: radial-gradient(circle at top, rgba(34, 197, 94, 0.18), rgba(15, 23, 42, 0.95));
    border: 1px solid rgba(34, 197, 94, 0.7);
    box-shadow: 0 0 25px rgba(34, 197, 94, 0.8);
}

.result-negative {
    background: radial-gradient(circle at top, rgba(239, 68, 68, 0.18), rgba(15, 23, 42, 0.95));
    border: 1px solid rgba(239, 68, 68, 0.7);
    box-shadow: 0 0 25px rgba(239, 68, 68, 0.8);
}

.result-neutral {
    background: radial-gradient(circle at top, rgba(234, 179, 8, 0.18), rgba(15, 23, 42, 0.95));
    border: 1px solid rgba(234, 179, 8, 0.7);
    box-shadow: 0 0 25px rgba(234, 179, 8, 0.8);
}

/* Metric cards */
.css-1xarl3l, .css-12w0qpk {
    background: transparent !important;
}

/* Footer */
.footer {
    margin-top: 2rem;
    padding-top: 1rem;
    border-top: 1px solid rgba(55, 65, 81, 0.7);
    font-size: 0.8rem;
    color: #6b7280;
    text-align: center;
}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# ---------------------- SENTIMENT WORD LISTS (UNCHANGED) ---------------------- #
NEGATIVE_WORDS = [
    "poor","bad","worst","waste","not good","terrible",
    "boring","slow","hard","difficult","disappointed",
    "dirty","confusing","useless","frustrating",
    "annoying","unhelpful","ineffective","unorganized",
    "irrelevant","incomplete","unclear","stressful",
    "outdated","weak","poorly","disappointing",
    "complicated","lengthy","unfair","rude",
    "careless","unprofessional","inaccurate",
    "problematic","tedious","unsatisfactory"
]

POSITIVE_WORDS = [
    "clear","clearly","good","excellent","great",
    "awesome","perfect","nice","satisfied",
    "best","happy","amazing","fantastic",
    "outstanding","wonderful","helpful",
    "informative","interesting","effective",
    "supportive","friendly","interactive",
    "engaging","brilliant","impressive",
    "valuable","motivating","enjoyable",
    "comfortable","professional",
    "knowledgeable","organized",
    "responsive","appreciated","successful"
]

NEUTRAL_WORDS = [
    "okay","average","fine","normal","medium",
    "maybe","not bad","so so","acceptable",
    "moderate","ordinary","fair","reasonable",
    "standard","general","typical","balanced",
    "adequate","consistent","regular",
    "expected","usual","satisfactory",
    "mixed","partially","somewhat",
    "occasionally","depends","uncertain",
    "basic","common"
]

# ---------------------- SIDEBAR ---------------------- #
with st.sidebar:
    st.markdown("### 🎓 Project Info")
    st.markdown(
        """
        **Student Feedback Sentiment Analysis**

        - 🔍 Rule-based sentiment detection  
        - 📊 Word-count based statistics  
        - 🌌 Modern dark UI with glassmorphism  
        - 📈 Interactive Plotly charts  

        _Tip: Try mixing positive, negative and neutral words to see how counts change._
        """
    )
    st.markdown("---")
    st.markdown("**Tech Stack**")
    st.markdown("- 🐍 Python\n- 🧊 Streamlit\n- 📊 Plotly")

# ---------------------- HEADER ---------------------- #
header_container = st.container()
with header_container:
    col_h1, col_h2 = st.columns([3, 1])
    with col_h1:
        st.markdown(
            '<div class="glass-card">'
            '<div class="app-title">🎓 Student Feedback Sentiment Dashboard</div>'
            '<div class="app-subtitle">'
            'Analyze student feedback using simple rule-based sentiment logic with a modern, dark-themed interface.'
            '</div>'
            '</div>',
            unsafe_allow_html=True
        )
    with col_h2:
        st.metric(label="Version", value="1.0", delta="Rule-based")

st.markdown("")  # small spacing

# ---------------------- MAIN LAYOUT ---------------------- #
main_container = st.container()
with main_container:
    input_col, result_col = st.columns([1.2, 1])

    # -------- Feedback Input Section -------- #
    with input_col:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("#### ✍️ Enter Student Feedback")
        feedback = st.text_area(
            label="",
            placeholder="Type or paste feedback here... (e.g., 'The faculty explanation was excellent and helpful')",
            height=180
        )
        analyze_button = st.button("Analyze Sentiment")
        st.markdown("</div>", unsafe_allow_html=True)

    # Initialize variables for later use
    sentiment = None
    positive_count = negative_count = neutral_count = 0

    # -------- Sentiment Analysis Logic (UNCHANGED) -------- #
    if analyze_button:
        if feedback.strip() == "":
            st.warning("Please enter some feedback text before analyzing.")
        else:
            # Animated progress bar + spinner
            progress_placeholder = st.empty()
            with progress_placeholder.container():
                progress_bar = st.progress(0)
                with st.spinner("Analyzing feedback..."):
                    for i in range(1, 101, 10):
                        time.sleep(0.05)
                        progress_bar.progress(i)

            text = feedback.lower()

            positive_count = 0
            negative_count = 0
            neutral_count = 0

            for word in POSITIVE_WORDS:
                if word in text:
                    positive_count += 1

            for word in NEGATIVE_WORDS:
                if word in text:
                    negative_count += 1

            for word in NEUTRAL_WORDS:
                if word in text:
                    neutral_count += 1

            if positive_count > negative_count and positive_count > neutral_count:
                sentiment = "Positive 😊"

            elif negative_count > positive_count and negative_count > neutral_count:
                sentiment = "Negative 😞"

            elif neutral_count > positive_count and neutral_count > negative_count:
                sentiment = "Neutral 😐"

            elif positive_count > 0 and negative_count == 0:
                sentiment = "Positive 😊"

            elif negative_count > 0 and positive_count == 0:
                sentiment = "Negative 😞"

            else:
                sentiment = "Neutral 😐"

            # Clear progress bar after done
            progress_placeholder.empty()

   
    with result_col:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("#### 📌 Sentiment Result")

        if sentiment:
            # Choose CSS class based on sentiment
            if "Positive" in sentiment:
                result_class = "result-positive"
            elif "Negative" in sentiment:
                result_class = "result-negative"
            else:
                result_class = "result-neutral"

            result_html = f"""
            <div class="result-card {result_class}">
                Predicted Sentiment:<br><span style="font-size:1.6rem;">{sentiment}</span>
            </div>
            """
            st.markdown(result_html, unsafe_allow_html=True)
        else:
            st.info("Sentiment result will appear here after you click **Analyze Sentiment**.")

        st.markdown("</div>", unsafe_allow_html=True)

    # -------- Statistics + Visualizations -------- #
    if sentiment:
        stats_container = st.container()
        with stats_container:
            st.markdown("")
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            st.markdown("#### 📊 Sentiment Statistics")

            # Metric cards
            m1, m2, m3 = st.columns(3)
            with m1:
                st.metric("Positive Words", positive_count)
            with m2:
                st.metric("Negative Words", negative_count)
            with m3:
                st.metric("Neutral Words", neutral_count)

            # Prepare data for charts
            labels = ["Positive", "Negative", "Neutral"]
            values = [positive_count, negative_count, neutral_count]

            # Plotly Pie Chart
            pie_col, bar_col = st.columns(2)
            with pie_col:
                pie_fig = px.pie(
                    names=labels,
                    values=values,
                    color=labels,
                    color_discrete_map={
                        "Positive": "#22c55e",
                        "Negative": "#ef4444",
                        "Neutral": "#eab308"
                    },
                    title="Sentiment Word Distribution (Pie)"
                )
                pie_fig.update_layout(
                    paper_bgcolor="rgba(0,0,0,0)",
                    plot_bgcolor="rgba(0,0,0,0)",
                    font_color="#e5e7eb",
                    legend_title_text="Sentiment"
                )
                st.plotly_chart(pie_fig, use_container_width=True)

            # Plotly Bar Chart
            with bar_col:
                bar_fig = px.bar(
                    x=labels,
                    y=values,
                    color=labels,
                    color_discrete_map={
                        "Positive": "#22c55e",
                        "Negative": "#ef4444",
                        "Neutral": "#eab308"
                    },
                    title="Sentiment Word Counts (Bar)"
                )
                bar_fig.update_layout(
                    paper_bgcolor="rgba(0,0,0,0)",
                    plot_bgcolor="rgba(15,23,42,0.7)",
                    font_color="#e5e7eb",
                    xaxis_title="Sentiment",
                    yaxis_title="Word Count"
                )
                st.plotly_chart(bar_fig, use_container_width=True)

            st.markdown("</div>", unsafe_allow_html=True)

st.markdown(
    """
    <div class="footer">
        Built with ❤️ using Streamlit & Plotly · Rule-based sentiment logic preserved exactly as in the original code.
    </div>
    """,
    unsafe_allow_html=True
)
