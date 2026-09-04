import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.models.samples import SAMPLE_RESUMES
from app.profile_importer import clean_linkedin_name, extract_linkedin_username, extract_github_username

client = TestClient(app)

def test_get_builder():
    response = client.get("/")
    assert response.status_code == 200
    assert "rockCV" in response.text

def test_list_samples():
    response = client.get("/api/samples")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 5

def test_get_sample_detail():
    response = client.get("/api/samples/accounting")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == "accounting"
    assert data["personal_info"]["full_name"] == "Alexander Morgan, CPA"

def test_get_nonexistent_sample():
    response = client.get("/api/samples/nonexistent_industry")
    assert response.status_code == 404

@pytest.mark.parametrize("sample_key", list(SAMPLE_RESUMES.keys()))
def test_render_resume_all_templates(sample_key):
    sample_data = SAMPLE_RESUMES[sample_key]
    response = client.post("/api/render", json=sample_data)
    assert response.status_code == 200
    assert sample_data["personal_info"]["full_name"] in response.text

def test_export_resume_json():
    sample_data = SAMPLE_RESUMES["it"]
    response = client.post("/api/export", json=sample_data)
    assert response.status_code == 200
    data = response.json()
    assert data["personal_info"]["full_name"] == "Samantha Chen"

def test_resume_max_pages_validation():
    sample_data = SAMPLE_RESUMES["it"].copy()
    sample_data["max_pages"] = 3
    response = client.post("/api/render", json=sample_data)
    assert response.status_code == 200

    # Test invalid max_pages (> 3)
    sample_data["max_pages"] = 4
    bad_response = client.post("/api/render", json=sample_data)
    assert bad_response.status_code == 422

def test_extract_linkedin_and_github_helpers():
    li_url = "www.linkedin.com/in/amedzo-edem-robin-2a484890"
    username = extract_linkedin_username(li_url)
    assert username == "amedzo-edem-robin-2a484890"
    name = clean_linkedin_name(username)
    assert name == "Amedzo Edem Robin"

    gh_url = "https://github.com/torvalds/"
    gh_user = extract_github_username(gh_url)
    assert gh_user == "torvalds"

def test_import_profile_endpoint_amedzo():
    response = client.post("/api/import-profile", json={
        "linkedin_url": "www.linkedin.com/in/amedzo-edem-robin-2a484890",
        "github_url": "https://github.com/torvalds"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["personal_info"]["full_name"] == "Amedzo Edem Robin"
    assert "linkedin.com/in/amedzo-edem-robin-2a484890" in data["personal_info"]["linkedin"]
    assert "github.com/torvalds" in data["personal_info"]["github"]
    assert len(data["projects"]) > 0
    assert "GitHub Portfolio Analysis" in data["projects"][0]["name"]
