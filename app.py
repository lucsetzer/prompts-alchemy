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
app = FastAPI()



# Add this debug endpoint to see the full layout
@app.get("/debug-layout")
async def debug_layout():
    # Show what layout() produces with minimal content
    test_content = "<h1>Test</h1>"
    full_html = layout("Test", test_content)
    
    # Return first 2000 chars to see navbar
    return HTMLResponse(f"<pre>{full_html[:2000]}</pre>")



@app.get("/home")
async def home_page():
    content = '''
    <div style="max-width: 1200px; margin: 0 auto;">
        <!-- HERO SECTION -->
        <section style="text-align: center; padding: 4rem 0;">
            <div style="font-size: 5rem; color: var(--primary); margin-bottom: 1rem;">
                <i class="fas fa-flask"></i>
            </div>
            <h1 style="font-size: 3.5rem; color: var(--primary); margin-bottom: 1rem;">
                Prompts Alchemy
            </h1>
            <p style="font-size: 1.5rem; color: #374151; max-width: 800px; margin: 0 auto 2rem; font-weight: 500;">
                Transform your content creation with 5 specialized AI wizards
            </p>
            <div style="display: flex; gap: 1rem; justify-content: center; margin-top: 2rem;">
                <a href="#wizards" role="button" style="padding: 1rem 2.5rem; font-size: 1.2rem;">
                    <i class="fas fa-eye"></i> Explore Wizards
                </a>
                <a href="#pricing" role="button" class="secondary" style="padding: 1rem 2.5rem; font-size: 1.2rem;">
                    <i class="fas fa-crown"></i> View Pricing
                </a>
            </div>
        </section>

        <!-- PROBLEM SECTION -->
        <section style="background: #f9fafb; border-radius: 1rem; padding: 3rem; margin: 3rem 0;">
            <h2 style="text-align: center; color: var(--primary); margin-bottom: 2rem;">
                The Content Creation Struggle is Real
            </h2>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem;">
                <div style="text-align: center;">
                    <div style="font-size: 3rem; color: #ef4444; margin-bottom: 1rem;">
                        <i class="fas fa-clock"></i>
                    </div>
                    <h3 style="color: #374151;">Time-Consuming</h3>
                    <p style="color: #4b5563;">Hours spent on thumbnails, scripts, and prompts that don't convert</p>
                </div>
                <div style="text-align: center;">
                    <div style="font-size: 3rem; color: #ef4444; margin-bottom: 1rem;">
                        <i class="fas fa-question-circle"></i>
                    </div>
                    <h3 style="color: #374151;">Uncertain Results</h3>
                    <p style="color: #4b5563;">Not knowing if your content will perform until it's too late</p>
                </div>
                <div style="text-align: center;">
                    <div style="font-size: 3rem; color: #ef4444; margin-bottom: 1rem;">
                        <i class="fas fa-tools"></i>
                    </div>
                    <h3 style="color: #374151;">Tool Overload</h3>
                    <p style="color: #4b5563;">Jumping between 10+ different apps for each content type</p>
                </div>
            </div>
        </section>

        <!-- SOLUTION: 5 WIZARDS + MARKETPLACE -->
        <section id="wizards" style="padding: 3rem 0;">
            <h2 style="text-align: center; color: var(--primary); margin-bottom: 3rem;">
                One Suite, Five Specialized Wizards
            </h2>
            
            <!-- Creator Wizards -->
            <div style="margin-bottom: 4rem;">
                <h3 style="text-align: center; color: var(--primary); margin-bottom: 2rem;">
                    <i class="fas fa-magic"></i> Creator Wizards
                </h3>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem;">
                    <!-- Prompt Wizard -->
                    <div style="background: white; border-radius: 1rem; padding: 2rem; box-shadow: 0 4px 6px rgba(0,0,0,0.1); text-align: center;">
                        <div style="font-size: 2.5rem; color: var(--primary); margin-bottom: 1rem;">
                            <i class="fas fa-hat-wizard"></i>
                        </div>
                        <h4 style="color: #374151;">Prompt Wizard</h4>
                        <p style="color: #4b5563;">Create perfect AI prompts tailored to any platform</p>
                        <div style="margin-top: 1rem; padding: 0.5rem 1rem; background: #10b981; color: white; border-radius: 2rem; display: inline-block; font-weight: bold;">
                            Available Now
                        </div>
                    </div>
                    
                    <!-- Hook Wizard -->
                    <div style="background: white; border-radius: 1rem; padding: 2rem; box-shadow: 0 4px 6px rgba(0,0,0,0.1); text-align: center;">
                        <div style="font-size: 2.5rem; color: var(--primary); margin-bottom: 1rem;">
                            <i class="fas fa-fish"></i>
                        </div>
                        <h4 style="color: #374151;">Hook Wizard</h4>
                        <p style="color: #4b5563;">Generate viral hooks that stop scrollers in their tracks</p>
                        <div style="margin-top: 1rem; padding: 0.5rem 1rem; background: #10b981; color: white; border-radius: 2rem; display: inline-block; font-weight: bold;">
                            Available Now
                        </div>
                    </div>
                    
                    <!-- Script Wizard -->
                    <div style="background: white; border-radius: 1rem; padding: 2rem; box-shadow: 0 4px 6px rgba(0,0,0,0.1); text-align: center;">
                        <div style="font-size: 2.5rem; color: var(--primary); margin-bottom: 1rem;">
                            <i class="fas fa-cube"></i>
                        </div>
                        <h4 style="color: #374151;">Marketplace</h4>
                        <p style="color: #4b5563;">Buy & sell AI templates, prompts, and workflows</p>
                        <div style="margin-top: 1rem; padding: 0.5rem 1rem; background: #f59e0b; color: white; border-radius: 2rem; display: inline-block; font-weight: bold;">
                            Coming Soon
                        </div>
                    </div>
                </div>
            </div>
            
            <!-- Analyzer Wizards -->
            <div>
                <h3 style="text-align: center; color: var(--primary); margin-bottom: 2rem;">
                    <i class="fas fa-search"></i> Analyzer Wizards
                </h3>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem;">
                    <!-- Thumbnail Wizard -->
                    <div style="background: white; border-radius: 1rem; padding: 2rem; box-shadow: 0 4px 6px rgba(0,0,0,0.1); text-align: center;">
                        <div style="font-size: 2.5rem; color: var(--primary); margin-bottom: 1rem;">
                            <i class="fas fa-image"></i>
                        </div>
                        <h4 style="color: #374151;">Thumbnail Wizard</h4>
                        <p style="color: #4b5563;">AI analysis of thumbnails with actionable improvement tips</p>
                        <div style="margin-top: 1rem; padding: 0.5rem 1rem; background: #10b981; color: white; border-radius: 2rem; display: inline-block; font-weight: bold;">
                            Available Now
                        </div>
                    </div>
                    
                    <!-- Document Wizard -->
                    <div style="background: white; border-radius: 1rem; padding: 2rem; box-shadow: 0 4px 6px rgba(0,0,0,0.1); text-align: center;">
                        <div style="font-size: 2.5rem; color: var(--primary); margin-bottom: 1rem;">
                            <i class="fas fa-file-contract"></i>
                        </div>
                        <h4 style="color: #374151;">Document Wizard</h4>
                        <p style="color: #4b5563;">Decode legal/medical jargon into plain English</p>
                        <div style="margin-top: 1rem; padding: 0.5rem 1rem; background: #10b981; color: white; border-radius: 2rem; display: inline-block; font-weight: bold;">
                            Available Now
                        </div>
                    </div>
                    
                    <!-- Video Wizard -->
                    <div style="background: white; border-radius: 1rem; padding: 2rem; box-shadow: 0 4px 6px rgba(0,0,0,0.1); text-align: center;">
                        <div style="font-size: 2.5rem; color: var(--primary); margin-bottom: 1rem;">
                            <i class="fas fa-video"></i>
                        </div>
                        <h4 style="color: #374151;">Video Wizard</h4>
                        <p style="color: #4b5563;">Analyze video content for engagement optimization</p>
                        <div style="margin-top: 1rem; padding: 0.5rem 1rem; background: #10b981; color: white; border-radius: 2rem; display: inline-block; font-weight: bold;">
                            Available Now
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- HOW IT WORKS -->
        <section style="background: linear-gradient(135deg, #f0f9ff, #e0f2fe); border-radius: 1rem; padding: 3rem; margin: 3rem 0;">
            <h2 style="text-align: center; color: var(--primary); margin-bottom: 3rem;">
                How It Works: AI Magic in 3 Steps
            </h2>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 2rem;">
                <div style="text-align: center;">
                    <div style="font-size: 3rem; color: var(--primary); margin-bottom: 1rem;">
                        <div style="background: var(--primary); color: white; width: 60px; height: 60px; border-radius: 50%; display: inline-flex; align-items: center; justify-content: center; font-weight: bold;">
                            1
                        </div>
                    </div>
                    <h3 style="color: #374151;">Choose Your Wizard</h3>
                    <p style="color: #4b5563;">Select from 5 specialized tools for your content type</p>
                </div>
                <div style="text-align: center;">
                    <div style="font-size: 3rem; color: var(--primary); margin-bottom: 1rem;">
                        <div style="background: var(--primary); color: white; width: 60px; height: 60px; border-radius: 50%; display: inline-flex; align-items: center; justify-content: center; font-weight: bold;">
                            2
                        </div>
                    </div>
                    <h3 style="color: #374151;">Input Your Content</h3>
                    <p style="color: #4b5563;">Upload, paste, or describe what you're working on</p>
                </div>
                <div style="text-align: center;">
                    <div style="font-size: 3rem; color: var(--primary); margin-bottom: 1rem;">
                        <div style="background: var(--primary); color: white; width: 60px; height: 60px; border-radius: 50%; display: inline-flex; align-items: center; justify-content: center; font-weight: bold;">
                            3
                        </div>
                    </div>
                    <h3 style="color: #374151;">Get AI Magic</h3>
                    <p style="color: #4b5563;">Receive optimized content or detailed analysis</p>
                </div>
            </div>
        </section>

        <!-- SIMPLIFIED PRICING -->
        <section id="pricing" style="padding: 3rem 0;">
            <h2 style="text-align: center; color: var(--primary); margin-bottom: 2rem;">
                Simple, Transparent Pricing
            </h2>
            <p style="text-align: center; color: #4b5563; max-width: 800px; margin: 0 auto 3rem; font-size: 1.1rem;">
                One credit system for all 5 wizards. Use credits on any tool, anytime.
            </p>
            
            <!-- Credit Cost Table -->
            <div style="background: #f9fafb; border-radius: 1rem; padding: 2rem; margin-bottom: 3rem;">
                <h3 style="text-align: center; color: var(--primary); margin-bottom: 1.5rem;">
                    <i class="fas fa-coins"></i> Credit Costs
                </h3>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; max-width: 800px; margin: 0 auto;">
                    <div style="background: white; padding: 1rem; border-radius: 0.5rem; text-align: center; border: 1px solid #e5e7eb;">
                        <div style="font-weight: bold; color: var(--primary);">Thumbnail Wizard</div>
                        <div style="color: #374151; font-size: 1.1rem; margin: 0.5rem 0;">3 credits</div>
                    </div>
                    <div style="background: white; padding: 1rem; border-radius: 0.5rem; text-align: center; border: 1px solid #e5e7eb;">
                        <div style="font-weight: bold; color: var(--primary);">Document Wizard</div>
                        <div style="color: #374151; font-size: 1.1rem; margin: 0.5rem 0;">2 credits</div>
                    </div>
                    <div style="background: white; padding: 1rem; border-radius: 0.5rem; text-align: center; border: 1px solid #e5e7eb;">
                        <div style="font-weight: bold; color: var(--primary);">Video Wizard</div>
                        <div style="color: #374151; font-size: 1.1rem; margin: 0.5rem 0;">1 credit</div>
                    </div>
                    <div style="background: white; padding: 1rem; border-radius: 0.5rem; text-align: center; border: 1px solid #e5e7eb;">
                        <div style="font-weight: bold; color: var(--primary);">Hook Wizard</div>
                        <div style="color: #374151; font-size: 1.1rem; margin: 0.5rem 0;">1 credit</div>
                    </div>
                    <div style="background: white; padding: 1rem; border-radius: 0.5rem; text-align: center; border: 1px solid #e5e7eb;">
                        <div style="font-weight: bold; color: var(--primary);">Prompt Wizard</div>
                        <div style="color: #374151; font-size: 1.1rem; margin: 0.5rem 0;">2 credits</div>
                    </div>
                </div>
            </div>
            
            <!-- Three Simple Plans -->
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem;">
                <!-- Student Plan -->
                <div style="background: white; border-radius: 1rem; padding: 2rem; box-shadow: 0 4px 6px rgba(0,0,0,0.1); text-align: center; border: 2px solid #e5e7eb;">
                    <h3 style="color: #374151; margin-bottom: 1rem;">Student</h3>
                    <div style="font-size: 2.5rem; color: var(--primary); margin-bottom: 0.5rem;">
                        $9.99<span style="font-size: 1rem; color: #6b7280;">/month</span>
                    </div>
                    <div style="color: #374151; margin-bottom: 1.5rem; font-weight: bold; font-size: 1.1rem;">
                        50 credits/month
                    </div>
                    <ul style="list-style: none; padding: 0; margin: 0 0 2rem 0; text-align: left;">
                        <li style="margin-bottom: 0.75rem; padding-left: 1.5rem; position: relative;">
                            <i class="fas fa-check" style="color: #10b981; position: absolute; left: 0;"></i>
                            All 5 wizards
                        </li>
                        <li style="margin-bottom: 0.75rem; padding-left: 1.5rem; position: relative;">
                            <i class="fas fa-check" style="color: #10b981; position: absolute; left: 0;"></i>
                            Verified students only
                        </li>
                        <li style="margin-bottom: 0.75rem; padding-left: 1.5rem; position: relative;">
                            <i class="fas fa-times" style="color: #ef4444; position: absolute; left: 0;"></i>
                            Watermarked outputs
                        </li>
                    </ul>
                    <a href="#pricing" role="button" style="width: 100%;">Start as Student</a>
                </div>
                
                <!-- Creator Plan (Most Popular) -->
                <div style="background: white; border-radius: 1rem; padding: 2rem; box-shadow: 0 8px 16px rgba(139, 92, 246, 0.15); text-align: center; border: 2px solid var(--primary); position: relative;">
                    <div style="position: absolute; top: -12px; left: 50%; transform: translateX(-50%); background: var(--primary); color: white; padding: 0.25rem 1rem; border-radius: 1rem; font-size: 0.9rem;">
                        Most Popular
                    </div>
                    <h3 style="color: var(--primary); margin-bottom: 1rem;">Creator</h3>
                    <div style="font-size: 2.5rem; color: var(--primary); margin-bottom: 0.5rem;">
                        $19<span style="font-size: 1rem; color: #6b7280;">/month</span>
                    </div>
                    <div style="color: #374151; margin-bottom: 1.5rem; font-weight: bold; font-size: 1.1rem;">
                        100 credits/month
                    </div>
                    <ul style="list-style: none; padding: 0; margin: 0 0 2rem 0; text-align: left;">
                        <li style="margin-bottom: 0.75rem; padding-left: 1.5rem; position: relative;">
                            <i class="fas fa-check" style="color: #10b981; position: absolute; left: 0;"></i>
                            Clean, watermark-free outputs
                        </li>
                        <li style="margin-bottom: 0.75rem; padding-left: 1.5rem; position: relative;">
                            <i class="fas fa-check" style="color: #10b981; position: absolute; left: 0;"></i>
                            Save & organize projects
                        </li>
                        <li style="margin-bottom: 0.75rem; padding-left: 1.5rem; position: relative;">
                            <i class="fas fa-check" style="color: #10b981; position: absolute; left: 0;"></i>
                            Priority processing
                        </li>
                    </ul>
                    <a href="#pricing" role="button" style="width: 100%; background: var(--primary);">Choose Creator Plan</a>
                </div>
                
                <!-- Power User Plan -->
                <div style="background: white; border-radius: 1rem; padding: 2rem; box-shadow: 0 4px 6px rgba(0,0,0,0.1); text-align: center; border: 2px solid #e5e7eb;">
                    <h3 style="color: #374151; margin-bottom: 1rem;">Power User</h3>
                    <div style="font-size: 2.5rem; color: var(--primary); margin-bottom: 0.5rem;">
                        $49<span style="font-size: 1rem; color: #6b7280;">/month</span>
                    </div>
                    <div style="color: #374151; margin-bottom: 1.5rem; font-weight: bold; font-size: 1.1rem;">
                        300 credits/month
                    </div>
                    <ul style="list-style: none; padding: 0; margin: 0 0 2rem 0; text-align: left;">
                        <li style="margin-bottom: 0.75rem; padding-left: 1.5rem; position: relative;">
                            <i class="fas fa-check" style="color: #10b981; position: absolute; left: 0;"></i>
                            Everything in Creator
                        </li>
                        <li style="margin-bottom: 0.75rem; padding-left: 1.5rem; position: relative;">
                            <i class="fas fa-check" style="color: #10b981; position: absolute; left: 0;"></i>
                            Bulk processing
                        </li>
                        <li style="margin-bottom: 0.75rem; padding-left: 1.5rem; position: relative;">
                            <i class="fas fa-check" style="color: #10b981; position: absolute; left: 0;"></i>
                            Custom workflows
                        </li>
                    </ul>
                    <a href="#pricing" role="button" class="secondary" style="width: 100%;">Choose Power User</a>
                </div>
            </div>
            
            <!-- Free Plan -->
            <div style="background: #f0f9ff; border-radius: 1rem; padding: 2rem; margin-top: 2rem; text-align: center;">
                <h3 style="color: var(--primary); margin-bottom: 1rem;">
                    <i class="fas fa-gift"></i> Free Trial
                </h3>
                <div style="font-size: 2rem; color: var(--primary); margin-bottom: 1rem;">
                    10 credits free
                </div>
                <p style="color: #374151; margin-bottom: 1.5rem;">Try all 5 wizards with no credit card required</p>
                <a href="#pricing" role="button" style="background: var(--primary); color: white; border: none; padding: 0.75rem 1.5rem;">
                    Start Free Trial
                </a>
            </div>
            
            <!-- Business Contact CTA -->
            <div style="background: linear-gradient(135deg, #1f2937, #374151); color: white; border-radius: 1rem; padding: 2rem; margin-top: 2rem; text-align: center;">
                <h3 style="margin-bottom: 1rem;">
                    <i class="fas fa-building"></i> Business & Team Plans
                </h3>
                <p style="margin-bottom: 1.5rem; opacity: 0.9;">
                    Need custom plans for your team? Contact us for volume discounts, white-label solutions, and enterprise features.
                </p>
                <a href="mailto:business@prompts-alchemy.com" role="button" style="background: white; color: #1f2937; border: none; padding: 1rem 2rem; font-weight: bold;">
                    <i class="fas fa-envelope"></i> Contact for Business Plans
                </a>
            </div>
        </section>

        <!-- FAQ -->
        <section style="padding: 3rem 0;">
            <h2 style="text-align: center; color: var(--primary); margin-bottom: 3rem;">
                Frequently Asked Questions
            </h2>
            <div style="max-width: 800px; margin: 0 auto;">
                <details style="background: white; border-radius: 0.5rem; padding: 1.5rem; margin-bottom: 1rem; border: 1px solid #e5e7eb;">
                    <summary style="font-weight: bold; color: var(--primary); cursor: pointer; color: #374151;">
                        What counts as an AI credit?
                    </summary>
                    <p style="margin-top: 1rem; color: #4b5563;">
                        One AI credit = one use of any wizard. Whether you're analyzing a thumbnail, generating a prompt, or reviewing a document, each complete operation uses one credit. Credits reset monthly.
                    </p>
                </details>
                
                <details style="background: white; border-radius: 0.5rem; padding: 1.5rem; margin-bottom: 1rem; border: 1px solid #e5e7eb;">
                    <summary style="font-weight: bold; color: var(--primary); cursor: pointer; color: #374151;">
                        Can I switch between plans?
                    </summary>
                    <p style="margin-top: 1rem; color: #4b5563;">
                        Yes! You can upgrade, downgrade, or cancel anytime. Unused credits roll over for 30 days. We prorate changes.
                    </p>
                </details>
                
                <details style="background: white; border-radius: 0.5rem; padding: 1.5rem; margin-bottom: 1rem; border: 1px solid #e5e7eb;">
                    <summary style="font-weight: bold; color: var(--primary); cursor: pointer; color: #374151;">
                        Do you offer refunds?
                    </summary>
                    <p style="margin-top: 1rem; color: #4b5563;">
                        We offer a 7-day money-back guarantee for all paid plans. If you're not satisfied, we'll refund your payment, no questions asked.
                    </p>
                </details>
            </div>
        </section>

        <!-- FINAL CTA -->
        <section style="background: linear-gradient(135deg, var(--primary), #7c3aed); color: white; border-radius: 1rem; padding: 4rem 2rem; text-align: center; margin: 3rem 0;">
            <h2 style="margin-bottom: 1rem;">Start Creating Better Content Today</h2>
            <p style="font-size: 1.2rem; margin-bottom: 2rem; opacity: 0.9;">
                Join creators who are saving hours every week with AI-powered tools
            </p>
            <div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap;">
                <a href="#pricing" role="button" style="background: white; color: var(--primary); border: none; padding: 1rem 2.5rem;">
                    <i class="fas fa-gift"></i> Start Free Trial
                </a>
                <a href="#wizards" role="button" style="background: transparent; border: 2px solid white; color: white; padding: 1rem 2.5rem;">
                    <i class="fas fa-eye"></i> Explore Wizards
                </a>
            </div>
        </section>
    </div>
    '''
    return HTMLResponse(layout("Prompts Alchemy - AI Wizard Suite", content))

