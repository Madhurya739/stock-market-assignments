# src/nlp/pros_cons_generator.py

"""
Pros/Cons Generator for NLP tasks.
Applies rule-based heuristics to generate advantages (pros) and disadvantages (cons)
for a given topic or text input.
"""

from typing import List, Callable


class ProsConsGenerator:
    def __init__(self):
        # Define 12 pro rules
        self.pro_rules: List[Callable[[str], str]] = [
            lambda text: f"Enhances efficiency in {text}",
            lambda text: f"Improves accuracy of {text}",
            lambda text: f"Reduces manual effort in {text}",
            lambda text: f"Provides scalability for {text}",
            lambda text: f"Facilitates better decision-making in {text}",
            lambda text: f"Supports automation of {text}",
            lambda text: f"Enables faster processing of {text}",
            lambda text: f"Improves user experience in {text}",
            lambda text: f"Offers flexibility in handling {text}",
            lambda text: f"Encourages innovation in {text}",
            lambda text: f"Strengthens reliability of {text}",
            lambda text: f"Boosts productivity in {text}",
        ]

        # Define 12 con rules
        self.con_rules: List[Callable[[str], str]] = [
            lambda text: f"May increase complexity in {text}",
            lambda text: f"Requires high initial investment for {text}",
            lambda text: f"Can introduce bias in {text}",
            lambda text: f"Demands specialized skills for {text}",
            lambda text: f"Potential data privacy risks in {text}",
            lambda text: f"May reduce human oversight in {text}",
            lambda text: f"Risk of over-reliance on {text}",
            lambda text: f"Possible errors in {text} interpretation",
            lambda text: f"Maintenance challenges for {text}",
            lambda text: f"Integration difficulties with {text}",
            lambda text: f"Scalability issues in {text}",
            lambda text: f"Limited transparency in {text}",
        ]

    def generate_pros(self, topic: str) -> List[str]:
        """Apply all pro rules to the given topic."""
        return [rule(topic) for rule in self.pro_rules]

    def generate_cons(self, topic: str) -> List[str]:
        """Apply all con rules to the given topic."""
        return [rule(topic) for rule in self.con_rules]

    def generate_summary(self, topic: str) -> dict:
        """Generate both pros and cons for the topic."""
        return {
            "pros": self.generate_pros(topic),
            "cons": self.generate_cons(topic),
        }


# Example usage
if __name__ == "__main__":
    generator = ProsConsGenerator()
    topic = "Natural Language Processing"
    summary = generator.generate_summary(topic)

    print("Pros:")
    for p in summary["pros"]:
        print(f"- {p}")

    print("\nCons:")
    for c in summary["cons"]:
        print(f"- {c}")
