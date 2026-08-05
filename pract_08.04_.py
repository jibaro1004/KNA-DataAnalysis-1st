# ====== 26.08.04 실습 2번 ======
def machine(name, temp):
    print(f"{name} {temp}")


machine("모터", 78)


def pump(name, temp):
    print(f"{name} {temp}")


pump("펌프", 92)


# ====== 실습 3번 ======
def report(name, temp):
    print(f"{name} {temp}")


report(name="모터", temp=78)
report(name="펌프", temp=92)
