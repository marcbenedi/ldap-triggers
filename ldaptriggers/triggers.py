import os
import subprocess

from .params import TRIGGERS_PATH
from .log import get_logger


def trigger(deleted_people, added_people, deleted_groups, added_groups):
    """
    Fetches the stored triggers in TRIGGERS_PATH and executes them.
    :param deleted_people: Array
    :param added_people: Array
    :param deleted_groups: Array
    :param added_groups: Array
    :return:
    """
    logger = get_logger()

    triggers = os.listdir(TRIGGERS_PATH)

    # TODO: make this more efficient
    add_people_triggers = list(filter(lambda f: f.startswith("add_people_"), triggers))
    delete_people_triggers = list(filter(lambda f: f.startswith("delete_people_"), triggers))

    add_groups_triggers = list(filter(lambda f: f.startswith("add_groups_"), triggers))
    delete_groups_triggers = list(filter(lambda f: f.startswith("delete_groups_"), triggers))

    get_param_person = lambda p: str(p.uid)
    get_param_group = lambda g: str(g.cn)
    get_param_person_group = lambda p: str(p.uid) + ' ' + str(p.groupName) + ' ' + " ".join(p.groups)

    def call_trigger(entities, triggers, get_param):
        for e in entities:
            for t in triggers:
                rc = subprocess.call(TRIGGERS_PATH + t + ' ' + get_param(e), shell=True)
                if rc != 0:
                    logger.error(t + ' | ' + get_param(e) + ' | ' + str(rc))
                else:
                    logger.info(t + ' | ' + get_param(e) + ' | ' + str(rc))

    call_trigger(deleted_people, delete_people_triggers, get_param_person)
    call_trigger(deleted_groups, delete_groups_triggers, get_param_group)
    call_trigger(added_groups, add_groups_triggers, get_param_group)
    call_trigger(added_people, add_people_triggers, get_param_person_group)
