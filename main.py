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

@app.route('/summarise', methods=['GET'])
def summarize_youtube():
    try:
        youtube_url = request.args.get('youtube_url')
        transcribe = request.args.get('transcribe', type=bool, default=False)
        api_token = request.args.get('api_token', default='')
        generation_temperature = request.args.get('generation_temperature', type=float, default=0.5)
        summary_length = request.args.get('summary_length', type=int, default=300)
        set_temperature = request.args.get('set_temperature', type=bool, default=True)

        data = {
            'youtube_url': youtube_url,
            'transcribe': transcribe,
            'api_token': api_token,
            'generation_temperature': generation_temperature,
            'summary_length': summary_length,
            'set_temperature': set_temperature
        }

        validation_errors = validate_params(data)
        if validation_errors:
            return jsonify({"error": validation_errors}), 400
        
        client = Client("https://prakhardoneria-summarize-youtube.hf.space/")
        result = client.predict(
            youtube_url,
            transcribe,
            api_token,
            generation_temperature,
            summary_length,
            set_temperature,
            api_name="/summarize_youtube_video"
        )

        # Remove the unwanted line from the response
        result = [item for item in result if "The summary was generated using" not in item]

        return jsonify(result)
    except Exception as e:
        error_msg = str(e)
        print("Error:", error_msg)
        return jsonify({"error": error_msg}), 500

@app.route('/', methods=['GET'])
def today_summary():
    try:
        # Placeholder for the logic to retrieve today's summary
        summary = "Today's summary goes here."
        return jsonify({"summary": summary})
    except Exception as e:
        error_msg = str(e)
        print("Error:", error_msg)
        return jsonify({"error": error_msg}), 500

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"error": "The requested URL was not found on the server."}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
