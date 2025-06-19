# 🧠 Local LLM Inference API (FastAPI + llama.cpp)

A production-grade, containerized FastAPI backend for running quantized GGUF language models via `llama.cpp`.  
Supports local inference with models like Mistral, LLaMA 3, MythoMax, and Chronos Hermes.

This project forms the backend layer of a broader system for creative tools, research assistants, and experimental RAG-based storytelling agents — all powered locally.

---

## 🚀 Features

- 🔒 **Private, local inference** – no API keys, no 3rd-party requests
- 🐳 **Dockerized** with Makefile automation
- ⚡ **FastAPI** backend with route modularization
- 🧪 **Test suite** using `pytest` and `unittest.mock`
- ⚙️ **Config system** using `.env` + `config.yml`
- 📦 **Supports quantized .gguf models** via `llama-cpp-python`

---

## 🐳 Usage

### 🔧 Setup

```bash
cp .env.example .env
make up        # Build and run the container
```

### ✅ Test

```bash
make test-local    # Runs tests locally
make test          # Runs tests in Docker
```

### 🛑 Stop

```bash
make down
```

---

## 📋 Config

Config values come from both:

- `config.yml` – Model path, API host/port, etc.
- `.env` – Used for environment-level overrides

---

## 🧪 Test Coverage

- ✅ `run_prompt()` logic via mock injection
- ✅ FastAPI route: `/infer`
- 🔜 More integration tests planned
- 🔜 Add streaming support

---
## 🔭 Roadmap

A living development plan — checkmarks mark what's done, and everything else is on deck.

- [x] Clone Dockerized FastAPI boilerplate
- [x] Choose initial inference model & download `.gguf`
- [x] Load the model via `llama-cpp`
- [x] Connect model to FastAPI inference route
- [x] Validate functionality with test prompts

### Up Next

- [ ] 🖼 Build Tauri-based desktop UI
- [ ] 📚 Add RAG pipeline (chunking, embeddings, vector DB)
- [ ] 🌐 Research self-hosting / remote deployment options
- [ ] 🚀 Deploy project to selected hosting platform
- [ ] 🔁 Implement hot-reload dev server (Uvicorn + volume mounts)
- [ ] 🛠 Refactor Dockerfile for multi-stage (dev/prod)
- [ ] 🧪 Split test/dev containers with `docker-compose.override.yml`

### 🛣️ Down the Road

- [ ] 🔐 Add Auth Layer
    - Options: API key, OAuth2, JWT, or local password-protected endpoints
    - Might pair well with user/session context for future multi-user RAG
- [ ] 🔄 Model Switching Mechanism
    - Dynamically load different .gguf models via config or runtime param
- [ ] 🌊 Streaming Responses
    - Add `stream=True` support for real-time token generation in `/infer/`
- [ ] ✅ Test Coverage Expansion
    - Auth endpoints, error handling, config fallbacks
---

## 🧠 Target Models for Local Inference

| Model | Strength | Notes | Download |
|-------|----------|-------|----------|
| ✅ **Mistral-7B-Instruct** | Fast, lightweight | Perfect for bootstrapping | [mistral-7b-instruct.Q4_K_M.gguf](https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF) |
| ⏳ **LLaMA 3 8B** | Balanced & powerful | Step up once base is stable | [llama-3-8B-Instruct.Q4_K_M.gguf](https://huggingface.co/TheBloke/Llama-3-8B-Instruct-GGUF) |
| 🌀 **MythoMax 13B** | Imaginative & surreal | Great for narrative/story gen | [MythoMax-L2-13B.Q4_K_M.gguf](https://huggingface.co/TheBloke/MythoMax-L2-13B-GGUF) |
| ⏱ **Chronos Hermes 13B** | Time-sensitive & verbose | Ideal for longform + RAG fusion | [Chronos-Hermes-13B.Q4_K_M.gguf](https://huggingface.co/TheBloke/Chronos-Hermes-13B-GGUF) |

---

## 📄 License

MIT – free for personal or commercial use.