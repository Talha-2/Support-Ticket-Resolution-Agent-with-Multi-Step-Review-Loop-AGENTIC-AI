from StateGraph.ticket_state import TicketState
import csv

def log_escalation(state):
    with open("escalation_log.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            state["ticket"]["subject"],
            state["ticket"]["description"],
            state["category"],
            state["draft"],
            state["review_feedback"]
        ])


def retry_or_escalate(state: TicketState) -> str:
    retry_count = state.get("retry_count", 0)
    print(f"Retry count: {retry_count}")  # Debugging
    if state.get("final_response"):
        print("Ending due to final response")
        return "end"
    if retry_count >= 2:
        print("Escalating to CSV log")
        log_escalation(state)
        return "end"
    state["retry_count"] = retry_count + 1
    print("Retrying, returning to retrieve")
    return "retrieve"

