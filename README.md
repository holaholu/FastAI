# Practical Deep Learning for Coders

This repository tracks my progress through the fast.ai course: [Practical Deep Learning for Coders](https://course.fast.ai/).

## Lesson 1: Your First Model

- **Project**: "Is it a bird?" - A simple image classifier.
- **Concepts Covered**:
  - Gathering image data using an API.
  - Using the `DataBlock` API to prepare data for a model.
  - Understanding and using pre-trained models (`resnet18`).
  - Fine-tuning a model on a new dataset.
  - Making predictions (inference) with a trained model.
- **File**: `isitabird.ipynb`
- **Deployed App**: [Bird or Forest Detector on Hugging Face Spaces](https://huggingface.co/spaces/OLA007/BirdDeployFinal)

### Deployment Notes

- Training and experimentation are done in `isitabird.ipynb` on Kaggle using fastai.
- The notebook exports three artifacts for deployment:
  - `bird_detector.pkl` (fastai export, for local experiments).
  - `classes.json` (class labels).
  - `bird_model_full.pth` (full fastai model used by the Space).
- The Hugging Face Space uses a small Gradio app defined in `BirdDeployFinal_src/app.py` with dependencies in `BirdDeployFinal_src/requirements.txt`.
