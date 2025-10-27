# from ftplib import FTP
# from packaging.version import parse as parse_version


# class Version:
#     def __init__(self, major=None, minor=None, patch=None):
#         self.major = major
#         self.minor = minor
#         self.patch = patch
#         self.version = parse_version(f"{self.major}.{self.minor}.{self.patch}")
#         self.latest = None
#         self.__ftp

#     def check(self, host, user, passwd):
#         self.__ftp = FTP(host, user, passwd)
#         versions = self.__ftp.nlst()
#         vs = []
#         for version in versions:
#             try:
#                 v = parse_version(version)
#                 vs.append(v)
#             except:
#                 pass

#         if len(vs) > 0:
#             latest = vs[0]

#         for v in vs:
#             if v > latest:
#                 latest = v

#         self.latest = latest
#         return self.latest > self.version
    
#     def update(self):
#         handle = open(path.rstrip("/") + "/" + filename.lstrip("/"), 'wb')
# ftp.retrbinary('RETR %s' % filename, handle.write)
