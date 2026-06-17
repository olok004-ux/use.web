import re
import os

HTML_FILE = "0531.html"

def main():
    if not os.path.exists(HTML_FILE):
        print(f"Error: {HTML_FILE} not found.")
        return

    with open(HTML_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Extract Design System (CSS variables in :root)
    root_match = re.search(r":root\s*\{([^}]*)\}", content)
    design_system_md = "# DESIGN SYSTEM (Tokens)\n\n"
    if root_match:
        root_content = root_match.group(1)
        design_system_md += "## CSS Variables from :root\n\n```css\n"
        for line in root_content.splitlines():
            line = line.strip()
            if line:
                design_system_md += f"{line}\n"
        design_system_md += "```\n"

    with open("DESIGN_SYSTEM.md", "w", encoding="utf-8") as f:
        f.write(design_system_md)

    # 2. Extract Components (CSS classes starting with certain prefixes)
    style_matches = re.findall(r"<style>(.*?)</style>", content, re.DOTALL)
    styles = "\n".join(style_matches)

    components = []
    # simple extraction of class definitions
    class_def_pattern = re.compile(r"(\.[a-zA-Z0-9_-]+)(?:\s|\n|\.|:|{)", re.MULTILINE)
    all_classes = set(class_def_pattern.findall(styles))
    
    components_md = "# COMPONENTS\n\n"
    components_md += "## Common Classes\n\n"
    for c in sorted(all_classes):
        if c.startswith(".btn-") or c.startswith(".nb-") or c.startswith(".ob-") or c.startswith(".field-"):
            components_md += f"- `{c}`\n"
    
    with open("COMPONENTS.md", "w", encoding="utf-8") as f:
        f.write(components_md)

    # 3. Extract Pages (Sections/Divs with id starting with s- or p- or class screen)
    pages_md = "# PAGES\n\n## Main Screens and Sections\n\n"
    
    # Extract tags with id
    id_pattern = re.compile(r'id="([^"]+)"')
    ids = set(id_pattern.findall(content))
    
    pages_md += "### Notable IDs\n"
    for i in sorted(ids):
        pages_md += f"- `#{i}`\n"
        
    class_pattern = re.compile(r'class="([^"]*screen[^"]*)"')
    screens = class_pattern.findall(content)
    pages_md += "\n### Screen Classes\n"
    for s in screens:
        pages_md += f"- `{s}`\n"

    with open("PAGES.md", "w", encoding="utf-8") as f:
        f.write(pages_md)

    # 4. Generate README.md
    readme_md = """# 프로젝트 문서 인덱스

이 디렉토리에는 `0531.html`에서 추출한 핵심 구조와 디자인 시스템이 3단계로 나뉘어 정리되어 있습니다.

- **[Level 1: DESIGN_SYSTEM.md](./DESIGN_SYSTEM.md)**
  - 색상, 폰트, 여백 등 핵심 디자인 토큰(CSS Variables) 정의.
- **[Level 2: COMPONENTS.md](./COMPONENTS.md)**
  - 재사용 가능한 주요 UI 컴포넌트 클래스 목록.
- **[Level 3: PAGES.md](./PAGES.md)**
  - 주요 페이지 및 화면 섹션(ID/Class) 구조 요약.
"""
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_md)

    print("Extraction complete. Generated DESIGN_SYSTEM.md, COMPONENTS.md, PAGES.md, README.md.")

if __name__ == "__main__":
    main()
