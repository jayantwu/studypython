import pexpect
import time
import sys
import pdb
import pytest

def send_cmd(sh, command, expect_string=['\$', '#'], sleep_duration:int=1, callback=None):

    attempt = 0
    sh.sendline(command)
    #print(sh.before.decode('utf-8'))
    #print(sh.timeout) #有默认值30
    sh.timeout=10
    if isinstance(expect_string, str):
        expect_pat = [expect_string, pexpect.TIMEOUT]
    
    if isinstance(expect_string, list):
        expect_pat = expect_string + [pexpect.TIMEOUT]

    while attempt < 3:
        index = sh.expect(expect_pat) # 返回这个列表的索引
        if callback != None:
            callback(index)
        else:
            if index == 0 or index == 1:
                print(command+" matched")
                
                time.sleep(sleep_duration)
                
                break
            elif index == 2:
                print("Timeout occurred")

        attempt += 1
        print("Retry attempt:", attempt)

def execut_1():
    with open('./logfile1.txt', 'w') as f:
        sh = pexpect.spawn('/bin/bash', encoding='utf8')
        #logfile = open(f"logfile1.txt", 'wb')
        sh.logfile = f
        # sh.logfile_send = sys.stdout
        # sh.logfile_read = f
        # sh.sendline('ls -al')

        # sh.expect(['#']) # 确保上一条命令执行完毕

        # sh.sendline("ps -aux")

        # sh.expect(['#', pexpect.EOF])

        #send_cmd(sh, 'pwd', '#', 2)

        # send_cmd(sh, 'ls -al', '#', 2)

        send_cmd(sh, 'ls -al', '#', 2)
        send_cmd(sh, 'pwd', '#', 2)

        # for i in range(10):
        #     send_cmd(sh, 'echo hello world', '#', 1)

        # send_cmd(sh, 'sleep 5', '#', 1)

        # send_cmd(sh, 'rm logfile1.txt', '#', 2)

        # send_cmd(sh, "sh -c 'echo hello world'", '#', 1)

        # send_cmd(sh, "echo hello world", '#', 1)

        # try:
        #     sh.expect(pexpect.EOF)
        # except pexpect.TIMEOUT:
        #     print('vxvxvxvxvx')

        #sh.close()
        #sh.expect(pexpect.EOF)

        # output = sh.read()
        # f.write(output)
    # sh.close()


def execut_2():
    with open('./logfile1.txt', 'w', buffering=1) as f:
        sh = pexpect.spawn('/bin/bash', encoding='utf8')
        sh.logfile = f
        sh.sendline('ls -al')
        time.sleep(1) # sleep 1 is ok
        sh.expect('#')
        sh.close()


def execut_3():
    with open('./logfile1.txt', 'wb') as f:
        ssh = pexpect.spawn("ssh wujy@10.18.0.25")
        ssh.logfile = f

        # ssh.expect(['(yes/no)? '])
        # ssh.sendline('yes')
        ssh.expect(['password:'])

        def cb(index):
            if index == 0 or index == 1:
                print('matched.')
            if index == 2:
                send_cmd(ssh, 'yes')

        #send_cmd(ssh, 'wujy123', ['#', '\$', '(yes/no)?'], callback=cb)
        
        ssh.sendline('wujy123')

        ssh.expect('\$')

        send_cmd(ssh, 'pwd')

        send_cmd(ssh, 'docker ps -a | grep wujy')

        send_cmd(ssh, 'docker exec -it c9ff05c23cd5 bash')

        #send_cmd(ssh, 'ps -aux')


        send_cmd(ssh, 'cd build')

        send_cmd(ssh, 'sh -c "./bin/cosim_gtest --gtest_filter=*testlog"')

        send_cmd(ssh, 'echo excute3 completed.')
        # try:
        #     ssh.expect(pexpect.EOF)
        # except pexpect.TIMEOUT:
        #     print('time out')
        # cont = ssh.read()
        # f.write(cont)
        ssh.close()

        
    with open('./logfile1.txt', 'r') as f:
        if 'PASSED' in f.read():
            print('test success')
        else:
            print('test failed.')
        


def test_gtest():
    execut_3()


#execut_1()
#execut_2()


if __name__ == '__main__':
    pytest.main(['-v', '-s', './test10.py::test_gtest'])
    #execut_2()

