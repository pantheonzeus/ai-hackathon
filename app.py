from llama_index.llms.openai import OpenAI
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.agent import ReActAgent

import importer_csv
import indexing
from prompts import klarna

# from dotenv import load_dotenv

# load_dotenv("./.env")

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

agent = ReActAgent.from_tools(query_engine_tools, llm=llm, verbose=True)

personas = importer_csv.get_rows()
persona = personas[1]

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


from llama_index.core.query_pipeline import QueryPipeline
from llama_index.core import PromptTemplate


prompt_tmpl_1 = PromptTemplate(
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
prompt_tmpl_2 = PromptTemplate(
    "Take this content {text} and do not change the content, tone of voice. Adapt it for this output channel : EMAIL"
)
llm_c = llm.as_query_component(streaming=True)
p = QueryPipeline(chain=[prompt_tmpl_1, llm_c, prompt_tmpl_2, llm_c], verbose=True)
output = p.run()
for o in output:
    print(o.delta, end="")


query_engine_tools
from llama_index.agent.openai import OpenAIAgent
from llama_index.core.tools import QueryPlanTool
from llama_index.core import get_response_synthesizer

response_synthesizer = get_response_synthesizer()


query_tool_klarna_customer_service = QueryEngineTool.from_defaults(
    query_engine=klarna_customer_segment_engine,
    name="klarna_faq",
    description=(
        f"Provides information about problems with Klarna services"
        f" Use a detailed plain text question as input to the tool."
    ),
)
query_tool_klarna_customer_segment = QueryEngineTool.from_defaults(
    query_engine=klarna_customer_segment_engine,
    name="klarna_customer_segments",
    description=(
        f"Provides information about the user and in which customer segment he or she belogns. This is important because of the reply."
        f" Use a detailed plain text question as input to the tool."
    ),
)
query_plan_tool = QueryPlanTool.from_defaults(
    query_engine_tools=[
        query_tool_klarna_customer_segment,
        query_tool_klarna_customer_service,
    ],
    response_synthesizer=response_synthesizer,
)

agent = OpenAIAgent.from_tools(
    [query_plan_tool],
    max_function_calls=10,
    llm=OpenAI(temperature=0, model="gpt-4-0613"),
    verbose=True,
)

response = agent.query(
    klarna.BASIC_CUSTOMER_PROMPT_PLANNER.format(
        persona[1],
        persona[3],
        persona[4],
    )
)

print(str(response))
