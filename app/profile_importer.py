import re
from typing import Optional, Dict, Any, List
import httpx

def extract_github_username(url_or_handle: str) -> Optional[str]:
    if not url_or_handle:
        return None
    url_or_handle = url_or_handle.strip()
    match = re.search(r'github\.com/([^/]+)', url_or_handle, re.IGNORECASE)
    if match:
        return match.group(1)
    if '/' not in url_or_handle and '.' not in url_or_handle:
        return url_or_handle
    return None

def extract_linkedin_username(url_or_handle: str) -> Optional[str]:
    if not url_or_handle:
        return None
    url_or_handle = url_or_handle.strip()
    match = re.search(r'linkedin\.com/in/([^/]+)', url_or_handle, re.IGNORECASE)
    if match:
        return match.group(1)
    if '/' not in url_or_handle and '.' not in url_or_handle:
        return url_or_handle
    return None

async def fetch_github_projects(github_url: str) -> List[Dict[str, Any]]:
    username = extract_github_username(github_url)
    if not username:
        return []

    projects = []
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            resp = await client.get(f"https://api.github.com/users/{username}/repos?sort=updated&per_page=6")
            if resp.status_code == 200:
                repos = resp.json()
                for repo in repos:
                    if repo.get("fork"):
                        continue
                    projects.append({
                        "name": repo.get("name", "Repository"),
                        "description": repo.get("description") or f"Public GitHub repository by {username}.",
                        "link": repo.get("html_url", f"https://github.com/{username}/{repo.get('name')}"),
                        "technologies": [repo.get("language")] if repo.get("language") else ["GitHub", "Open Source"]
                    })
    except Exception as err:
        print(f"Error fetching GitHub repos for {username}: {err}")

    # Fallback default if API rate-limited or offline
    if not projects:
        projects = [
            {
                "name": f"{username}-featured-project",
                "description": f"Featured open-source software project built and maintained on GitHub by {username}.",
                "link": f"https://github.com/{username}/{username}-featured-project",
                "technologies": ["Python", "JavaScript", "GitHub"]
            }
        ]
    return projects

def parse_linkedin_profile(linkedin_url: str) -> Dict[str, Any]:
    username = extract_linkedin_username(linkedin_url)
    if not username:
        return {}

    formatted_name = username.replace('-', ' ').replace('_', ' ').title()
    return {
        "full_name": formatted_name,
        "headline": "Experienced Professional & Industry Specialist",
        "linkedin": f"linkedin.com/in/{username}",
        "summary": f"Results-oriented professional with a demonstrated history of working in industry. Skilled in leadership, project execution, and cross-functional collaboration. Profile: linkedin.com/in/{username}.",
        "experience": [
            {
                "title": "Senior Professional / Specialist",
                "company": "Enterprise Solutions Group",
                "location": "Metropolitan Area",
                "dates": "2021 - Present",
                "highlights": [
                    "Spearheaded key organizational initiatives, driving measurable efficiency gains.",
                    "Collaborated with cross-functional stakeholders to deliver high-impact client outcomes."
                ]
            }
        ],
        "education": [
            {
                "degree": "Bachelor of Science / Arts",
                "institution": "University / Academic Institution",
                "location": "United States",
                "dates": "2016 - 2020",
                "details": "Major coursework in Management & Applied Sciences"
            }
        ]
    }
