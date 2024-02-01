import torch
from transformers import pipeline

class SecondSummarizer:
    def __init__(self, model_name="pszemraj/led-base-book-summary", min_length=8, max_length=256, no_repeat_ngram_size=3, encoder_no_repeat_ngram_size=3, repetition_penalty=3.5, num_beams=4, do_sample=False, early_stopping=True):
        self.summarizer = pipeline("summarization", model=model_name, device=0 if torch.cuda.is_available() else -1)
        self.min_length = min_length
        self.max_length = max_length
        self.no_repeat_ngram_size = no_repeat_ngram_size
        self.encoder_no_repeat_ngram_size = encoder_no_repeat_ngram_size
        self.repetition_penalty = repetition_penalty
        self.num_beams = num_beams
        self.do_sample = do_sample
        self.early_stopping = early_stopping

    def generate_summary(self, text):
        return self.summarizer(text, min_length=self.min_length, max_length=self.max_length, no_repeat_ngram_size=self.no_repeat_ngram_size, encoder_no_repeat_ngram_size=self.encoder_no_repeat_ngram_size, repetition_penalty=self.repetition_penalty, num_beams=self.num_beams, do_sample=self.do_sample, early_stopping=self.early_stopping)