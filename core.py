import streamlit as st
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel
from typing import Optional, List
from langchain_core.output_parsers import PydanticOutputParser
import json

# --- 1. Pydantic Schema ---
class MovieInfo(BaseModel):
    title: str
    release_year: Optional[int]
    genre: List[str]
    director: Optional[str]
    main_cast: Optional[List[str]]
    setting_location: Optional[str]
    plot: Optional[str]
    themes: Optional[List[str]]
    ratings: Optional[str]
    notable_features: Optional[str]
    short_summary: str

# --- 2. Setup ---
load_dotenv()
st.set_page_config(page_title="JSON Movie Extractor", page_icon="🤖", layout="wide")

# Custom CSS for a sleek look
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; }
    .status-box {
        padding: 15px;
        border-radius: 10px;
        background-color: #1e2129;
        border-left: 5px solid #00ffcc;
    }
    </style>
    """, unsafe_allow_html=True)

# Initialize Components
parser = PydanticOutputParser(pydantic_object=MovieInfo)
model = ChatMistralAI(model="mistral-small-latest", temperature=0)

prompt_template = ChatPromptTemplate.from_messages([
    ('system', "Extract movie information from the paragraph. {format_instructions}"),
    ("human", "{paragraph}")
])

# --- 3. Streamlit UI ---
st.title("📂 Machine-Readable Movie Extractor")
st.write("Convert unstructured movie descriptions into clean, validated **JSON**.")

col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.subheader("📝 Source Content")
    para = st.text_area(
        "Paste movie description here:", 
        height=400, 
        placeholder="E.g. Directed by Christopher Nolan..."
    )
    process_btn = st.button("Generate JSON", type="primary", use_container_width=True)

with col2:
    st.subheader("🔢 Structured JSON Output")
    
    if process_btn:
        if not para.strip():
            st.error("Please provide some text first.")
        else:
            with st.spinner("Parsing to JSON..."):
                try:
                    # Chain execution
                    final_prompt = prompt_template.invoke({
                        "paragraph": para, 
                        "format_instructions": parser.get_format_instructions()
                    })
                    
                    response = model.invoke(final_prompt)
                    
                    # Parse to Pydantic object then to dict for Streamlit's JSON viewer
                    parsed_output = parser.parse(response.content)
                    json_dict = parsed_output.dict()
                    
                    # Display
                    st.success("Successfully Parsed!")
                    st.json(json_dict) # Beautifully formatted interactive JSON
                    
                    # Download button for the JSON file
                    st.download_button(
                        label="Download JSON Result",
                        data=json.dumps(json_dict, indent=4),
                        file_name="movie_data.json",
                        mime="application/json"
                    )
                except Exception as e:
                    st.error(f"Extraction failed. Ensure the text has enough detail.")
                    with st.expander("Show Technical Error"):
                        st.write(str(e))
    else:
        st.info("The extracted JSON object will appear here.")

st.divider()
st.caption("Built with LangChain • Mistral AI • Pydantic")