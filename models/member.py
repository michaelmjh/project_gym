class Member:

    def __init__(self, first_name, last_name, premium_member, active = True, member_id = None):
        self.first_name = first_name
        self.last_name = last_name
        self.premium_member = premium_member
        self.active = active
        self.member_id = member_id