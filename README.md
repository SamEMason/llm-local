# 🚀 FastAPI Docker Boilerplate

A minimal, reusable FastAPI + Docker starter template for quickly spinning up API projects.

Designed to be cloned or used with tools like `degit` to kickstart development with a production-ready base.

---

## ⚡ Boilerplate Usage

You can use this repo as a boilerplate using [`degit`](https://github.com/Rich-Harris/degit):

```bash
npx degit your-username/fastapi-docker-boilerplate my-new-api
cd my-new-api
make up
```

Or clone manually:

```bash
git clone https://github.com/your-username/fastapi-docker-boilerplate.git my-new-api
cd my-new-api
rm -rf .git
git init
```

---

## 🐳 Usage

### Build and Run

```bash
make up
```

This will build the Docker image and run the container.

### Stop and Remove

```bash
make down
```

Stops and removes the running container.

### Rebuild Container

```bash
make rebuild
```

Stops the container, rebuilds the image, and runs it again.

---

## 📂 Environment Setup

1. Copy `.env.example` to `.env`
2. Update variables as needed.

---

## 📄 License

MIT – free for personal or commercial use. No guarantees, use at your own risk.

---

## 🤝 Contribute

PRs and issues welcome. Fork it, improve it, and make something cool.