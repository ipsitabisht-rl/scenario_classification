
import asyncio
import time
import os
import pandas as pd
import tiktoken
from openai import OpenAI
client = OpenAI()

from datetime import datetime
from runloop_api_client import AsyncRunloop
from utils.embeddings_utils import get_embedding

RUNLOOP_API_KEY = os.environ["RUNLOOP_PROD_IPSITA_KEY"]

client = AsyncRunloop(bearer_token=RUNLOOP_API_KEY)

def get_embedding(text, model="text-embedding-3-small"):
    text = text.replace("\n", " ")
    return client.embeddings.create(input = [text], model=model).data[0].embedding


async def main():
    benchmark_id = "bmd_2zu7uSdEwF8HQcTsvkqOQ"
    swe_bench = await client.benchmarks.retrieve(benchmark_id)
    swe_scenario_id= swe_bench.scenarioIds[0]

    scenario_view = client.scenarios.retrieve(
        swe_scenario_id,
    )
    problem_statement = scenario_view.input_context.problem_statement
    ref_solution = scenario_view.reference_output

    combined_context = problem_statement + ref_solution

    get_embedding(text = combined_context, model='text-embedding-3-small')






