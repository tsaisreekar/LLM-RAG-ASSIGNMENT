import streamlit as st
import requests

# Streamlit UI
st.title("RAG LLM System")
st.write("Ask a question, and the system will search the internet and provide an AI-generated answer!")

# Input box for user query
query = st.text_input("Enter your query")

if st.button("Submit"):
    if query.strip():
        with st.spinner("Processing..."):
            response = requests.post(
                "http://127.0.0.1:5001/query",  # Flask API endpoint
                json={"query": query}
            )
            if response.status_code == 200:
                result = response.json()
                st.success("AI Response:")
                st.write(result.get("response", "No AI response available."))

                st.write("Search Results:")
                search_results = result.get("search_results", [])
                if search_results:
                    for result in search_results:
                        st.markdown(f"[{result['title']}]({result['link']})")
                        st.write(result.get('snippet', 'No description available.'))
                        st.write("---")
                else:
                    st.warning("No results found.")
            else:
                st.error(f"Error: {response.json().get('error', 'Unknown error')}")
    else:
        st.error("Please enter a query.")
