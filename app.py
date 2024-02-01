from flask import Flask
import pandas as pd

from api import controller
from models.FirstSummarizer import FirstSummarizer
from models.SecondSummarizer import SecondSummarizer
from models.ThirdSummarizer import ThirdSummarizer

app = Flask(__name__)
app.register_blueprint(controller.summarize_blueprint)

# Setting up summarizers
first_summarizer = FirstSummarizer()
second_summarizer = SecondSummarizer()
third_summarizer = ThirdSummarizer()

# Getting data from a csv file
file = pd.read_csv("data/data.csv")

texts = file['text'].tolist()

first_summarizer_generated_summaries = []
second_summarizer_generated_summaries = []
third_summarizer_generated_summaries = []

for text in texts:
    first_summarizer_generated_summaries.append(first_summarizer.generate_summary(text))
    # second_summarizer_generated_summaries.append(second_summarizer.generate_summary(text))
    # third_summarizer_generated_summaries.append(third_summarizer.generate_summary(text))

print(first_summarizer_generated_summaries)
# print(second_summarizer_generated_summaries)
# print(third_summarizer_generated_summaries)



# Evaluating model accuracy through the ROUGE (Recall-Oriented Understudy for Gisting Evaluation) metric

# rouge-1, rouge-2, rouge-l:
# Different versions of ROUGE metrics.
# "rouge-1" evaluates unigram overlap, "rouge-2" evaluates bigram overlap, and "rouge-l" evaluates the longest common subsequence.
#
# f, p, r: These stand for F1 score, precision, and recall, respectively.
#
# F1 score (f): The harmonic mean of precision and recall. It provides a balanced measure of both precision and recall.
#
# Precision (p): The ratio of correctly predicted positive observations to the total predicted positives.
# In the context of ROUGE, it represents the precision of the generated summary.
#
# Recall (r): The ratio of correctly predicted positive observations to all the actual positives.
# In the context of ROUGE, it represents the recall of the generated summary.



# rouge = Rouge()
#
# reference_summary = """The American Society for the Prevention of Cruelty to Animals (ASPCA) reports that around 78
# million dogs are owned as pets in the US. Dogs have been domesticated since 20,000-40000 years ago in Europe.
# They have historically been used for safety, hunting, and companionship.
# Research shows that dogs can make people happier, more resilient, and physically healthier, supporting their well-being."""
#
# generated_summary_third = third_summarizer.generate_summary(example_text)[0]["summary_text"]
#
# scores = rouge.get_scores(generated_summary_third, reference_summary)
# print(scores[0])


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == 'main':
    app.run()