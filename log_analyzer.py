import pandas as pd

# sample log data
logs = [
    "INFO User login",
    "ERROR Database failed",
    "INFO File uploaded",
    "WARNING Disk space low",
    "ERROR Network timeout",
    "INFO User logout",
    "ERROR Access denied",
    "WARNING Memory high"
]

df = pd.DataFrame(logs, columns=["Log"])

print("All logs:")
print(df)

# count error logs
error_logs = df[df["Log"].str.contains("ERROR")]

print("\nError logs:")
print(error_logs)

# count warning logs
warning_logs = df[df["Log"].str.contains("WARNING")]

print("\nWarning logs:")
print(warning_logs)

# count info logs
info_logs = df[df["Log"].str.contains("INFO")]

print("\nInfo logs:")
print(info_logs)

print("\nSummary")
print("Errors:", len(error_logs))
print("Warnings:", len(warning_logs))
print("Info:", len(info_logs))
