class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = set()
        self.users = set()

    def add_group(self, group):
        self.groups.add(group)

    def add_user(self, user):
        self.users.add(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

    def __repr__(self):
        return "name: {} <groups: {} users: {}>".format(self.name, self.groups, self.users)

    def __str__(self):
        return "name: {} <groups: {} users: {}>".format(self.name, self.groups, self.users)


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """

    if user == group.get_name():
        return True
    if user in group.get_users():
        return True
    for g in group.get_groups():
        return is_user_in_group(user, g)
    return False


print(is_user_in_group("child", child))
print(is_user_in_group("subchild", parent))
print(is_user_in_group("Sub_child", child))
print(is_user_in_group("sub_child_user", parent))
