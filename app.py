# app.py - SINGLE APP FOR EVERYTHING
from fastapi import FastAPI, Request, Form, Query
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import os
import sys

app = FastAPI(title="Prompts Alchemy Suite")

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Setup templates
templates = Jinja2Templates(directory="templates")

# Import layout
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from layout import layout

# ---------- HOME PAGE -----------



# ---------- DOCUMENT WIZARD -----------


# ---------- HOOK WIZARD -----------


# ---------- PROMPTS WIZARD -----------


# ---------- THUMBNAIL WIZARD -----------


# ---------- VIDEO WIZARD -----------

