# Webslides Reorganization - Complete

## Overview
All webslides have been reorganized to align with the 8-week Introduction to Applied AI framework defined in `lesson_plans_intro/`.

## New Structure

```
webslides/
├── week01_what-is-ai/       # Week 1: What is AI? (8 slides)
├── week02_data-learning/    # Week 2: Data & Learning (7 slides)
├── week03_applications/     # Week 3: Applications (9 slides)
├── week04_ethics-policy/    # Week 4: Ethics & Policy (7 slides)
├── week05_gen-convo/        # Week 5: Generative & Conversational (16 slides)
├── week06_deployment/       # Week 6: Deployment & Integration (10 slides)
├── week07_workshop/         # Week 7: Project Workshop (7 slides)
├── week08_capstone/         # Week 8: Capstone (3 slides)
├── 00_foundations/          # Pre-course foundational materials (3 slides)
├── advanced/                # Advanced course materials (5 slides)
├── reference/               # Reference materials (1 slide)
└── images/                  # All images (centralized)
```

## What Changed

### 1. Folder-Based Organization
- Each week now has its own folder
- All related materials grouped together
- Clear progression from Week 1 through Week 8

### 2. Consistent Numbering
- Main lesson files: `01-main-lesson.md`
- Supporting materials: `02-`, `03-`, etc.
- Easy to see the recommended reading order

### 3. Updated Navigation
- `index.html` updated to use new folder structure
- Week-based navigation in sidebar
- Links to most important slides from each week

### 4. README Files
- Each week folder has a README explaining:
  - Learning objectives
  - Duration
  - Key vocabulary
  - Description of each webslide

## How to Use

### For Students
1. Open `index.html` in a browser
2. Navigate week-by-week using the sidebar
3. Start with "Main Lesson" for each week
4. Explore supporting materials as needed

### For Instructors
1. Each week folder aligns with lesson plans in `/lesson_plans_intro/`
2. Use `01-main-lesson.md` as the core presentation
3. Pull in additional slides as needed for your class
4. READMEs provide context for each slide's purpose

## Total Content
- **68 organized webslides** across all weeks
- **11 README files** documenting structure
- **8 core week folders** matching lesson plan framework
- **Maintained backward compatibility** - old files still in root directory

## Next Steps

### Optional Cleanup (Future)
- Remove duplicate files from root directory after verifying all links work
- Archive old naming conventions
- Create additional cross-reference documents

### Testing
1. Open `index.html` in browser
2. Test navigation for each week
3. Verify all images load correctly
4. Check that PDF export works

## Benefits

1. **Clear Alignment**: Webslides match lesson plans exactly
2. **Easy Navigation**: Week-by-week progression is intuitive
3. **Better Discoverability**: Related materials grouped together
4. **Scalable**: Easy to add new materials to appropriate weeks
5. **Maintainable**: Clear structure reduces confusion

## Files Reference

See `WEBSLIDES_REORGANIZATION_PLAN.md` for detailed file mapping showing which original files went into which new locations.

---

**Reorganization completed**: December 29, 2025
**Aligned with**: `/lesson_plans_intro/` 8-week framework
**Status**: Ready for use
