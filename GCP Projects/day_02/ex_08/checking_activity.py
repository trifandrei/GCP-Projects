import psutil

def print_info():
     for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['cpu_percent','cwd','pid', 'name', 'username','status', 'nice','ppid'])
        except psutil.NoSuchProcess:
            pass
        else:
            print ("Process id: {:<5} Status: {:<10} Priority: {:<5} CPU%: {:<5} Username: {:<10} Parent id: {:<5} Current working dir: {}".format( pinfo["pid"], pinfo["status"], pinfo["nice"],pinfo["cpu_percent"],pinfo["username"],pinfo["ppid"],pinfo["cwd"]))

if __name__ == "__main__":
    print_info()
   
   

    