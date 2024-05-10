pipeline {
    agent any
    environment {
        BRANCH='dev'
        REPO='https://github.com/all-right-consultoria/all-right-landing-page'
        REGISTRY_URL='https://ghcr.io'
        IMAGE_APP='ghcr.io/all-right-consultoria/landing-page-app'
        IMAGE_NGINX='ghcr.io/all-right-consultoria/landing-page-nginx'
    }
    stages {
        stage('checkout') {
            steps {
                git branch: env.BRANCH, url: env.REPO
            }
        }
        stage('build & push') {
            steps {
                script {
                    docker.withRegistry(env.REGISTRY_URL, 'github-token') {
                        def app = docker.build(env.IMAGE_APP, '-f ./allright/Dockerfile.prod ./allright')
                        def nginx = docker.build(env.IMAGE_NGINX, './allright/nginx')
                        app.push(env.BUILD_ID)
                        app.push('latest')
                        nginx.push(env.BUILD_ID)
                        nginx.push('latest')
                    }
                }
            }
        }
        stage('deploy') {
            steps {
                timeout (time: 4, unit: 'HOURS') {
                    input 'Entregar em Produção?'
                }
                withCredentials([usernamePassword(credentialsId: 'github-token', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                    sshagent (credentials: ['e92ea3bb-bcaf-4189-abf3-28a7b1ab4f5e']) {
                        sh 'ssh jenkins@allright-consultoria.com.br -t /home/app/deploy.sh ${REGISTRY_URL} -u ${USERNAME} -p ${PASSWORD}'
                    }
                }
                timeout (time: 5, unit: 'MINUTES') {
                    waitUntil {
                        script {
                            try {
                                def response = httpRequest 'https://allright-consultoria.com.br'
                                return (response.status == 200)
                            }
                            catch (exception) {
                                 return false
                            }
                        }
                    }
                }
            }
        }
    }
}
