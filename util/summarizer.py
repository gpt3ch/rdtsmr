import torch
import streamlit as st
from transformers import AutoTokenizer, AutoModelWithLMHead

class Summarizer:

    st.cache_resource
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained('facebook/bart-large-cnn')                        
        self.model = AutoModelWithLMHead.from_pretrained('facebook/bart-large-cnn', return_dict=True)
    
    def tokenize(self, input):
        inputs = self.tokenizer.encode("summarize: " + input,                  
        return_tensors='pt',              
        max_length=512,             
        truncation=True)
        return inputs

    def summarize(self, input):
        summary_ids = self.model.generate(self.tokenize(input=input), max_length=512, min_length=80, length_penalty=5., num_beams=2)
        summary = self.tokenizer.decode(summary_ids[0])
        return summary