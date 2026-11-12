# Undergrad Machine Learning

Day-to-day content for Foundations of Machine Learning (DS3001) / Analytics 1 (DS3021).

**Course site:** https://lilykoff.github.io/undergrad_ml/

## Getting started

```bash
git clone https://github.com/lilykoff/undergrad_ml.git
cd undergrad_ml
python get_data.py   # downloads data/ from Zenodo
```

Each lecture lives in its own folder under `lectures/` with its notebook, its slides, and its images. Notebooks read data from `../../data/`.

## Updating the site

The site is built by GitHub Pages using the [Just the Docs](https://just-the-docs.com) theme with UVA colors.

- Schedule: edit `_data/schedule.yml`
- Lecture list: edit `_data/lectures.yml`
- Setup instructions: edit `setup.md`
- Colors: `_sass/color_schemes/uva.scss` and `_sass/custom/custom.scss`
