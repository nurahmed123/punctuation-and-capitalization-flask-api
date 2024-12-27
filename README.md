
# Flask Puntuation Fixer API

This project is a Flask-based API that formats and fixes grammar in given text content using a pre-trained Transformer model (`T5`). The application is exposed to the internet using `ngrok`, allowing for easy testing and sharing.

## Features

- **Grammar Fixing**: Utilizes the `T5-small-wav2vec2-grammar-fixer` model to improve the grammar of the input text.
- **Authentication**: Requires a secret code to access the API.
- **Ngrok Integration**: Exposes the Flask app to the internet using `ngrok`.

## Requirements

- Python 3.8+
- Pip (Python package manager)
- Ngrok account with an authentication token

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/grammar-fixer-api.git
   cd grammar-fixer-api
   ```
Install the dependencies:

```bash
pip install -r requirements.txt
```
Example dependencies:

Set your ngrok authentication token:

```python
ngrok.set_auth_token("your-ngrok-auth-token")
```
Update the SECRET_CODE variable in the script for secure access.

### Usage
Run the Application:
```bash
python3 app.py
```
The app will start running on port 5002 and ngrok will provide a public URL.

Test the API: Use an API testing tool (e.g., Postman or Curl) to send a POST request to the /get-reading-time endpoint.

Example request body:

```json
{
  "secret_code": "amrseccode",
  "content": "this is an example text needing grammar fixes"
}
```
Example response:

```json
{
  "formatted_text": "This is an example text needing grammar fixes."
}
```
Redirect: Accessing any undefined route will redirect to the npm package page.

### Parameters:
- secret_code (string, required): The authentication code.
- content (string, required): The text content to format.
### Response:
- 200 OK: Returns the formatted text.
- 400 Bad Request: Missing or invalid payload.
- 403 Unauthorized: Invalid secret code.
- 500 Internal Server Error: Any server-side error.
/<path:path> (GET)
Description: Redirects to npm package page.
### Notes
- Model: The API uses the flexudy/t5-small-wav2vec2-grammar-fixer model from Hugging Face Transformers.
- Ngrok: Ensure ngrok is installed and authenticated to expose the Flask app publicly.
- Security: Use a strong secret code to prevent unauthorized access.
Troubleshooting
- Ngrok Errors: Ensure your ngrok token is valid and properly set.
- Dependencies Issues: Verify the required packages are installed using pip install -r requirements.txt.
Model Loading: Ensure internet access for downloading the model on the first run.
