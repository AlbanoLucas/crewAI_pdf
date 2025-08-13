# Em agents/writer_agent.py

from crewai import Agent
from langchain_ollama import OllamaLLM

ollama_llm = OllamaLLM(model="ollama/llama3.1:8b", base_url="http://localhost:11434")

writer_agent = Agent(
    role="Escritor Técnico Especialista em Meio Ambiente",
    goal=(
        "Compilar, revisar e estruturar o resumo inicial e as transcrições do debate em um único "
        "documento coeso, bem-organizado e de fácil leitura."
    ),
    backstory=(
        "Você é um escritor e editor profissional com especialização em publicações científicas e relatórios ambientais. "
        "Sua habilidade é transformar discussões complexas e dados brutos em narrativas claras, lógicas e "
        "informativas, prontas para publicação."
    ),
    verbose=True,
    allow_delegation=False,
    llm=ollama_llm
)