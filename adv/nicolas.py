import adv_test
import adv

def module():
    return Nicolas

class Nicolas(adv.Adv):
    pass


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1
        `s2
        `s3
        """

    adv_test.test(module(), conf, verbose=0)

