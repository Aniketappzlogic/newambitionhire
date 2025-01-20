def handle_response(response):
    """Handles API response and extracts relevant information."""
    try:
        data = response.json()
        print("Response Data:", data)
        return data
    except ValueError:
        raise Exception(f"Failed to parse JSON. Response: {response.text}")
