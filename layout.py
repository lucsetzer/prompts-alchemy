def layout(title: str, content: str) -> str:
    return f'''<!DOCTYPE html>
<html>
<head>
    <title>{title}</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@picocss/pico@1/css/pico.min.css">
</head>
<body>
    <nav>
        <ul>
            <li><strong>Prompts Alchemy</strong></li>
        </ul>
        <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/prompt-wizard">Prompt Wizard</a></li>
            <li><a href="/thumbnail-wizard">Thumbnail Wizard</a></li>
            <li><a href="/video-wizard">Video Wizard</a></li>
        </ul>
    </nav>
    <main class="container">
        {content}
    </main>
</body>
</html>'''
   
     