@app.get("/")
async def root():
    return await home_page()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


# ---------- DOCUMENT WIZARD -----------
app = FastAPI()
DEEPSEEK_KEY = "sk-849662e0871841a5a4496e006311beb9"



# Add this debug endpoint to see the full layout
@app.get("/debug-layout")
async def debug_layout():
    # Show what layout() produces with minimal content
    test_content = "<h1>Test</h1>"
    full_html = layout("Test", test_content)
    
    # Return first 2000 chars to see navbar
    return HTMLResponse(f"<pre>{full_html[:2000]}</pre>")



# ========== DASHBOARD ==========
@app.get("/")
async def home():
    content = '''
    <div style="text-align: center; padding: 4rem 0;">
        <h1 style="color: var(--primary);">
            <i class="fas fa-file-contract"></i><br>
            Document Decoder
        </h1>
        <p style="font-size: 1.25rem; color: #6b7280; max-width: 600px; margin: 1rem auto;">
            AI-powered translation of complex documents. Understand legal, medical, and technical language in plain English.
        </p>
        
        <div style="margin: 3rem 0;">
            <a href="wizard" role="button" style="padding: 1rem 2.5rem; font-size: 1.25rem;">
                <i class="fas fa-magic"></i> Decode a Document
            </a>
        </div>
        
        <div class="card-grid">
            <div class="step-card">
                <i class="fas fa-gavel"></i>
                <h3>Legal Documents</h3>
                <p>Contracts, leases, terms of service</p>
            </div>
            
            <div class="step-card">
                <i class="fas fa-heart-pulse"></i>
                <h3>Medical Papers</h3>
                <p>Reports, prescriptions, instructions</p>
            </div>
            
            <div class="step-card">
                <i class="fas fa-file-signature"></i>
                <h3>Contracts</h3>
                <p>Employment, service, rental agreements</p>
            </div>
            
            <div class="step-card">
                <i class="fas fa-warning"></i>
                <h3>Warning Labels</h3>
                <p>Safety instructions, disclaimers</p>
            </div>
            
            <div class="step-card">
                <i class="fas fa-graduation-cap"></i>
                <h3>Academic Papers</h3>
                <p>Research, studies, technical docs</p>
            </div>
            
            <div class="step-card">
                <i class="fas fa-building"></i>
                <h3>Government Forms</h3>
                <p>Applications, permits, official docs</p>
            </div>
        </div>
        
        <div class="warning-box" style="max-width: 600px; margin: 3rem auto;">
            <h3 style="color: #d97706; margin-top: 0;">
                <i class="fas fa-exclamation-triangle"></i> Important Notice
            </h3>
            <p style="margin-bottom: 0;">
                This tool provides AI-assisted interpretation for educational purposes only. 
                For legal, medical, or financial decisions, always consult a qualified professional.
            </p>
        </div>
    </div>
    '''
    return HTMLResponse(layout("Home", content))

