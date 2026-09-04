import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.models.samples import SAMPLE_RESUMES

client = TestClient(app)

def test_get_builder():
    response = client.get("/")
    assert response.status_code == 200
    assert "rockCV" in response.text
    assert "Choose Professional Style Template" in response.text

def test_list_samples():
    response = client.get("/api/samples")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 5
    sample_ids = [item["id"] for item in data]
    assert "accounting" in sample_ids
    assert "it" in sample_ids
    assert "executive" in sample_ids
    assert "marketing" in sample_ids
    assert "healthcare" in sample_ids

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
    assert data["template"] == "modern_tech"

def test_import_profile_endpoint():
    response = client.post("/api/import-profile", json={
        "linkedin_url": "https://linkedin.com/in/john-doe",
        "github_url": "https://github.com/johndoe"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["personal_info"]["github"] == "github.com/johndoe"
    assert data["personal_info"]["linkedin"] == "linkedin.com/in/john-doe"
    assert len(data["projects"]) > 0
