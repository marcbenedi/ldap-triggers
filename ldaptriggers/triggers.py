import os

def trigger(deleted_people, added_people, deleted_groups, added_groups):

    triggers = os.listdir("/etc/ldaptriggers/triggers/")

    add_people_triggers = list(filter(lambda f: f.startswith("add_people_"), triggers))
    delete_people_triggers = list(filter(lambda f: f.startswith("delete_people_"), triggers))

    add_groups_triggers = list(filter(lambda f: f.startswith("add_groups_"), triggers))
    delete_groups_triggers = list(filter(lambda f: f.startswith("delete_groups_"), triggers))

    print(add_people_triggers)
    print(add_groups_triggers)
    print(delete_people_triggers)
    print(delete_groups_triggers)


    for p in deleted_people:
        pass
    
    for p in added_people:
        pass

    for g in deleted_groups:
        pass

    for g in added_groups:
        pass