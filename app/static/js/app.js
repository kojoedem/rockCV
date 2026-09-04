// rockCV Frontend Application Logic

let currentResumeData = {
    title: "Professional Resume",
    template: "modern_tech",
    personal_info: {
        full_name: "",
        headline: "",
        email: "",
        phone: "",
        location: "",
        website: "",
        linkedin: "",
        github: ""
    },
    summary: "",
    experience: [],
    education: [],
    skills: [],
    projects: [],
    certifications: []
};

// Debounce helper for live preview updates
function debounce(func, wait) {
    let timeout;
    return function (...args) {
        clearTimeout(timeout);
        timeout = setTimeout(() => func.apply(this, args), wait);
    };
}

const renderPreviewDebounced = debounce(renderPreview, 300);

document.addEventListener('DOMContentLoaded', async () => {
    initEventListeners();
    await loadSampleOptions();
    // Load default sample (IT or Accounting) on start
    await loadSample('it');
});

function initEventListeners() {
    // Template Selector
    const templateSelect = document.getElementById('template-select');
    if (templateSelect) {
        templateSelect.addEventListener('change', (e) => {
            currentResumeData.template = e.target.value;
            renderPreview();
        });
    }

    // Sample Selector
    const sampleSelect = document.getElementById('sample-select');
    if (sampleSelect) {
        sampleSelect.addEventListener('change', (e) => {
            if (e.target.value) {
                loadSample(e.target.value);
            }
        });
    }

    // Form inputs live sync
    document.getElementById('resume-form').addEventListener('input', () => {
        collectFormData();
        renderPreviewDebounced();
    });

    // Profile Importer Button
    const buildProfileBtn = document.getElementById('build-profile-cv-btn');
    if (buildProfileBtn) {
        buildProfileBtn.addEventListener('click', importFromProfileLinks);
    }

    // Add buttons
    document.getElementById('add-exp-btn').addEventListener('click', () => addExperienceItem());
    document.getElementById('add-edu-btn').addEventListener('click', () => addEducationItem());
    document.getElementById('add-skill-btn').addEventListener('click', () => addSkillItem());
    document.getElementById('add-project-btn').addEventListener('click', () => addProjectItem());
    document.getElementById('add-cert-btn').addEventListener('click', () => addCertItem());

    // Export JSON
    document.getElementById('export-json-btn').addEventListener('click', exportJSON);

    // Import JSON
    document.getElementById('import-json-input').addEventListener('change', importJSON);

    // Print / Download PDF
    document.getElementById('print-pdf-btn').addEventListener('click', printResume);
}

async function loadSampleOptions() {
    try {
        const response = await fetch('/api/samples');
        const samples = await response.json();
        const sampleSelect = document.getElementById('sample-select');
        sampleSelect.innerHTML = '<option value="">-- Load Sample Resume --</option>';
        samples.forEach(s => {
            const opt = document.createElement('option');
            opt.value = s.id;
            opt.textContent = `${s.name} (${s.industry})`;
            sampleSelect.appendChild(opt);
        });
    } catch (err) {
        console.error('Failed to load sample options:', err);
    }
}

async function loadSample(sampleId) {
    try {
        const response = await fetch(`/api/samples/${sampleId}`);
        if (!response.ok) return;
        const data = await response.json();
        currentResumeData = data;

        // Update template dropdown if available
        const templateSelect = document.getElementById('template-select');
        if (templateSelect && data.template) {
            templateSelect.value = data.template;
        }

        populateForm(data);
        renderPreview();
    } catch (err) {
        console.error('Failed to load sample:', err);
    }
}

async function importFromProfileLinks() {
    const linkedinUrl = document.getElementById('import-linkedin-url').value.trim();
    const githubUrl = document.getElementById('import-github-url').value.trim();

    if (!linkedinUrl && !githubUrl) {
        alert('Please enter a LinkedIn or GitHub link/username to import.');
        return;
    }

    collectFormData();

    try {
        const response = await fetch('/api/import-profile', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                linkedin_url: linkedinUrl,
                github_url: githubUrl,
                base_resume: currentResumeData
            })
        });

        if (!response.ok) {
            alert('Failed to import profile.');
            return;
        }

        const data = await response.json();
        currentResumeData = data;
        populateForm(data);
        renderPreview();
    } catch (err) {
        console.error('Error importing profile:', err);
        alert('Error importing profile.');
    }
}

