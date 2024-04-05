from llama_index.llms.openai import OpenAI
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.agent import ReActAgent

import importer_csv
import indexing
from prompts import klarna

llm = OpenAI(model="gpt-3.5-turbo")
llm = OpenAI(model="gpt-4-1106-preview")

klarna_faq_index = indexing.indexing(
    ["https://www.klarna.com/us/customer-service/"], "./storage/klarna"
)
klarna_customer_segment_index = indexing.indexing(
    ["./data/klarna_customer_segments.csv"], "./storage/klarna_customer_segment"
)

klarna_faq_engine = klarna_faq_index.as_query_engine(similarity_top_k=3)
klarna_customer_segment_engine = klarna_customer_segment_index.as_query_engine(
    similarity_top_k=3
)

query_engine_tools = [
    QueryEngineTool(
        query_engine=klarna_faq_engine,
        metadata=ToolMetadata(
            name="klarna_faq",
            description=(
                "Provides information about problems with Klarna services"
                "Use a detailed plain text question as input to the tool."
            ),
        ),
    ),
    QueryEngineTool(
        query_engine=klarna_customer_segment_engine,
        metadata=ToolMetadata(
            name="klarna_customer_segments",
            description=(
                "Provides information about the user and in which customer segment he or she belogns. This is important because of the reply."
                "Use a detailed plain text question as input to the tool."
            ),
        ),
    ),
]

agent = ReActAgent.from_tools(
    query_engine_tools,
    llm=llm,
)

personas = importer_csv.get_rows()
persona = personas[10]

response = agent.chat(
    klarna.BASIC_CUSTOMER_PROMPT.format(
        persona[0],
        persona[1],
        persona[2],
        persona[3],
        persona[7],
        persona[5],
        persona[6],
    )
)
print(str(response))
