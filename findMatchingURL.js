// Keyword URL Mapping
const keywordUrlMap = {
    'ab, a/b, a-b, ab., test, tests, testing, ab-test, ab-testing, a/b-testing, ab-tests, split, multivariate, hotjar, heatmaps, suite, api, api-based, api-base, aws, marketo, hubspot, clearbit, trigger, triggers, event, events, compare, comparing, experiment, experiments, experimentation, variable, variables, control, variation, variations, statistic, statistics, statistical, result, results, hypothesis, hypotheses, inference, adobe, vwo, monetate, tasty, mobile': 
        'https://www.brillmark.com/hire-ab-test-developer/',
    
    'ecommerce, e-commerce, ecom, e-com, shop, shopping, shopify, shopify-plus, shopify plus, store, stores, theme, themes, facebook shop, amazon, buy button, custom, liquid, admin, pos, point of sale, klaviyo, mailchimp, amp, metafield, metafields, nitro, wishlist, omni, omnisend, email marketing, product reviews, sms, html, css, campaign, campaigns, partner, partners, code, coding, merchant, listings, SEO': 
        'https://www.brillmark.com/hire-shopify-developer/',
    
    'wp, wordpress, word press, landing, builder, divi, elementor, avada, wpbakery, wp bakery, beaver, fusion, plugin, plugins, customize, customization, form7, form 7, forms, newsletter, newsletters, gravity, constant, slider, sliders, soliloquy, pop-up, icegram, updater, blog, blogs, woocommerce, woo commerce, accordions, accordions, ad, ads, creative, creatives, unbounce': 
        'https://www.brillmark.com/wordpress-development-services/',
    
    'ga, ga4, google, analytic, analytics, tag, tags, audit, studio, manager, looker, universal, migration, ua, monitor, cross-device, parameter, parameters': 
        'https://www.brillmark.com/ga4-service/',
    
    'google optimize, optimize360, optimize 360, optimize, split-url, split url, funnel, segment, segments': 
        'https://www.brillmark.com/hire-google-optimize-developer/',
    
    'optimizely, widerfunnel, wider funnel, single page, react, angular, angular, react.js, angular.js, spa': 
        'https://www.brillmark.com/hire-optimizely-developer/',
    
    'java script, javascript, js, dmp, profiling, database, js-enabled, js enabled, geo, geo-targeting, flicker, flickering': 
        'https://www.brillmark.com/convert-test-developers/',
    
    'cro, agency, conversion, personalize, personalization, website, site, redesign, ui, ux, ui/ux, user interface, user experience, qa, quality, assurance, in-house, in house, graphic, graphics, design, designs, designer, designers, full stack, full-stack, frontend, front-end, backend, back-end, mockup, mockups, mock up, launch': 
        'https://www.brillmark.com/services/'
};

// Enhanced Keyword Matching Function
function findMatchingURL(query, keywordUrlMap) {
    // Convert the query to lowercase and split into words
    const queryWords = query.toLowerCase().split(/\W+/).filter(word => word.length > 0);
    
    // Iterate through the keyword-URL map
    for (const [keywords, url] of Object.entries(keywordUrlMap)) {
        // Convert keywords to an array and lowercase
        const keywordList = keywords.split(',').map(k => k.trim().toLowerCase());
        
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

// Test Queries
const testQueries = [
    // A/B Testing Related
    'I want to run AB tests on my website',
    'Need help with multivariate testing',
    'Looking for experiment tracking tools',
    'How to compare website variations',
    
    // Shopify Specific
    'Building an ecommerce store with Shopify',
    'Customize Shopify theme for my online shop',
    'Need help with Shopify POS system',
    'Implement buy button for Facebook shop',
    
    // WordPress Development
    'Create a WordPress landing page',
    'Install and customize Elementor plugin',
    'Looking for WooCommerce developer',
    'Need help with WordPress newsletter forms',
    
    // Google Analytics
    'Migrate from UA to GA4',
    'Set up cross-device tracking',
    'Google Analytics audit needed',
    
    // Optimization Platforms
    'Implement Google Optimize on my site',
    'Single page application A/B testing',
    'Need Optimizely developer for React app',
    
    // JavaScript and Technical
    'Improve website JavaScript performance',
    'Geo-targeting implementation',
    'Prevent page flickering during tests',
    
    // Conversion Rate Optimization
    'Redesign website for better conversion',
    'Need UX/UI improvement for my site',
    'Full-stack design and launch services',
    
    // Corner Cases
    'I want to test my website', // Multiple category matches possible
    'simple shop', // Short, generic words
    'js testing', // Partial word matches
    'conversions for ecommerce', // Multiple word partial matches
    'wordpress shop', // Combination of keywords
    
    // Negative/No Match Cases
    'Random query with no keywords',
    'Help me with something unrelated',
    'General consultation'
];

// Function to demonstrate query matching
function demonstrateQueryMatching() {
    console.log("=== Keyword URL Matching Demonstration ===");
    testQueries.forEach(query => {
        const matchedURL = findMatchingURL(query, keywordUrlMap);
        console.log(`Query: "${query}"`);
        console.log(`Matched URL: ${matchedURL || 'No match found'}\n`);
    });
}

// Run the demonstration
demonstrateQueryMatching();