import requests


payload = {
    "name": "ishan jain",
    "regNo": "0827IT221067",  
    "email": "ishanjain220808@acropolis.in"
}

# Step 2: Generate webhook
response = requests.post("https://bfhldevapigw.healthrx.co.in/hiring/generateWebhook/PYTHON", json=payload)

if response.status_code == 200:
    data = response.json()
    webhook_url = data.get("webhook")
    access_token = data.get("accessToken")

    print("Webhook URL:", webhook_url)
    print("Access Token:", access_token)

    # Step 3: Your final SQL query
    final_sql = """
SELECT 
  p.AMOUNT AS SALARY,
  CONCAT(e.FIRST_NAME, ' ', e.LAST_NAME) AS NAME,
  FLOOR(DATEDIFF('2025-03-05', e.DOB) / 365) AS AGE,
  d.DEPARTMENT_NAME
FROM PAYMENTS p
JOIN EMPLOYEE e ON p.EMP_ID = e.EMP_ID
JOIN DEPARTMENT d ON e.DEPARTMENT = d.DEPARTMENT_ID
WHERE DAY(p.PAYMENT_TIME) != 1
ORDER BY p.AMOUNT DESC
LIMIT 1;
"""

    # Step 4: Send query to webhook
    headers = {
        "Authorization": access_token,
        "Content-Type": "application/json"
    }

    submit_payload = {
        "finalQuery": final_sql.strip()
    }

    submit_response = requests.post(webhook_url, headers=headers, json=submit_payload)

    if submit_response.status_code == 200:
        print("Successfully submitted the SQL query!")
    else:
        print("Submission failed:", submit_response.text)

else:
    print(" Webhook generation failed:", response.text)

    import requests

access_token = " eyJhbGciOiJIUzI1NiJ9.eyJyZWdObyI6IjA4MjdJVDIyMTA2NyIsIm5hbWUiOiJpc2hhbiBqYWluIiwiZW1haWwiOiJpc2hhbmphaW4yMjA4MDhAYWNyb3BvbGlzLmluIiwic3ViIjoid2ViaG9vay11c2VyIiwiaWF0IjoxNzQ2OTYyODIzLCJleHAiOjE3NDY5NjM3MjN9.Jal2MyFw1L126BnKkmO6NGhY6hVxQapjDhfNURkvMWY"
webhook_url ="https://bfhldevapigw.healthrx.co.in/hiring/testWebhook/PYTHON"

query = """
SELECT 
    E1.EMP_ID,
    E1.FIRST_NAME,
    E1.LAST_NAME,
    D.DEPARTMENT_NAME,
    COUNT(E2.EMP_ID) AS YOUNGER_EMPLOYEES_COUNT
FROM EMPLOYEE E1
JOIN DEPARTMENT D ON E1.DEPARTMENT = D.DEPARTMENT_ID
LEFT JOIN EMPLOYEE E2 
    ON E1.DEPARTMENT = E2.DEPARTMENT
    AND E2.DOB > E1.DOB
GROUP BY E1.EMP_ID, E1.FIRST_NAME, E1.LAST_NAME, D.DEPARTMENT_NAME
ORDER BY E1.EMP_ID DESC;
"""

headers = {
    "Authorization": access_token,
    "Content-Type": "application/json"
}

payload = {
    "Query": query.strip()
}

response = requests.post(webhook_url, headers=headers, json=payload)

print("Status Code:", response.status_code)
print("Response:", response.text)