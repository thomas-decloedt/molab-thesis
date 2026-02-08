# Mo-Lab: Interactive Model Reporting and Analysis in OpenCAESER

> Master's thesis — Interactive model reporting and analysis in openCAESAR through Natural Language Processing and SPARQL integration.

**[Download thesis (PDF)](main.pdf)** — Research presented at [onto Nexus Forum 2025](https://www.opencaesar.io/events/onto-Nexus-Forum-2025/Talk-18) (NASA JPL). If the link is unavailable, see [documentation/archive/onto-nexus-forum-2025-talk-18/](documentation/archive/onto-nexus-forum-2025-talk-18/) for an archived snapshot and video.

## Abstract

The task of generating reports in Model-Based Systems Engineering (MBSE) often demands significant effort and technical expertise, creating barriers resulting in inflexibility. This thesis addresses data scarcity through domain adaptation, controlled natural language (CNL), and retrieval-augmented generation (RAG). The experimental results demonstrate promising potential for interactive model reporting, evaluated through the proof-of-concept implementation Mo-Lab.

**Keywords:** Model-Based Systems Engineering, openCAESAR, text-to-SPARQL, domain adaptation, data scarcity

## Building

Requirements: LuaLaTeX, Biber, makeglossaries.

```bash
./compile.sh
```

The build includes `cover-sheet.pdf` and optionally `extended-abstract.pdf` if present (add manually if you have it).

## Citation

```bibtex
@mastersthesis{decloedt2025molab,
  author  = {Thomas Decloedt},
  title   = {Mo-Lab: Interactive Model Reporting and Analysis in OpenCAESER through Natural Language Processing and SPARQL Integration},
  school  = {Ghent University},
  year    = {2025},
  note    = {Master's thesis}
}
```

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — You may use, share, and adapt this work with attribution.

## Code

The thesis describes several sub-projects (KGQA pipeline, Flask server, notebooks, etc.). The implementation code is **available upon request** — contact the author if you need access.

## Fonts

This thesis uses **UGent Panno Text**, which is not freely redistributable. Ghent University holds a license for institutional use only; see the [UGent style guide](https://styleguide.ugent.be/basic-principles/typography.html). For an exact build you need the fonts (obtainable via UGent if eligible). For builds without them, you can switch `main.tex` to use Arial, which UGent recommends for material shared outside the university.

See [documentation/](documentation/) for thesis structure and sub-project descriptions.

**Author:** [Thomas Decloedt](https://thomas-decloedt.be)
