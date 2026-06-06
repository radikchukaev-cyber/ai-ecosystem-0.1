/**
 * Safe JSON Parser
 * 
 * A robust utility to parse JSON strings that might be malformed, truncated,
 * or contain trailing commas. Particularly useful for parsing LLM outputs.
 */

const SafeJsonParser = {
    /**
     * Attempts to parse a JSON string safely, applying various fix heuristics if standard parsing fails.
     * @param {string} input - The JSON string to parse
     * @param {any} fallback - The value to return if parsing fails completely
     * @returns {any} The parsed object or the fallback value
     */
    parse: function(input, fallback = null) {
        if (!input || typeof input !== 'string') return fallback;
        
        try {
            // First attempt: standard parse
            return JSON.parse(input);
        } catch (e) {
            // Parsing failed, try heuristics
            let cleaned = input.trim();
            
            // Fix trailing commas
            cleaned = cleaned.replace(/,\s*([\]}])/g, '$1');
            
            // Fix missing quotes around keys
            cleaned = cleaned.replace(/([{,]\s*)([a-zA-Z0-9_]+)\s*:/g, '$1"$2":');
            
            // Try extracting JSON from markdown code blocks
            const markdownMatch = cleaned.match(/```(?:json)?\s*([\s\S]*?)\s*```/);
            if (markdownMatch && markdownMatch[1]) {
                try {
                    return JSON.parse(markdownMatch[1].trim());
                } catch (e2) {
                    // Continue to fallback
                }
            }
            
            try {
                // Try parsing the cleaned version
                return JSON.parse(cleaned);
            } catch (finalError) {
                console.warn("SafeJsonParser: Could not parse input.", finalError.message);
                return fallback;
            }
        }
    }
};

module.exports = SafeJsonParser;

// Example usage
if (require.main === module) {
    const badJson = '{ "name": "AI Agent", "skills": ["coding", "writing",], }';
    console.log("Original:", badJson);
    console.log("Parsed:", SafeJsonParser.parse(badJson));
}
