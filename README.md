# Simple Gradio Image Upload App

This is a simple web app built with [Gradio](https://gradio.app/) that allows users to upload an image and displays the uploaded image.

## Running Locally

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the app:
   ```bash
   python app.py
   ```
3. Open the provided local URL in your browser.

## Deploying to AWS

You can deploy this app to AWS using services like EC2, Elastic Beanstalk, or ECS. Here is a basic outline for EC2:

1. Launch an EC2 instance (Amazon Linux or Ubuntu recommended).
2. SSH into your instance and install Python 3 and pip.
3. Upload your project files to the instance.
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Run the app:
   ```bash
   python app.py --server.port 80 --server.enable_queue False --server.address 0.0.0.0
   ```
6. Make sure your EC2 security group allows inbound traffic on the port you choose (e.g., 80).

For production, consider using a process manager (like `pm2` or `gunicorn`), HTTPS, and a domain name. 