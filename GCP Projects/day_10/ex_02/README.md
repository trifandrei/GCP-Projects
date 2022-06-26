Synchronous vs Asynchronous messaging?

Synchronous messaging involves a client that waits for the server to respond to a message. Messages are able to flow in both directions, to and from. Essentially it means that synchronous messaging is a two way communication. i.e. Sender sends a message to receiver and receiver receives this message and gives reply to the sender. Sender will not send another message until it gets a reply from receiver.
Asynchronous messaging involves a client that does not wait for a message from the server. An event is used to trigger a message from a server. So even if the client is down, the messaging will complete successfully. Asynchronous Messaging means that, it is a one way communication and the flow of communication is one way only.
