# BirdDeployFinal_src

This folder contains a copy of the deployment code used for the **Bird or Forest Detector** app on Hugging Face Spaces.

## Overview

- **Training** happens in `../isitabird.ipynb` using fastai on Kaggle.
- The notebook exports:
  - `classes.json` – the list of class labels from `learn.dls.vocab`.
  - `bird_model_full.pth` – the full fastai model (`learn.model`) saved with `torch.save`.
- These artifacts are downloaded and placed in the Hugging Face Space repository.

## Files

- `app.py`  
  Gradio application that:

  - Loads `classes.json` for label names.
  - Loads `bird_model_full.pth` with `torch.load(..., weights_only=False)`.
  - Applies simple image preprocessing and returns class probabilities.

- `requirements.txt`  
  Minimal Python dependencies needed to run the Space (e.g. `fastai`, `torch`, `torchvision`, `gradio`).

## Live Demo

The deployed app is available here:

- https://huggingface.co/spaces/OLA007/BirdDeployFinal
