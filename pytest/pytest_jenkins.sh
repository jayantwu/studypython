#!/bin/bash

if [ $# -ne 0 ]; then
    docker run \
    -v /Users/wujiayang/wujiayang/STUDY/docker/study/wujiayang/local_jenkins/jenkins_home/workspace/github_project/pytest_auto/:/var/wujy/ debian-wjy-0207:2.0-cling \
    bash -c "pip3 install pytest && cd /var/wujy/pytest/ && pip3 install -r requirements.txt && $@"
else
    echo "need present prama.."
fi

# 感觉有点绕， jenkins 把代码拉下来之后， 所在的路径上就是studypthon/, 需要现在jenkins 中 cd pytest/, 然后执行这个脚本， 进入
# 新的容器， 安装 pytest,  进入 项目所在路径， 执行相关命令

#docker run  -v /Users/wujiayang/wujiayang/STUDY/docker/study/wujiayang/local_jenkins/jenkins_home/workspace/github_project/pytest_auto/:/var/wujy/ debian-wjy-0207:2.0-cling
