from flask import Flask, request, jsonify, redirect
from transformers import T5Tokenizer, T5ForConditionalGeneration
from pyngrok import ngrok

app = Flask(__name__)

# Set your ngrok authtoken
ngrok.set_auth_token("2lNKs9bbKc5FU37Q3Ma9hY00cpb_2FwkBm1g6cVtitdquBhvS")

# Load the model and tokenizer
model_name = "flexudy/t5-small-wav2vec2-grammar-fixer"
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

# Secret code for authentication
SECRET_CODE = "amrseccode"


def format_text(message: str) -> str:
    """
    Format the given message using the pre-trained model.
    """
    try:
        input_text = f"fix: {{ {message} }} </s>"
        input_ids = tokenizer.encode(
            input_text,
            return_tensors="pt",
            max_length=256,
            truncation=True,
            add_special_tokens=True,
        )
        outputs = model.generate(
            input_ids=input_ids,
            max_length=256,
            num_beams=4,
            repetition_penalty=1.0,
            length_penalty=1.0,
            early_stopping=True,
        )
        formatted_text = tokenizer.decode(
            outputs[0], skip_special_tokens=True, clean_up_tokenization_spaces=True
        )
        return formatted_text
    except Exception as e:
        return str(e)


@app.route("/get-reading-time", methods=["POST"])
def get_reading_time():
    try:
        data = request.get_json()
        if not data or "secret_code" not in data or "content" not in data:
            return (
                jsonify(
                    {"error": "Invalid payload. Provide 'secret_code' and 'content'."}
                ),
                400,
            )

        secret_code = data["secret_code"]
        content = data["content"]

        if secret_code != SECRET_CODE:
            return jsonify({"error": "Unauthorized. Incorrect secret code."}), 403

        # Format the content using the NLP model
        formatted_text = format_text(content)
        return jsonify({"formatted_text": formatted_text}), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def catch_all(path):
    return redirect("https://www.npmjs.com/package/get-reading-time", code=302)


# Create a tunnel and run the Flask app
if __name__ == "__main__":
    # Set up the tunnel to the Flask app
    public_url = ngrok.connect(5002)
    print("Flask app is accessible at:", public_url)

    app.run(debug=True, use_reloader=False,host="0.0.0.0", port=5002)  # Ensure `use_reloader=False` to prevent issues


