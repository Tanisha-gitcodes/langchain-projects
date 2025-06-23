import streamlit as st
import nest_asyncio
from Task_4_LangGraph_UI import build_graph

# Apply asyncio patch (needed for LangGraph + Streamlit)
nest_asyncio.apply()

# Build LangGraph agent
graph = build_graph()

# Streamlit UI
st.set_page_config(page_title="AI Joke Generator", page_icon="😂")
st.title("AI Joke Generator")
st.markdown("Enter a topic and let the AI tell you a joke!")

topic = st.text_input("Enter a topic:")

if st.button("Tell me a joke!"):
    if topic.strip() == "":
        st.warning("Please enter a topic first.")
    else:
        with st.spinner("Generating joke..."):
            result = graph.invoke({"topic": topic})
            st.success(result["joke"])



