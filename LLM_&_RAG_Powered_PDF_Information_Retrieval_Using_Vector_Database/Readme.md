# LLM & RAG- leveraged Information Retrieval System using Vector Database Store

### Designed Retrieval Query Assistant for given Document employing-:
1. Vector Database-Store -(Pinecone) --built with underlying metric of Cosine |||Arity in Embedding Space.2.
2. Huggingface Embedding model(From HuggingfaceEmbeddings & Sentence Transformers)
   - Addtionally try building on custom embedding model using **HuggingFacelocal pipelines & OllamaEmbeddings**(refer Imp_notes.md) & manuevering Embedding_Vector_Dimensions.
4. Open-Source LLM models built on top of Ollama, HuggingFace - (LLAMA-3, PHI-3) for fetching query results
5. LANGCHAIN Q_A (To invoke answer from Document_passage(input_document) constructed based on selected chunks containing relevant info pertained to User's Query & constrained with prompt.)
---------------------------------------------------------------------------------------------------------------------------------------------------------------
