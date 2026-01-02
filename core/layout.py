# core/layout.py - Put this in core/layout.py
def layout(title: str, content: str, current_tool: str = None) -> str:
    # Your wizard paths - UPDATE if different
    wizards = [
        ("/", "Home", "fas fa-home", "home"),
        ("/prompt-wizard", "Prompt", "fas fa-hat-wizard", "prompt"),
        ("/document-wizard", "Document", "fas fa-file-contract", "document"),
        ("/hook-wizard", "Hook", "fas fa-fish", "hook"),
        ("/video-wizard", "Video", "fas fa-video", "video"),
        ("/thumbnail-wizard", "Thumbnail", "fas fa-image", "thumbnail"),
    ]
    
    nav_html = ""
    for path, label, icon, tool_id in wizards:
        is_active = current_tool == tool_id
        active_style = "background: var(--primary); color: white;" if is_active else ""
        nav_html += f'''
        <a href="{path}" style="
            margin: 0 0.25rem;
            padding: 0.5rem 1rem;
            border-radius: 0.5rem;
            text-decoration: none;
            color: {'white' if is_active else '#6b7280'};
            {active_style}
            transition: all 0.2s;
        ">
            <i class="{icon}"></i> {label}
        </a>
        '''
    
    return f'''<!DOCTYPE html>
<html>
<head>
    <title>{title} | Prompts Alchemy</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@picocss/pico@1/css/pico.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        :root {{
            --primary: #8b5cf6;
            --primary-hover: #7c3aed;
            --secondary: #f59e0b;
        }}
        body {{ background: #f9fafb; min-height: 100vh; }}
        .suite-nav {{
            background: white;
            border-bottom: 2px solid #e5e7eb;
            padding: 1rem 0;
            position: sticky;
            top: 0;
            z-index: 100;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 1rem;
        }}
        [role="button"], button {{
            background: var(--primary);
            border-color: var(--primary);
        }}
    </style>
</head>
<body>
    <nav class="suite-nav">
        <div class="container" style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap;">
            <a href="/" style="text-decoration: none; font-size: 1.25rem; font-weight: bold; color: var(--primary);">
                <i class="fas fa-flask"></i> Prompts Alchemy
            </a>
            <div style="display: flex; flex-wrap: wrap; margin: 0.5rem 0;">
                {nav_html}
            </div>
        </div>
    </nav>
    <main class="container" style="padding: 2rem 0; min-height: 80vh;">
        {content}
    </main>
</body>
</html>'''
