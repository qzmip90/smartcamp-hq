# 🏕️ SmartCamp HQ

SmartCamp HQ is a multi-agent AI system designed to manage camping gear operations and answer customer inquiries, powered by **Semantic Kernel** and **Azure AI**.

We use:
- 🛠️ **Semantic Kernel** for orchestrating agents
- 📑 **PDF knowledge ingestion** for product support
- 💬 **Chainlit** frontend for chatting with agents
- ☁️ Azure or Open Source LLMs from [GitHub Models Marketplace](https://github.com/marketplace/models)

---

## 🚀 Project Features

- **Product Inquiry Agent**: Answers questions about tents and gear from datasheets (e.g., Contoso Tents PDF).
- **File Search**: Allows agents to reason over PDF documents.
- **Chainlit Interface**: Easy-to-use web chat frontend.
- **Multi-model flexibility**: Support both Azure OpenAI or OSS Models.

---

## 📂 Project Structure

```plaintext
smartcamp-hq/
├── agents/
│   └── tent_inquiry_agent.py    # Agent for tent questions
├── data/
│   └── contoso-tents-datasheet.pdf  # Product knowledge base
├── frontend/
│   └── chainlit_app.py           # Chainlit UI
├── skills/
│   └── ChatRouter/
│       └── chat_router.skill     # Simple router skill
├── utils/
│   └── file_loader.py            # Helper for PDF search
├── README.md
├── requirements.txt
└── main.py                       # Main app entry
```

---

## 🛠️ Getting Started

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Set up environment variables

```bash
cp .env.example .env
```
Fill in:
- `AZURE_OPENAI_API_KEY`
- `AZURE_OPENAI_ENDPOINT`
- `AZURE_OPENAI_DEPLOYMENT_NAME`
- `AZURE_OPENAI_API_VERSION`

Or configure OSS model access if not using Azure.

### 3. Start the Chainlit app

```bash
chainlit run frontend/chainlit_app.py
```

Visit ➡️ [http://localhost:8000](http://localhost:8000) to start chatting with SmartCamp HQ!

---

## ✨ Roadmap

- [ ] Add inventory management agent
- [ ] Add order tracking agent
- [ ] Deploy on Azure App Service
- [ ] Fine-tune tent product model
