world = [[], [], []]  # 게임 월드는 객체들의 집합


def add_object(o, depth):
    world[depth].append(o)


def add_objects(ol, depth):
    world[depth] += ol


def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            del o
            return
    raise ValueError('Trying destroy non existing object')
    # world.remove(o) # 리스트에서만 삭제됨
    # del o # 실제로 메모리에서까지 삭제


def all_objects():
    for layer in world:
        for o in layer:
            yield o


def clear():
    for o in all_objects():
        del o
    for layer in world:
        layer.clear()
