class Version:
    def __init__(self, major=None, minor=None, patch=None):
        self.major = major
        self.minor = minor
        self.patch = patch

    def from_string(self, v: str):
        paths = v.split(".")
        paths += [None] * (3 - len(paths))
        major = int(paths[0])
        minor = int(paths[1])
        patch = int(paths[2])
        self = Version(major=major, minor=minor, patch=patch)

        return self

    def print(self):
        print(f"major {self.major}, minor {self.minor}, patch {self.patch}")

    def timeline(self, v):
        if v.major > self.major:
            return 1

        if v.minor > self.minor:
            return 1

        if v.patch > self.patch:
            return 1

        if v.major < self.major:
            return 1

        if v.minor < self.minor:
            return 1

        if v.patch < self.patch:
            return 1

        return 0
