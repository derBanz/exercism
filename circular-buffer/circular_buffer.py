"""Set task: Create a circular buffer (list) with a fixed capacity (int) and the following functionality.
* A function to write a value (String) into the next open slot of the buffer. If the buffer is full, an exception is forced.
* A function to read the oldest value in the buffer. If the buffer is empty, an exception is forced.
* A function to overwrite the oldest value in the buffer if there is no open slots. If there is an open slot, the data is written there instead.
* A function to clear all values from the buffer.
Method:
* On init, self.buffer (list) is created with self.capacity=capacity (int) empty entries. Also two indices self.oldest=1 (int) and self.writeIndex=0 (int) are set.
* On write, data (String) is saved in self.buffer. The list index used is self.writeIndex, which increments by 1 afterwards. If there is already a value in self.buffer on that index, BufferFullException is raised. If this is the first value to be written into the buffer, self.oldest is set to the index as well.
* On read, the String in self.buffer on index self.oldest is returned. If there is no value in self.buffer on that index, BufferEmptyException is raised. self.buffer is set empty on that index, self.oldest is incremented by 1 afterwards.
* On overwrite, data (String) is saved in self.buffer. The list index used is self.writeIndex, which increments by 1 afterwards. If self.buffer was previously not empty on that index, self.oldest is incremented by 1.
* On clear, all entries in self.buffer get set to "" and self.oldest is reset to -1.
Example:
* C = CircularBuffer(7) (-> ["","","","","","",""])
* C.read() (-> "") -> BufferEmptyException("Buffer is empty.")
* C.write("1") (-> ["1","","","","","",""])
* C.write("2") (-> ["1","2","","","","",""])
* C.read() (-> ["","2","","","","",""]) -> "1"
* C.write("1") (-> ["","2","1","","","",""])
* C.overwrite("1") (-> ["","2","1","1","","",""])
* C.clear() (-> ["","","","","","",""])
"""

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
        self.capacity = capacity

    def read(self):
        if self.buffer[self.oldest] == "":
            raise BufferEmptyException("Buffer is empty.")
        res = self.buffer[self.oldest]
        self.buffer[self.oldest] = ""
        self.oldest = (self.oldest + 1) % self.capacity
        return res

    def write(self, data):
        if self.buffer[self.writeIndex] != "":
            raise BufferFullException("Buffer is full.")
        self.buffer[self.writeIndex] = data
        if self.oldest == -1:
            self.oldest = self.writeIndex
        self.writeIndex = (self.writeIndex + 1) % self.capacity


    def overwrite(self, data):
        if self.oldest == -1 and self.buffer[self.writeIndex] == "" or self.buffer[self.writeIndex] != "":
            self.oldest = (self.oldest + 1) % self.capacity
        self.buffer[self.writeIndex] = data
        self.writeIndex = (self.writeIndex + 1) % self.capacity
        


    def clear(self):
        for i in range(self.capacity):
            self.buffer[i] = ""
        self.oldest = -1

    @property
    def getBuffer(self):
        return self.buffer