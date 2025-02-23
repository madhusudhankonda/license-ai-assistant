# AI License Assistant 📜

AI License Assistant is a Streamlit-based application that helps developers understand, analyze, and compare software licenses using OpenAI's GPT-4 model.

## Features

- **License Analysis**: Get detailed breakdowns of common software licenses
- **License Comparison**: Compare different licenses side by side
- **Custom License Analysis**: Upload and analyze custom license documents
- **General Guidance**: Ask questions about software licensing
- **Export**: Download analyses as PDF documents

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/license-ai-assistant.git
   cd license-ai-assistant
   ```

2. **Create a virtual environment and activate it:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` file in the root directory and add your OpenAI API key:**

   ```text
   OPENAI_API_KEY=your-openai-api-key-here
   ```

## Usage

### Running Locally
1. **Start the application:**

   ```bash
   streamlit run app.py
   ```

2. **Open your browser and navigate to `http://localhost:8501`.**

### Running with Docker

1. **Build and start the container:**
   ```bash
   docker compose up -d --build
   ```

2. **Open your browser and navigate to `http://localhost:8501`.**

3. **Stop the container:**
   ```bash
   docker compose down
   ```

3. **Use the different tabs to:**
   - Analyze common software licenses.
   - Compare different licenses.
   - Upload custom license documents.
   - Ask general licensing questions.

## Project Structure
