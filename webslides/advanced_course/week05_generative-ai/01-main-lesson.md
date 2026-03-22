# Week 5 — Generative AI
# Focus: Text-to-Image, Safety Filters, and Responsible Use

> Generative AI creates new content rather than just analyzing existing data. This week focuses on text-to-image generation with attention to safety and responsible use.
---

## Generative Models Overview

- Text (GPT)
- Image (DALL-E, Stable Diffusion)
- Audio (music, voice)
- Multimodal systems that combine capabilities

> Generative models span text (GPT), images (DALL-E, Stable Diffusion), audio (music, voice), and multimodal systems that combine these capabilities.
---

## Diffusion Models

- Gradual denoising from random noise
- State-of-the-art for images
- Iteratively refines until coherent images emerge

> Diffusion models generate images through gradual denoising - starting from random noise and iteratively refining until coherent images emerge. This process is computationally intensive but produces high-quality results.
---

## VAEs and GANs

- **VAEs** — latent representations
- **GANs** — adversarial training
- Earlier generative approaches

> VAEs (Variational Autoencoders) and GANs (Generative Adversarial Networks) represent earlier generative approaches using latent spaces and adversarial training respectively.
---

## Prompting for Images

- Descriptive prompts (subject, style, lighting, composition)
- Negative prompts to exclude unwanted elements
- Seeds for reproducibility

> Image prompting requires descriptive language specifying subject, style, lighting, composition. Negative prompts exclude unwanted elements. Random seeds enable reproducibility.
---

## Control and Conditioning

- **ControlNet** — edge maps, depth maps, pose guidance
- **Guidance scales** — balance creativity vs. prompt adherence
- **Inpainting** — edit specific regions

> Control and conditioning tools like ControlNet provide fine-grained control over generation through edge maps, depth maps, or pose guidance. Guidance scales balance creativity versus prompt adherence.
---

## Safety Filters

- NSFW filters block harmful content
- Watermarking indicates AI-generated images
- Usage policies define acceptable use cases

> Safety filters block NSFW content, watermarking indicates AI-generated images, and usage policies define acceptable use cases to prevent harm.
---

## Copyright and Licensing

- Training data sourcing issues
- Output ownership and rights
- Legal frameworks still evolving

> Copyright and licensing issues arise from training data sourcing and output ownership. Legal frameworks are still evolving around generative AI.
---

## Evaluation of Generations

- **Aesthetics** — does it look good?
- **Relevance** — does it match the prompt?
- **Diversity** — can it produce varied outputs?
- Human review for subtleties

> Generation evaluation considers aesthetics (does it look good?), relevance (does it match the prompt?), diversity (can it produce varied outputs?), plus human review for subtleties.
---

## Red Teaming Generators

- Probe for unsafe outputs through adversarial prompting
- Log failures
- Update policies to prevent future problems

> Red teaming generators means probing for unsafe outputs through adversarial prompting, logging failures, and updating policies to prevent future problems.
---

## Cost and Latency

- Batch similar requests
- Cache popular generations
- Choose model sizes appropriate to use case and budget

> Cost and latency management requires batching requests, caching popular generations, and choosing model sizes appropriate to your use case and budget.
---

## Dataset Curation

- Style diversity
- Deduplication to prevent memorization
- Bias awareness in training data

> Dataset curation for training generative models requires diverse styles, deduplication to prevent memorization, and awareness of biases that affect outputs.
---

## Prompt Templates

- Reusable patterns
- Parameterized attributes
- Consistent generation across similar requests

> Prompt templates create reusable patterns with parameterized attributes, enabling consistent generation across many similar requests.
---

## Multimodal Systems

- Image + text, audio + text
- Alignment challenges — modalities must complement rather than contradict

> Multimodal systems combine image and text, or audio and text, with alignment challenges ensuring modalities complement rather than contradict each other.
---

## Guardrails for GenAI

- Safety classifier pre-filtering (before generation)
- Safety classifier post-filtering (after generation)

> Guardrails for generative AI include safety classifiers that filter both prompts (before generation) and outputs (after generation).
---

## Watermarks & Provenance

