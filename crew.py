from crewai import Crew
from agents.summarizer_agent import summarizer_agent
from agents.debate_agents import preservationist_agent, sustainable_dev_agent, socio_economic_agent
from agents.writer_agent import writer_agent
from tasks.summarize_task import SummarizeTask
from tasks.analysis_tasks import AnalysisTasks


analysis_tasks = AnalysisTasks()

debate_team = [preservationist_agent, sustainable_dev_agent, socio_economic_agent]

summarize_task = SummarizeTask()

debate_task_1 = analysis_tasks.debate(
    agent_list=debate_team,
    context_task=summarize_task
)

debate_task_2 = analysis_tasks.debate(
    agent_list=debate_team,
    context_task=debate_task_1
)

write_task = analysis_tasks.write(
    agent=writer_agent,
    context_tasks_list=[summarize_task, debate_task_1, debate_task_2]
)

summary_crew = Crew(
    agents=[summarizer_agent, preservationist_agent, sustainable_dev_agent, socio_economic_agent, writer_agent],
    tasks=[summarize_task, debate_task_1, debate_task_2, write_task],
    verbose=True
)