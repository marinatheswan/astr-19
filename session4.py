class Swan:
    def __init__(self, arm_length_m: float, leg_length_m: float, num_eyes: int, has_tail: bool, is_furry: bool):

        self.arm_length = arm_length_m
        self.leg_length = leg_length_m
        self.number_of_eyes = num_eyes
        self.has_tail = has_tail
        self.is_furry = is_furry

    def describe_physical_characteristics(self):

        print("--- Swan Physical Characteristics ---")
        print(f"* Arm Length: {self.arm_length} meters (wingspan)")
        print(f"* Leg Length: {self.leg_length} meters")
        print(f"* Number of Eyes: {self.number_of_eyes}")
        print(f"* Has a Tail: {self.has_tail}")
        print(f"* Is Furry: {self.is_furry} (Swans have feathers, not fur)")
        print("-----------------------------------")


graceful_swan = Swan(arm_length_m=2.0, 
                      leg_length_m=0.3, 
                      num_eyes=2,
                      has_tail=True,
                      is_furry=False)


graceful_swan.describe_physical_characteristics()
