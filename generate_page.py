import os
from head_css import HEAD_AND_CSS
from body_html import BODY_HTML
from app_js import APP_JS

print("Generating single-file luxury index.html for ÉLIXORA...")

full_html = HEAD_AND_CSS + "\n" + BODY_HTML + "\n" + APP_JS

output_path = os.path.join(os.path.dirname(__file__), "index.html")
with open(output_path, "w", encoding="utf-8") as f:
    f.write(full_html)

print(f"Successfully generated {output_path}! Total length: {len(full_html)} characters.")
