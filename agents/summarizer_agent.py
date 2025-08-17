from crewai import Agent
from langchain_ollama import OllamaLLM


ollama_llm = OllamaLLM(model="ollama/llama3.1:8b", base_url="http://localhost:11434")

summarizer_agent = Agent(
    name="SummarizerAgent",
    role="Text Summarizer",
    goal="Summarize the provided text, highlighting its main topic.",
    backstory="Expert in creating concise and informative summaries from text documents.",
    verbose=True,
    allow_delegation=False,
    llm=ollama_llm 
)