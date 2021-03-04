FROM watinha/nltk

# Download CoreNLP full Stanford Tagger for English
RUN wget https://nlp.stanford.edu/software/stanford-ner-4.2.0.zip && \
    unzip stanford-ner-*.zip && \
    rm stanford-ner-*.zip && \
    mv stanford-ner-* stanford-corenlp

# Install openjdk8 for Stanford Tagger
RUN apk add --no-cache openjdk8

# Install requirements
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

# Download NLTK data
RUN python -c "import nltk; nltk.download('punkt')"

# Copy project files in working directory
COPY src .
COPY examples ./examples

# Set input_file_name env variable
ENV input_file_name="examples/test1.txt"

CMD [ "/bin/sh", "-c", "python ./run.py $input_file_name" ]