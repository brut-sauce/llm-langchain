# llm-langchain

This repository provides tools and examples for leveraging Large Language Models (LLMs) using API keys, and LangChain to build AI-powered applications. Follow the steps below to set up and run the repository on your local machine.


## Prerequisites
- Python 3.8 or above
- `pip` (Python package installer)


## Getting Started

### Step 1: Clone the Repository
```
git clone https://github.com/brut-sauce/llm-langchain.git

cd llm-langchain
```

### Step 2: Create a Virtual Environment
Create a virtual environment to isolate your project's dependencies.
```
python -m venv venv
```

### Step 3: Activate the Virtual Environment
Activate the virtual environment based on your operating system.

- On **Windows**:
```
.\venv\Scripts\activate
```

- On **Mac/Linux**:
```
source venv/bin/activate
```

### Step 4: Install Dependencies
Install the required Python packages using `requirements.txt`.
```
pip install -r requirements.txt
```

### Step 5: Set Up Environment Variables
To access external APIs, you need to set up the following environment variables:

- `OPENAI_API_KEY` (if you want to use this)
- `GOOGLE_API_KEY` (if you want to use this)
- `ANTHROPIC_API_KEY` (if you want to use this)

Recommend getting 2 keys, in order to understand the extensibility of langchain framework

#### Option 1: Add to a `.env` File
Create a `.env` file in the root directory of the project and add the keys:
```
OPENAI_API_KEY=your_openai_api_key
GOOGLE_API_KEY=your_google_api_key
ANTHROPIC_API_KEY=your_anthropic_api_key
```

#### Option 2: Add to Your Shell Configuration
You can add the variables directly to your shell configuration file (`.zshrc`, `.bashrc`, or `.bash_profile`).

For example:
```
export OPENAI_API_KEY=your_openai_api_key
export GOOGLE_API_KEY=your_google_api_key
export ANTHROPIC_API_KEY=your_anthropic_api_key
```
After editing the file, run:
```
source ~/.zshrc  # or source ~/.bashrc
```

## Running the Project

Once the environment is set up, you can start using the project. Refer to the specific examples or files. Each file can be run independently


## Deactivating the Virtual Environment
When you're done, deactivate the virtual environment:
```
deactivate
```
