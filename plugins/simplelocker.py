from templates import Plugin

class Androrat(Plugin):
    NAME = 'Simplelocker'

    def recon(self):
        for cls in self.dvm.get_classes():
            if 'Lorg/simplelocker/HttpSender$1;'.lower() in cls.get_name().lower():
                self.process_class = cls
                return True
        return False

    def extract(self):
        c2 = ""
        string = None
        for method in self.process_class.get_methods():
            if method.name == 'run':
                for inst in method.get_instructions():
                    if inst.get_name() == 'const-string':
                        string = inst.get_output().split(',')[-1].strip(" '")
                        c2 = string
                    if c2 :
                        break


        return {'c2': [c2]}

