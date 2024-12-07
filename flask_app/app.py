from flask import Flask, request, jsonify
from googleapiclient.discovery import build
from transformers import pipeline

app = Flask(__name__)

# API keys
my_api_key = "AIzaSyBoU47872vZXsxg5GadNgr001SALhlgizU"
my_cse_id = "24defbbbae93e459d"
huggingface_api_key = "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"  #Hugging Face API key

# Initialize Hugging Face model (GPT-2)
generator = pipeline('text-generation', model='gpt2', device=0)  

# Route for the home page (root URL)
@app.route('/')
def home():
    return "Flask app is running. Use the /query endpoint for search functionality."

# Route for the /query endpoint
@app.route('/query', methods=['POST'])
def query():
    user_query = request.json.get('query')  # Get the query from the request

    if not user_query:
        return jsonify({"error": "No query provided"}), 400

    try:
        # Call Google Custom Search API to search the query
        service = build("customsearch", "v1", developerKey=my_api_key)
        res = service.cse().list(q=user_query, cx=my_cse_id).execute()

        if 'items' in res:
            # Extracting the relevant content (Title and Snippet) from search results
            text_content = ""
            for item in res['items']:
                title = item.get('title', '')
                snippet = item.get('snippet', '')
                text_content += f"Title: {title}\nSnippet: {snippet}\n\n"

            # Use Hugging Face GPT-2 model to generate a response based on the content retrieved
            full_input = f"Based on the following information, answer the question: '{user_query}'\n\n{text_content}"

            # Generate the response using max_new_tokens to avoid exceeding the limit
            gpt_response = generator(full_input, max_new_tokens=150, num_return_sequences=1)

            # Return the response and the search results
            return jsonify({
                "response": gpt_response[0]['generated_text'].strip(),
                "search_results": res['items']
            })
        else:
            return jsonify({"error": "No results found"}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001)
