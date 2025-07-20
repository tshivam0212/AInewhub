import streamlit as st
from langchain import PromptTemplate
#from langchain_openai import OpenAI

#llm = ChatOpenAI(model="gpt-3.5-turbo")
from langchain_groq import ChatGroq
st.set_page_config(
    page_title = "Blog Post Generator"
)

st.title("Blog Post Generator")

groq_api_key = st.sidebar.text_input(
    "groq API Key",
    type = "password"
)

# LLM and key loading function
def load_LLM(groq_api_key):
    """Load LLaMA model from Groq API."""
    llm = ChatGroq(
        model="llama3-70b-8192",  # or "llama3-8b-8192" if you want smaller model
        groq_api_key=groq_api_key,
        temperature=0.7
    )
    return llm

def generate_response(topic):
    llm = load_LLM(groq_api_key=groq_api_key)
    template = """
    As experienced startup and venture capital writer, 
    generate a 400-word blog post about {topic}.
    
    Your response should be in this format:
    First, print the blog post.
    Then, sum the total number of words on it and print the result like this: This post has X words.
    """
    prompt = PromptTemplate(
        input_variables=["topic"],
        template=template
    )
    query = prompt.format(topic=topic)
    response = llm.invoke(query)  # ✅ FIXED
    st.write(response.content if hasattr(response, "content") else response)

  


topic_text = st.text_input("Enter topic: ")
if not groq_api_key.startswith("gsk-"):
    st.warning("Enter OpenAI API Key")
if groq_api_key.startswith("gsk"):
    generate_response(topic_text)
        
