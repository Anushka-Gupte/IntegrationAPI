# IntegrationAPI — LLM Integration API (LangServe + Mistral)

A small, local API to expose LLM endpoints you can integrate into any web application. Built with LangServe to provide a production-ready HTTP API and Swagger UI for interactive exploration. Uses a Mistral model (locally hosted via Ollama or a compatible runtime) as the LLM backend.

This repository provides:
- An HTTP API that wraps LLM inference for easy integration into web frontends or services
- Swagger UI for interactive testing and documentation
- Example configuration for connecting a Mistral model
- Guidance for local development and deployment

Quick summary: start LangServe with the included model configuration, open Swagger UI to try endpoints, then call the API from your frontend or server code.

---

## Screenshots

![](/api/photo1.jpeg)

![](/api/photo2.jpeg)

![](/api/photo3.jpeg)

## Features
- Exposes LLM endpoints over HTTP (JSON-based)
- Interactive Swagger UI at /docs
- Pluggable model configuration (point to local Mistral via Ollama or another host)
- Example request/response formats and integration snippets
- Optional streaming support if enabled by the model/runtime

---

## Prerequisites
- Python 3.10+
- pip
- LangServe installed (see installation below)
- A Mistral model available in your model runtime:
  - Common option: Ollama running locally with a Mistral model pulled
  - Alternative: any LangServe-compatible LLM backend exposing the model

---

## Contributing
Contributions welcome. Please:
- Open an issue for feature requests or bugs
- Make PRs against main with clear descriptions and tests where applicable
