from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
import os
import logging
from keys import *

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Set environment variable for API token
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

def initialize_llm():
    """
    Initialize the language model.
    """
    model = "gemini-2.0-flash-exp"
    logger.info("Initializing LLM: %s", model)
    return ChatGoogleGenerativeAI(
        model=model,
        temperature=0.7,
        max_tokens=None,
        max_retries=2
    )

def extract_responses_with_llm(posts_comments):
    """
    Extract responses from the language model based on Reddit comments.
    """
    logger.info("Starting extraction of responses with LLM")
    try:
        llm = initialize_llm()
        
        # Define the prompt template for the LLM
        prompt = PromptTemplate(
            template=(
                "Analyze the provided collection of Reddit comments and summarize the top 10 most insightful, "
                "popular, or frequently mentioned points. Focus on extracting key themes, opinions, or ideas, "
                "and present them in a concise and organized list format:\n{text}"
            ),
            input_variables=["text"]
        )

        comments = "\n".join(posts_comments)
        formatted_prompt = prompt.format(text=comments)
        response = llm.invoke(formatted_prompt)
        
        return response.content
        
    except Exception as e:
        logger.error(f"Error in LLM processing: {str(e)}")
        return f"Error processing text: {str(e)}"

def get_formatted_response(posts_comments):
    """
    Get a formatted response from the extracted LLM responses.
    """
    # Extract responses from the LLM
    response = extract_responses_with_llm(posts_comments).strip()
    
    # Formatting the response to make it more readable
    lines = response.split("\n")
    formatted_response = []
    for line in lines:
        line = line.strip()
        if line:
            formatted_response.append(line)
    formatted_response = "\n".join(formatted_response)
    return f"""Top insights from reddit comments:\n\n{formatted_response}"""