# ========== STEP 1: DOCUMENT TYPE ==========
@app.get("/wizard")
async def step1():
    content = '''
    <div style="max-width: 800px; margin: 0 auto;">
        <div class="steps">
            <div class="step active">1</div>
            <div class="step">2</div>
            <div class="step">3</div>
            <div class="step">4</div>
        </div>
        
        <h1 style="text-align: center; color: var(--primary);">Step 1: Document Type</h1>
        <p style="text-align: center; color: #6b7280;">
            What type of document are you trying to understand?
        </p>
        
        <div class="card-grid">
            <a href="/wizard/step2?doc_type=legal" class="step-card">
                <i class="fas fa-gavel"></i>
                <h3>Legal Document</h3>
                <p>Contract, lease, terms of service, agreement</p>
            </a>
            
            <a href="/wizard/step2?doc_type=medical" class="step-card">
                <i class="fas fa-heart-pulse"></i>
                <h3>Medical Document</h3>
                <p>Report, prescription, diagnosis, instructions</p>
            </a>
            
            <a href="/wizard/step2?doc_type=contract" class="step-card">
                <i class="fas fa-file-signature"></i>
                <h3>Contract/Agreement</h3>
                <p>Employment, service, rental, purchase agreement</p>
            </a>
            
            <a href="/wizard/step2?doc_type=financial" class="step-card">
                <i class="fas fa-money-bill-wave"></i>
                <h3>Financial Document</h3>
                <p>Loan terms, investment, insurance, tax forms</p>
            </a>
            
            <a href="/wizard/step2?doc_type=technical" class="step-card">
                <i class="fas fa-cogs"></i>
                <h3>Technical Manual</h3>
                <p>Instructions, specifications, warranty</p>
            </a>
            
            <a href="/wizard/step2?doc_type=government" class="step-card">
                <i class="fas fa-landmark"></i>
                <h3>Government Form</h3>
                <p>Application, permit, official document</p>
            </a>
            
            <a href="/wizard/step2?doc_type=academic" class="step-card">
                <i class="fas fa-graduation-cap"></i>
                <h3>Academic Paper</h3>
                <p>Research, study, scientific paper</p>
            </a>
            
            <a href="/wizard/step2?doc_type=other" class="step-card">
                <i class="fas fa-file-alt"></i>
                <h3>Other Complex Document</h3>
                <p>Any difficult-to-understand text</p>
            </a>
        </div>
        
        <div style="text-align: center; margin-top: 2rem;">
            <a href="/" role="button" class="secondary">Cancel</a>
        </div>
    </div>
    '''
    return HTMLResponse(layout("Step 1: Document Type", content))

