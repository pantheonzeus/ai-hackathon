import streamlit as st

st.set_page_config(page_title='Example')
st.title('Hello From Streamlit 👋')

st.write(
"""
This is a simple user interface built using [Streamlit](https://streamlit.io).
Check out its documentation to see what you can do:

* [Basic concepts](https://docs.streamlit.io/get-started/fundamentals/main-concepts)
* [Build a basic LLM chat app](https://docs.streamlit.io/develop/tutorials/llms/build-conversational-apps)
* [Cheat sheet](https://docs.streamlit.io/develop/quick-reference/cheat-sheet)
* [API reference](https://docs.streamlit.io/develop/api-reference)

Below is an example of a chat interface that simply echoes every message.

---
"""
)

if "messages" not in st.session_state:
    st.session_state.messages = []


def append_message(role, content):
    with st.chat_message(role):
        st.write(content)

    st.session_state.messages.append({
        "role": role,
        "content": content,
    })


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

prompt = st.chat_input("Say something")

if prompt:
    append_message(role="user", content=prompt)
    # (Something smart could happen here)
    append_message(role="assistant", content=prompt)