function populateForm(data) {
    // Personal Info
    document.getElementById('info-name').value = data.personal_info?.full_name || '';
    document.getElementById('info-headline').value = data.personal_info?.headline || '';
    document.getElementById('info-email').value = data.personal_info?.email || '';
    document.getElementById('info-phone').value = data.personal_info?.phone || '';
    document.getElementById('info-location').value = data.personal_info?.location || '';
    document.getElementById('info-website').value = data.personal_info?.website || '';
    document.getElementById('info-linkedin').value = data.personal_info?.linkedin || '';
    document.getElementById('info-github').value = data.personal_info?.github || '';

    // Summary
    document.getElementById('info-summary').value = data.summary || '';

    // Clear dynamic sections
    document.getElementById('exp-container').innerHTML = '';
    document.getElementById('edu-container').innerHTML = '';
    document.getElementById('skills-container').innerHTML = '';
    document.getElementById('projects-container').innerHTML = '';
    document.getElementById('certs-container').innerHTML = '';

    // Populate Experience
    (data.experience || []).forEach(exp => addExperienceItem(exp));

    // Populate Education
    (data.education || []).forEach(edu => addEducationItem(edu));

    // Populate Skills
    (data.skills || []).forEach(skill => addSkillItem(skill));

    // Populate Projects
    (data.projects || []).forEach(proj => addProjectItem(proj));

    // Populate Certifications
    (data.certifications || []).forEach(cert => addCertItem(cert));
}

function collectFormData() {
    const templateSelect = document.getElementById('template-select');

    currentResumeData = {
        title: "Professional Resume",
        template: templateSelect ? templateSelect.value : "modern_tech",
        personal_info: {
            full_name: document.getElementById('info-name').value,
            headline: document.getElementById('info-headline').value,
            email: document.getElementById('info-email').value,
            phone: document.getElementById('info-phone').value,
            location: document.getElementById('info-location').value,
            website: document.getElementById('info-website').value,
            linkedin: document.getElementById('info-linkedin').value,
            github: document.getElementById('info-github').value
        },
        summary: document.getElementById('info-summary').value,
        experience: collectExperienceData(),
        education: collectEducationData(),
        skills: collectSkillsData(),
        projects: collectProjectsData(),
        certifications: collectCertsData()
    };
}

// --- Dynamic Item Builders & Collectors ---

// Experience
function addExperienceItem(data = {}) {
    const container = document.getElementById('exp-container');
    const id = 'exp-' + Date.now() + '-' + Math.random().toString(36).substr(2, 5);
    const itemHtml = `
        <div class="p-4 border rounded-lg bg-gray-50 dark:bg-gray-800 mb-4 exp-item" id="${id}">
            <div class="flex justify-between items-center mb-2">
                <span class="font-semibold text-gray-700 dark:text-gray-200">Experience Entry</span>
                <button type="button" onclick="removeItem('${id}')" class="text-red-500 hover:text-red-700 text-sm font-bold">Remove</button>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-3 mb-2">
                <input type="text" class="exp-title input-field" placeholder="Job Title (e.g., Senior Accountant)" value="${data.title || ''}">
                <input type="text" class="exp-company input-field" placeholder="Company Name" value="${data.company || ''}">
                <input type="text" class="exp-location input-field" placeholder="Location (e.g., New York, NY)" value="${data.location || ''}">
                <input type="text" class="exp-dates input-field" placeholder="Dates (e.g., Jan 2021 - Present)" value="${data.dates || ''}">
            </div>
            <textarea class="exp-highlights input-field w-full h-20" placeholder="Key responsibilities & achievements (one per line)">${(data.highlights || []).join('\n')}</textarea>
        </div>
    `;
    container.insertAdjacentHTML('beforeend', itemHtml);
}

function collectExperienceData() {
    const items = document.querySelectorAll('.exp-item');
    return Array.from(items).map(item => {
        const highlightsRaw = item.querySelector('.exp-highlights').value;
        const highlights = highlightsRaw.split('\n').map(s => s.trim()).filter(s => s.length > 0);
        return {
            title: item.querySelector('.exp-title').value,
            company: item.querySelector('.exp-company').value,
            location: item.querySelector('.exp-location').value,
            dates: item.querySelector('.exp-dates').value,
            highlights: highlights
        };
    });
}

