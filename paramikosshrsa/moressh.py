#!/usr/bin/python3
"""Learning about Python SSH """

# used to remove warning from packaes
import warnings

import paramiko

warnings.filterwarnings(action="ignore", module=" .*paramiko.*")

def main():
    credz = [{"un": "bender", "ip": "10.10.2.3"}, {"un": "zoidberg", "ip": "10.10.2.5"},
            {"un": "fry", "ip": "10.10.2.4"}]

    mykey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")

    for cred in credz:
        ## create a session object
        sshsession = paramiko.SSHClient()
        
        sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        print("Connecting to... " + cred.get("un") + "@" + cred.get("ip"))

        sshsession.connect(hostname=cred.get("ip"), username=cred.get("un"), pkey=mykey)

        sshsesson.exec_command("touch /home/" + cred.get("un") + "/goodnews.everyone")

        sessin, sessout, sesserr = sshsession.exec_command("ls /home/" + cred.get("un"))

        print(session.read().decode('utf-8'))

        sshsession.close()

    print("Thanks for looping with Alta3!")

main()

