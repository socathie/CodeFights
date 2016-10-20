def incorrectPasscodeAttempts(passcode, attempts):
    cnt = 0
    for a in attempts:
        failed = False
        if a!=passcode:
            cnt+=1
            failed = True
        if cnt == 10:
            return True
        if not failed:
            cnt =0
    return False
