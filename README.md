# AWS Student Management Dashboard

A cloud-hosted Student Management Dashboard built with **Python, Streamlit, Amazon EC2, Amazon RDS, Amazon SQS, AWS Lambda, Amazon CloudWatch, Amazon SNS, and SQS Dead-Letter Queues (DLQ)**.

The project demonstrates how a Python application can be deployed on AWS and integrated with an event-driven architecture for reliable student-event processing and failure handling.

## 🚀 Project Overview

The application allows users to manage and view student information through a Streamlit web dashboard.

Student records are stored in **Amazon RDS MySQL**. When a new student is successfully added, the application sends an event to **Amazon SQS**. AWS Lambda processes the event and verifies the student record in RDS.

If processing fails, the message is automatically retried. After the configured number of failed attempts, the message is moved to an **SQS Dead-Letter Queue (DLQ)**. Amazon CloudWatch monitors the DLQ and **Amazon SNS sends an email notification** when a failed message appears.

## 🏗️ Architecture

```text
                     ┌──────────────────┐
                     │      User        │
                     └────────┬─────────┘
                              │
                              ▼
                    ┌──────────────────┐
                    │ Streamlit App    │
                    │    Amazon EC2    │
                    └────────┬─────────┘
                             │
                    ┌────────┴────────┐
                    │                 │
                    ▼                 ▼
             ┌─────────────┐    ┌─────────────┐
             │ Amazon RDS  │    │ Amazon SQS  │
             │    MySQL    │    │ student-    │
             │             │    │ events      │
             └─────────────┘    └──────┬──────┘
                                       │
                                       ▼
                                ┌─────────────┐
                                │ AWS Lambda  │
                                │ Event       │
                                │ Processor   │
                                └──────┬──────┘
                                       │
                                       ▼
                                ┌─────────────┐
                                │ Amazon RDS  │
                                │ Verification│
                                └─────────────┘
                                       │
                                  On failure
                                       ▼
                                ┌─────────────┐
                                │ SQS DLQ     │
                                └──────┬──────┘
                                       │
                                       ▼
                                ┌─────────────┐
                                │ CloudWatch  │
                                │ Alarm       │
                                └──────┬──────┘
                                       │
                                       ▼
                                ┌─────────────┐
                                │ Amazon SNS  │
                                │ Email Alert │
                                └─────────────┘
```

## ☁️ AWS Services Used

| AWS Service             | Purpose                                   |
| ----------------------- | ----------------------------------------- |
| **Amazon EC2**          | Hosts the Streamlit application           |
| **Amazon RDS (MySQL)**  | Stores student data                       |
| **Amazon SQS**          | Provides asynchronous event processing    |
| **AWS Lambda**          | Processes student events                  |
| **SQS DLQ**             | Stores messages that repeatedly fail      |
| **Amazon CloudWatch**   | Logs Lambda activity and monitors the DLQ |
| **Amazon SNS**          | Sends failure notifications by email      |
| **AWS IAM**             | Controls permissions between AWS services |
| **AWS Secrets Manager** | Securely manages RDS master credentials   |

## 🛠️ Technologies

* Python
* Streamlit
* Pandas
* MySQL
* Boto3
* AWS
* Linux
* Git & GitHub

## ✨ Features

* Student record management
* Student search
* Student data stored in MySQL
* GPA and student statistics
* Department-based student information
* Cloud-hosted Streamlit application
* Event-driven SQS processing
* AWS Lambda processing
* Automatic SQS message retries
* Dead-Letter Queue for failed messages
* CloudWatch monitoring
* SNS email alerts
* IAM-based AWS permissions
* Secure database credential management

## 🔄 Event Processing Flow

When a student is added:

```text
1. User adds student
        ↓
2. Student is stored in RDS MySQL
        ↓
3. Student event is sent to SQS
        ↓
4. Lambda receives the SQS message
        ↓
5. Lambda verifies the student in RDS
        ↓
6. Successful event is logged in CloudWatch
```

### Failure Flow

```text
Lambda processing error
        ↓
SQS retries message
        ↓
Maximum retry attempts reached
        ↓
Message moved to DLQ
        ↓
CloudWatch detects DLQ message
        ↓
SNS sends email notification
```

## 🔐 Security

The project uses AWS IAM and Secrets Manager to avoid hard-coding sensitive database credentials in the application code.

The EC2 instance uses an IAM role to access required AWS services.

Sensitive files such as `.env` should not be committed to GitHub.

Example `.gitignore`:

```text
.env
venv/
__pycache__/
*.pyc
```

## 📁 Project Structure

```text
Student_Management_Dashboard/
│
├── App.py
├── pages/
│   └── Student_Search.py
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ Local Setup

Clone the repository:

```bash
git clone https://github.com/hassaan9941/Student_Management_Dashboard.git
cd Student_Management_Dashboard
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

### Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file with your database configuration:

```text
DB_HOST=your-rds-endpoint
DB_USER=your-database-user
DB_PASSWORD=your-database-password
DB_NAME=student_dashboard
```

Run the application:

```bash
streamlit run App.py
```

## 📊 Monitoring

AWS CloudWatch is used to monitor Lambda execution and errors.

A CloudWatch alarm monitors the SQS Dead-Letter Queue.

When one or more failed messages remain visible in the DLQ, an SNS notification is sent by email.

## 🎯 Learning Objectives

This project was created to gain practical experience with:

* AWS cloud infrastructure
* EC2 deployment
* RDS database integration
* IAM permissions
* SQS messaging
* Lambda serverless computing
* Event-driven architecture
* Dead-Letter Queues
* CloudWatch monitoring
* SNS notifications
* Secrets Manager
* Linux server administration
* Python application deployment

## 👨‍💻 Author

**Hassaan**

Computer Science / Artificial Intelligence student interested in **Cloud Engineering, AWS, Python, and Machine Learning**.

## 📌 Future Improvements

* API Gateway integration
* Docker containerization
* Infrastructure as Code using Terraform
* CI/CD pipeline using GitHub Actions
* Improved authentication and authorization
* Additional CloudWatch dashboards

