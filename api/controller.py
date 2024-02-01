from flask import Blueprint, jsonify, request
from enum import Enum

from models.FirstSummarizer import FirstSummarizer
from models.SecondSummarizer import SecondSummarizer
from models.ThirdSummarizer import ThirdSummarizer


class SummarizerModel(Enum):
    FACEBOOK_BART = 'facebook/bart-large-cnn'
    PSZEMRAJ_LED = 'pszemraj/led-base-book-summary'
    FALCONSAI_SUMMARIZER = 'Falconsai/text_summarization'
summarize_blueprint = Blueprint('summarize', __name__, url_prefix='/api')

"""
ENDPOINT /api/summarize
METHOD: POST
BODY: {
    "model": "facebook/bart-large-cnn",
    "text_to_summarize": "Some text to summarize"
}
RESPONSE: {
    "summary": "Some summary"
}
"""
@summarize_blueprint.route('/summarize', methods=['POST'])
def summarize():
    try:
        data = request.get_json()
        model = data.get('model')
        text_to_summarize = data.get('text_to_summarize')

        if not model or not text_to_summarize:
            return jsonify({"error": "Both 'model' and 'text_to_summarize' are required"}), 400

        if model == SummarizerModel.FACEBOOK_BART.value:
            print('SELECTED MODEL: ' + SummarizerModel.FACEBOOK_BART.value)
            first_summarizer = FirstSummarizer()
            print('GENERATING SUMMARY.....')
            summary = first_summarizer.generate_summary(text_to_summarize)
            summary = summary[0]['summary_text']
            response_data = {"summary": summary}
            print('SUMMARY GENERATED, SENDING RESPONSE.')
            return jsonify(response_data), 200
        elif model == SummarizerModel.PSZEMRAJ_LED.value:
            print('SELECTED MODEL: ' + SummarizerModel.PSZEMRAJ_LED.value)
            second_summarizer = SecondSummarizer()
            print('GENERATING SUMMARY.....')
            summary = second_summarizer.generate_summary(text_to_summarize)
            summary = summary[0]['summary_text']
            response_data = {"summary": summary}
            print('SUMMARY GENERATED, SENDING RESPONSE.')
            return jsonify(response_data), 200
        elif model == SummarizerModel.FALCONSAI_SUMMARIZER.value:
            print('SELECTED MODEL: ' + SummarizerModel.FALCONSAI_SUMMARIZER.value)
            third_summarizer = ThirdSummarizer()
            print('GENERATING SUMMARY.....')
            summary = third_summarizer.generate_summary(text_to_summarize)
            summary = summary[0]['summary_text']
            response_data = {"summary": summary}
            print('SUMMARY GENERATED, SENDING RESPONSE.')
            return jsonify(response_data), 200
        else:
            return jsonify({"error": "Invalid model"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500
