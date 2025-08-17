from crewai import Task
from agents.summarizer_agent import summarizer_agent
from openai import OpenAI
import math

class SummarizeTask(Task):
    # O __init__ volta a ser simples, sem argumentos
    def __init__(self):
        super().__init__(
            description=(
                "Analisar o seguinte texto, que foi extraído de um documento, "
                "e gerar um resumo conciso e bem estruturado. Texto: {document_content}"
            ),
            expected_output="Um resumo textual coeso do documento de entrada.",
            agent=summarizer_agent,
        )

    # O método run agora pega o texto do dicionário de contexto
    def run(self, context: dict):
        # O 'context' aqui é o dicionário `inputs` que passamos no kickoff
        document_text = context['document_content']

        if not document_text or not document_text.strip():
            print("⚠️ Texto de entrada está vazio.")
            return "O texto de entrada estava vazio."

        client = OpenAI(api_key="ollama", base_url="http://localhost:11434/v1")
        
        chunk_size = 4000
        chunks = [document_text[i:i + chunk_size] for i in range(0, len(document_text), chunk_size)]
        
        # ... O resto do seu código de chunking continua exatamente o mesmo daqui para baixo ...
        print(f"🤖 Texto muito longo. Dividindo em {len(chunks)} pedaços para resumir...")
        
        partial_summaries = []
        for i, chunk in enumerate(chunks):
            print(f"📄 Resumindo pedaço {i + 1}/{len(chunks)}...")
            try:
                messages = [
                    {"role": "system", "content": "Você é um especialista em sumarizar partes de um documento. Sua tarefa é criar um resumo conciso do texto a seguir, focando nos pontos principais. Este é um pedaço de um documento maior."},
                    {"role": "user", "content": f"Por favor, resuma o seguinte trecho:\n\n{chunk}"}
                ]
                
                resposta = client.chat.completions.create(
                    model="ollama/llama3.1:8b", 
                    messages=messages,
                    temperature=0.0,
                )
                summary_part = resposta.choices[0].message.content
                partial_summaries.append(summary_part)
                
            except Exception as e:
                print(f"⚠️ Erro ao resumir o pedaço {i + 1}: {e}")
                partial_summaries.append(f"[Erro ao processar o pedaço {i+1}]")

        print("✅ Todos os pedaços foram resumidos. Criando o resumo final...")
        
        final_summary_text = "\n\n".join(partial_summaries)
        
        if len(final_summary_text) > chunk_size:
             print("📄 O conjunto de resumos ainda é grande, criando um resumo final consolidado...")
             messages = [
                {"role": "system", "content": "Você é um especialista em consolidar informações. A seguir estão vários resumos parciais de um mesmo documento. Sua tarefa é criar um único resumo final coeso e bem estruturado a partir deles."},
                {"role": "user", "content": f"Por favor, crie um resumo final a partir dos seguintes pontos:\n\n{final_summary_text}"}
            ]
             resposta_final = client.chat.completions.create(
                    model="ollama/llama3.1:8b", 
                    messages=messages,
                    temperature=0.2,
                )
             final_summary = resposta_final.choices[0].message.content
        else:
            final_summary = final_summary_text

        print("✅ Resumo final gerado com sucesso.")
        return final_summary