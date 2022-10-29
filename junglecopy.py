# junglecopy.py

from abc import ABCMeta, abstractmethod
import abc


class Vertebrate(metaclass=ABCMeta):
    
    @abstractmethod
    def vertebrate_sound(self):
        pass
    
class Elephant(Vertebrate):

    def vertebrate_sound(self):
        print("Bahruha Bahruha!!")
        
class Fox(Vertebrate):

    def vertebrate_sound(self):
        print("Howl Howl!!")
        
## to define Jungle factory 

class JungleFactory(object):

    def generate_sound(self, object_type):
        
        return eval(object_type)().vertebrate_sound()
        
## code of clients
if __name__ == '__main__':
    jf = JungleFactory()
    vertebrate = input("\nVertebrate (Elephant or Fox); What is their Native sound?\n" 
                   "Please enter a name. \n")  
    
    import logging

    logging.basicConfig(filename="logfile.txt",
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        filemode='w',
                        level = logging.DEBUG,
                        datefmt='%d/%m/%Y %I:%M:%S %p')
    
    logger = logging.getLogger()
    logging.info("The user has entered .... " + format(vertebrate))

jf.generate_sound(vertebrate.capitalize())