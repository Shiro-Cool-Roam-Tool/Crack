import os, sys
try:
    __import__("cyon").menu_apikey()
except Exception as e:
    exit(str(e))