// Education
function addEducationItem(data = {}) {
    const container = document.getElementById('edu-container');
    const id = 'edu-' + Date.now() + '-' + Math.random().toString(36).substr(2, 5);
    const itemHtml = `
        <div class="p-4 border rounded-lg bg-gray-50 dark:bg-gray-800 mb-4 edu-item" id="${id}">
            <div class="flex justify-between items-center mb-2">
                <span class="font-semibold text-gray-700 dark:text-gray-200">Education Entry</span>
                <button type="button" onclick="removeItem('${id}')" class="text-red-500 hover:text-red-700 text-sm font-bold">Remove</button>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-3 mb-2">
                <input type="text" class="edu-degree input-field" placeholder="Degree/Diploma (e.g., B.S. Accounting)" value="${data.degree || ''}">
                <input type="text" class="edu-institution input-field" placeholder="Institution Name" value="${data.institution || ''}">
                <input type="text" class="edu-location input-field" placeholder="Location" value="${data.location || ''}">
                <input type="text" class="edu-dates input-field" placeholder="Dates (e.g., 2016 - 2020)" value="${data.dates || ''}">
            </div>
            <input type="text" class="edu-details input-field w-full" placeholder="Honors / GPA / Details" value="${data.details || ''}">
        </div>
    `;
    container.insertAdjacentHTML('beforeend', itemHtml);
}

function collectEducationData() {
    const items = document.querySelectorAll('.edu-item');
    return Array.from(items).map(item => ({
        degree: item.querySelector('.edu-degree').value,
        institution: item.querySelector('.edu-institution').value,
        location: item.querySelector('.edu-location').value,
        dates: item.querySelector('.edu-dates').value,
        details: item.querySelector('.edu-details').value
    }));
}

// Skills
function addSkillItem(data = {}) {
    const container = document.getElementById('skills-container');
    const id = 'skill-' + Date.now() + '-' + Math.random().toString(36).substr(2, 5);
    const itemHtml = `
        <div class="p-4 border rounded-lg bg-gray-50 dark:bg-gray-800 mb-4 skill-item" id="${id}">
            <div class="flex justify-between items-center mb-2">
                <span class="font-semibold text-gray-700 dark:text-gray-200">Skill Category</span>
                <button type="button" onclick="removeItem('${id}')" class="text-red-500 hover:text-red-700 text-sm font-bold">Remove</button>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-3">
                <input type="text" class="skill-category input-field" placeholder="Category (e.g. Languages)" value="${data.category || ''}">
                <input type="text" class="skill-items input-field md:col-span-2" placeholder="Skills comma-separated (e.g., Python, SQL, Financial Modeling)" value="${(data.items || []).join(', ')}">
            </div>
        </div>
    `;
    container.insertAdjacentHTML('beforeend', itemHtml);
}

function collectSkillsData() {
    const items = document.querySelectorAll('.skill-item');
    return Array.from(items).map(item => {
        const itemsRaw = item.querySelector('.skill-items').value;
        const skillList = itemsRaw.split(',').map(s => s.trim()).filter(s => s.length > 0);
        return {
            category: item.querySelector('.skill-category').value,
            items: skillList
        };
    });
}

// Projects
function addProjectItem(data = {}) {
    const container = document.getElementById('projects-container');
    const id = 'proj-' + Date.now() + '-' + Math.random().toString(36).substr(2, 5);
    const itemHtml = `
        <div class="p-4 border rounded-lg bg-gray-50 dark:bg-gray-800 mb-4 proj-item" id="${id}">
            <div class="flex justify-between items-center mb-2">
                <span class="font-semibold text-gray-700 dark:text-gray-200">Project Entry</span>
                <button type="button" onclick="removeItem('${id}')" class="text-red-500 hover:text-red-700 text-sm font-bold">Remove</button>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-3 mb-2">
                <input type="text" class="proj-name input-field" placeholder="Project Name" value="${data.name || ''}">
                <input type="text" class="proj-link input-field" placeholder="Project Link / URL" value="${data.link || ''}">
            </div>
            <textarea class="proj-desc input-field w-full h-16 mb-2" placeholder="Project Description">${data.description || ''}</textarea>
            <input type="text" class="proj-tech input-field w-full" placeholder="Technologies Used (comma separated)" value="${(data.technologies || []).join(', ')}">
        </div>
    `;
    container.insertAdjacentHTML('beforeend', itemHtml);
}

