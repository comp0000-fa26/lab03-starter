"""A minimal MCP server exposing one tool: lookup_student_record."""

import csv
from pathlib import Path

from mcp.server.fastmcp import FastMCP

# TODO
# Write a reference path that the server can works well from any working directory
# Avoid to hardcoded the absolute path of the students.csv
CSV_PATH = "reference_for_students.csv"

mcp = FastMCP("student-records")


@mcp.tool()
def lookup_student_record(student_id: str) -> dict:
    """Look up a student record by ID.

    Returns a dict with id, name, programme, and year. Returns an error
    field if the student is not found.
    """
    # TODO: Implement the student record lookup logic.
    # Open the CSV file, loop through rows using csv.DictReader,
    # and return the matching row or an error dict if not found.
    pass


if __name__ == "__main__":
    mcp.run()    # stdio transport by default