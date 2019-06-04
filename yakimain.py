import quickstart as qs
import drawline as draw
import embeded as emb
import sys


def doall(infile, showfile, outfile):
    # f = open('ans.txt', 'w')
    # file_name='/root/pic/t3.jpg'
    file_name = infile
    draw.openpic(file_name)
    # os.system("export GOOGLE_APPLICATION_CREDENTIALS=\"/root/mykey.json\"")
    rst = qs.run_quickstart(file_name)
    draw.writepic(showfile)
    # f.close()

    emb.Embeded(infile, outfile, rst)

    return rst


if __name__ == '__main__':
    ret = doall('/root/pic/' + sys.argv[1], 'sho_' + sys.argv[1], 'rst_' + sys.argv[1])
