from query_executor import execute_query

query = """
SELECT
    customer_state,
    COUNT(*) AS total_customers
FROM customers
GROUP BY customer_state
ORDER BY total_customers DESC;
"""

df = execute_query(query)

print(df.head())