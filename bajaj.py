import requests

access_token = "eyJhbGciOiJIUzI1NiJ9.eyJyZWdObyI6IjA4MjdJVDIyMTA2NyIsIm5hbWUiOiJpc2hhbiBqYWluIiwiZW1haWwiOiJpc2hhbmphaW4yMjA4MDhAYWNyb3BvbGlzLmluIiwic3ViIjoid2ViaG9vay11c2VyIiwiaWF0IjoxNzQ2OTYzMDI3LCJleHAiOjE3NDY5NjM5Mjd9.Cup_Xaji8Iuxq9ZeME_MMQdoRi42RZEORQD2T4pAcds "
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