# Buffer Overflow Demonstration Lab 🔒

A controlled environment for demonstrating and understanding buffer overflow vulnerabilities in web applications. This project is designed for educational purposes as part of secure software development training.

## 🚨 Warning
This project intentionally contains vulnerable code for educational purposes. Do not deploy in a production environment.

## 🛠️ Technologies
- Python 3.9
- Flask
- Docker & Docker Compose
- Threading for concurrent attack simulation

## 🏗️ Project Structure
```
buffer-overflow-demo/
├── docker-compose.yml
├── exploit/
│   └── exploit.py
└── web/
    ├── Dockerfile
    ├── app.py
    ├── requirements.txt
    └── templates/
        └── index.html
```

## 🚀 Quick Start

### Prerequisites
- Docker
- Docker Compose
- Python 3.x (for running exploit scripts)
- pip (Python package manager)

### Installation & Running

1. Clone the repository:
```bash
git clone https://github.com/0x4m4/buffer-overflow-demo.git
cd buffer-overflow-demo
```

2. Start the vulnerable web application:
```bash
docker-compose up --build
```

3. Install Python dependencies for the exploit script:
```bash
pip install requests
```

4. Run the exploit demonstration:
```bash
cd exploit
python exploit.py
```

## 🎯 Features
- Controlled buffer overflow demonstration
- Web interface for manual testing
- Automated exploit script
- Resource-limited containerized environment
- Concurrent attack simulation

## 🔍 Testing Scenarios
1. Normal input (within buffer size)
2. Boundary case testing
3. Slight overflow demonstration
4. Medium overflow impact
5. Aggressive crash testing

## 🛡️ Security Notice
This application is intentionally vulnerable and should only be used in isolated, educational environments. The container includes security measures like:
- Resource limitations
- No privilege escalation
- Isolated network

## 👨‍💻 Author
- **0x4m4**
- Website: [www.0x4m4.com](https://www.0x4m4.com)

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/0x4m4/buffer-overflow-demo/issues).
