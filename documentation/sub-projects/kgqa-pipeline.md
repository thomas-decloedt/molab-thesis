---
title: KGQA Pipeline
---
Code available upon request (see README).

# Overview

Mo-Lab, the proof-of-concept implementation for the model reporting paradigm, primarily consists of a Knowledge Graph Question Answering (KGQA) pipeline. This pipeline was run on an AWS server.

# Experimentation Setup

The pipeline is capable of leveraging a domain expert model. However, for experimentation purposes, the domain expert model's inference was executed **prior to running the pipeline**. Results were translated from SQUALL to SPARQL and then were then passed to the pipeline. Consequently, during the experiments, the pipeline's primary function was limited to **linking**. Initial experimentation did to the entire process on the AWS server, but this was quickly abandoned due to much higher costs.

# Post-Processing Steps

Three post-processing techniques were evaluated:

1. **Natural Language Explanation**
2. **Tabulation**
3. **Visualization**

## Implementation Status

The post-processing steps were not robustly implemented in the pipeline due to the following reasons:

- **Limited Research Benefit**: These features were illustrative examples, unrelated to the research hypotheses. Instead, they served as motivational elements to demonstrate what the research aims to achieve in practice, highlighting its relevance to practitioners in MBSE. However, the text-to-SPARQL component remains the primary limitation in enabling model reporting and is thus the core focus of this research.
- **Engineering Complexity**: Developing and integrating these steps posed undesired technical challenges.

Despite this, partial implementations of these features were explored:

### Natural Language Explanation

- Conceptualized as a simple function that invokes ChatGPT with a structured prompt.
- Similar functionality was used to generate synthetic data.

### Tabulation

- Performed using a markup function in the a Jupyter Notebook.
- Straightforward but external to the pipeline.

### Visualization

- Implemented using [VizKG](https://github.com/fadirra/vizkg).
- Enabled visualization of results from the pipeline.

# Project Foundation

Mo-Lab's development began with a fork of the [KGQAn](https://github.com/CoDS-GCS/KGQAn) project. This repository provided a solid foundation, particularly in handling server requests and responses, allowing the research to focus on novel contributions.

## Modifications and Challenges

- **Modifications**: Substantial changes were made to adapt KGQAn to Mo-Lab's approach.
- **Challenges**: The original codebase presented a steep learning curve. While the modifications improved functionality, for our purposes, they did not necessarily enhance the code's clarity or maintainability.

# Summary

The Mo-Lab KGQA pipeline represents a significant step in demonstrating the feasibility of domain-specific knowledge graph question answering. While engineering complexities and resource constraints limited the implementation of post-processing features, the proof-of-concept showcases the potential for future work to build upon this foundation.