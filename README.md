# AWS EC2 Docker Deployment 🚀

A hands-on DevOps project demonstrating how to deploy and monitor a containerized FastAPI application on AWS EC2.

## Tech Stack

- AWS EC2 — cloud compute
- Amazon Linux 2023 — server operating system
- Docker — application containerization
- Python & FastAPI — REST API
- AWS VPC & Security Groups — networking and firewall
- SSH — remote server administration
- Amazon CloudWatch — infrastructure monitoring and alarms

## Architecture

```text
                Internet
                   |
                HTTP :80
                   |
            AWS Security Group
                   |
            AWS EC2 (t3.micro)
                   |
              Docker Engine
                   |
          FastAPI Container
               Port 8000
                   |
              / and /health

Monitoring:
EC2 CPUUtilization --> CloudWatch Alarm
```

## Features

- Containerized FastAPI application
- Public HTTP endpoint
- Docker HEALTHCHECK every 30 seconds
- Docker restart policy (`unless-stopped`)
- CloudWatch CPU monitoring
- CPU alarm threshold: above 70% for 2 consecutive 5-minute periods
- SSH access restricted through a Security Group

## API Endpoints

| Endpoint | Description |
|----------|-------------|
| `/` | Returns application information |
| `/health` | Returns application health status |

Example response:

```json
{
  "message": "Hello from AWS EC2!",
  "status": "running",
  "platform": "Docker + FastAPI"
}
```

## Local Deployment

Build the Docker image:

```bash
docker build -t aws-fastapi-app .
```

Run the container:

```bash
docker run -d \
  --name aws-fastapi \
  --restart unless-stopped \
  -p 80:8000 \
  aws-fastapi-app
```

Test the API:

```bash
curl http://localhost/
curl http://localhost/health
```

## AWS Deployment

1. Launch an Amazon Linux 2023 EC2 instance.
2. Configure a Security Group allowing HTTP and restricting SSH.
3. Install and start Docker.
4. Transfer or clone the application source code.
5. Build and run the Docker container.
6. Verify that the API is accessible through the instance's public IP.
7. Monitor EC2 metrics with Amazon CloudWatch.
8. Configure a CloudWatch CPU utilization alarm.

## Monitoring

Amazon CloudWatch monitors the EC2 instance's CPU utilization.

The alarm uses:
- Metric: `CPUUtilization`
- Statistic: Average
- Period: 5 minutes
- Threshold: Greater than 70%
- Evaluation: 2 out of 2 datapoints

The alarm has no notification actions configured.

## Security Notes

- SSH access should be limited to trusted IP addresses.
- Private SSH keys and AWS credentials must never be committed.
- This project uses HTTP for demonstration purposes.
- A production deployment should use HTTPS and additional security controls.

## Future Improvements

- HTTPS with a custom domain
- CI/CD pipeline using GitHub Actions
- Infrastructure as Code with Terraform
- Centralized application logging in CloudWatch
- Automated deployment and rollback
