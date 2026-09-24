class Ticket:
    def __init__(self, incident_id, bot, description):
        self.incident_id = incident_id
        self.bot = bot
        self.description = description
        self.next = None
 
 
class TicketManager:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
 
    def find(self, incident_id):
        current = self.head
        while current:
            if current.incident_id.upper() == incident_id.upper():
                return current
            current = current.next
        return None
 
    def add_ticket(self, incident_id, bot, description):
        if self.find(incident_id):
            print("Ticket already exists.")
            return
        node = Ticket(incident_id, bot, description)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.count += 1
        print("Ticket added.")
 
    def display_tickets(self):
        if self.head is None:
            print("No active tickets.")
            return
        print(f"{'No.':<5}{'Incident ID':<14}{'Bot':<18}Short Description")
        current, n = self.head, 1
        while current:
            print(f"{n:<5}{current.incident_id:<14}{current.bot:<18}{current.description}")
            current, n = current.next, n + 1
 
    def search(self, query):
        exact = self.find(query)
        if exact:
            return [exact]
        results, q, current = [], query.lower(), self.head
        while current:
            if q in current.incident_id.lower() or q in current.bot.lower() or q in current.description.lower():
                results.append(current)
            current = current.next
        return results
 
    def remove_ticket(self, incident_id):
        current, previous = self.head, None
        while current:
            if current.incident_id.upper() == incident_id.upper():
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                if current is self.tail:
                    self.tail = previous
                self.count -= 1
                print("Ticket removed.")
                return
            previous, current = current, current.next
        print("Ticket not found.")
 
 
manager = TicketManager()
 
while True:
    print("\n1. Add ticket")
    print("2. Display tickets")
    print("3. Search ticket")
    print("4. Remove ticket")
    print("5. Total tickets")
    print("0. Exit")
    choice = input("Choice: ").strip()
 
    if choice == "1":
        while True:
            incident_id = input("Incident ID (or 'done'): ").strip()
            if incident_id.lower() == "done":
                break
            if not incident_id:
                continue
            bot = input("Bot: ").strip()
            desc = input("Short Description: ").strip()
            if bot and desc:
                manager.add_ticket(incident_id, bot, desc)
    elif choice == "2":
        manager.display_tickets()
    elif choice == "3":
        query = input("Search: ").strip()
        results = manager.search(query) if query else []
        if results:
            for t in results:
                print(t.incident_id, t.bot, t.description)
        else:
            print("No match found.")
    elif choice == "4":
        while True:
            incident_id = input("Incident ID to remove (or 'done'): ").strip()
            if incident_id.lower() == "done":
                break
            if incident_id:
                manager.remove_ticket(incident_id)
    elif choice == "5":
        print(manager.count)
    elif choice == "0":
        break
    else:
        print("Invalid choice.")
