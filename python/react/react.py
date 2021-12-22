"""
Set task: Implement a basic reactive system.
Method:
* Each InputCell has a list of observers and a value. The value is set on init,
  Observers are added whenever a ComputeCell is created using this InputCell.
* Whenever an InputCell is changed, __setattr__ is called. If 'value' is
  changed, all observers are called to update.
* Each ComputeCell has a value as well as a list of inputs, a function and a
  list of callbacks. inputs, fuction and value are set on init, callbacks can
  be added and using the add_callback() and remove_callback() functions.
* When an InputCell is changed the update() function is called to recompute the
  value based on its function and inputs. If callbacks are saved they are
  also updated with the new value.
Example:
input_ = InputCell(1)
output = ComputeCell([input_], lambda inputs: inputs[0] + 1)
output.value -> 2

observer = []
callback1 = ...callback using observer as storage...

output.add_callback(callback1)
input_.value = 3
output.value -> 4
observer -> [4]
"""


class InputCell:

    observers = list()
    value = None

    def __init__(self, initial_value):
        self.value = initial_value

    def __add__(self, other):
        return self.value + other

    def __sub__(self, other):
        return self.value - other

    def __mul__(self, other):
        return self.value * other

    def __eq__(self, other):
        if type(other) is int:
            return self.value == other
        return self.value == other.value

    def __lt__(self, other):
        if type(other) is int:
            return self.value < other
        return self.value < other.value

    def __le__(self, other):
        if type(other) is int:
            return self.value <= other
        return self.value <= other.value

    def __gt__(self, other):
        if type(other) is int:
            return self.value >= other
        return self.value >= other.value

    def __ge__(self, other):
        if type(other) is int:
            return self.value > other
        return self.value > other.value

    def __setattr__(self, name, value):
        if name == "value":
            super().__setattr__(name, value)
            for observer in self.observers:
                observer.update()


class ComputeCell:

    def __init__(self, inputs, compute_function):
        self.inputs = inputs
        self.function = compute_function
        self.value = self.function(self.inputs)
        self.callbacks = list()
        observers = self.inputs[:]
        for input in observers:
            if type(input) == InputCell:
                if self not in input.observers:
                    input.observers.append(self)
                break
            else:
                for put in input.inputs:
                    observers.append(put)

    def __add__(self, other):
        if type(other) is int:
            return self.value + other
        return self.value + other.value

    def __sub__(self, other):
        if type(other) is int:
            return self.value - other
        return self.value - other.value

    def __mul__(self, other):
        if type(other) is int:
            return self.value * other
        return self.value * other.value

    def add_callback(self, callback):
        if callback not in self.callbacks:
            self.callbacks.append(callback)

    def remove_callback(self, callback):
        try:
            self.callbacks.remove(callback)
        except ValueError:
            pass

    def update(self):
        old = self.value
        self.value = self.function(self.inputs)
        if old != self.value and old is not None:
            for callback in self.callbacks:
                callback(self.value)
