# 🧠 Multi-Tool AI Agent for Bangladesh

A simple AI assistant that can answer questions about **hospitals**, **institutions**, and **restaurants** in Bangladesh — and also search the web for general knowledge questions.

---

## 💡 What Does This Project Do?

You ask a question in plain English, and the AI agent figures out:

- 🏥 Is it about **hospitals**? → It searches the hospitals database
- 🏫 Is it about **universities or institutions**? → It searches the institutions database
- 🍽️ Is it about **restaurants**? → It searches the restaurants database
- 🌐 Is it a **general knowledge** question? → It searches the web using Tavily

---

## 🗂️ Project Structure

```
Multi-tool ai agent/
│
├── main.py                  # ▶️  Start here — runs the AI agent
│
├── tools/                   # 🔧 Each file is one "tool" the agent can use
│   ├── hospitals_tool.py    #    Searches the hospitals database
│   ├── institution_tool.py  #    Searches the institutions database
│   ├── restaurants_tool.py  #    Searches the restaurants database
│   └── web_search_tool.py   #    Searches the web (Tavily)
│
├── utils/                   # ⚙️  Helper/shared code
│   ├── llm.py               #    Sets up the AI language model (GPT-4.1-mini)
│   └── sql_executor.py      #    Converts questions → SQL → runs query → returns result
│
├── data/
│   └── sql/                 # 🗄️  The 3 SQLite databases live here
│       ├── all_bangladesh_hosptals.db
│       ├── institution_information.db
│       └── resturants.db
│
├── dataset_save_db/         # 📓 Jupyter notebooks used to download & convert datasets to DB
│   ├── bangladeshi_hospitals_db_connection.ipynb
│   ├── bangladeshi_resturant_db_connection.ipynb
│   └── institution_information_db_connection.ipynb
│
├── .env                     # 🔑 Your secret API keys (never share this file!)
├── .gitignore               # 🚫 Files that should NOT be uploaded to GitHub
└── pyproject.toml           # 📦 Project dependencies list
```

---

## ⚙️ Setup Instructions

### Step 1 — Clone the project

```bash
git clone https://github.com/your-username/your-repo-name.git
cd "Multi-tool ai agent"
```

### Step 2 — Create a `.env` file

Create a file named `.env` in the root folder and add your API keys:

```
GITHUB_TOKEN=your_github_token_here
TAVILY_API_KEY=your_tavily_api_key_here
```

> 🔑 **Where to get keys?**
> - GitHub Token → [github.com/settings/tokens](https://github.com/settings/tokens)
> - Tavily API Key → [app.tavily.com](https://app.tavily.com)

### Step 3 — Install dependencies

This project uses `uv` as the package manager:

```bash
pip install uv
uv sync
```

Or if you prefer regular pip:

```bash
pip install langchain langchain-community langchain-openai langchain-tavily openai pandas python-dotenv huggingface-hub
```

### Step 4 — Run the agent

```bash
python main.py
```

---

## 💬 Example Questions You Can Ask

| Question | Which Tool |
|---|---|
| `List top 10 hospitals in Dhaka` | 🏥 HospitalsDBTool |
| `Which universities offer medical degrees in Bangladesh?` | 🏫 InstitutionsDBTool |
| `Find restaurants in Chattogram serving biryani` | 🍽️ RestaurantsDBTool |
| `What is the healthcare policy of Bangladesh?` | 🌐 WebSearchTool |
| `How many government institutions are in Rajshahi?` | 🏫 InstitutionsDBTool |

---

## 📦 Datasets Used

All datasets are from HuggingFace:

- 🏫 [Institutional Information of Bangladesh](https://huggingface.co/datasets/Mahadih534/Institutional-Information-of-Bangladesh)
- 🏥 [All Bangladeshi Hospitals](https://huggingface.co/datasets/Mahadih534/all-bangladeshi-hospitals)
- 🍽️ [Bangladeshi Restaurant Data](https://huggingface.co/datasets/Mahadih534/Bangladeshi-Restaurant-Data)

---

## 🧰 Built With

- [LangChain](https://www.langchain.com/) — AI agent framework
- [OpenAI GPT-4.1-mini](https://github.com/marketplace/models) — via GitHub Models
- [Tavily](https://tavily.com/) — web search API
- [SQLite](https://www.sqlite.org/) — lightweight local database
- [HuggingFace Datasets](https://huggingface.co/datasets) — source data