# ========== STEP 2: AUDIENCE LEVEL ==========
@app.get("/wizard/step2")
async def step2(doc_type: str = Query("legal")):
    doc_type_names = {
        "legal": "Legal Document",
        "medical": "Medical Document", 
        "contract": "Contract/Agreement",
        "financial": "Financial Document",
        "technical": "Technical Manual",
        "government": "Government Form",
        "academic": "Academic Paper",
        "other": "Complex Document"
    }
    
    content = f'''
    <div style="max-width: 800px; margin: 0 auto;">
        <div class="steps">
            <div class="step">1</div>
            <div class="step active">2</div>
            <div class="step">3</div>
            <div class="step">4</div>
        </div>
        
        <h1 style="text-align: center; color: var(--primary);">Step 2: Your Knowledge Level</h1>
        <p style="text-align: center; color: #6b7280;">
            How familiar are you with {doc_type_names[doc_type].lower()}s?
        </p>
        
        <p style="text-align: center;"><strong>Document Type:</strong> {doc_type_names[doc_type]}</p>
        
        <div class="card-grid">
            <a href="/wizard/step3?doc_type={doc_type}&level=novice" class="step-card">
                <i class="fas fa-seedling"></i>
                <h3>Novice</h3>
                <p>Little to no experience. Explain like I'm new.</p>
            </a>
            
            <a href="/wizard/step3?doc_type={doc_type}&level=general" class="step-card">
                <i class="fas fa-user"></i>
                <h3>General Public</h3>
                <p>Basic understanding. Use everyday language.</p>
            </a>
            
            <a href="/wizard/step3?doc_type={doc_type}&level=educated" class="step-card">
                <i class="fas fa-user-graduate"></i>
                <h3>Educated Layperson</h3>
                <p>Some background. Can handle some terminology.</p>
            </a>
            
            <a href="/wizard/step3?doc_type={doc_type}&level=professional" class="step-card">
                <i class="fas fa-briefcase"></i>
                <h3>Related Professional</h3>
                <p>Work in related field. Want deeper analysis.</p>
            </a>
        </div>
        
        <div class="info-box">
            <p style="margin: 0;">
                <strong>Tip:</strong> Choose "Novice" for maximum plain English translation. 
                The AI will avoid all jargon and use simple analogies.
            </p>
        </div>
        
        <div style="text-align: center; margin-top: 2rem;">
            <a href="wizard" role="button" class="secondary">Back</a>
        </div>
    </div>
    '''
    return HTMLResponse(layout("Step 2: Knowledge Level", content))

