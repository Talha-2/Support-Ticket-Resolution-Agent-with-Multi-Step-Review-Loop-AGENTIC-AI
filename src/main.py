from langgraph.graph import StateGraph, END
from StateGraph.nodes import input_node, classify_node, retrieve_node, draft_node, review_node,construct_workflow
from typing import Dict 
import csv
import json
from StateGraph.ticket_state import TicketState
from StateGraph import retry


graph = construct_workflow()

def run_agent(ticket: Dict[str, str]):
    initial_state = TicketState(
        ticket=ticket,
        category="",
        context=[],
        draft="",
        review_feedback="",
        retry_count=0,
        final_response=None
    )
    result = graph.invoke(initial_state, config={"thread_id": "ticket-001", "recursion_limit": 50})
    return result


if __name__ == "__main__":
   
    with open("escalation_log.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Subject", "Description", "Category", "Draft", "Feedback"])

    test_ticket = {
    "subject": "Unauthorized login attempt",
    "description": "I received an alert about a login attempt from an unknown device in another country."
}


    result = run_agent(test_ticket)
    print("Final State:", json.dumps(result, indent=2))
    if result["final_response"]:
        print("Final Response:", result["final_response"])
    else:
        print("Escalated to human review. Check escalation_log.csv")