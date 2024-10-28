import streamlit as st
# import docx2txt
import io
import re
from PIL import Image

# Sample image and page settings
# img = Image.open('Aldrich-Capital-Partners.jpg')
# st.set_page_config(page_title="Aldrich Capital Partners", page_icon=img)

# Sidebar with logo
# st.sidebar.image("aldrich-logo.png", width=250)

# Sample cost settings and calculation
COST_PER_MILLION_TOKENS = 0.13
st.session_state.running_total_cost = 0.0

# Function to calculate cost based on token count
def calculate_cost_based_on_tokens(tokens):
    cost = (len(tokens) / 1e6) * COST_PER_MILLION_TOKENS
    return cost

# Function to split text by description pattern
def split_company_info_by_description(company_info):
    description_pattern = r"(?:\n|^\s*?)description\s*?:"
    company_splits = re.split(description_pattern, company_info, flags=re.IGNORECASE)
    if len(company_splits) < 3:
        return [company_info]
    return company_splits

# Function to process DOCX files and extract text
def get_text_chunks_from_docx(docx_files):
    all_text_chunks = []
    for docx in docx_files:
        # text = docx2txt.process(io.BytesIO(docx.read()))
        pattern = r"(\n.*?interest\s*?check.*\n)"
        # splits = re.split(pattern, text, flags=re.IGNORECASE)
        # if splits:
            # companies = [splits[0]] + [f"{splits[i]}\n\n{splits[i + 1]}" for i in range(1, len(splits) - 1, 2)]
            # all_text_chunks.extend([split_company_info_by_description(company) for company in companies])
    return all_text_chunks

# UI structure
st.title("Aldrich Capital Partner IC BOT")

# Sidebar for uploading documents
with st.sidebar:
    st.subheader("Upload IC Documents:")
    docx_files = st.file_uploader("Upload your Word documents here", accept_multiple_files=True, type=['docx'])
    if st.button("Process"):
        with st.spinner("Processing documents..."):
            try:
                text_chunks = get_text_chunks_from_docx(docx_files)
                st.session_state.text_chunks = text_chunks
                st.success("Documents processed successfully!")
            except Exception as e:
                st.error(f"Error processing documents: {e}")

# Chat interface
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input for chat and simulate a response
if prompt := st.chat_input("Ask about IC Docs"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        with st.spinner("Processing your request..."):
            response = f"Simulated response for: {prompt}"  # Replace with actual processing logic as needed
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.write(response)
