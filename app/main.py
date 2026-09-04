from pathlib import Path
from typing import List, Dict, Any, Optional
from fastapi import FastAPI, Request, HTTPException, Body
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from app.models.resume import Resume, PersonalInfo, WorkExperience, Education, Project, SkillCategory, Certification
from app.models.samples import SAMPLE_RESUMES
from app.profile_importer import fetch_github_projects, parse_linkedin_profile, extract_github_username, extract_linkedin_username

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(
    title="rockCV - Professional Resume Builder",
    description="Locally hosted FastAPI resume builder with Tailwind CSS and industry-tailored templates.",
    version="1.0.0"
)

# Mount static directory
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")

# Jinja2 templates directory
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))


class ProfileImportRequest(BaseModel):
    linkedin_url: Optional[str] = None
    github_url: Optional[str] = None
    base_resume: Optional[Dict[str, Any]] = None


@app.get("/", response_class=HTMLResponse)
async def get_builder(request: Request):
    """Render the main resume builder web application."""
    return templates.TemplateResponse(request=request, name="builder.html")


@app.get("/api/samples")
async def list_samples():
    """List available sample resume templates across industries."""
    samples_list = [
        {
            "id": key,
            "name": val["name"],
            "industry": val["industry"],
            "template": val["template"]
        }
        for key, val in SAMPLE_RESUMES.items()
    ]
    return JSONResponse(content=samples_list)


@app.get("/api/samples/{sample_id}")
async def get_sample(sample_id: str):
    """Get sample resume data for a given industry key."""
    if sample_id not in SAMPLE_RESUMES:
        raise HTTPException(status_code=404, detail=f"Sample '{sample_id}' not found.")
    return JSONResponse(content=SAMPLE_RESUMES[sample_id])


@app.post("/api/render", response_class=HTMLResponse)
async def render_resume(request: Request, resume: Resume = Body(...)):
    """Render the HTML resume using the requested Jinja2 template."""
    template_name = resume.template or "modern_tech"
    template_file = f"resume_templates/{template_name}.html"

    # Fallback to modern_tech if template file doesn't exist
    template_path = BASE_DIR / "templates" / template_file
    if not template_path.exists():
        template_file = "resume_templates/modern_tech.html"

    return templates.TemplateResponse(
        request=request,
        name=template_file,
        context={"resume": resume.model_dump()}
    )


@app.post("/api/export")
async def export_resume_json(resume: Resume = Body(...)):
    """Validate and return JSON resume data for export/download."""
    return JSONResponse(content=resume.model_dump())


@app.post("/api/import-profile")
async def import_profile(req: ProfileImportRequest = Body(...)):
    """Import and build/enrich a CV from optional LinkedIn and GitHub profile links."""
    base_data = req.base_resume or SAMPLE_RESUMES.get("it", {}).copy()

    # Ensure nested structures
    personal = base_data.get("personal_info", {})
    projects = base_data.get("projects", [])

    # Process GitHub URL
    if req.github_url:
        gh_user = extract_github_username(req.github_url)
        if gh_user:
            personal["github"] = f"github.com/{gh_user}"
            gh_projects = await fetch_github_projects(req.github_url)
            if gh_projects:
                projects = gh_projects

    # Process LinkedIn URL
    if req.linkedin_url:
        li_data = parse_linkedin_profile(req.linkedin_url)
        if li_data:
            if li_data.get("full_name"):
                personal["full_name"] = li_data["full_name"]
            if li_data.get("headline"):
                personal["headline"] = li_data["headline"]
            if li_data.get("linkedin"):
                personal["linkedin"] = li_data["linkedin"]
            if li_data.get("summary"):
                base_data["summary"] = li_data["summary"]
            if li_data.get("experience"):
                base_data["experience"] = li_data["experience"]
            if li_data.get("education"):
                base_data["education"] = li_data["education"]

    base_data["personal_info"] = personal
    base_data["projects"] = projects

    # Validate against Resume model
    try:
        validated_resume = Resume(**base_data)
        return JSONResponse(content=validated_resume.model_dump())
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to build resume from profile: {str(e)}")
