# aether/workflow/nodes/agent_node.py
class AgentNode:
    def __init__(self, agent):
        self.agent = agent

    def execute(self, context):
        return self.agent.run(context["input"])
