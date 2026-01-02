# layout.py - Simple version for testing
def layout(title: str, content: str) -> str:
    return f'''<!DOCTYPE html>
<html>
<head>
    <title>{title}</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@picocss/pico@1/css/pico.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        :root {{
            --primary: #8b5cf6;
            --primary-hover: #7c3aed;
        }}
        [role="button"], button {{
            background: var(--primary);
            border-color: var(--primary);
        }}
        a {{ color: var(--primary); }}
    </style>
</head>
<body>
    <nav style="padding: 1rem 0; border-bottom: 1px solid #e5e7eb;">
        <div class="container">
            <a href="/" style="text-decoration: none; font-size: 1.25rem; font-weight: bold; color: var(--primary);">
                <i class="fas fa-flask"></i> Prompts Alchemy
            </a>
        </div>
    </nav>
    <main class="container" style="padding: 2rem 0;">
        {content}
    </main>
</body>
</html>'''
