pipeline {
    agent none 
    stages {
        stage('Build') { 
            agent {
                // 指定在一个基于 python:flask 镜像的 Docker 容器中执行该阶段
                // 可以将其理解为一个预先安装了 Flask 框架的 Docker 容器环境。​
                // 在 Jenkinsfile 中指定 python:flask 镜像，意味着 Jenkins 会拉取一个包含 Python 和 Flask 的基础镜像，并在此基础上运行应用程序
                docker {
                    image 'python:flask' 
                }
            }
            steps {
                sh 'pip install -r requirements.txt'
                sh 'python app.py' 
            }
        }
    }
}