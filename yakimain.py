import quickstart as qs
import drawline as draw
import sys


def doall(infile, outfile):
    f = open('ans.txt', 'w')
    # file_name='/root/pic/t3.jpg'
    file_name = infile
    draw.openpic(file_name)
    # os.system("export GOOGLE_APPLICATION_CREDENTIALS=\"/root/mykey.json\"")
    rst = qs.run_quickstart(file_name)
    draw.writepic(outfile)
    f.close()

    return rst


if __name__ == '__main__':
    ret = doall('/root/pic/' + sys.argv[1], 'pro_' + sys.argv[1])
