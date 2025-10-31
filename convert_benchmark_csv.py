import os
import csv
import asyncio
from runloop_api_client import AsyncRunloop

client = AsyncRunloop(bearer_token=os.environ.get("RUNLOOP_PROD_IPSITA_KEY"))

async def export_benchmark_to_csv(benchmark_id, output_file):
    # Get benchmark details
    benchmark = await client.benchmarks.retrieve(benchmark_id)
    
    # Open CSV file
    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['scenario_id', 'name', 'problem_statement', 'reference_output'])
        
        # Iterate through scenarios
        for scenario_id in benchmark.scenario_ids:
            scenario = await client.scenarios.retrieve(scenario_id)
            writer.writerow([
                scenario.id,
                scenario.name,
                scenario.input_context.problem_statement,
                scenario.reference_output
            ])
    
    print(f"Exported {len(benchmark.scenario_ids)} scenarios to {output_file}")

# Usage
asyncio.run(export_benchmark_to_csv("bmd_2zmp3Mu3LhWu7yDVIfq3m", "swebench_scenarios.csv"))