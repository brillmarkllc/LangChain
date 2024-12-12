# Unknown keywords, show contact page
UNKNOWN_KEYWORDS = {
    "blockchain": "https://www.brillmark.com/contact-us/",
    "crypto": "https://www.brillmark.com/contact-us/",
    "cybersecurity": "https://www.brillmark.com/contact-us/"
}

# Static mapping of keywords to URLs
KEYWORD_URL_MAPPING = {
    # "brillmark": "https://www.brillmark.com",
    "about us": "https://www.brillmark.com/about-us/",
    "services": "https://www.brillmark.com/services/",
    "a/b test": "https://www.brillmark.com/hire-ab-test-developer/",
    "shopify": "https://www.brillmark.com/hire-shopify-developer/",
    "wordpress": "https://www.brillmark.com/wordpress-development-services/"
}

def render_buttons(query):
    """Match keywords in the query to static URLs with prioritization."""
    # Check for unknown keywords first
    for keyword, url in UNKNOWN_KEYWORDS.items():
        if keyword.lower() in query.lower():
            print("\n\nConnect with us:")
            url = "https://www.brillmark.com/contact-us"
            print(f"<button>{url}</button>\n") 
            return [url] # Return immediately if a priority keyword is matched

    # Fallback to the default keyword-url mapping
    matched_sources = []
    for keyword, url in KEYWORD_URL_MAPPING.items():
        if keyword.lower() in query.lower():
            matched_sources.append(url)

    if matched_sources:
        print("\n\nConnect with us:")
        for source in matched_sources:
            print(f"<button>{source}</button>\n")
    return matched_sources
    