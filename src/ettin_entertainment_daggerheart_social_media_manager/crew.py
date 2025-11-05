import os

from crewai import LLM
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import (
	SerperDevTool,
	ScrapeWebsiteTool
)





@CrewBase
class EttinEntertainmentDaggerheartSocialMediaManagerCrew:
    """EttinEntertainmentDaggerheartSocialMediaManager crew"""

    
    @agent
    def social_media_content_strategist(self) -> Agent:
        
        return Agent(
            config=self.agents_config["social_media_content_strategist"],
            
            
            tools=[				SerperDevTool()],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            max_execution_time=None,
            llm=LLM(
                model="gpt-4o-mini",
                temperature=0.7,
            ),
            
        )
    
    @agent
    def community_engagement_manager(self) -> Agent:
        
        return Agent(
            config=self.agents_config["community_engagement_manager"],
            
            
            tools=[				ScrapeWebsiteTool()],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            max_execution_time=None,
            llm=LLM(
                model="gpt-4o-mini",
                temperature=0.7,
            ),
            
        )
    
    @agent
    def social_media_analytics_specialist(self) -> Agent:
        
        return Agent(
            config=self.agents_config["social_media_analytics_specialist"],
            
            
            tools=[				SerperDevTool()],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            max_execution_time=None,
            llm=LLM(
                model="gpt-4o-mini",
                temperature=0.7,
            ),
            
        )
    
    @agent
    def content_scheduler_and_publisher(self) -> Agent:
        
        return Agent(
            config=self.agents_config["content_scheduler_and_publisher"],
            
            
            tools=[				SerperDevTool()],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            max_execution_time=None,
            llm=LLM(
                model="gpt-4o-mini",
                temperature=0.7,
            ),
            
        )
    
    @agent
    def critical_role_competitive_intelligence_analyst(self) -> Agent:
        
        return Agent(
            config=self.agents_config["critical_role_competitive_intelligence_analyst"],
            
            
            tools=[				SerperDevTool(),
				ScrapeWebsiteTool()],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            max_execution_time=None,
            llm=LLM(
                model="gpt-4o-mini",
                temperature=0.7,
            ),
            
        )
    

    
    @task
    def research_trending_daggerheart_topics(self) -> Task:
        return Task(
            config=self.tasks_config["research_trending_daggerheart_topics"],
            markdown=False,
            
            
        )
    
    @task
    def analyze_optimal_posting_times_and_engagement_patterns(self) -> Task:
        return Task(
            config=self.tasks_config["analyze_optimal_posting_times_and_engagement_patterns"],
            markdown=False,
            
            
        )
    
    @task
    def research_critical_role_and_darrington_press_release_schedule(self) -> Task:
        return Task(
            config=self.tasks_config["research_critical_role_and_darrington_press_release_schedule"],
            markdown=False,
            
            
        )
    
    @task
    def create_community_engagement_strategy(self) -> Task:
        return Task(
            config=self.tasks_config["create_community_engagement_strategy"],
            markdown=False,
            
            
        )
    
    @task
    def develop_strategic_release_timing_plan(self) -> Task:
        return Task(
            config=self.tasks_config["develop_strategic_release_timing_plan"],
            markdown=False,
            
            
        )
    
    @task
    def generate_content_ideas_and_posts(self) -> Task:
        return Task(
            config=self.tasks_config["generate_content_ideas_and_posts"],
            markdown=False,
            
            
        )
    
    @task
    def develop_optimized_posting_schedule(self) -> Task:
        return Task(
            config=self.tasks_config["develop_optimized_posting_schedule"],
            markdown=False,
            
            
        )
    
    @task
    def create_social_media_management_action_plan(self) -> Task:
        return Task(
            config=self.tasks_config["create_social_media_management_action_plan"],
            markdown=False,
            
            
        )
    

    @crew
    def crew(self) -> Crew:
        """Creates the EttinEntertainmentDaggerheartSocialMediaManager crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )

    def _load_response_format(self, name):
        with open(os.path.join(self.base_directory, "config", f"{name}.json")) as f:
            json_schema = json.loads(f.read())

        return SchemaConverter.build(json_schema)
