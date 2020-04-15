ENCODING = 'utf-8'

class Person:
    def __init__(self, tuple):

        info = tuple[1]

        self.uid = info['uid'][0].decode(ENCODING)
        self.homeDirectory = info['homeDirectory'][0].decode(ENCODING)
        self.uidNumber = info['uidNumber'][0].decode(ENCODING)
        self.gidNumber = info['gidNumber'][0].decode(ENCODING)

        self.groups = []

    def __eq__(self, other):
        if not isinstance(other, Person):
            return NotImplemented
        return (
            self.uid == other.uid and 
            self.homeDirectory == other.homeDirectory and 
            self.uidNumber == other.uidNumber and 
            self.gidNumber == other.gidNumber and 
            self.groups == other.groups
        )

#    def __hash__(self):
#        return (
#            hash(self.uid) ^ hash(self.homeDirectory) ^ hash(self.uidNumber) ^ hash(self.gidNumber) ^ hash(self.groups)
#        )

    def __repr__(self):
        return """
            Person:
                uid: {uid}
                homeDirectory: {homeDirectory}
                uidNumber: {uidNumber}
                gidNumber: {gidNumber}
                groups: {groups}
        """.format(uid=self.uid, homeDirectory=self.homeDirectory, uidNumber=self.uidNumber, gidNumber=self.gidNumber, groups=str(self.groups))

class Group:
    def __init__(self, tuple):

        info = tuple[1]

        self.memberUid = info.setdefault('memberUid', [])
        self.memberUid = list(map(lambda m: m.decode(ENCODING), self.memberUid))
        self.gidNumber = info['gidNumber'][0].decode(ENCODING)
        self.cn = info['cn'][0].decode(ENCODING)

    def __eq__(self, other):
        if not isinstance(other, Group):
            return NotImplemented
        return (
            self.memberUid == other.memberUid and
            self.gidNumber == other.gidNumber and
            self.cn == other.cn
        )

#    def __hash__(self):
#        return (
#            hash(self.memberUid) ^ hash(self.gidNumber) ^ hash(self.cn)
#        )

    def __repr__(self):
        return """
            Group:
                memberUid: {memberUid}
                gidNumber: {gidNumber}
                cn: {cn} 
        """.format(memberUid=self.memberUid, gidNumber=self.gidNumber, cn=self.cn)