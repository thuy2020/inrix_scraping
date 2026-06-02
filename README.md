# INRIX and ACS Data Collection

This repository contains scripts and workflows for collecting and processing transportation and demographic data from multiple sources, including INRIX Traffic Scorecard data and the U.S. Census Bureau's American Community Survey (ACS).

## Objectives

- Scrape and download INRIX Traffic Scorecard datasets, including congestion rankings, delay metrics, and related transportation indicators.
- Retrieve demographic, commuting, and socioeconomic data from the U.S. Census Bureau ACS API.
- Clean, standardize, and merge datasets for analysis.
- Produce output files that can be used for transportation research, urban mobility analysis, and public policy studies.

## Data Sources

### INRIX: https://inrix.com/scorecard/#city-ranking-list
- Global Traffic Scorecard
- City congestion rankings
- Delay and mobility indicators

### U.S. Census Bureau ACS
- American Community Survey (ACS)
- Subject Tables (e.g., S0802 Journey to Work)
- Demographic and economic indicators
- Metropolitan statistical area (MSA) data

## Repository Structure

- inrix_2024.py – INRIX data collection and processing scripts.
- acs_2024.py = CENSUS data collection
- output/ – Generated datasets and exports.
- .env – Local environment variables (not committed to Git).
- requirements.txt – Python package dependencies.

## Notes

API keys and other credentials should be stored in environment variables or a local .env file and should not be committed to GitHub.