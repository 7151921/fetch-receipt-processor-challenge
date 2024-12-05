# Simple Receipt Processor

### Language
This is written in Python, as this has been my primary language for last few years, 
but excited to potentially learn Go! Been mainly surrounded around Java/Python/TypeScript

### How to Run
```
docker build -t fetch-rewards . && docker run -p 8000:8000 fetch-rewards
```

### Guidelines Followed
https://github.com/fetch-rewards/receipt-processor-challenge/blob/main/README.md

### Testing 
Tested against all the datasets provided in Guidelines section as well as individual testing.
Other testing includes using PyTest to run my test. I wrote a small shell script to run the test before starting 
the container.

### FAQ

Q: Why am I adding this? 
```
@app.exception_handler(RequestValidationError)
```
A: With Pydantic the regex is applied as soon as it start mapping. This returns a 422, however the api.yml 
requires a 400, so this intercepts it and transforms it to a 400. 
