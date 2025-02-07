# Number Classification API

## Overview
The Number Classification API is a web service that takes a number and returns interesting mathematical properties about it, along with a fun fact. This project is implemented using Flask and deployed on Render.

## Technology Stack
- **Language**: Python
- **Framework**: Flask
- **Deployment Platform**: Render

## Features
- Accepts GET requests with a number parameter.
- Returns JSON responses in the specified format.
- Handles CORS (Cross-Origin Resource Sharing).
- Provides mathematical properties and a fun fact for the given number.

## API Specification

### Endpoint: 
GET `<your-domain.com>/api/classify-number?number=<number>`

### Query Parameter:
- `number`: The number to classify (can be positive or negative).

### Response Formats:
#### 200 OK:
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
