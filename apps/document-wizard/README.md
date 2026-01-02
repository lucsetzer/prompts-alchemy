# 🧙‍♂️ AI Wizard Suite

A suite of AI-powered tools for content creators and document analysis.

## 🎯 Features

### 1. **Hook Wizard** (Port 8000)
- Generates viral video hooks for YouTube, TikTok, Instagram
- Creates 3 hook options with psychology explanations
- Provides visual tips for each hook

### 2. **Video Wizard** (Port 8001) 
- Analyzes and optimizes video structure
- Provides platform-specific recommendations
- Scores video optimization (1-10)
- Covers hooks, retention, SEO, engagement

### 3. **Document Wizard** (Port 8002)
- Translates complex documents into plain English
- Analyzes legal, medical, technical documents
- Highlights tricky language and red flags
- Provides rights vs responsibilities breakdown

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/yourusername/ai-wizard-suite.git
cd ai-wizard-suite

# Run Hook Wizard
cd hook_wizard
pip install -r requirements.txt
python app.py
# Open http://localhost:8000

# Run Video Wizard (in new terminal)
cd ../video_wizard
pip install -r requirements.txt  
python app.py
# Open http://localhost:8001

# Run Document Wizard (in new terminal)
cd ../document_wizard
pip install -r requirements.txt
python app.py
# Open http://localhost:8002
