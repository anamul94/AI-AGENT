import streamlit as st
import uuid
from langchain_core.messages import HumanMessage, SystemMessage
from agents.agents import app  # replace with your actual filename if needed

st.set_page_config(page_title="PubMed Chat", page_icon="🧬")

st.title("🔍 PubMed Research Assistant")

# Generate and store a thread UUID per session
if "thread_id" not in st.session_state:
    st.session_state.thread_id = str(uuid.uuid4())
    st.session_state.chat_history = []

# Chat input
user_input = st.chat_input("Ask a PubMed research question...")
if user_input:
    # Display the user message
    st.chat_message("user").markdown(user_input)

    # Store the user message
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    # Invoke LangGraph app
    config = {"configurable": {"thread_id": st.session_state.thread_id}}
    user_message = HumanMessage(content=user_input)
    system_message = SystemMessage(content="You are a helpful assistant. For medical research, you can search PubMed and summarize the results.")
    response = app.invoke({"messages": [system_message, user_message]}, config=config)

    messages = response["messages"][-1]
    st.write(messages.content)

    # Append and display the AI/tool response
#     for msg in response["messages"]:
#         content = msg.content if hasattr(msg, "content") else str(msg)
#         st.chat_message("assistant").markdown(content)
#         st.session_state.chat_history.append({"role": "assistant", "content": content})

# # Display previous chat history (when refreshing or navigating)
# for msg in st.session_state.chat_history:
#     st.chat_message(msg["role"]).markdown(msg["content"])
