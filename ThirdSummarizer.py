from transformers import pipeline

class ThirdSummarizer:
    def __init__(self, model_name="Falconsai/text_summarization", max_length=230, min_length=30, do_sample=False):
        self.summarizer = pipeline("summarization", model=model_name)
        self.max_length = max_length
        self.min_length = min_length
        self.do_sample = do_sample

    def generate_summary(self, text):
        return self.summarizer(text, max_length=self.max_length, min_length=self.min_length, do_sample=self.do_sample)