function collectProjectsData() {
    const items = document.querySelectorAll('.proj-item');
    return Array.from(items).map(item => {
        const techRaw = item.querySelector('.proj-tech').value;
        const technologies = techRaw.split(',').map(s => s.trim()).filter(s => s.length > 0);
        return {
            name: item.querySelector('.proj-name').value,
            link: item.querySelector('.proj-link').value,
            description: item.querySelector('.proj-desc').value,
            technologies: technologies
        };
    });
}

// Certifications
function addCertItem(data = {}) {
    const container = document.getElementById('certs-container');
    const id = 'cert-' + Date.now() + '-' + Math.random().toString(36).substr(2, 5);
    const itemHtml = `
        <div class="p-4 border rounded-lg bg-gray-50 dark:bg-gray-800 mb-4 cert-item" id="${id}">
            <div class="flex justify-between items-center mb-2">
                <span class="font-semibold text-gray-700 dark:text-gray-200">Certification Entry</span>
                <button type="button" onclick="removeItem('${id}')" class="text-red-500 hover:text-red-700 text-sm font-bold">Remove</button>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-3">
                <input type="text" class="cert-name input-field" placeholder="Certification Name (e.g. CPA / AWS)" value="${data.name || ''}">
                <input type="text" class="cert-issuer input-field" placeholder="Issuing Body" value="${data.issuer || ''}">
                <input type="text" class="cert-date input-field" placeholder="Date / Year" value="${data.date || ''}">
            </div>
        </div>
    `;
    container.insertAdjacentHTML('beforeend', itemHtml);
}

function collectCertsData() {
    const items = document.querySelectorAll('.cert-item');
    return Array.from(items).map(item => ({
        name: item.querySelector('.cert-name').value,
        issuer: item.querySelector('.cert-issuer').value,
        date: item.querySelector('.cert-date').value
    }));
}

function removeItem(id) {
    const elem = document.getElementById(id);
    if (elem) {
        elem.remove();
        collectFormData();
        renderPreviewDebounced();
    }
}

// --- Preview & Render ---
async function renderPreview() {
    collectFormData();
    try {
        const response = await fetch('/api/render', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(currentResumeData)
        });

        if (!response.ok) {
            console.error('Render error:', await response.text());
            return;
        }

        const html = await response.text();
        const iframe = document.getElementById('preview-iframe');
        if (iframe) {
            iframe.srcdoc = html;
        }
    } catch (err) {
        console.error('Failed to render preview:', err);
    }
}

// --- Export & Import ---
function exportJSON() {
    collectFormData();
    const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(currentResumeData, null, 2));
    const downloadAnchor = document.createElement('a');
    downloadAnchor.setAttribute("href", dataStr);
    const fileName = (currentResumeData.personal_info.full_name || 'resume').toLowerCase().replace(/\s+/g, '_') + '_resume.json';
    downloadAnchor.setAttribute("download", fileName);
    document.body.appendChild(downloadAnchor);
    downloadAnchor.click();
    downloadAnchor.remove();
}

function importJSON(event) {
    const file = event.target.files[0];
    if (!file) return;

    const reader = new FileReader();
    reader.onload = (e) => {
        try {
            const data = JSON.parse(e.target.result);
            currentResumeData = data;

            const templateSelect = document.getElementById('template-select');
            if (templateSelect && data.template) {
                templateSelect.value = data.template;
            }

            populateForm(data);
            renderPreview();
        } catch (err) {
            alert('Invalid JSON file format');
        }
    };
    reader.readAsText(file);
}

// --- Print / PDF Generation ---
function printResume() {
    const iframe = document.getElementById('preview-iframe');
    if (iframe && iframe.contentWindow) {
        iframe.contentWindow.focus();
        iframe.contentWindow.print();
    }
}
