# Red Wine Quality Prediction: ML Pipeline Implementation

This project implements a machine learning pipeline to predict the quality of red wine based on its physicochemical attributes. Using a dataset of red wine samples, the project explores feature engineering, model training, evaluation, and deployment in a streamlined and reproducible pipeline.

In addition to building the ML pipeline, the project integrates **AWS services** for deploying the trained model and leverages **GitHub Actions** for automating the CI/CD workflow. The deployment process uses **Amazon EC2** (Elastic Compute Cloud) and **Amazon ECR** (Elastic Container Registry), while GitHub Actions ensures a seamless and automated pipeline for building, testing, and deploying the containerized application.

## Key Features

- **Comprehensive ML Pipeline**: From data ingestion to model deployment, the project implements a fully functional and automated machine learning pipeline.
- **Feature Engineering**: Includes techniques for handling missing values, scaling, and transforming the dataset for improved model performance.
- **Model Training and Tuning**: Employs multiple machine learning algorithms, with performance optimization via hyperparameter tuning.
- **Evaluation Metrics**: Uses appropriate metrics to assess model performance.
- **AWS Deployment**: 
  - **Amazon EC2**: The model is deployed on an EC2 instance to handle prediction requests in a cloud environment.
  - **Amazon ECR**: The application and model are containerized using Docker and stored in Amazon ECR for seamless deployment on EC2.
  - The setup ensures a scalable and robust environment for hosting the machine learning model.
- **GitHub Actions Integration**:
  - Automates the CI/CD workflow for the project.
  - Automatically builds the Docker container, pushes it to Amazon ECR, and triggers the deployment on the EC2 instance.
  - Simplifies the testing and deployment process, reducing manual overhead and ensuring consistency in production releases.
- **Reproducibility**: The pipeline is structured for clarity and reproducibility, making it easier for users to adapt and extend.
- **Focus on Wine Quality Prediction**: Targets a practical application in the wine industry by using physicochemical properties (e.g., acidity, sugar, pH, etc.) to predict wine quality.

## AWS Integration

This project utilizes the following AWS services for deployment:

1. **Amazon EC2**: The machine learning model is deployed on an EC2 instance, allowing the application to serve predictions in real-time.
2. **Amazon ECR**: The project application and model are containerized using Docker and stored in Amazon Elastic Container Registry (ECR). This ensures efficient deployment and management of the Docker images on the EC2 instance.

The combination of EC2 and ECR enables a scalable, cloud-based deployment that supports containerized applications, making the model accessible via REST API endpoints hosted on the EC2 instance.

## CI/CD Workflow with GitHub Actions

The project uses **GitHub Actions** to automate the CI/CD process, enabling seamless deployment from code changes to production. Key steps include:

1. **Docker Build**: Automatically builds the Docker image for the application when code changes are pushed to the repository.
2. **Push to ECR**: Pushes the newly built Docker image to the Amazon Elastic Container Registry (ECR).
3. **Deploy on EC2**: Triggers the deployment on the EC2 instance, ensuring the latest version of the application is running in production.
4. **Automated Testing**: Includes steps for running tests to verify the code and container integrity before deployment.

The CI/CD integration streamlines the development process, ensuring fast and reliable deployments.

# Workflows

## Update Configuration Files
- `config.yaml`
- `schema.yaml`
- `params.yaml`

## Update Application Components
- Update the entity
- Update the configuration manager in `src/config`
- Update the components
- Update the pipeline
- `main.py`
- `app.py`

## How to Run?

**STEPS:**
1. `conda create -n redwine python -y`
2. `conda activate redwine`
3. `pip install -r requirements.txt`
4. `python app.py`
5. Now open up your local host at `0.0.0.0:8080`

## AWS CI/CD Deployment with GitHub Actions

### 1. Login to AWS Console

### 2. Create IAM User for Deployment

#### Permissions Required:
- EC2 Access: Virtual machine
- ECR: Elastic Container Registry to save your Docker image in AWS

### Description: About the Deployment

1. Build Docker image of the source code.
2. Push your Docker image to ECR.
3. Launch your EC2.
4. Pull your image from ECR in EC2.
5. Launch your Docker image in EC2.

### Policy:

1. `AmazonEC2ContainerRegistryFullAccess`
2. `AmazonEC2FullAccess`

### Steps:

3. Create ECR repo to store/save Docker image.
   - Save the URI: `136566696263.dkr.ecr.us-east-1.amazonaws.com/mlproject`
4. Create EC2 machine (Ubuntu).

5. Open EC2 and Install Docker in EC2 Machine:

    ```bash
    sudo apt-get update -y
    sudo apt-get upgrade
    curl -fsSL https://get.docker.com -o get-docker.sh
    sudo sh get-docker.sh
    sudo usermod -aG docker ubuntu
    newgrp docker
    ```

6. Configure EC2 as self-hosted runner:
    - Settings > Actions > Runner > New self-hosted runner > Choose OS, then run commands one by one.

7. Setup GitHub secrets:
   - `AWS_ACCESS_KEY_ID`
   - `AWS_SECRET_ACCESS_KEY`
   - `AWS_REGION=us-east-1`
   - `AWS_ECR_LOGIN_URI=demo>> 438465150317.dkr.ecr.eu-north-1.amazonaws.com`
   - `ECR_REPOSITORY_NAME=simple-app`