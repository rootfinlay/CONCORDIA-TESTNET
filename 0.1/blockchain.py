class Blockchain:
    def __init__(self, id, timestamp, sender, recipient, difficultyLevel, block):
        self.id = block_id
        self.timestamp = timestamp
        self.sender = sender
        self.recipient = recipient
        self.difficultyLevel = difficultyLevel
        self.block = block

    def __str__():
        blockchain_entry = (
                            "Block ID: " + self.id +
                            "\nTimestamp: " + self.timestamp +
                            "\nSender: " + self.sender +
                            "\nRecipient: " + self.recipient +
                            "\nDifficulty Level: " + self.difficultyLevel +
                            "\nBlock: " + self.block
                            )

        return blockchain_entry