# ========== STEP 3: DOCUMENT INPUT ==========
@app.get("/wizard/step3")
async def step3(
    doc_type: str = Query("legal"),
    level: str = Query("novice")
):
    doc_type_names = {
        "legal": "Legal Document",
        "medical": "Medical Document",
        "contract": "Contract/Agreement", 
        "financial": "Financial Document",
        "technical": "Technical Manual",
        "government": "Government Form",
        "academic": "Academic Paper",
        "other": "Complex Document"
    }
    
    level_names = {
        "novice": "Novice",
        "general": "General Public", 
        "educated": "Educated Layperson",
        "professional": "Related Professional"
    }
    
    content = f'''
    <div style="max-width: 800px; margin: 0 auto;">
        <div class="steps">
            <div class="step">1</div>
            <div class="step">2</div>
            <div class="step active">3</div>
            <div class="step">4</div>
        </div>
        
        <h1 style="text-align: center; color: var(--primary);">Step 3: Paste Your Document</h1>
        <p style="text-align: center; color: #6b7280;">
            Copy and paste the text you want to understand
        </p>
        
        <div style="background: #f9fafb; padding: 1.5rem; border-radius: 0.75rem; margin: 2rem 0;">
            <h3>Your Selections:</h3>
            <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem; margin: 1rem 0;">
                <div><strong>Document Type:</strong><br>{doc_type_names[doc_type]}</div>
                <div><strong>Your Level:</strong><br>{level_names[level]}</div>
            </div>
        </div>
        
        <div class="warning-box">
            <h4 style="color: #d97706; margin-top: 0;">
                <i class="fas fa-shield-alt"></i> Privacy & Security
            </h4>
            <p style="margin-bottom: 0;">
                • Your document is processed securely via API<br>
                • No data is stored permanently<br>
                • Remove sensitive personal information before pasting<br>
                • For highly confidential documents, use generic examples
            </p>
        </div>
        
        <form action="/process" method="POST">
            <input type="hidden" name="doc_type" value="{doc_type}">
            <input type="hidden" name="level" value="{level}">
            
            <div style="margin: 2rem 0;">
                <label for="document_text">
                    <strong>Document Text:</strong>
                    <p style="color: #6b7280; margin: 0.5rem 0;">
                        Paste the full document or the specific section you want decoded.
                    </p>
                </label>
                <textarea id="document_text" name="document_text" rows="12" 
                          placeholder="Paste your legal clause, medical report, contract section, or any complex text here..."
                          class="doc-input"></textarea>
            </div>
            
            <div style="margin: 2rem 0;">
                <label for="specific_questions">
                    <strong>Specific Questions (Optional):</strong>
                    <p style="color: #6b7280; margin: 0.5rem 0;">
                        What specifically do you want to understand about this document?
                    </p>
                </label>
                <textarea id="specific_questions" name="specific_questions" rows="4" 
                          placeholder="Example questions: 
• What are the hidden risks in this clause?
• What does this medical term mean for my treatment?
• What am I really agreeing to here?
• What are my rights vs. responsibilities?"
                          style="width: 100%; padding: 1rem; border: 2px solid #e5e7eb; border-radius: 0.5rem;"></textarea>
            </div>
            
            <div style="text-align: center; margin: 2rem 0;">
                <button type="submit" style="padding: 1rem 3rem; font-size: 1.2rem;">
                    <i class="fas fa-search"></i> Decode This Document
                </button>
                <p style="margin-top: 1rem; color: #6b7280;">
                    <i class="fas fa-clock"></i> AI analysis takes 15-30 seconds
                </p>
            </div>
        </form>
        
        <div style="text-align: center; margin-top: 2rem;">
            <a href="/wizard/step2?doc_type={doc_type}" role="button" class="secondary">Back</a>
        </div>
    </div>
    '''
    return HTMLResponse(layout("Step 3: Document Input", content))

