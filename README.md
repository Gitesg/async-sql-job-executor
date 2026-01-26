# async-sql-job-executor

An asynchronous SQL query execution service that runs heavy SQL queries using background workers and controlled database connection pooling.

---

## Objective
To execute heavy and long-running SQL queries efficiently without blocking APIs or overloading the database.

---

## Problem
In many applications, generating reports for dashboards requires executing **heavy SQL queries**.  
These queries are often handled directly by the backend APIs, which leads to:

- Slow API responses for other users
- Increased latency and timeouts
- Degraded backend performance
- Exhaustion of database connections

As a result, the overall system becomes unstable under load.

---

## Approach
This project solves the problem by:
- Executing heavy SQL queries **asynchronously**
- Offloading query execution to **background workers**
- Using **strict database connection pooling** to limit concurrent access
- Returning job IDs immediately instead of blocking API requests
- Allowing users to fetch results once execution is complete


