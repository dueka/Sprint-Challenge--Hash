#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    cache = {}
    route = [None] * length
    """
    YOUR CODE HERE
    """
    for ticket in tickets:
        cache.update(ticket.source, ticket.destination)
    first_ticket = cache.get('None')
    route[0] = first_ticket

    for i in range(1, len(route)):
        prev_ticket = route[i - 1]
        prev_ticket_key = cache.get(prev_ticket)
        route[i] = prev_ticket_key
    return route
