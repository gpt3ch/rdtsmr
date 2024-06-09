import streamlit as st
from util.thread_fetcher import ThreadFetcher 
from util.summarizer import Summarizer

def on_submit(url):
    print(url)
    submission, comments = threadFetcher.fetchThread(url)
    st.text(f'Submission title: {submission.title[:50]}')
    st.text(f'Total comments found: {len(comments)}')
    st.text(comments[0:5])
    return comments

if __name__ == "__main__":
    st.title("Reddit Summarizer")
    smr = Summarizer()
    url_str = st.text_input("Reddit url", "https://reddit.com/r/abc")
    btn = st.button("Submit", type="primary")
    threadFetcher = ThreadFetcher()
    commentStr = ''
    if btn:
        commentStr = on_submit(url_str)
        print(commentStr[0:20])
        summary = smr.summarize(commentStr) 
        st.text_area(label="", value=summary, label_visibility='collapsed',
                            disabled=False, max_chars=5000)