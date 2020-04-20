import os
import subprocess

from .params import TRIGGERS_PATH
from .log import get_logger


def trigger(deleted_people, added_people, deleted_groups, added_groups):
    logger = get_logger()

    triggers = os.listdir(TRIGGERS_PATH)

    add_people_triggers = list(filter(lambda f: f.startswith("add_people_"), triggers))
    delete_people_triggers = list(filter(lambda f: f.startswith("delete_people_"), triggers))

    add_groups_triggers = list(filter(lambda f: f.startswith("add_groups_"), triggers))
    delete_groups_triggers = list(filter(lambda f: f.startswith("delete_groups_"), triggers))

    # TODO: remove code duplication
    for p in deleted_people:
        for f in delete_people_triggers:
            rc = subprocess.call(TRIGGERS_PATH + f + ' ' + str(p.uid), shell=True)
            if rc != 0:
                logger.error(f + ' | ' + p.uid + ' | ' + str(rc))
            else:
                logger.info(f + ' | ' + p.uid + ' | ' + str(rc))

    for g in deleted_groups:
        for f in delete_groups_triggers:
            rc = subprocess.call(TRIGGERS_PATH + f + ' ' + str(g.cn), shell=True)
            if rc != 0:
                logger.error(f + ' | ' + g.cn + ' | ' + str(rc))
            else:
                logger.info(f + ' | ' + g.cn + ' | ' + str(rc))

    for g in added_groups:
        for f in add_groups_triggers:
            rc = subprocess.call(TRIGGERS_PATH + f + ' ' + str(g.cn), shell=True)
            if rc != 0:
                logger.error(f + ' | ' + g.cn + ' | ' + str(rc))
            else:
                logger.info(f + ' | ' + g.cn + ' | ' + str(rc))

    for p in added_people:
        for f in add_people_triggers:
            rc = subprocess.call(
                TRIGGERS_PATH + f + ' ' + str(p.uid) + ' ' + str(p.groupName) + ' ' + " ".join(p.groups), shell=True)
            if rc != 0:
                logger.error(f + ' | ' + p.uid + ' | ' + str(rc))
            else:
                logger.info(f + ' | ' + p.uid + ' | ' + str(rc))
