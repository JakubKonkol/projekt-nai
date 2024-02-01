from flask import Flask

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

# Printing the summaries
print(first_summarizer.generate_summary(example_text))
print(second_summarizer.generate_summary(example_text))
print(third_summarizer.generate_summary(example_text))

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == 'main':
    app.run()