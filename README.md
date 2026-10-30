
# AI Job Transformation & Displacement Risk Explorer (2026–2040)

An interactive data analytics project exploring how AI and automation may transform occupations across 19 industries.

## Project Overview

This application allows users to:
- Explore 388 occupation-category records.
- Filter occupations by industry and risk classification.
- Search for specific job titles.
- Compare occupational risk distributions across industries.
- Examine qualitative risk assessments.

## Technology Stack

- Python
- Pandas
- Plotly
- Streamlit
- CSV

## Dataset Structure

| Column | Description |
|---|---|
| Industry / Job Category | One of 19 industry groups |
| Job / Occupation | Occupation title |
| Description | Summary of the occupation |
| Risk Category | Very High, High, Moderate, Lower |

## Run Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Launch the application:

```bash
streamlit run app.py
```

## Methodology and Limitations

Risk categories are qualitative assessments from an initial occupation-level analysis. They are not statistically validated probabilities of job loss or official employment forecasts.

The project is exploratory and intended to support discussion about AI exposure, workforce transformation, and future skills.

## Author

Independent data analytics portfolio project.

## Project Status

Initial interactive version – 2026.
