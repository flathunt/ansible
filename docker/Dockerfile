# Use the ubuntu image as the base image
FROM ubuntu:latest

# Install nmap
RUN apt-get update && apt-get install -y nmap python3

# Copy the script into the container
COPY nscan.py /nscan.py

# Make the script executable
RUN chmod +x /nscan.py

# Set the script to run when the container starts
CMD ["python3 /nscan.py"]
