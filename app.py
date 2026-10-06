import streamlit as st

from rag import ResearchAssistant
from utils import extract_pdf_text

from ollama import chat


st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="📚",
    layout="wide"
)


st.title("📚 AI Research Assistant")

st.write(
    "Upload a research paper and ask questions about it."
)


@st.cache_resource
def load_assistant():

    return ResearchAssistant()


assistant = load_assistant()

with st.sidebar:

    st.header("📄 Research Paper")

    uploaded_file = st.file_uploader(
        "Upload a PDF",
        type=["pdf"]
    )

if uploaded_file:

    st.success(
        f"Uploaded: {uploaded_file.name}"
    )

    if st.button("⚙️ Process Document"):

        with st.spinner(
            "Reading and processing PDF..."
        ):

            # Extract text
            text = extract_pdf_text(
                uploaded_file
            )

            # Store chunks
            chunks = assistant.add_document(
                text,
                uploaded_file.name
            )

        st.success(
            f"✅ Document processed! "
            f"{len(chunks)} chunks created."
        )


        st.subheader("📦 Document Chunks")

        for i, chunk in enumerate(chunks):

            with st.expander(
                f"Chunk {i + 1}"
            ):

                st.write(chunk)


st.divider()

st.header("💬 Ask Your Research Assistant")


question = st.text_input(
    "Ask a question about your research paper"
)


if st.button("🔍 Ask"):

    if not question:

        st.warning(
            "Please enter a question."
        )

    else:
        with st.spinner("Searching the research paper..."):
            results = assistant.search(
                question,
                n_results=5 )
        documents = results["documents"][0]
        st.subheader("🔎 Relevant Sections")
        for i, document in enumerate(documents):
            with st.expander(f"Relevant Section {i + 1}"):
                st.write(document)

        context = "\n\n".join(
            documents
        )

        prompt = f"""
You are an AI research assistant.

Answer the user's question using ONLY
the research paper context provided below.

If the answer cannot be found in the context,
say:

"I could not find this information in the
uploaded research paper."

Do not make up information.

Research paper context:

{context}
User question:
{question}
"""
        with st.spinner("Llama 3.2 is generating the answer..."):
            response = chat(
                model="llama3.2",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

        st.subheader("🤖 Answer")
        st.write(response["message"]["content"])