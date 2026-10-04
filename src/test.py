import requests
import os

passedTests = 0
amountOfTests = 3
def getRequestText(ending):
    return requests.get(f"http://127.0.0.1:{os.environ.get("PORT", "8080")}{ending}").text
    

if getRequestText("/") == "notes service":
    passedTests += 1
if getRequestText("/healthz") == "ok":
    passedTests += 1
if getRequestText("/notes") == "3":
    passedTests += 1

print(f"TESTS: {passedTests}/{amountOfTests}")
