import sys
import traceback
import pdb

class AutoPdb():
    def __init__(self, confirm=False):
        self.confirm = confirm

    def __enter__(self):
        pass

    def __exit__(self, extype, value, tb):
        if extype is None:
            return True

        traceback.print_exc()
        print('')

        if not self.confirm or self.yes_no_input():
            pdb.post_mortem(tb)
            return False

        return True

    def yes_no_input(self):
        choice = input(">>> start pdb debug? [y/n]: ").lower()
        if choice in ['y', 'ye', 'yes']:
            return True
        elif choice in ['n', 'no']:
            return False

def trap(**args):
    return AutoPdb(**args)