# ========== PROCESS ==========
@app.post("/process")
async def process_document(
    doc_type: str = Form(...),
    level: str = Form(...),
    document_text: str = Form(...),
    specific_questions: str = Form("")
):
    loading_content = f'''
    <div style="max-width: 800px; margin: 0 auto; text-align: center; padding: 4rem 0;">
        <div style="font-size: 4rem; color: var(--primary); margin-bottom: 2rem;">
            <i class="fas fa-search"></i>
        </div>
        
        <h1 style="color: var(--primary);">Decoding Your Document...</h1>
        <p style="font-size: 1.2rem; color: #6b7280; max-width: 500px; margin: 1rem auto;">
            Analyzing {doc_type.replace("_", " ").title()} text for a {level} understanding...
        </p>
        
        <div class="loading-bar">
            <div class="loading-progress"></div>
        </div>
        
        <p style="color: #6b7280; margin-top: 2rem;">
            <i class="fas fa-lightbulb"></i> Looking for tricky language, hidden meanings, and plain English translations...
        </p>
        
        <meta http-equiv="refresh" content="3;url=/result?doc_type={doc_type}&level={level}&document_text={document_text}&specific_questions={specific_questions}">
    </div>
    '''
    
    return HTMLResponse(layout("Decoding...", loading_content))

