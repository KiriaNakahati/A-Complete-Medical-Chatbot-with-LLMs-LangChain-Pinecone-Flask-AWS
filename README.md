# A-Complete-Medical-Chatbot-with-LLMs-LangChain-Pinecone-Flask-AWS

## Project Overview

This project is an end-to-end Medical Chatbot built using Large Language Models, designed to answer health-related questions in a conversational way. The system leverages a Retrieval-Augmented Generation approach, combining semantic search with generative AI to provide accurate and context-aware responses.

The chatbot integrates multiple technologies: LangChain is used to orchestrate the LLM pipeline, Pinecone serves as a vector database for  similarity search over medical knowledge, and Flask provides a web interface for user interaction. The application is designed to be scalable and production-ready, with support for deployment on AWS using containerization and CI/CD workflows.

Users can ask medical questions in natural language, and the chatbot retrieves relevant information from a knowledge base before generating responses, improving reliability compared to purely generative models. This project demonstrates how to build a full-stack AI application, combining machine learning, backend development, and cloud deployment in a healthcare-focused use case.

# How to run?

# steps:
clone the repository

```bash
Project repo: git clone https://github.com/KiriaNakahati/A-Complete-Medical-Chatbot-with-LLMs-LangChain-Pinecone-Flask-AWS.git
```
### tools: 
```bash 
1. You will need to install Anaconda as a package manager: https://www.anaconda.com/download
2. Configure it so it appears in the PowerShell of your VS Code: after installation -> search for Anaconda Prompt -> run "conda init powershell"
```

### step 01- create a conda enviroment after opening the repository

```bash
conda create -n medibot python=3.10 -y
```

```bash
conda activate medibot
```

## step 02 - install the requirements

```bash
pip install -r requirements.txt
```

## tech stack

```bash
- python
- groq
- langchain - framework para arquitetura
- pineCone as my vector database
- flask for back and front development
- aws for the deployment -> CI / CD
```

## steps in general

```bash
1 - github repository
2 - project template 
3 - project setup
4 - notebook Eap
5 - modular code 
6 - web app
```
