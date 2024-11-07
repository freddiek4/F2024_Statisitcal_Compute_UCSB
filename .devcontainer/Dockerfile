# Use a Python base image
FROM python:3.8

# Install Jupyter Lab and any required libraries
RUN pip install jupyterlab torch torch-geometric matplotlib scipy numpy

# Set the working directory inside the container
WORKDIR /workspace

# Expose Jupyter's default port
EXPOSE 8888

# Set the default command to start Jupyter Lab (optional if you prefer running it manually)
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
