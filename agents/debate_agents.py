from crewai import Agent
from langchain_ollama import OllamaLLM

# Configuração do LLM que será compartilhada por todos os agentes
ollama_llm = OllamaLLM(model="ollama/llama3.1:8b", base_url="http://localhost:11434")

# Agente 1: Foco na Preservação
preservationist_agent = Agent(
    role="Ambientalista Focado na Preservação",
    goal="Analisar o resumo e identificar os riscos ambientais, defendendo a proteção máxima dos ecossistemas.",
    backstory=(
        "Você é um biólogo renomado e ativista ambiental, com décadas de experiência em campo. "
        "Sua prioridade é a preservação da biodiversidade e a minimização de qualquer impacto humano, "
        "independentemente dos custos econômicos."
    ),
    verbose=True,
    allow_delegation=False,
    llm=ollama_llm
)

# Agente 2: Foco no Desenvolvimento Sustentável
sustainable_dev_agent = Agent(
    role="Especialista em Desenvolvimento Sustentável",
    goal="Avaliar o resumo buscando um equilíbrio entre proteção ambiental, viabilidade econômica e justiça social.",
    backstory=(
        "Você é um economista e planejador urbano, especializado em projetos de infraestrutura sustentável. "
        "Você acredita que o desenvolvimento é necessário, mas deve ser feito de forma inteligente e responsável, "
        "encontrando sinergias entre progresso e conservação."
    ),
    verbose=True,
    allow_delegation=False,
    llm=ollama_llm
)

# Agente 3: Foco no Aspecto Social
socio_economic_agent = Agent(
    role="Analista Socioeconômico",
    goal="Examinar o resumo sob a ótica do impacto nas comunidades locais, empregos e tradições.",
    backstory=(
        "Você é um sociólogo com vasta experiência em estudos de impacto social. "
        "Seu trabalho é dar voz às comunidades afetadas por grandes projetos, garantindo que os benefícios sociais "
        "sejam maximizados e os ônus, minimizados. Você foca nos aspectos humanos do licenciamento."
    ),
    verbose=True,
    allow_delegation=False,
    llm=ollama_llm
)