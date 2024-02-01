from flask import Flask

import pandas as pd

from rouge import Rouge

from FirstSummarizer import FirstSummarizer
from SecondSummarizer import SecondSummarizer
from ThirdSummarizer import ThirdSummarizer

app = Flask(__name__)

example_text = """According to the American Society for the Prevention of Cruelty to Animals (ASPCA), an estimated 78 million dogs are owned as pets in the United States.

It is unclear when dogs were first domesticated, but a studyTrusted Source published last year claims that, at least in Europe, dogs were tamed 20,000–40,000 years ago.

It is likely that humans and dogs have shared a special bond of friendship and mutual support ever since at least the Neolithic period — but why has this bond been so long-lasting?

Of course, these cousins of the wolves have historically been great at keeping us and our dwellings safe, guarding our houses, our cattle, and our various material goods. Throughout history, humans have also trained dogs to assist them with hunting, or they have bred numerous quirky-looking species for their cuteness or elegance.

However, dogs are also — and might have always been — truly valued companions, famed for their loyalty and seemingly constant willingness to put a smile on their owners’ faces.

In this Spotlight, we outline the research that shows how our dogs make us happier, more resilient when facing stress, and physically healthier, to name but a few ways in which these much-loved quadrupeds support our well-being."""

# Setting up summarizers
first_summarizer = FirstSummarizer()
second_summarizer = SecondSummarizer()
third_summarizer = ThirdSummarizer()

# Getting data from a csv file

file = pd.read_csv("wiki_movie_plots_with_summaries.csv")

texts = file['Plot'].tolist()
summaries = file['PlotSummary'].tolist()

first_summarizer_generated_summaries = []
second_summarizer_generated_summaries = []
third_summarizer_generated_summaries = []

for text in texts:
    first_summarizer_generated_summaries.append(first_summarizer.generate_summary(text))

print(first_summarizer_generated_summaries)



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