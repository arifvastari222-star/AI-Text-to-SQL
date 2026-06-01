def validate_sql(sql):

    sql_upper = sql.upper()

    if ";" in sql:
        raise ValueError("Multiple SQL statements are not allowed.")

    forbidden = [
        "DROP",
        "DELETE",
        "UPDATE",
        "INSERT",
        "ALTER",
        "TRUNCATE"
    ]

    for keyword in forbidden:
        if keyword in sql_upper:
            raise ValueError(
                f"Forbidden SQL operation detected: {keyword}"
            )

    if not sql_upper.strip().startswith("SELECT"):
        raise ValueError(
            "Only SELECT queries are allowed."
        )

    return True