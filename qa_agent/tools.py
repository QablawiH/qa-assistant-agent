def get_security_and_edge_cases(feature_category: str) -> dict:
    """Retrieves mandatory security checks and edge cases based on the software feature category.

    Args:
        feature_category: The category of the feature being tested (e.g., 'auth', 'input_form', 'api', 'payment', or 'general').

    Returns:
        A dictionary containing security checks and boundary edge cases for QA testing.
    """
    category = feature_category.lower().strip()

    checklists = {
        "auth": {
            "security_checks": [
                "Brute-force rate limiting after 5 failed attempts",
                "SQL Injection and NoSQL Injection in username/email fields",
                "Session token expiration and invalidation on logout",
                "Password masking and secure transmission (HTTPS only)"
            ],
            "edge_cases": [
                "Leading/trailing whitespaces in email or password",
                "Case sensitivity check on email vs password",
                "Simultaneous login from multiple devices"
            ]
        },
        "input_form": {
            "security_checks": [
                "Cross-Site Scripting (XSS) payloads in text fields",
                "HTML tag injection and script sanitization"
            ],
            "edge_cases": [
                "Empty submission and whitespace-only strings",
                "Boundary Value Analysis: min-1, min, max, max+1 character lengths",
                "Unicode characters, emojis, and RTL/LTR mixed text"
            ]
        },
        "api": {
            "security_checks": [
                "Missing or expired Authorization Bearer token (401 Unauthorized)",
                "Accessing another user's resource ID (IDOR / 403 Forbidden)",
                "Rate limiting / throttling under burst traffic (429 Too Many Requests)"
            ],
            "edge_cases": [
                "Malformed JSON payload or wrong Content-Type header (400/415)",
                "Missing required fields or unexpected data types",
                "Large payload stress test"
            ]
        },
        "payment": {
            "security_checks": [
                "Replay attack prevention (idempotency key validation)",
                "Price/amount tampering in client request payload"
            ],
            "edge_cases": [
                "Zero or negative transaction amounts",
                "Network timeout during payment gateway callback",
                "Double-click on Pay button (duplicate charge prevention)"
            ]
        }
    }

    default_checklist = {
        "security_checks": [
            "Input sanitization against injection attacks",
            "Proper error handling without exposing stack traces"
        ],
        "edge_cases": [
            "Null, empty, and extreme boundary values",
            "Concurrent user actions and network interruption"
        ]
    }

    selected = checklists.get(category, default_checklist)
    return {
        "category_matched": category,
        "mandatory_checks": selected
    }