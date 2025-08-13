# Em main.py

from crewai import Crew
from utils.pdf_utils import extrair_texto_pdf 
from crew import summary_crew 

if __name__ == "__main__":
    pdf_file = 'pdf.pdf'

    print(f"📄 Etapa 1: Extraindo texto de '{pdf_file}'...")
    try:
        texto_extraido = extrair_texto_pdf(pdf_file)
        print(f"✅ Texto extraído com sucesso ({len(texto_extraido)} caracteres).")
    except Exception as e:
        print(f"❌ Erro fatal ao extrair texto: {e}")
        exit()

    print("\n🚀 Etapa 2: Iniciando pipeline de resumo com CrewAI...")
    
    inputs = {
        'document_content': texto_extraido
    }

    summary_result = summary_crew.kickoff(inputs=inputs)
    
    print("\n\n✅ PROCESSO FINALIZADO ✅")
    
    output_filename = "relatorio_final.txt" 
    try:
        with open(output_filename, 'w', encoding='utf-8') as f:
            f.write(str(summary_result))
            
        print("======================================================")
        print(f"📄 Relatório final salvo com sucesso no arquivo: {output_filename}")
        print("======================================================")
    except Exception as e:
        print(f"❌ Erro ao salvar o relatório no arquivo: {e}")
        print("\n--- Conteúdo do Relatório ---\n")
        print(summary_result)