import sys

import ldap

from .params import PATH, GROUPS_PATH, PEOPLE_PATH
from .model import Person, Group
from .utils import fetch_ldap, store_to_yaml
from .log import get_logger
from .triggers import trigger

import ruamel.yaml


# TODO: Implement more efficiently
def diff_left(l1, l2):
    diff = l1.copy()
    for e2 in l2:
        for e1 in l1:
            if e1 == e2:
                diff.remove(e1)

    return diff


def sync():
    logger = get_logger()

    yaml = ruamel.yaml.YAML()
    yaml.register_class(Person)
    yaml.register_class(Group)

    # TODO: Extract read_from_yaml to utils function (also used in config)
    with open(PEOPLE_PATH, 'r') as f:
        old_people = yaml.load(f)
    with open(GROUPS_PATH, 'r') as f:
        old_groups = yaml.load(f)

    people, groups = fetch_ldap()

    deleted_people = diff_left(old_people, people)
    added_people = diff_left(people, old_people)
    deleted_groups = diff_left(old_groups, groups)
    added_groups = diff_left(groups, old_groups)

    if (
            len(deleted_people) == 0 and
            len(added_people) == 0 and
            len(deleted_groups) == 0 and
            len(added_groups) == 0
    ):
        logger.info('No changes')
    else:
        trigger(deleted_people, added_people, deleted_groups, added_groups)

    store_to_yaml(people, PEOPLE_PATH)
    store_to_yaml(groups, GROUPS_PATH)
