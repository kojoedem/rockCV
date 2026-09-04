from typing import Dict, Any

SAMPLE_RESUMES: Dict[str, Dict[str, Any]] = {
    "accounting": {
        "id": "accounting",
        "name": "Accounting & Finance Professional",
        "industry": "Accounting / Finance",
        "template": "accounting_corporate",
        "title": "Senior Financial Analyst Resume",
        "personal_info": {
            "full_name": "Alexander Morgan, CPA",
            "headline": "Senior Financial Analyst & Corporate Auditor",
            "email": "alexander.morgan@example.com",
            "phone": "+1 (555) 234-5678",
            "location": "Chicago, IL",
            "website": "https://alexmorgan-finance.com",
            "linkedin": "linkedin.com/in/alexmorgan-cpa",
            "github": ""
        },
        "summary": "Results-driven Certified Public Accountant (CPA) with over 7 years of experience in financial reporting, corporate auditing, variance analysis, and budget forecasting. Proven track record of optimizing accounting workflows, reducing closing cycle times by 30%, and identifying $1.2M in tax credits across enterprise balance sheets.",
        "experience": [
            {
                "title": "Senior Financial Analyst",
                "company": "Midwest Capital Partners",
                "location": "Chicago, IL",
                "dates": "Mar 2021 - Present",
                "highlights": [
                    "Lead quarterly and annual financial closing processes for $120M division, ensuring 100% GAAP compliance.",
                    "Develop complex financial models using Excel and SAP BPC to forecast cash flows and evaluating capital expenditure options.",
                    "Collaborate with internal auditors to streamline SOX compliance controls, reducing internal audit friction by 25%."
                ]
            },
            {
                "title": "Staff Accountant / Auditor",
                "company": "Deloitte & Touche LLP",
                "location": "Chicago, IL",
                "dates": "Jul 2017 - Feb 2021",
                "highlights": [
                    "Executed financial statement audits for Fortune 500 manufacturing clients, reviewing balance sheets, income statements, and tax provisions.",
                    "Identified material weaknesses in client revenue recognition procedures and implemented corrective action plans.",
                    "Mentored junior audit associates on statutory reporting and automated ledger reconciliation tools."
                ]
            }
        ],
        "education": [
            {
                "degree": "Bachelor of Science in Accountancy",
                "institution": "University of Illinois Urbana-Champaign",
                "location": "Urbana, IL",
                "dates": "2013 - 2017",
                "details": "Summa Cum Laude, GPA 3.92/4.00"
            }
        ],
        "skills": [
            {
                "category": "Accounting & Financial",
                "items": ["GAAP & IFRS Standards", "Financial Modeling", "Corporate Tax Planning", "Variance & Trend Analysis", "SOX Compliance"]
            },
            {
                "category": "Software & Tools",
                "items": ["SAP ERP", "Oracle NetSuite", "QuickBooks Premier", "Advanced Excel (VBA/Macros)", "Power BI", "Tableau"]
            }
        ],
        "projects": [
            {
                "name": "Automated Reconciliation Pipeline",
                "description": "Designed custom VBA scripts to automate high-volume bank reconciliations, reducing manual review hours by 15 hours weekly.",
                "link": "",
                "technologies": ["Excel VBA", "SQL", "NetSuite API"]
            }
        ],
        "certifications": [
            {
                "name": "Certified Public Accountant (CPA)",
                "issuer": "Illinois Board of Examiners",
                "date": "2018"
            },
            {
                "name": "Chartered Financial Analyst (CFA) - Level II Candidate",
                "issuer": "CFA Institute",
                "date": "2023"
            }
        ]
    },
    "it": {
        "id": "it",
        "name": "IT & Software Engineering",
        "industry": "Information Technology / Software",
        "template": "modern_tech",
        "title": "Senior Software Engineer Resume",
        "personal_info": {
            "full_name": "Samantha Chen",
            "headline": "Senior Full-Stack & Cloud Architect",
            "email": "samantha.chen@techmail.io",
            "phone": "+1 (555) 876-5432",
            "location": "San Francisco, CA",
            "website": "https://samchen.dev",
            "linkedin": "linkedin.com/in/samchen-dev",
            "github": "github.com/samchen-code"
        },
        "summary": "Full-Stack Software Engineer and Cloud Architect with 8+ years building high-concurrency microservices, scalable RESTful APIs, and responsive web applications. Expert in Python (FastAPI/Django), React, TypeScript, and AWS cloud infrastructure. Led teams delivering 99.99% uptime services serving over 2 million active daily users.",
        "experience": [
            {
                "title": "Lead Software Engineer",
                "company": "CloudScale Technologies",
                "location": "San Francisco, CA",
                "dates": "Jan 2021 - Present",
                "highlights": [
                    "Architected high-throughput async FastAPI microservices handling 10,000+ requests/sec with average latency < 45ms.",
                    "Migrated monolithic backend to AWS Kubernetes (EKS), reducing infrastructure expenditure by $180,000 annually.",
                    "Mentored a team of 8 engineers, enforcing strict CI/CD pipelines, unit testing coverage (> 90%), and code review standards."
                ]
            },
            {
                "title": "Software Engineer",
                "company": "DataPulse Analytics",
                "location": "San Jose, CA",
                "dates": "Jun 2017 - Dec 2020",
                "highlights": [
                    "Engineered real-time dashboard applications using React, Next.js, and WebSockets.",
                    "Designed PostgreSQL & Redis caching strategy that improved page load speed by 60%.",
                    "Integrated OAuth2 and JWT authentication across all external customer endpoints."
                ]
            }
        ],
        "education": [
            {
                "degree": "B.S. in Computer Science",
                "institution": "University of California, Berkeley",
                "location": "Berkeley, CA",
                "dates": "2013 - 2017",
                "details": "Honors in Computer Science, ACM Student Chapter President"
            }
        ],
        "skills": [
            {
                "category": "Languages & Frameworks",
                "items": ["Python (FastAPI, Django)", "JavaScript / TypeScript", "React", "Node.js", "Go", "HTML5/CSS3/Tailwind CSS"]
            },
            {
                "category": "Cloud & DevOps",
                "items": ["AWS (EC2, Lambda, S3, RDS)", "Docker & Kubernetes", "Terraform", "GitHub Actions", "PostgreSQL", "Redis"]
            }
        ],
        "projects": [
            {
                "name": "FastCV Generator",
                "description": "Open-source asynchronous resume generation suite built with FastAPI and Tailwind CSS.",
                "link": "https://github.com/samchen-code/fastcv",
                "technologies": ["FastAPI", "Python", "Tailwind CSS", "Docker"]
            }
        ],
        "certifications": [
            {
                "name": "AWS Certified Solutions Architect – Professional",
                "issuer": "Amazon Web Services",
                "date": "2022"
            },
            {
                "name": "Certified Kubernetes Administrator (CKA)",
                "issuer": "CNCF",
                "date": "2021"
            }
        ]
    },
    "executive": {
        "id": "executive",
        "name": "Executive & Operations Leadership",
        "industry": "Management / Operations",
        "template": "executive_leadership",
        "title": "Director of Operations Resume",
        "personal_info": {
            "full_name": "Marcus Vance",
            "headline": "Director of Operations & Organizational Strategy",
            "email": "marcus.vance@leadership.org",
            "phone": "+1 (555) 432-1098",
            "location": "New York, NY",
            "website": "https://marcusvance.com",
            "linkedin": "linkedin.com/in/marcusvance-ops",
            "github": ""
        },
        "summary": "Dynamic Executive Leader with 12+ years driving strategic growth, operational excellence, and organizational transformation across multi-site global enterprises. Adept at scaling operations from $15M to $80M ARR, optimizing supply chain logistics, and building high-performance cross-functional teams.",
        "experience": [
            {
                "title": "Director of Operations",
                "company": "Apex Global Solutions",
                "location": "New York, NY",
                "dates": "2019 - Present",
                "highlights": [
                    "Oversaw $85M annual operational budget and 140+ personnel across North America and Europe.",
                    "Restructured procurement operations, yielding a 18% cost reduction in global vendor contracts within 12 months.",
                    "Spearheaded enterprise Agile adoption, increasing product launch cadence by 40%."
                ]
            },
            {
                "title": "Senior Operations Manager",
                "company": "Vanguard Logistics Inc.",
                "location": "New York, NY",
                "dates": "2014 - 2019",
                "highlights": [
                    "Managed distribution center operations serving over 500 retail outlets nationwide.",
                    "Implemented Lean Six Sigma standards, achieving a 99.4% on-time order fulfillment rate."
                ]
            }
        ],
        "education": [
            {
                "degree": "Master of Business Administration (MBA)",
                "institution": "Columbia Business School",
                "location": "New York, NY",
                "dates": "2012 - 2014",
                "details": "Concentration in Operational Strategy & Executive Leadership"
            },
            {
                "degree": "B.S. in Industrial Engineering",
                "institution": "Cornell University",
                "location": "Ithaca, NY",
                "dates": "2008 - 2012",
                "details": "Dean's List"
            }
        ],
        "skills": [
            {
                "category": "Core Competencies",
                "items": ["Strategic Planning", "P&L Management", "Supply Chain Optimization", "Change Management", "M&A Integration"]
            },
            {
                "category": "Methodologies",
                "items": ["Lean Six Sigma", "Agile & Scrum", "OKRs & KPI Tracking", "Vendor Negotiations"]
            }
        ],
        "projects": [],
        "certifications": [
            {
                "name": "Lean Six Sigma Black Belt (LSSBB)",
                "issuer": "ASQ",
                "date": "2016"
            },
            {
                "name": "Project Management Professional (PMP)",
                "issuer": "PMI",
                "date": "2015"
            }
        ]
    },
    "marketing": {
        "id": "marketing",
        "name": "Marketing & Digital Growth",
        "industry": "Marketing / Creative / Communications",
        "template": "creative_portfolio",
        "title": "Digital Growth Lead Resume",
        "personal_info": {
            "full_name": "Elena Rostova",
            "headline": "Head of Digital Marketing & Brand Growth",
            "email": "elena.rostova@growthmarket.com",
            "phone": "+1 (555) 654-3210",
            "location": "Austin, TX",
            "website": "https://elenarostova.creative",
            "linkedin": "linkedin.com/in/elena-rostova-mkt",
            "github": ""
        },
        "summary": "Creative and data-obsessed Marketing Director with 6+ years driving customer acquisition, content strategy, and multi-channel performance marketing. Managed $3M+ annual ad budgets across Google, Meta, and LinkedIn, generating 350% ROI and boosting organic site traffic by 4x.",
        "experience": [
            {
                "title": "Head of Digital Growth",
                "company": "BrightSpark SaaS",
                "location": "Austin, TX",
                "dates": "2021 - Present",
                "highlights": [
                    "Designed omnichannel acquisition strategy scaling user base from 50k to 300k active subscribers.",
                    "Optimized conversion rate funnel (CRO), resulting in a 32% lift in free-to-paid conversion.",
                    "Directed creative team producing video assets, landing pages, and email nurture campaigns."
                ]
            },
            {
                "title": "Senior Content & Performance Marketer",
                "company": "Elevate Marketing Group",
                "location": "Austin, TX",
                "dates": "2018 - 2021",
                "highlights": [
                    "Executed SEO strategy increasing non-branded organic search traffic by 240% in 14 months.",
                    "Produced weekly analytics reports tracking CAC, LTV, ROAS, and retention metrics for C-suite."
                ]
            }
        ],
        "education": [
            {
                "degree": "B.A. in Advertising & Digital Media",
                "institution": "University of Texas at Austin",
                "location": "Austin, TX",
                "dates": "2014 - 2018",
                "details": "President of University Marketing Association"
            }
        ],
        "skills": [
            {
                "category": "Growth & Strategy",
                "items": ["Performance Marketing", "SEO / SEM Strategy", "CRO & A/B Testing", "Email Marketing & Automation", "Brand Storytelling"]
            },
            {
                "category": "Analytics & Tools",
                "items": ["Google Analytics 4", "HubSpot", "Meta Ads Manager", "Semrush", "Figma", "Webflow"]
            }
        ],
        "projects": [
            {
                "name": "Viral Rebrand Campaign 'SparkTheFuture'",
                "description": "Led complete visual and message rebranding campaign yielding 12M impressions across social channels.",
                "link": "https://elenarostova.creative/spark",
                "technologies": ["Meta Ads", "HubSpot", "Figma"]
            }
        ],
        "certifications": [
            {
                "name": "Google Ads & Analytics Certified",
                "issuer": "Google",
                "date": "2023"
            },
            {
                "name": "HubSpot Inbound Marketing Certification",
                "issuer": "HubSpot Academy",
                "date": "2022"
            }
        ]
    },
    "healthcare": {
        "id": "healthcare",
        "name": "Healthcare & Clinical Care",
        "industry": "Healthcare / Nursing",
        "template": "classic_professional",
        "title": "Registered Nurse & Clinical Supervisor Resume",
        "personal_info": {
            "full_name": "David Miller, RN, BSN",
            "headline": "Nurse Specialist & Clinical Supervisor",
            "email": "david.miller@healthnet.org",
            "phone": "+1 (555) 987-6543",
            "location": "Boston, MA",
            "website": "",
            "linkedin": "linkedin.com/in/davidmiller-rn",
            "github": ""
        },
        "summary": "Dedicated Registered Nurse with 9 years of ICU and emergency clinical experience. Compassionate patient advocate skilled in critical care management, trauma triage, electronic health records (Epic), and multidisciplinary team leadership. Recognized for zero medication administration errors and excellence in patient safety standards.",
        "experience": [
            {
                "title": "Clinical Nurse Supervisor - ICU",
                "company": "Massachusetts General Hospital",
                "location": "Boston, MA",
                "dates": "2019 - Present",
                "highlights": [
                    "Supervise 18 RNs and clinical staff in a 24-bed Intensive Care Unit delivering level-1 trauma care.",
                    "Ensure strict compliance with Joint Commission standards and infection control protocols.",
                    "Spearheaded hospital-wide patient fall prevention program reducing incidents by 40%."
                ]
            },
            {
                "title": "Staff Registered Nurse - Emergency Dept.",
                "company": "Boston Medical Center",
                "location": "Boston, MA",
                "dates": "2015 - 2019",
                "highlights": [
                    "Provided rapid emergency response, triage assessment, and critical intervention for acute trauma patients.",
                    "Utilized Epic Systems EHR for seamless, real-time documentation and patient charting."
                ]
            }
        ],
        "education": [
            {
                "degree": "Bachelor of Science in Nursing (BSN)",
                "institution": "Northeastern University",
                "location": "Boston, MA",
                "dates": "2011 - 2015",
                "details": "Sigma Theta Tau International Honor Society of Nursing"
            }
        ],
        "skills": [
            {
                "category": "Clinical Competencies",
                "items": ["Critical Care Nursing", "Trauma Triage & Resuscitation", "Patient Advocacy", "EHR / Epic Systems", "Infection Prevention"]
            },
            {
                "category": "Certifications & Standard Skills",
                "items": ["BLS / ACLS Certified", "PALS Certification", "IV Administration & Phlebotomy"]
            }
        ],
        "projects": [],
        "certifications": [
            {
                "name": "Registered Nurse (RN) License",
                "issuer": "Massachusetts Board of Registration in Nursing",
                "date": "2015"
            },
            {
                "name": "Advanced Cardiovascular Life Support (ACLS)",
                "issuer": "American Heart Association",
                "date": "2023"
            },
            {
                "name": "Basic Life Support (BLS)",
                "issuer": "American Heart Association",
                "date": "2023"
            }
        ]
    }
}
