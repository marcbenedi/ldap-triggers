import sys

import ldap

from .params import PATH, GROUPS_PATH, PEOPLE_PATH
from .model import Person, Group
from .utils import fetch_ldap, store_to_yaml, read_from_yaml
from .log import get_logger
from .triggers import trigger


# TODO: Implement more efficiently
def diff_left(l1, l2):
    """
    Computes which elements are in l1 but not in l2
    :param l1: Array
    :param l2: Array
    :return: diff -> Array
    """
    diff = l1.copy()
    for e2 in l2:
        for e1 in l1:
            if e1 == e2:
                diff.remove(e1)

    return diff


def full_diff_left(l1, l2):
    """
    Computes which elements are in l1 but not in l2
    :param l1: Array
    :param l2: Array
    :return: diff -> Array
    """
    diff = l1.copy()
    for e2 in l2:
        for e1 in l1:
            if e1.full_diff(e2):
                diff.remove(e1)

    return diff


def sync():
    """
    Fetches the LDAP server.
    Computes which users and groups have been deleted or added.
    Calls triggers.
    Stores current LDAP server status into PATH.
    :return
    """
    logger = get_logger()

    old_people = read_from_yaml(PEOPLE_PATH)
    old_groups = read_from_yaml(GROUPS_PATH)

    people, groups = fetch_ldap()

    # Compare unique identifiers
    deleted_people = diff_left(old_people, people)
    added_people = diff_left(people, old_people)
    deleted_groups = diff_left(old_groups, groups)
    added_groups = diff_left(groups, old_groups)

    old_people_existing = list(filter(lambda i: i not in deleted_people, old_people))
    old_groups_existing = list(filter(lambda i: i not in deleted_groups, old_groups))
    people_existing = list(filter(lambda i: i not in added_people, people))
    groups_existing = list(filter(lambda i: i not in added_groups, groups))

    # modified_X contains the new information of elements that have been modified
    modified_people = list(filter(lambda new: len(list(filter(lambda old: new.full_eq(old), old_people_existing))) == 0,
                                  people_existing))
    modified_groups = list(filter(lambda new: len(list(filter(lambda old: new.full_eq(old), old_groups_existing))) == 0,
                                  groups_existing))

    if (
            len(deleted_people) == 0 and
            len(added_people) == 0 and
            len(deleted_groups) == 0 and
            len(added_groups) == 0 and
            len(modified_people) == 0 and
            len(modified_groups) == 0
    ):
        logger.info('No changes')
    else:
        trigger(deleted_people, added_people, deleted_groups, added_groups, modified_people, modified_groups)

    store_to_yaml(people, PEOPLE_PATH)
    store_to_yaml(groups, GROUPS_PATH)
