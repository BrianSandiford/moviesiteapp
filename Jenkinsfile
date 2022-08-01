node {
    def app
        stage('Cloning Git') {
            
              checkout scm     
            
        }
        // Building Docker images
        stage('Building image') {
            
                script {
                  //
                  dockerImage = docker.build "655895384845.dkr.ecr.us-east-2.amazonaws.com/docker-private-repo:"+env.BUILD_NUMBER
        }
      
    }
      // Uploading Docker images into AWS ECR
    stage('Pushing to ECR') {
      
         script {
                sh 'aws ecr get-login-password --region us-east-2 | docker login --username AWS --password-stdin 655895384845.dkr.ecr.us-east-2.amazonaws.com'
                sh 'docker push 655895384845.dkr.ecr.us-east-2.amazonaws.com/docker-private-repo:'+env.BUILD_NUMBER
         }
        
      }
    
    stage("Deploy") {  
        
            withCredentials([usernameColonPassword(credentialsId: 'git-pass-credentials-ID', variable: 'USERPASS')]) {
            
            
         
            sh('''
                rm -R -f moviesiteapp-helmcharts
                git clone https://github.com/BrianSandiford/moviesiteapp-helmcharts.git
                ''')
                // git clone https://$USERPASS@github.com/BrianSandiford/moviesiteapp-helmcharts.git came from sh () above
                }
         
            dir("moviesiteapp-helmcharts"){
             sh "chmod +x changeTag.sh"
             sh "./changeTag.sh $BUILD_NUMBER"
             sh "git add ."
             sh " git commit -am '[Jenkins CI] Updated image tag $BUILD_NUMBER.' "
             sh "git remote set-url origin git@github.com:BrianSandiford/moviesiteapp-helmcharts.git"
             sshagent(['d3633d00-8a44-460a-b45c-6d767b1b3621']) {
              sh "git checkout master"
              sh "git fetch"
              sh "git rebase origin/master"
              sh "git push origin master:master"
              // sh " git remote show origin"
              // sh "git push -u origin master"
             }
            
            
          
        } 
    }  
}
