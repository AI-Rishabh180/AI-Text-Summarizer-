## 🧠 AI Text Summarizer

AI Text Summarizer is a **production-level, full-stack web application** designed to summarize long paragraphs, articles, and documents using **Generative AI**. The application allows users to input large amounts of text and receive a **clear, concise summary in real time**.

The backend is built with **FastAPI** and integrates a **Hugging Face Transformer model (`facebook/bart-large-cnn`)** for high-quality text summarization. To efficiently handle long documents, the system implements **text chunking**, ensuring model limitations are respected while maintaining summary accuracy. Each generated summary is stored in a **SQLite database** for persistence and future reference.

The frontend is developed using **React (Vite)** and **Tailwind CSS**, providing a **clean, modern, and user-friendly interface**. The application follows a well-defined **client–server architecture** and includes proper **API communication, error handling, and loading states**.

This project demonstrates **real-world usage of Generative AI in a full-stack environment** and is well-suited for **portfolios, internships, and entry-to-mid level AI or full-stack engineering roles**.
