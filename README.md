
# **LLM-RAG Assignment**

This project implements a **Retrieval-Augmented Generation (RAG) System** using a Flask backend and a Streamlit frontend. The system integrates a **Google Custom Search API** for web content retrieval and the **Hugging Face API** for response generation. Users can input queries through the Streamlit interface, and the system will fetch relevant search results, process them, and generate a meaningful response.

---

## **Features**
1. **Content Retrieval**:
   - Uses the **Google Custom Search API** to search for web pages related to a user's query.
   - Extracts relevant content such as headings and snippets from the search results.

2. **Response Generation**:
   - Leverages the **Hugging Face API** (FLAN-T5 model) to generate responses based on the user's query and retrieved content.

3. **Frontend Interface**:
   - Built using **Streamlit**, enabling users to interact with the system via a clean and simple web interface.

4. **Backend Service**:
   - Built with **Flask**, which processes the query, fetches search results, and communicates with the Hugging Face API to generate a response.

---

## **Project Structure**

```
LLM-RAG-ASSIGNMENT/
├── flask_app/
│   └── app.py                 # Flask backend
├── streamlit_app/
│   └── streamlit_app.py       # Streamlit frontend
├── requirements.txt           # Required Python packages
└── README.md                  # Project documentation
```

---

## **Setup Instructions**

Follow these steps to set up and run the project on your local machine.

### **1. Clone the Repository**
```bash
git clone https://github.com/tsaisreekar/LLM-RAG-ASSIGNMENT.git
cd LLM-RAG-ASSIGNMENT
```

### **2. Set Up a Virtual Environment**
- **Windows**:
  ```bash
  python -m venv env
  env\Scripts\activate
  ```
- **Mac/Linux**:
  ```bash
  python3 -m venv env
  source env/bin/activate
  ```

### **3. Install Dependencies**
Install the required Python packages using:
```bash
pip install -r requirements.txt
```

### **4. Set Up Environment Variables**
Create a `.env` file in the root directory to securely store your API keys:
```
GOOGLE_API_KEY=your_google_custom_search_api_key
CSE_ID=your_google_custom_search_engine_id
HUGGINGFACE_API_KEY=your_hugging_face_api_key
```

Replace the placeholders with your actual API keys.

### **5. Run the Flask Backend**
Navigate to the `flask_app` directory and start the Flask server:
```bash
cd flask_app
python app.py
```
The backend will run at `http://127.0.0.1:5001`.

### **6. Run the Streamlit Frontend**
In a new terminal, navigate to the `streamlit_app` directory and start the Streamlit app:
```bash
cd streamlit_app
streamlit run streamlit_app.py
```
The frontend will be available at `http://localhost:8501`.

---

## **Usage**

1. Open the Streamlit app in your browser.
2. Enter your query in the input box and click "Submit".
3. The system will:
   - Retrieve relevant search results from the internet.
   - Process the content and generate a response using the Hugging Face model.
   - Display both the generated response and the search results on the interface.

---

## **Example Query**

- **Query**: *What is a product?*
- **Response**:
   *A product is an item or service created to fulfill a need or want. It can be physical, virtual, or a hybrid and serves a specific market.*

---

## **Dependencies**

The project uses the following Python libraries:
- `Flask` - For the backend server.
- `requests` - For API requests.
- `google-api-python-client` - For Google Custom Search.
- `streamlit` - For the frontend interface.

Ensure all dependencies are installed using `requirements.txt`.

---

## **Notes**

- Ensure your API keys are valid and have sufficient quotas.
- The Hugging Face model used (`google/flan-t5-large`) may have limitations based on your plan.
- For better conversational memory, you can enhance the system with tools like **LangChain** (optional).

---

## **Contact**

**Author**: T Sai Sreekar  
**Email**: [thimmavajjalasaisreekar@gmail.com](mailto:thimmavajjalasaisreekar@gmail.com)  
**GitHub**: [tsaisreekar](https://github.com/tsaisreekar)

---
