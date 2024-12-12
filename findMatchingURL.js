function findMatchingURL(query, keywordUrlMap) {
    // Convert the query to lowercase and split into words
    const queryWords = query.toLowerCase().split(/\W+/).filter(word => word.length > 0);
    
    // Iterate through the keyword-URL map
    for (const [keywords, url] of Object.entries(keywordUrlMap)) {
        // Convert keywords to an array and lowercase
        const keywordList = Array.isArray(keywords) 
            ? keywords 
            : keywords.split(',').map(k => k.trim().toLowerCase());
        
        // Check if any query word matches any keyword exactly
        const match = queryWords.some(queryWord => 
            keywordList.includes(queryWord)
        );
        
        // If a match is found, return the associated URL
        if (match) {
            return url;
        }
    }
    
    // Return null if no matching keywords are found
    return null;
}

// Example usage
const keywordUrlMap = {
    'cro, agency, conversion, personalize, personalization, website': 
        'https://www.brillmark.com/services/',
    'ab, a/b, a-b, ab., test, tests, testing, ab-test': 
        'https://www.brillmark.com/hire-ab-test-developer/',
    'ecommerce, e-commerce, ecom, e-com, shop': 
        'https://www.brillmark.com/hire-shopify-developer/'
};

// Example function to demonstrate usage in a chatbot context
function handleChatbotQuery(query) {
    return findMatchingURL(query, keywordUrlMap);
}

// Test cases
console.log(handleChatbotQuery('I want to improve my website conversion')); 
// Expected: https://www.brillmark.com/services/

console.log(handleChatbotQuery('Can you help me with ab testing?')); 
// Expected: https://www.brillmark.com/hire-ab-test-developer/

console.log(handleChatbotQuery('Looking for an ecommrce solution')); 
// Expected: https://www.brillmark.com/hire-shopify-developer/

console.log(handleChatbotQuery('Unrelated query')); 
// Expected: null