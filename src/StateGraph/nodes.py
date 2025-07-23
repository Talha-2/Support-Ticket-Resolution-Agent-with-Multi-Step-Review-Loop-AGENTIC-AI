from src.StateGraph.ticket_state  import TicketState
from src.StateGraph.nodes_def import classify_ticket, retrieve_context, generate_draft, review_draft 
from src.StateGraph import retry
from langgraph.graph import StateGraph, END

def construct_workflow():
    workflow = StateGraph(TicketState)

    workflow.add_node("input", input_node)
    workflow.add_node("classify", classify_node)
    workflow.add_node("retrieve", retrieve_node)
    workflow.add_node("draft", draft_node)
    workflow.add_node("review", review_node)

    workflow.set_entry_point("input")
    workflow.add_edge("input", "classify")
    workflow.add_edge("classify", "retrieve")
    workflow.add_edge("retrieve", "draft")
    workflow.add_edge("draft", "review")
    workflow.add_conditional_edges("review", retry.retry_or_escalate, {"retrieve": "retrieve", "end": END})

    return workflow.compile()

def input_node(state: TicketState) -> TicketState:
    print("Input State:", state)
    return state

def classify_node(state: TicketState) -> TicketState:

    state["category"] = classify_ticket(state["ticket"])
    print("State at classification node ", state)
    return state

def retrieve_node(state: TicketState) -> TicketState:
    state["context"] = retrieve_context(state["category"], state["ticket"], state.get("review_feedback", ""))
    print("State at retrieve node:", state)
    return state

def draft_node(state: TicketState) -> TicketState:
    state["draft"] = generate_draft(state["ticket"], state["context"])
    print("State at draft node:", state)
    return state

def review_node(state: TicketState) -> TicketState:
    review = review_draft(state["draft"], state["ticket"])
    state["review_feedback"] = review["feedback"]

    if review["pass"]:
        state["final_response"] = state["draft"]

    print("State at review node:", state)
    return state