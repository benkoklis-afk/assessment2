#latest version that doesnt enforce 668 error (external-managed enviroment requirement for pip)
FROM alpine:3.16

# Install Python and the required tools bash, wget
RUN apk add --no-cache python3 bash wget

# Work directory inside container
WORKDIR /app

# Copy the project files
COPY . /app


# Install Assignment requirements
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python3 get-pip.py 



# Install Python dependencies
RUN pip install --no-cache-dir -r battlesnakes/requirements.txt


# Expose Battlesnake port
EXPOSE 8080

# Run the Battlesnake Flask server
CMD ["python3", "battlesnakes/main.py"]