# ========== RESULT ==========
@app.get("/result")
async def show_result(
    doc_type: str = Query(...),
    level: str = Query(...),
    document_text: str = Query(...),
    specific_questions: str = Query("")
):
    # YOUR TURQUOISE COLOR
    TURQUOISE = "#0d96c1"
    TURQUOISE_LIGHT = "#ecfeff"
    TURQUOISE_DARK = "#0c4a6e"
    
    # CHECK DOCUMENT SIZE FIRST
    word_count = len(document_text.split())
    
    if word_count > 2000:
        result_content = f'''
<div style="max-width: 800px; margin: 0 auto; text-align: center;">
    <h1 style="color: #d97706;"><i class="fas fa-exclamation-triangle"></i> Document Too Large</h1>
    <div style="background: #fef3c7; border: 2px solid #f59e0b; border-radius: 0.5rem; padding: 1.5rem; margin: 1rem 0;">
        <p><strong>{word_count} words detected (limit: 2,000 words)</strong></p>
        <p>For best results:</p>
        <ol style="text-align: left; max-width: 500px; margin: 1rem auto;">
            <li><strong>Extract the most important section</strong> (1-2 paragraphs)</li>
            <li>Focus on the <strong>specific clause</strong> you don't understand</li>
            <li>Copy just the <strong>key paragraphs</strong></li>
        </ol>
    </div>
    <div style="margin: 2rem 0;">
        <a href="/wizard/step3?doc_type={doc_type}&level={level}" 
           role="button" style="background: {TURQUOISE}; border-color: {TURQUOISE};">
            <i class="fas fa-edit"></i> Try Again with Smaller Section
        </a>
    </div>
</div>
'''
        return HTMLResponse(layout("Document Too Large", result_content))
    
    # TEST MODE
    TEST_MODE = False
    
    try:
        if TEST_MODE:
            ai_text = '''OVERALL COMPLEXITY SCORE: 8/10 - This legal clause uses dense legal terminology but follows standard contract structure

PLAIN ENGLISH TRANSLATION:
This section says: "If someone sues the other party for any reason, the first party will pay for all legal costs and damages." 
• You're agreeing to cover ALL legal expenses if the other party gets sued
• This applies even if the lawsuit isn't really their fault
• There's no limit to how much you might have to pay

TRICKY LANGUAGE ALERT:
• "Indemnifies and holds harmless": Means you'll pay ALL legal costs for the other party | This is very broad protection for them | Example: If they get sued for $1M, you pay it
• "Any and all claims, demands, damages": Means EVERY possible type of legal complaint | Very broad language that covers things you can't predict | Example: Future lawsuits you can't imagine today
• "Causes of action or suits at law or in equity": Means ANY type of lawsuit in ANY court system | Covers more than just normal lawsuits | Example: Arbitration, mediation, court cases

RED FLAGS TO WATCH FOR:
• Unlimited liability: You could owe millions with no cap | Very risky for individuals/small businesses | Ask for: A dollar limit or "to the extent permitted by law"
• One-sided protection: Only protects the other party, not you | Creates unequal relationship | Ask for: Mutual indemnification (both sides protect each other)
• Broad language: "Any and all" means literally everything | Could cover lawsuits unrelated to your actual work | Ask for: Specific list of what's covered

STANDARD/BOILERPLATE SECTIONS:
• Legal jurisdiction: Which state's laws apply | Most contracts have this | No need to worry unless it's an unusual state
• Notice provisions: How to send official letters | Standard administrative detail | Just note the addresses/email
• Severability: If one part is illegal, rest stays valid | Standard protection for both sides | Nothing to negotiate

YOUR RIGHTS (What you can do):
• Right to receive notice: They must notify you before suing | How to exercise: Make sure your contact info is correct
• Right to defend: You can choose the lawyers (usually) | How to exercise: Ask for "right to select counsel" in clause

YOUR RESPONSIBILITIES (What you must do):
• Pay all legal costs: You cover everything if they get sued | Consequences if not done: They can sue you for reimbursement
• Cooperate with defense: You must help with the legal case | Consequences if not done: Could lose insurance coverage

NEXT STEPS & QUESTIONS TO ASK:
1. Question to ask a lawyer: "Is there a way to cap my liability at a specific dollar amount or my insurance limits?"
2. Action to take: Ask for "mutual indemnification" - both sides protect each other equally
3. What to research: Your insurance policy - does it cover "contractual liability"?

BOTTOM LINE SUMMARY:
This is a very one-sided liability clause that could leave you responsible for unlimited legal costs if the other party gets sued for any reason. For a novice, this is risky without a liability cap. Ask for either a dollar limit or make it mutual so both sides have the same protection.'''
        else:
            ai_text = "Real API mode - set TEST_MODE = False"
        
        # Parse sections
        sections = {}
        current_section = None
        current_content = []
        
        for line in ai_text.split('\n'):
            line = line.strip()
            if not line:
                continue
            if line.endswith(':'):
                if current_section and current_content:
                    sections[current_section] = '\n'.join(current_content).strip()
                current_section = line.rstrip(':')
                current_content = []
            elif current_section:
                current_content.append(line)
        
        if current_section and current_content:
            sections[current_section] = '\n'.join(current_content).strip()
        
        # Build cards - SIMPLE VERSION THAT WON'T BREAK
        analysis_html = ""
        
        section_config = [
            ("PLAIN ENGLISH TRANSLATION", "fa-language", "The document in simple terms"),
            ("TRICKY LANGUAGE ALERT", "fa-exclamation-triangle", "Watch out for these terms"),
            ("RED FLAGS TO WATCH FOR", "fa-flag", "Potential concerns to address"),
            ("STANDARD/BOILERPLATE SECTIONS", "fa-check-circle", "Normal sections, nothing to worry"),
            ("YOUR RIGHTS", "fa-shield-alt", "What you're entitled to"),
            ("YOUR RESPONSIBILITIES", "fa-tasks", "What you need to do"),
            ("NEXT STEPS & QUESTIONS TO ASK", "fa-question-circle", "Actionable advice"),
            ("BOTTOM LINE SUMMARY", "fa-bullseye", "The most important takeaway")
        ]
        
        for section_title, icon, description in section_config:
            if section_title in sections:
                content = sections[section_title]
                
                analysis_html += f'''
<div style="background: white; border: 2px solid {TURQUOISE}; border-radius: 12px; padding: 1.5rem; margin-bottom: 2rem; display: block;">
    <h3 style="color: {TURQUOISE}; margin-top: 0; border-bottom: 2px solid {TURQUOISE_LIGHT}; padding-bottom: 0.5rem;">
        <i class="fas {icon}" style="margin-right: 0.5rem;"></i>{section_title}
    </h3>
    <p style="color: #64748b; font-size: 0.9rem; margin-bottom: 1rem;">
        <i class="fas fa-info-circle"></i> {description}
    </p>
    <div style="background: {TURQUOISE_LIGHT}; padding: 1rem; border-radius: 8px; border-left: 4px solid {TURQUOISE}; color: {TURQUOISE_DARK}; line-height: 1.6;">
        {content.replace(chr(10), '<br>').replace('•', '•')}
    </div>
</div>
'''
        
        # Score card
        if "OVERALL COMPLEXITY SCORE" in ai_text:
            score = "5"
            try:
                import re
                score_match = re.search(r'(\d+(?:\.\d+)?)/10', ai_text)
                if score_match:
                    score = score_match.group(1)
            except:
                pass
            
            try:
                score_num = float(score)
                if score_num >= 8:
                    score_color = "#dc2626"
                    score_icon = "fa-brain"
                    score_text = "Very Complex"
                elif score_num >= 6:
                    score_color = "#d97706"
                    score_icon = "fa-exclamation-triangle"
                    score_text = "Complex"
                elif score_num >= 4:
                    score_color = TURQUOISE
                    score_icon = "fa-balance-scale"
                    score_text = "Moderate"
                else:
                    score_color = "#059669"
                    score_icon = "fa-check-circle"
                    score_text = "Fairly Simple"
            except:
                score_color = TURQUOISE
                score_icon = "fa-file-alt"
                score_text = "Document Analysis"
            
            score_html = f'''
<div style="background: white; border: 3px solid {score_color}; border-radius: 12px; padding: 2rem; margin-bottom: 2rem; text-align: center; display: block;">
    <div style="font-size: 0.9rem; color: {score_color}; margin-bottom: 0.5rem; text-transform: uppercase; letter-spacing: 1px; font-weight: 600;">
        <i class="fas {score_icon}"></i> Document Complexity Score
    </div>
    <div style="font-size: 4rem; font-weight: bold; color: {score_color}; margin: 0.5rem 0; line-height: 1;">
        {score}<span style="font-size: 2rem; opacity: 0.7;">/10</span>
    </div>
    <div style="font-size: 1.1rem; color: #374151; margin-top: 0.5rem;">
        {score_text} • {doc_type.replace("_", " ").title()} • {level.replace("_", " ").title()} Level
    </div>
</div>
'''
            analysis_html = score_html + analysis_html
        
        result_content = f'''
<div style="max-width: 800px; margin: 0 auto;">
    <div style="text-align: center; margin-bottom: 2rem;">
        <div style="font-size: 3rem; color: {TURQUOISE};">
            <i class="fas fa-file-contract"></i>
        </div>
        <h1 style="color: {TURQUOISE};">Document Decoded!</h1>
        <p style="color: #64748b;">Translated for <strong>{level.replace("_", " ").title()}</strong> understanding</p>
    </div>
    
    <div style="background: #fef3c7; border: 2px solid #f59e0b; border-radius: 0.5rem; padding: 1rem; margin: 1rem 0;">
        <h4 style="color: #d97706; margin-top: 0;">
            <i class="fas fa-gavel"></i> Legal Disclaimer
        </h4>
        <p style="margin-bottom: 0;">
            This AI analysis is for educational purposes only. It helps you understand documents better, 
            but is NOT legal, medical, or financial advice. For important decisions, consult a qualified professional.
        </p>
    </div>
    
    {analysis_html}
    
    <div style="text-align: center; margin-top: 3rem;">
        <a href="wizard" role="button" style="margin-right: 1rem; background: {TURQUOISE}; border-color: {TURQUOISE};">
            <i class="fas fa-file-contract"></i> Decode Another Document
        </a>
        <a href="/" role="button" style="background: #64748b; border-color: #64748b;">
            <i class="fas fa-home"></i> Dashboard
        </a>
    </div>
</div>
'''
    
    except Exception as e:
        result_content = f'''
<div style="max-width: 800px; margin: 0 auto; text-align: center;">
    <h1 style="color: #dc2626;"><i class="fas fa-exclamation-triangle"></i> Analysis Error</h1>
    <p>{str(e)}</p>
    <a href="/wizard/step3?doc_type={doc_type}&level={level}" 
       role="button" style="margin-top: 2rem; background: {TURQUOISE}; border-color: {TURQUOISE};">Try Again</a>
</div>
'''
    
    return HTMLResponse(layout("Document Analysis Results", result_content))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8002)
  

# ---------- HOOK WIZARD -----------


# ---------- PROMPTS WIZARD -----------


# ---------- THUMBNAIL WIZARD -----------


# ---------- VIDEO WIZARD -----------

