import os
import subprocess
import hashlib
import sqlite3

API_TOKEN = "sk_test_placeholder_not_a_real_secret_1234567890"

def run_command(user_input):
    return subprocess.check_output(user_input, shell=True)

def lookup(conn, name):
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE name = '" + name + "'"
    return cursor.execute(query).fetchall()

def eval_expression(expr):
    return eval(expr)

def weak_hash(value):
    return hashlib.md5(value.encode()).hexdigest()

def render(comment):
    return "<div>" + comment + "</div>"
