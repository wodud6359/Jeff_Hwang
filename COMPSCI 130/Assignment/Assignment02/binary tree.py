
class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.__data = data
        self.__left = left
        self.__right = right
        
    def insert_left(self, new_data):
        if self.__left == None:
            self.__left = BinaryTree(new_data)
        else:
            tree = BinaryTree(new_data, left=self.__left)
            self.__left = tree
            
    def insert_right(self, new_data):
        if self.__right == None:
            self.__right = BinaryTree(new_data)
        else:
            tree = BinaryTree(new_data, right=self.__right)
            self.__right = tree
            
    def get_left(self):
        return self.__left
    
    def get_right(self):
        return self.__right
    
    def set_data(self, data):
        self.__data = data
        
    def get_data(self):
        return self.__data
    
    def set_left(self, left):
        self.__left = left
        
    def set_right(self, right):
        self.__right = right



