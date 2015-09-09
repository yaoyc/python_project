#coding:utf-8
########################################################################
######## Apache 访问日志统计，PV量###############
#######################################################################

def analyze_pv(readline):
        fr = open('/var/log/httpd/access_log', 'r')
        D_pv = {}
        for fr_line in fr:
                eachLine = fr_line.split()[0]
                if eachLine in D_pv:
                        D_pv[eachLine] += 1
                else:
                        D_pv[eachLine] = 1
        fr.close()
        fw = file('/root/python/apache_pv.txt', 'w')
        for key in sorted(D_pv):
                fw.write(key)
                fw.write('\t')
                value = str(D_pv[key])
                fw.write(value)
                fw.write('\n')
        fw.close()
        return fw

if __name__ == '__main__':
        analyze_pv('/var/log/httpd/access_log')
