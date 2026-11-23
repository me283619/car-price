FROM python:3.12-slim

# Hugging Face Spaces بيشغّل الحاوية بمستخدم عادي (UID 1000)
RUN useradd -m -u 1000 user
USER user

ENV PATH="/home/user/.local/bin:$PATH" \
    GRADIO_SERVER_NAME=0.0.0.0 \
    GRADIO_SERVER_PORT=15157

WORKDIR /app

COPY --chown=user requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY --chown=user . .

EXPOSE 7860

CMD ["python", "app.py"]
