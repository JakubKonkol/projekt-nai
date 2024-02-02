from flask import Flask
import json
from rouge import Rouge

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

# Getting data from a json file
with open("data/test.txt", 'r') as file:
    data = json.load(file)

texts = data["text"]
referenced_summaries = data["summary"]

first_summarizer_generated_summaries = []
second_summarizer_generated_summaries = []
third_summarizer_generated_summaries = []

for text in texts:
    first_summarizer_generated_summaries.append(first_summarizer.generate_summary(text))
    second_summarizer_generated_summaries.append(second_summarizer.generate_summary(text))
    third_summarizer_generated_summaries.append(third_summarizer.generate_summary(text))

# Getting only the text of generated summaries
first_summarizer_generated_summaries_text = [item[0]['summary_text'] for item in first_summarizer_generated_summaries]
second_summarizer_generated_summaries_text = [item[0]['summary_text'] for item in second_summarizer_generated_summaries]
third_summarizer_generated_summaries_text = [item[0]['summary_text'] for item in third_summarizer_generated_summaries]

# Mapping model-generated summaries to online generated summaries (reference summaries)
# Reference summaries have been generated using: https://quillbot.com/summarize
first_generated_summaries_mapped_to_reference = {key: value for key, value in zip(first_summarizer_generated_summaries_text, referenced_summaries)}
second_generated_summaries_mapped_to_reference = {key: value for key, value in zip(second_summarizer_generated_summaries_text, referenced_summaries)}
third_generated_summaries_mapped_to_reference = {key: value for key, value in zip(third_summarizer_generated_summaries_text, referenced_summaries)}

first_summarizer_scores = []
second_summarizer_scores = []
third_summarizer_scores = []

# Evaluating model accuracy through the ROUGE (Recall-Oriented Understudy for Gisting Evaluation) metric
# Getting the scores from the summarizers
rouge = Rouge()

for key, value in first_generated_summaries_mapped_to_reference.items():
    first_summarizer_scores.append(rouge.get_scores(key, value))

for key, value in second_generated_summaries_mapped_to_reference.items():
    second_summarizer_scores.append(rouge.get_scores(key, value))

for key, value in third_generated_summaries_mapped_to_reference.items():
    third_summarizer_scores.append(rouge.get_scores(key, value))

# Getting the total F1 scores of all summarizers
first_summarizer_total_f1_scores = [item[key]['f'] for sublist in first_summarizer_scores for item in sublist for key in item]
second_summarizer_total_f1_scores = [item[key]['f'] for sublist in second_summarizer_scores for item in sublist for key in item]
third_summarizer_total_f1_scores = [item[key]['f'] for sublist in third_summarizer_scores for item in sublist for key in item]

# Calculating F1 means of summarizers
# F1 = combination of precision and recall
first_summarizer_mean_score = sum(first_summarizer_total_f1_scores)/len(first_summarizer_total_f1_scores)
second_summarizer_mean_score = sum(second_summarizer_total_f1_scores)/len(second_summarizer_total_f1_scores)
third_summarizer_mean_score = sum(third_summarizer_total_f1_scores)/len(third_summarizer_total_f1_scores)

print("First summarizer F1 mean score: " + str(first_summarizer_mean_score))
print("Second summarizer F1 mean score: " + str(second_summarizer_mean_score))
print("Third summarizer F1 mean score: " + str(third_summarizer_mean_score))

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == 'main':
    app.run()