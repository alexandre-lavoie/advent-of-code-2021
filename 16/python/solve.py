from enum import Enum
from typing import Tuple, Union, List, Callable, Dict
from dataclasses import dataclass

class Type(Enum):
    SUM=0
    PRODUCT=1
    MINIMUM=2
    MAXIMUM=3
    LITERAL=4
    GREATER_THAN=5
    LESS_THAN=6
    EQUAL_TO=7

TYPE_INTERPRETERS: Dict[Type, Callable[List[int], any]] = {
    Type.SUM: sum,
    Type.PRODUCT: product,
    Type.MINIMUM: min,
    Type.MAXIMUM: max,
    Type.GREATER_THAN: lambda a: a[0] > a[1],
    Type.LESS_THAN: lambda a: a[0] < a[1],
    Type.EQUAL_TO: lambda a: a[0] == a[1]
}

def product(values: int) -> int:
    product = 1

    for value in values:
        product *= value

    return product

@dataclass
class Packet():
    version: int
    type: Type
    value: Union[int, List["Packet"]]
    span: Tuple[int, int]

class Parser():
    bits: str
    pointer: int

    def __init__(self, bits):
        self.bits = bits
        self.pointer = 0

    @classmethod
    def hex2bits(cls, hex: str) -> str:
        bits = bin(int(hex, 16))[2:]

        if not len(bits) % 4 == 0:
            bits = bits.zfill(len(bits) + (4 - len(bits) % 4))

        return bits

    @classmethod
    def from_hex(cls, hex: str) -> "Parser":
        return Parser(cls.hex2bits(hex))

    @classmethod
    def from_file(cls, path: str) -> "Parser":
        return cls.from_hex(open(path).read())

    def parse_bits(self, n: int) -> int:
        bits = self.bits[self.pointer:self.pointer+n]
        self.pointer += n

        return int(bits, 2)

    def parse_version(self) -> int:
        return self.parse_bits(3)

    def parse_type(self) -> Type:
        return Type(self.parse_bits(3))

    def parse_length_type_id(self) -> int:
        return self.parse_bits(1)

    def parse_literal_section(self) -> Tuple[bool, int]:
        return self.parse_bits(1) == 1, self.parse_bits(4)

    def parse_literal(self) -> int:
        literal = ""

        while True:
            has_next, section = self.parse_literal_section()
            literal += bin(section)[2:].zfill(4)

            if not has_next: 
                break

        return int(literal, 2)

    def parse_length_sub_packets(self) -> int:
        return self.parse_bits(15)

    def parse_number_sub_packets(self) -> int:
        return self.parse_bits(11)

    def parse_packet(self):
        start = self.pointer
        version = self.parse_version()
        type = self.parse_type()

        if type == Type.LITERAL:
            value = self.parse_literal()
        else:
            value = []

            length_type_id = self.parse_length_type_id()

            if length_type_id == 0:
                length_sub_packets = self.parse_length_sub_packets()
                next_pointer = self.pointer + length_sub_packets

                while self.pointer < next_pointer:
                    value.append(self.parse_packet())
            elif length_type_id == 1:
                number_sub_packets = self.parse_number_sub_packets()

                for _ in range(number_sub_packets):
                    value.append(self.parse_packet())

        end = self.pointer

        return Packet(
            version=version, 
            type=type, 
            value=value, 
            span=(start, end)
        )

def version_sum(packet: Packet):
    if packet.type == Type.LITERAL:
        return packet.version
    else:
        return packet.version + sum(version_sum(child) for child in packet.value)

def interpret(packet: Packet) -> int:
    if packet.type == Type.LITERAL:
        return packet.value
    else:
        return int(TYPE_INTERPRETERS[packet.type]([interpret(child) for child in packet.value]))

if __name__ == "__main__":
    parser = Parser.from_file("../input.txt")
    packet = parser.parse_packet()

    print("Task 1:", version_sum(packet))
    print("Task 2:", interpret(packet))
