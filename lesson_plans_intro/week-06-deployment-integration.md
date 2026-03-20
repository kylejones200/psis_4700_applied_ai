# Week 6 — Deployment and Integration

## Course Learning Outcomes (CLO) Alignment
- **CLO-D**: Apply AI concepts to analyze real-world problems and evaluate solutions
- **CLO-E**: Demonstrate understanding of data requirements and evaluation methods for AI systems

---

## Module 6.1: API Design and Validation

### Module Learning Outcomes
- **LO 6.1**: Design a simple API contract and validate inputs [CLO-D, CLO-E]
- **LO 6.2**: Understand packaging options and environment management [CLO-E]
- **LO 6.3**: Identify inputs that should be rejected and why [CLO-D, CLO-E]

### Required Materials & Resources
- **Readings**:
  - Course slides: `webslides/week06_deployment/`
  - API design best practices guide (provided)
  - Schema validation examples
- **Videos** (if available):
  - API basics and contract-first design walkthrough
  - Packaging and environment management overview
- **Interactive Activities**:
  - Minimal API template (FastAPI or equivalent) or notebook-to-web starter
  - API contract design worksheet

### Key Vocabulary
- Endpoint, API contract, Schema, Validation, Input validation, Environment management, Packaging, Dependency management

### Learning Activities (Formative - Not Graded)
1. **Self-Study**: Review course slides on API design and validation
2. **Practice Exercise**: Design an API contract for a simple use-case
3. **Hands-On Practice**: Follow along with provided template to create a minimal endpoint with validation

### Estimated Time to Complete
- Reading and review: 60-75 minutes
- Practice exercises: 45-60 minutes
- Hands-on practice: 60-90 minutes
- **Total: 2.75-3.75 hours**

---

## Module 6.2: Deployment and Monitoring

### Module Learning Outcomes
- **LO 6.4**: Package and deploy a minimal model-backed endpoint [CLO-D]
- **LO 6.5**: Define basic monitoring KPIs and rollback steps [CLO-E]
- **LO 6.6**: Understand cost considerations and security best practices [CLO-E]

### Required Materials & Resources
- **Readings**:
  - Course slides: `webslides/week06_deployment/`
  - Example monitoring checklist (provided)
  - Deployment best practices guide
- **Videos** (if available):
  - Deployment walkthrough (no-code and code options)
  - Monitoring and observability overview
- **Interactive Activities**:
  - Deployment templates (notebook share option and code option)
  - Monitoring dashboard examples
  - Cost calculator or examples

### Key Vocabulary
- Deployment, CI/CD, Canary deployment, Rollback, Observability, Monitoring, KPIs, Golden signals, Cost management, SBOM (Software Bill of Materials), Least-privilege

### Learning Activities (Formative - Not Graded)
1. **Self-Study**: Review materials on deployment and monitoring
2. **Hands-On Practice**: Deploy a minimal endpoint using provided template
3. **Practice Exercise**: Draft monitoring KPIs and rollback plan for a scenario

### Estimated Time to Complete
- Reading and review: 60-75 minutes
- Hands-on practice: 90-120 minutes
- Practice exercises: 45-60 minutes
- **Total: 3.25-4.25 hours**

---

## Gradable Activities

### Discussion: Deployment Considerations (25 points)
- **Initial Post** (200 words minimum): What input would you reject in your app (from Week 5 chatbot/pipeline) and why? Describe one monitoring KPI you would track and explain why it matters. What would trigger a rollback in your system?
- **Reply** (75 words minimum): Respond to one peer's post, either suggesting an additional KPI, discussing their rollback trigger, or sharing a similar consideration.
- **Due Dates**:
  - Initial post: End of Week 6 (Sunday 11:59 PM)
  - Reply to peer: 48 hours after initial post deadline
- **Evaluation Criteria**:
  - Clear input validation rationale (30%)
  - Appropriate KPI selection with explanation (40%)
  - Thoughtful engagement with peers in reply (30%)

### Activity: Deployment and Runbook (75 points)
- **Task**: Deploy a minimal endpoint and create a one-page runbook
- **Required Components**:
  1. **Deployed Endpoint**: Working endpoint (can be notebook share, simple web app, or API)
  2. **Runbook** (1 page): Document your deployment including:
     - **API Contract**: What inputs/outputs? What validation rules?
     - **Monitoring KPIs**: What 3-5 metrics will you track? Why?
     - **Rollback Plan**: What triggers a rollback? What are the steps?
     - **Cost Considerations**: What are the main cost drivers? How would you monitor costs?
     - **Security Notes**: What security considerations are important?
- **Format**: 
  - Link to deployed endpoint OR code/notebook files
  - Runbook as PDF or Word document, 1 page
- **Due**: End of Week 6 (Sunday 11:59 PM)
- **Evaluation Criteria**:
  - Functional deployed endpoint (30%)
  - Complete API contract and validation (20%)
  - Appropriate monitoring KPIs (20%)
  - Clear rollback plan (15%)
  - Thoughtful cost and security considerations (15%)

---

## Instructor Notes
- **Module 6.1**: Emphasize contract-first design. Provide clear examples of validation rules. Reinforce privacy and least-privilege principles.
- **Module 6.2**: Provide both no-code deployment (notebook share) and code template options. Keep scope small and achievable. Emphasize that monitoring is critical from day one.
- **Differentiation**: Provide both no-code and code deployment options. Advanced learners can add canary deployment and log sampling.
- **Asynchronous Considerations**: Provide step-by-step deployment instructions. Create video walkthroughs for both deployment options. Offer starter templates to reduce setup time. Set up Q&A forum for deployment questions. Provide clear guidance on free/low-cost deployment options.

## Accessibility & Inclusion
- Provide code snippets in accessible text format
- Ensure demo videos have captions/transcripts
- Offer alternative formats for all activities
- Provide clear instructions for all tools and platforms
- Ensure all deployment options are accessible

## References
- Course slides: `webslides/week06_deployment/`
- FastAPI docs or equivalent framework documentation
- Observability primers
- CI/CD basics
- Deployment templates: Provided in course materials
