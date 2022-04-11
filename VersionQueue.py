class VersionQueueV2:
    '''
    This version Queue is not storing a copy of the version Queue.
    It is dynamically calculating the desired version based on a set of list containing the additions and deletions t the queue. 
    '''
    version_stack = []
    def __init__(self):
        self.queue = []
        self.version_number = 0
        self.deleted_numbers = []

    def enqueue(self, value):
        self.version_number += 1
        self.queue.append(value)
        self.version_stack.append('e')
    
    def dequeue(self):
        top = self.queue[0]
        self.version_number += 1
        self.queue.remove(self.queue[0])
        self.version_stack.append('d' + str(top))
        return top

    def printQueue(self, version=None):
        if version is "":
            version = self.version_number
        version = int(version)
        version_queue = self.queue.copy()
        version_stack = self.version_stack.copy()
        while version < self.version_number:
            calc = version_stack.pop()
            if calc == 'e':
                #remove last element
                version_queue.pop()
            elif 'd' in calc:
                #add last removed element
                version_queue.insert(0, int(calc[1]))
            version+=1
        return version_queue


class VersionQueueV1:
    '''
    This is the initial version of the solution, This one stores a copy of each version of the queue.
    '''
    versions = {0:[]}
    def __init__(self):
        self.queue = []
        self.version_number = 0

    def enqueue(self, value):
        self.queue.append(value)
        self.version_number += 1
        self.versions[self.version_number] = self.queue.copy()
    
    def dequeue(self):
        top = self.queue[0]
        self.queue.remove(self.queue[0])
        self.version_number += 1
        self.versions[self.version_number] = self.queue.copy()
        return top

    def printQueue(self, version=None):
        if version in [None, '',0]:
            version  = self.version_number
        return self.versions[version]