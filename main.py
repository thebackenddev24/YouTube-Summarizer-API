from flask import Flask, request, jsonify
from gradio_client import Client

app = Flask(__name__)

def validate_params(data):
    errors = []
    if data is None:
        errors.append("Request data is missing.")
    else:
        if 'generation_temperature' not in data or data['generation_temperature'] is None or data['generation_temperature'] < 0.01 or data['generation_temperature'] > 1.0:
            errors.append("Generation temperature must be between 0.01 and 1.0.")
        if 'summary_length' not in data or data['summary_length'] is None or data['summary_length'] < 100 or data['summary_length'] > 500:
            errors.append("Summary length must be between 100 and 500.")
    return errors

@app.route('/summarise', methods=['POST'])
def summarize_youtube():
    try:
        data = request.json
        validation_errors = validate_params(data)
        if validation_errors:
            return jsonify({"error": validation_errors}), 400

        client = Client("https://prakhardoneria-summarize-youtube.hf.space/")
        result = client.predict(
            data.get('youtube_url', ''),
            data.get('transcribe', False),
            data.get('api_token', ''),  # Adding empty string as default value for missing token
            data.get('generation_temperature', 0.5),
            data.get('summary_length', 300),
            data.get('set_temperature', True),
            api_name="/summarize_youtube_video"
        )

        # Remove the unwanted line from the response
        result = [item for item in result if "The summary was generated using" not in item]

        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/', methods=['GET'])
def today_summary():
    try:
        
        summary = "Let's summaries something"
        return jsonify({"summary": summary})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"error": "The requested URL was not found on the server."}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
