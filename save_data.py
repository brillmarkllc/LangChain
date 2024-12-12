def save_to_file(query, response, sources, filename="chat_history.txt"):
    """Save query, response, and sources to a file in real-time."""
    with open(filename, "a") as file:
        file.write(f"Query: {query}\n")
        file.write(f"Response: {response}\n")
        file.write(f"Sources: {', '.join(sources)}\n")
        file.write("\n")  # Newline between different sessions