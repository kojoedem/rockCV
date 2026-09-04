from typing import List, Optional
from pydantic import BaseModel, EmailStr, Field

class PersonalInfo(BaseModel):
    full_name: str = Field(..., json_schema_extra={"example": "Jane Doe"})
    headline: Optional[str] = Field(None, json_schema_extra={"example": "Senior Software Engineer"})
    email: Optional[str] = Field(None, json_schema_extra={"example": "jane.doe@example.com"})
    phone: Optional[str] = Field(None, json_schema_extra={"example": "+1 (555) 019-2834"})
    location: Optional[str] = Field(None, json_schema_extra={"example": "New York, NY"})
    website: Optional[str] = Field(None, json_schema_extra={"example": "https://janedoe.dev"})
    linkedin: Optional[str] = Field(None, json_schema_extra={"example": "linkedin.com/in/janedoe"})
    github: Optional[str] = Field(None, json_schema_extra={"example": "github.com/janedoe"})

class WorkExperience(BaseModel):
    title: str = Field(..., json_schema_extra={"example": "Senior Financial Analyst"})
    company: str = Field(..., json_schema_extra={"example": "Goldman Sachs"})
    location: Optional[str] = Field(None, json_schema_extra={"example": "New York, NY"})
    dates: Optional[str] = Field(None, json_schema_extra={"example": "Jan 2021 - Present"})
    highlights: List[str] = Field(default_factory=list, json_schema_extra={"example": ["Managed $50M portfolio", "Reduced audit risks by 35%"]})

class Education(BaseModel):
    degree: str = Field(..., json_schema_extra={"example": "B.S. in Accounting & Finance"})
    institution: str = Field(..., json_schema_extra={"example": "NYU Stern School of Business"})
    location: Optional[str] = Field(None, json_schema_extra={"example": "New York, NY"})
    dates: Optional[str] = Field(None, json_schema_extra={"example": "2016 - 2020"})
    details: Optional[str] = Field(None, json_schema_extra={"example": "Magna Cum Laude, GPA 3.9/4.0"})

class SkillCategory(BaseModel):
    category: str = Field(..., json_schema_extra={"example": "Financial Analysis & Modeling"})
    items: List[str] = Field(default_factory=list, json_schema_extra={"example": ["GAAP", "IFRS", "Valuation", "Excel VBA", "SAP"]})

class Project(BaseModel):
    name: str = Field(..., json_schema_extra={"example": "Automated Ledger Reconciliation Tool"})
    description: Optional[str] = Field(None, json_schema_extra={"example": "Python script to reconcile multi-currency ledger entries automatically."})
    link: Optional[str] = Field(None, json_schema_extra={"example": "https://github.com/example/reconciler"})
    technologies: List[str] = Field(default_factory=list, json_schema_extra={"example": ["Python", "Pandas", "SQL"]})

class Certification(BaseModel):
    name: str = Field(..., json_schema_extra={"example": "Certified Public Accountant (CPA)"})
    issuer: Optional[str] = Field(None, json_schema_extra={"example": "AICPA"})
    date: Optional[str] = Field(None, json_schema_extra={"example": "2021"})

class Resume(BaseModel):
    title: Optional[str] = "Professional Resume"
    template: str = Field("modern_tech", json_schema_extra={"example": "accounting_corporate"})
    max_pages: int = Field(1, ge=1, le=3, json_schema_extra={"example": 1})
    personal_info: PersonalInfo
    summary: Optional[str] = None
    experience: List[WorkExperience] = Field(default_factory=list)
    education: List[Education] = Field(default_factory=list)
    skills: List[SkillCategory] = Field(default_factory=list)
    projects: List[Project] = Field(default_factory=list)
    certifications: List[Certification] = Field(default_factory=list)
