### Reference_Docs to Overcome dependancy Impediments-
- Pertinent to pinecone initialization 
- https://canyon-quilt-082.notion.site/Pinecone-Python-SDK-v3-0-0-Migration-Guide-056d3897d7634bf7be399676a4757c7b#a21aff70b403416ba352fd30e300bce3
- Reference-:https://python.langchain.com/v0.1/docs/integrations/vectorstores/pinecone/
- Note - Assign appropriate embedding vector dimension in Pinecone based on Hf1_embedding model's word_embedding_dimension initialized in the Sentencetransformers sections incorporated(currently by defualt sets to 768 but can be modified at users interest.) .
- To build Custom Embedding models using HuggingFacelocalpipleines(i.e huggeingFaceIpelines)(prereq-Transformers)& Ollama -[https://ollama.com/blog/embedding-models] to deploy/run locally.
- Insights on RAG-: https://python.langchain.com/v0.1/docs/use_cases/question_answering/quickstart/
- https://python.langchain.com/v0.1/docs/integrations/chat/maritalk/
- ***"""REFRESH PineCone API Key"""* & Visit Vector Data base console to view Live querying metrics & schema/ metadata of input docs.** 
##### **CARDINAL TO CLEAR CACHE BY PURGING PRIOR TO REINSTALLING PACKAGE AFRESH**
