import re

class IPv4:
    def __init__(self, segment1, segment2, segment3, segment4):
        self.segment1 = segment1
        self.segment2 = segment2
        self.segment3 = segment3
        self.segment4 = segment4
    def print_ip(self):
        print("{0}.{1}.{2}.{3}".format(self.segment1, self.segment2,
                                       self.segment3, self.segment4))
    def calc_seg_len(self, segment):
        return len(segment)

    def print_seg_length(self):
        print("Segment 1 has length {0} ".format(self.calc_seg_len(
            self.segment1)))
        print("Segment 2 has length {0} ".format(self.calc_seg_len(
            self.segment2)))
        print("Segment 3 has length {0} ".format(self.calc_seg_len(
            self.segment3)))
        print("Segment 4 has length {0} ".format(self.calc_seg_len(
            self.segment4)))

    def ip_getter():
        address = input("Enter the ip v4 address: \n")
        charTest = re.finditer('[a-zA-Z]', address)
        if charTest != "None":
            dots = re.compile('[.]')
            dotiter = dots.finditer(address)
            ip = []
            for i in dotiter:
                ip.append(int(i.start()))
            out = IPv4.ip_setter(ip, address)
            return out
        else:
            print("Sorry, ipv4 is numbers and periods only, no letters")
            print("Please try again")
            ip_getter()

    def ip_setter(ip, address):
        ipAddress = IPv4(address[0:ip[0]], address[ip[0]+1:ip[1]],
                         address[ip[1]+1:ip[2]],address[ip[2]+1:len(address)])
        return ipAddress


ipTest = IPv4.ip_getter()
ipTest.print_ip()
ipTest.print_seg_length()
