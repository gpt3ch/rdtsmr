import streamlit as st
from util.thread_fetcher import ThreadFetcher 

def on_submit(url):
    print(url)
    submission, comments = threadFetcher.fetchThread(url)
    st.text(f'Submission title: {submission.title[:10]} Total comments found: {len(comments)}')
    st.text(comments[0:5])

if __name__ == "__main__":
    st.title("Reddit Summarizer")
    url_str = st.text_input("Reddit url", "https://reddit.com/r/abc")
    st.text(f"Getting data for reddit thread {url_str}")
    btn = st.button("Submit", type="primary")
    threadFetcher = ThreadFetcher()
    if btn:
        on_submit(url_str)