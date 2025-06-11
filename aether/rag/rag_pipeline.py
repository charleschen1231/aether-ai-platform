# aether/rag/rag_pipeline.py
class RAGPipeline:
    def __init__(self, retriever, generator):
        self.retriever = retriever
        self.generator = generator

    def run(self, query):
        docs = self.retriever.retrieve(query)
        response = self.generator.generate(docs, query)
        return response
