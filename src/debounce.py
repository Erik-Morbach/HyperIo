class Block:
    def __init__(self, blockSize) -> None:
        self.blockSize = blockSize
        self.currentIndex = 0
        self.block = [0] * self.blockSize
        self.currentSum = 0

    def add(self, value):
        self.currentSum -= self.block[self.currentIndex]
        self.block[self.currentIndex] = value
        self.currentSum += self.block[self.currentIndex]
        self.currentIndex = (self.currentIndex + 1) % self.blockSize

    def get(self):
        return self.currentSum/self.blockSize

class Debouncer:
    def __init__(self, updatePeriod, addPeriod, blockSize) -> None:
        self.updatePeriod = updatePeriod
        self.lastUpdateTime = 0

        self.addPeriod = addPeriod
        self.lastAddTime = 0

        self.block = Block(blockSize)

    def get(self):
        return self.block.get()

    def updateValueIfNeed(self, currentTime, func):
        if currentTime - self.lastUpdateTime < self.updatePeriod:
            return
        func(self.get())
        self.lastUpdateTime = currentTime

    def addToBufferIfNeed(self, currentTime, getValueFunc):
        if currentTime - self.lastAddTime < self.addPeriod:
            return
        self.block.add(getValueFunc())
