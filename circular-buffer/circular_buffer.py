class BufferFullException(Exception):
    pass


class BufferEmptyException(Exception):
    pass


class CircularBuffer:
    def __init__(self, capacity):
        self.buffer = list()
        for i in range(capacity):
            self.buffer.append("")
        self.oldest = -1
        self.writeIndex = 0
        self.readIndex = 0
        self.capacity = capacity

    def read(self):
        if self.buffer[self.readIndex] == "":
            raise BufferEmptyException
        res = self.buffer[self.readIndex]
        self.buffer[self.readIndex] = ""
        self.readIndex = (self.readIndex + 1) % self.capacity
        return res

    def write(self, data):
        if self.buffer[self.writeIndex] == "":
            self.buffer[self.writeIndex] = data
            if self.oldest == -1:
                self.oldest = self.writeIndex
            self.writeIndex = (self.writeIndex + 1) % self.capacity
        else:
            raise BufferFullException


    def overwrite(self, data):
        if self.oldest == -1 and self.buffer[self.writeIndex] == "" or self.buffer[self.writeIndex] != "":
            self.oldest = (self.oldest + 1) % self.capacity
        self.buffer[self.writeIndex] = data
        self.writeIndex = (self.writeIndex + 1) % self.capacity
        


    def clear(self):
        if self.buffer[self.oldest] == "":
            raise BufferEmptyException
        self.buffer[self.oldest] = ""
        self.oldest = (self.oldest + 1) % self.capacity