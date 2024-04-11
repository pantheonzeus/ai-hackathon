# Project Name: AI Hackathon

## Description
This repo provides an example how to use llama index to build a customer support assistant.
The assistant uses data about customer segments and FAQ to provide a personalized solution for the customer issue.
The data is first generated/scraped and indexed, afterwards the llama index agents are created.

## Table of Contents
- [Features](#features)
- [Getting Started](#getting-started)
- [Project structure](#project-structure)

## Features
* scrape data from Klarna FAQs and index it
* create customer segments data for Klarna
* agents to find best fitting customer segment and FAQ to customer issues

## Project structure
* app.py main function going through steps:
    * crawl data source
    * index data
    * create query engine tools for indexes
    * create an agents for the query engine tools and an LLM tool
    * run on sample customer query
* data folder contains the customer segemnt of klarna - created with ChatGPT
* prompts is a folder to store a basic user prompts

## Getting started

### Cloning the Repository

```bash
git clone https://github.com/pantheonzeus/ai-hackathon.git
```

## Running Locally

For running the app locally:
1. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source .venv/bin/activate
    ```

2. Ensure you have pip and dependencies installed   
    ```bash
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    ```

3. Copy the `sample_<your_os>.env` into `.env`, and fill in your OPENAI_KEY. 

4. Run the app only:
```bash
   python app.py
   ```

