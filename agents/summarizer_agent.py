from crewai import Agent
# Passo 1: Importe da nova biblioteca que acabamos de instalar
from langchain_ollama import OllamaLLM

# Passo 2: Adicione o prefixo "ollama/" ao nome do modelo
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