- Mark outputs as AI-generated
- Disclose artificial origin
- Prevent deception

> Watermarks and provenance tracking mark outputs as AI-generated and disclose artificial origin to prevent deception.
---

## T2I API Landscape

- OpenAI DALL-E, Stability AI, Midjourney-like services
- Capabilities, costs, and constraints differ by provider

> The text-to-image API landscape includes OpenAI DALL-E, Stability AI, and Midjourney-like services, each with different capabilities, costs, and constraints.
---

## Negative Prompts

- Exclude undesired attributes to refine outputs
- Steer away from common failure modes or unwanted styles

> Negative prompts explicitly exclude undesired attributes, steering generation away from common failure modes or unwanted styles.
---

## Seeds and Reproducibility

- Fix seeds to reproduce generations reliably
- Crucial for iterative refinement and scientific reproducibility

> Seeds and reproducibility let you regenerate the same image, crucial for iterative refinement and scientific reproducibility.
---

## Style Transfer

- Preserve content while altering style aesthetics
- Separate "what" from "how" in the representation

> Style transfer preserves image content while changing artistic style, separating 'what' from 'how' in the representation.
---

## Inpainting and Outpainting

- **Inpainting** — fill masked regions
- **Outpainting** — extend canvases beyond original boundaries
- Both useful for image editing workflows

> Inpainting fills masked regions while outpainting extends canvases beyond original boundaries, both useful for image editing workflows.
---

## Safety Classifiers

- Pre-screen prompts
- Post-check outputs
- Flag violence, sexual content, hate symbols, and other harmful categories

> Safety classifiers pre-screen prompts and post-check outputs for violence, sexual content, hate symbols, and other harmful categories.
---

## Prompt Libraries

- Shareable templates across teams
- Version prompts to track what works
- Iterate on successful patterns

> Prompt libraries share tested templates across teams, with versioning to track what works and iterate on successful patterns.
---

## Dataset Consent

- Respect training data licenses
- Opt-out mechanisms for artists whose work was used

> Dataset consent considerations include respecting training data licenses and implementing opt-out mechanisms for artists whose work was used in training.
---

## Fairness in Generations

- Represent diversity in outputs
- Avoid stereotypical associations that reinforce biases

> Fairness in generation requires representing diversity in outputs and avoiding stereotypical associations that reinforce biases.
---

## Watermark Detection

- Verify provenance
- Detect manipulations
- Adversarial attacks can remove watermarks

> Watermark detection verifies image provenance and potentially detects manipulations, though adversarial attacks can remove watermarks.
---

## Batch Generation

- Create multiple variations to explore options
- Humans select best candidates rather than using first output

> Batch generation creates multiple variations to explore options, then humans select the best candidates rather than using the first output.
---

## Post-processing

- Upscaling for higher resolution
- Color correction
- Artifact removal to polish final outputs

> Post-processing includes upscaling for higher resolution, color correction, and artifact removal to polish final outputs.
---

## API Quotas

- Monitor usage
- Backoff and retry logic for temporary quota exhaustion

> API quotas limit usage rates and total volume. Implement backoff and retry logic to handle temporary quota exhaustion gracefully.
---

## Practical Lab Preview

- Build a text-to-image mini-app with filters
- Demonstrate technical capability and responsible deployment

> Your practical lab builds a text-to-image application with safety filters, demonstrating both technical capability and responsible deployment.
---

## Reflection Prompt

- Where could generative images mislead users in your domain?
- News media, medical imaging, and legal evidence require extra caution

> Reflect on where generative images could mislead users in your domain. News media, medical imaging, and legal evidence require extra caution with AI-generated content.
---

## Reading List

- DDPM (Denoising Diffusion Probabilistic Models)
- Stable Diffusion architecture
- Safety taxonomies

> The reading list covers foundational papers on DDPM (Denoising Diffusion Probabilistic Models), Stable Diffusion architecture, and safety taxonomies.
---

## Assignment Brief

- Build T2I app
- Document safety measures and known limitations
- Demonstrate responsible deployment

> Your assignment builds a text-to-image application with comprehensive documentation of safety measures and known limitations, demonstrating responsible deployment.
