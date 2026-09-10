# Retrieval-Augmented Generation (RAG)

A document-based question-answering application built using Retrieval-Augmented Generation (RAG). The project retrieves relevant information from user-provided documents and supplies that context to a Large Language Model (LLM) to generate focused, context-aware responses.

## Overview

Traditional LLM applications can struggle when answers depend on information specific to a user's documents. This project addresses that by introducing a retrieval step before generation.

The application follows this flow:

```text
Documents
   ↓
Document Processing
   ↓
Text Chunking
   ↓
Embeddings
   ↓
Vector / Semantic Retrieval
   ↓
Relevant Context
   ↓
Large Language Model
   ↓
Generated Answer
