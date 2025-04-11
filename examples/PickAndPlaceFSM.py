class PickAndPlaceFSM:
    def __init__(self):
        self.state = "Idle"

    def on_event(self, event):
        if self.state == "Idle":
            if event == "start":
                self.state = "Pick"
                print("Starting operation: Picking object.")

        elif self.state == "Pick":
            if event == "picked":
                self.state = "Move"
                print("Object picked: Moving to place position.")

        elif self.state == "Move":
            if event == "arrived":
                self.state = "Place"
                print("Arrived at place location: Placing object.")

        elif self.state == "Place":
            if event == "placed":
                self.state = "Return"
                print("Object placed: Returning to start.")

        elif self.state == "Return":
            if event == "returned":
                self.state = "Idle"
                print("Returned to start: Ready for next task.")

    def current_state(self):
        return self.state

# Example usage
fsm = PickAndPlaceFSM()
events = ["start", "picked", "arrived", "placed", "returned"]

for event in events:
    fsm.on_event(event)
    print("Current State:", fsm.current_state())
