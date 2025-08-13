# Em tasks/analysis_tasks.py

from crewai import Task

class AnalysisTasks:
    def debate(self, agent_list, context_task):
        return Task(
            description=(
                "Realizar um debate aprofundado sobre o texto fornecido. O texto é um resumo sobre licenciamento ambiental. "
                "Cada um de vocês deve trazer a perspectiva do seu 'role' (Preservacionista, Desenvolvimentista Sustentável, Analista Socioeconômico) "
                "para analisar criticamente os pontos levantados. Discutam os pontos fortes, fracos e as implicações do que foi apresentado. "
                "O objetivo é enriquecer a análise inicial com múltiplos pontos de vista. Ao final, consolidem a discussão em um texto único."
            ),
            expected_output=(
                "Uma transcrição do debate, contendo as análises e contrapontos de cada especialista, "
                "seguida por uma lista de conclusões e pontos-chave consolidados a partir da discussão."
            ),
            agents=agent_list,
            # AQUI ESTÁ A CORREÇÃO: Designa o primeiro agente da lista como o responsável.
            agent=agent_list[0],
            context=[context_task]
        )

    def write(self, agent, context_tasks_list):
        return Task(
            description=(
                "Sua tarefa é agir como o editor final. Você recebeu um resumo inicial de um documento e as transcrições de dois debates sobre ele. "
                "Seu trabalho é sintetizar todo esse material em um relatório final, coeso e bem-estruturado. "
                "Comece com o resumo, depois integre os principais pontos, críticas e conclusões levantadas nos debates. "
                "Organize o texto com títulos e subtítulos claros. A linguagem deve ser formal e técnica."
            ),
            expected_output=(
                "Um relatório final completo e bem-formatado em português, com uma introdução (baseada no resumo), "
                "uma seção de 'Análise Multidisciplinar' (baseada nos debates) e uma seção de 'Conclusões'."
            ),
            agent=agent,
            context=context_tasks_list
        )